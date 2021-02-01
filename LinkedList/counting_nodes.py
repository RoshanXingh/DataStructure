class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class llist:
    def __init__(self):
        self.head = None
        
    def count(self):
        num = 0
        temp = self.head
        while(temp):
            num += 1
            temp = temp.next
        return str(num)

if(__name__ == "__main__"):

    ll = llist()
    h = int(input("enter head of linked list:"))
    ll.head = node(h)

    val = []
    v = list(map(int, input("enter data of linked list saparated by space:").split()))
    
    for i in v:
        #n = int(input("enter next value of linked list:"))
        val.append(node(i))

    
    ll.head.next = val[0]
    for i in range(len(val)-1):
        val[i].next = val[i+1]

    print("node in current linked list is:"+ll.count())

    
