
def removeDuplicates(self,head):
    ptr = head
    while ptr.next is not None:
        if(ptr.data == ptr.next.data):
            ptr.next = ptr.next.next
            continue
        ptr = ptr.next
    return head

