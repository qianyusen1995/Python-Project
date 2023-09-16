#定义阶段
class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
  def reversePrint(self, head: ListNode) -> list[int]:
    return self.reversePrint(head.next) + [head.val] if head else []

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next

#执行阶段
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(print_linked_list(head))

solution = Solution()
reversed_list = solution.reversePrint(head)
print(reversed_list)