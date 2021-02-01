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

    def make(self, a, h):
        self.head = node(h)
        val = []

        for i in a:
            val.append(node(i))

    
        ll.head.next = val[0]
        for i in range(len(val)-1):
            val[i].next = val[i+1]


class sort:

    def sort_linkedlist(self, v):
        ln = len(v)
        qs = sort()

        if (ln<1):
            return v

        else:
            left, right = [], []
            i, j = 0, ln-2
            p = v.pop(ln-1)

            for item in v:
                if(item < p):
                    left.append(item)
                else:
                    right.append(item)

            return s.sort_linkedlist(left) + [p] + s.sort_linkedlist(right)
        

if(__name__ == "__main__"):

    ll = llist()
    h = int(input("enter head of linked list:"))

    val = []
    l = list(map(int, input("enter data of linked list saparated by space:").split()))

    ll.make(l, h)
    ll.disp()

    s = sort()
    l.append(h)
    sl = s.sort_linkedlist(l)
    h = sl.pop(0)
    ll.make(sl, h)
    print("\nsorted ", end = ' ')
    ll.disp()

    
