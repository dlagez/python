# https://leetcode.cn/problems/merge-two-sorted-lists/

# 将两个升序链表合并为一个新的 升序 链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。 

# 思路：新建两个链表dummy，p，dummy用来返回，p用来合并两个链表。
# 链表可能长短不一，所以判断只其中一个链表遍历完了就结束合并。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        pre = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 is not None else l2
        return prehead.next

if __name__ == '__main__':
    solution = Solution()
    solution.mergeTwoLists()