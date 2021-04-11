"""
date:2021-03-19
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutions(object):
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while count < left:
            count += 1
            pre = pre.next
        cur = pre.next
        tail = cur
        while count <= right:
            nxt = cur.next
            cur.next = pre.next
            pre.next = cur
            tail.next = nxt
            cur = nxt
            count += 1
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = Solutions().reverseBetween(head, 2, 4)
    L = []
    while res:
        L.append(res.val)
        res = res.next
    print(L)
