from unittest import TestSuite, TextTestRunner

import hashlib


def run(test):
    suite = TestSuite()
    suite.addTest(test)
    TextTestRunner().run(suite)



def hash256(s):
    '''two rounds of sha256'''
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def encode_base58(s):
    count = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
    num = int.from_bytes(s, 'big')
    prefix = '1' * count
    result = ''
    while num > 0:
        num, mod = divmod(num, 58)
        result = BASE58_ALPHABET[mod] + result
    return prefix + result

def encode_base58_checksum(b):
    return encode_base58(b + hash256(b)[:4])

def hash160(s):
    ''' sha256 followed by ripemd160 '''
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()

def little_endian_to_int(b):
    ''' little_endian_to_int takes byte sequence as a little-endian number.
    Return as integer'''
    return int.from_bytes(b, 'little')

def int_to_little_endian(n, length):
    ''' int_to_little_endian takes an integer and returns the little-endian
    byte sequence of length '''
    return n.to_bytes(length, 'little')
    