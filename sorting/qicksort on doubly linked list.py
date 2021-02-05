class node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class double_linkedlist:
    def __init__(self):
        self.head = None

    def disp(self):
        temp = self.head
        print("list is:", end = " ")
        while(temp):
            print(temp.val, end = " ")
            temp = temp.next

    def make(self, a, h):
        self.head = node(h)
        val = []
        for i in a:
             val.append(node(i))

        dll.head.next = val[0]
        val[0].next = val[1]
        val[0].prev = dll.head

        for i in range(1, len(v)-1):
            val[i].next = val[i+1]
            val[i].prev = val[i-1]

class sort:
    def quicksort(self, v):
        qs = sort()
        ln = len(v)

        if(ln < 1):
            return v

        else:
            left, right = [], []
            p = v.pop(ln-1)

        for item in v:
            if(item < p):
                left.append(item)
            else:
                right.append(item)

        return qs.quicksort(left) + [p] + qs.quicksort(right) 
            


if(__name__ == '__main__'):

    dll = double_linkedlist()
    h = int(input("enter head of linked list:"))
    v = list(map(int, input("enter value of linked list seprated by space:").split()))

    dll.make(v, h)
    dll.disp()

    s = sort()
    v.append(h)
    sdl = s.quicksort(v)
    h = sdl.pop(0)
    dll.make(sdl, h)
    print("\nsorted ", end = " ")
    dll.disp()
