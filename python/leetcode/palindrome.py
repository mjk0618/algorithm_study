# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        pc = len(head) // 2
        if len(head) % 2 == 1:
            head_head = head[:pc]
            head_tail = head[pc+1:]
        else:
            head_head = head[:pc]
            head_tail = head[pc:]
        head_tail.reverse()
        if head_head == head_tail:
            return True, head_head, head_tail
        else: return False, head_head, head_tail

n = list(input('input number'))
sol = Solution().isPalindrome(n)
print(sol)


# -> Linked List 개념공부해서 코드 수정하기