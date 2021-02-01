class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        print("list is :", end = " ")
        while(temp):
            print(temp.val, end = " ")
            temp = temp.next


if(__name__ == '__main__'):

    dll = double_linked_list()
    h = int(input("enter head of linked list:"))
    dll.head = node(h)
    val = []
    v = list(map(int, input("enter space seperated value of list:").split()))
    for i in v:
        val.append(node(i))

    dll.head.next = val[0]
    val[0].next = val[1]
    val[0].prev = dll.head

    for i in range(1, len(v)-1):
        val[i].next = val[i+1]
        val[i].prev = val[i-1]

    dll.display()
