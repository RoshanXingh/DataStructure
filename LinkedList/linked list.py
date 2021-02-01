class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class llist:
    def __init__(self):
        self.head = None

    def disp(self):
        temp = self.head
        print("linked list is:", end = "")
        while(temp):
            print(temp.val, end = " ")
            temp = temp.next

        

if(__name__ == "__main__"):

    ll = llist()
    h = int(input("enter head of linked list:"))
    ll.head = node(h)

    val = []
    v = list(map(int, input("enter data of linked list saparated by space:").split()))
    
    for i in v:
        val.append(node(i))

    
    ll.head.next = val[0]
    for i in range(len(val)-1):
        val[i].next = val[i+1]


    ll.disp()

    
