from typing import List,Optional
import heapq
from ListNode import ListNode
from operator import attrgetter

# Definition for singly-linked list.

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        curr=head
        h=[]
        for i in range(len(lists)):
            print(type(lists[i]))
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        print(h)
        while h:
            val, i =heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next 
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i))
                lists[i]=lists[i].next
        return head.next
    
    
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None


print(Solution().mergeKLists1([[1,4,5],[1,3,4],[2,6]]))