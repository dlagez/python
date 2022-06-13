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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total%10)
            remainder = total//10

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            curr = curr.next

        if remainder : curr.next = ListNode(remainder)
        return result.next


if __name__ == '__main__':
    data1 = [2, 4, 3, 5, 6]
    data2 = [5, 6, 4]
    linkList = LinkList()
    l1 = linkList.initList(data1)
    l2 = linkList.initList(data2)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    linkList.printList(result)


