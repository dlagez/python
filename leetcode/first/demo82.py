# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，
# 只留下不同的数字 。返回 已排序的链表 。

# 思路：由于重复出现的元素是连续的，首先在链表的头节点前加个哑节点，然后进行遍历
# 如果cur.next == cur.next.next 那么记下这个元素，
# 然后不断的删除cur.next。直到元素不同或者到达链表结尾

# Definition for singly-linked list.
# from multiprocessing import dummy


from calendar import c
from os import link


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
    
    def initList(self, data):
        self.head = ListNode(data[0])
        r = p = self.head
        for i in data[1:]:
            p.next = ListNode(i)
            p = p.next
        return r
    
    def printList(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end='')
            node = node.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        cur = dummy
        # 首先要判断它是否为空
        while cur.next and cur.next.next:
            # 这里的判断如果不加.val在vscode里面运行这里永远不会相等
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

if __name__=='__main__':
    solution = Solution()
    linklist = LinkList()
    data = linklist.initList([1, 2, 3, 3, 4, 4, 5])
    result = solution.deleteDuplicates(data)
    print()
       