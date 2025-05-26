# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # First solution
            # # Calculate the length of each linked list
            # list1_length = 0
            # current = list1
            # while not (current == None):
            #     list1_length += 1
            #     current = current.next
            
            # list2_length = 0
            # current = list2
            # while not (current == None):
            #     list2_length += 1
            #     current = current.next
            

            # # Determine which list is longer and which is shorter.
            # larger_list_node = list1 if list1_length > list2_length else list2
            # smaller_list_node = list1 if list1_length <= list2_length else list2
            # prev_node = None
            # head = larger_list_node

            # while larger_list_node is not None:
            #     # If all smaller list nodes have been checked, we are done
            #     if smaller_list_node is None:
            #         break
            #     # Compare the values of the node
            #     if larger_list_node.val > smaller_list_node.val:
            #         # Store the next value on smaller list
            #         next_value = smaller_list_node.next
            #         # If this is the head (first comparision)
            #         if prev_node is None:
            #             # Place the node from smaller list as head and link next to
            #             #   current head
            #             smaller_list_node.next = larger_list_node
            #             head = smaller_list_node
            #             # Move previous node to be newly added node
            #             prev_node = smaller_list_node
            #         else:
            #             # Place the node between current and previous nodes on larger
            #             # lists
            #             smaller_list_node.next = larger_list_node
            #             prev_node.next = smaller_list_node
            #             # Move previous node to be newly added node
            #             prev_node = smaller_list_node
            #         # Move to next node on smaller list
            #         smaller_list_node = next_value   
            #     else:
            #         # If this is the last node of the larger list
            #         if larger_list_node.next is None:
            #             # Set smaller list node as next node
            #             larger_list_node.next = smaller_list_node
            #             break
            #         # Move to next node on larger list
            #         prev_node = larger_list_node
            #         larger_list_node = larger_list_node.next
            #     print("Current linked list", head)
            # return head
        
        # Better solution
        new_list = ListNode()
        tail = new_list
        while (l1 and l2):
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2

        return new_list.next
