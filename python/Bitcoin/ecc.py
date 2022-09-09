from random import randint
from unittest import TestCase

import hashlib
import hmac

## 유한체 정의
class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f'Num {num} not in field range 0 to {prime - 1}'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f'FieldElement_{self.prime}({self.num})'

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        '''
        if other is None:
            return False
        return self.num != other.num or self.prime != other.prime
        '''
        return not (self == other)
        
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)
    
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)
    '''
    def __pow__(self, exponent):
        n = exponent
        while n < 0:
            n += self.prime - 1
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    '''
    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        # num = (self.num * ((other.num) ** (self.prime -2))) % self.prime
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return self.__class__(num, self.prime)
    
    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num = num, prime = self.prime)


#### 타원곡선(Elliptic Curve: EC)의 한 점에 관심을 가짐
class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y ** 2 != self. x ** 3 + a * x + b:
            raise ValueError(f'({x}, {y}) is not on the curve.')

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return f'Point({self.x.num},{self.y.num})_{self.a.num}_{self.b.num} FieldElement({self.x.prime})'
        else:
            return f'Point({self.x},{self.y})_{self.a}_{self.b}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b # \는 줄바꿈

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(f'Points {self}, {other} are not on the same curve.')
        
        # Case 0.0: self is the point at infinity, return other
        if self.x is None:
            return other
        
        # Case 0.1: other is the point at infinity, return self
        if other.x is None:
            return self
        
        # Case 1: Result is point at infinity
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
        
        # Case 2: x1 != x2
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s ** 2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
        
        # Case 4: if we are tangent  to the vertical line
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)
        
        # Case 3: x1 == x2
        if self == other:
            s = (3 * self.x ** 2 + self.a) / (2 * self.y)
            x = s ** 2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

    '''
    # 곱하는 값이 커지면 연산 시간이 오래 걸림
    def __rmul__(self, coefficient):
        product = self.__class__(None, None, self.a, self.b)
        for _ in range(coefficient):
            product += self
        return product
    '''

    # 이진수 전개(binary expansion) 방법으로 위 문제 해결
    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result
    
class ECCTest(TestCase):

    def test_add(self):
        # tests the following additions on curve y^2 = x^3 - 7 over F_223:
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        additions = (
            # (x1, y1, x2, y2, x3, y3)
            (170, 142, 60, 139, 220, 181),
            (47, 71, 117, 141, 60, 139),
            (143, 98, 76, 66, 47, 71),
        )

        for x1_raw, y1_raw, x2_raw, y2_raw, x3_raw, y3_raw in additions:
            x1 = FieldElement(x1_raw, prime)
            y1 = FieldElement(y1_raw, prime)
            p1 = Point(x1, y1, a, b)
            x2 = FieldElement(x2_raw, prime)
            y2 = FieldElement(y2_raw, prime)
            p2 = Point(x2, y2, a, b)
            x3 = FieldElement(x3_raw, prime)
            y3 = FieldElement(y3_raw, prime)
            p3 = Point(x3, y3, a, b)
            self.assertEqual(p1 + p2, p3)



P = 2 ** 256 - 2 ** 32 - 977

class S256Field(FieldElement):

    def __init__(self, num, prime=None):
        super().__init__(num = num, prime = P)

    def __repr__(self):
        return f'{self.num:x}'.zfill(64)

A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class S256Point(Point):

    def __init__(self, x, y, a=None, b=None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x = S256Field(x), y = S256Field(y), a = a, b = b)
        else:
            super().__init__(x = x, y = y, a = a, b = b)

    def __repr__(self):
        if self.x is None:
            return 'S256Point(infinity)'
        else:
            return f'S256Point({self.x}, {self.y})'

    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)

    def verify(self, z, sig):
        s_inv = pow(sig.s, N - 2, N)
        u = z * s_inv % N
        v = sig.r * s_inv % N
        total = u * G + v * self
        return total.x.num == sig.r

G = S256Point(
    0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
)

class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s
    
    def __repr__(self):
        return f'Signature({self.r:x}, {self.s:x})'

class PrivateKey:

    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G

    def hex(self):
        return f'{self.secret:x}'.zfill(64)

    def sign(self, z):
        k = self.deterministic_k(z)
        r = (k * G).x.num
        k_inv = pow(k, N - 2, N)
        s = (z + r * self.secret) * k_inv % N
        if s > N/2:
            s = N - s
        return Signature(r, s)
    
    def deterministic_k(self, z):
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = hashlib.sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).giest()
        v = hmac.new(k, v, s256).digest()
        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()