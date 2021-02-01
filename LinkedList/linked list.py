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

class operation:
    def __init__(self, ll):
        self.ll = ll

    def insert(self, data, pos):
        temp = self.ll.head
        i = 0
        tn = temp.next
        while(i != int(pos)-1):
            temp = temp.next
            tn = temp.next
            i += 1

        temp.next = node(data)
        t = temp.next
        t.next = tn

   # def delete():

    #def search():

    #def update():
        

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

    op = operation(ll)

    data, pos = input("\nenter value and position of element to add:").split()
    
    op.insert(data, pos)

    ll.disp()
    

    
