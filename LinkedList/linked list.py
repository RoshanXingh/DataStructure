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
        print("\n")

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

    def delete(self, ll, value):
        headval = ll.head
        if(headval is not None):
            if(headval.val == value):
                ll.head = headval.next
                headval = None
                return

        while(headval is not None):
            if (int(headval.val) == int(value)):
                break
            prev = headval
            headval = headval.next

        if(headval == None):
            return

        prev.next = headval.next

        headval = None

    def length(self):
        temp = self.ll.head
        flag = 0
        while(temp):
            temp = temp.next
            flag += 1
        return flag
        

    def search(self, sr, l):
        temp = self.ll.head
        if(temp.val == sr):
            print("value is found at head")

        else:
            flag = 1
            while(flag <=l and temp.val != sr):
                temp = temp.next
                flag += 1

            if(flag == l+1):
                print("element not found")

            else:
                print("element is found at {} position".format(flag))

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

    
    i = 1
    while(int(i) == 1):
        op = operation(ll)

        choise = int(input(""" choose from the following operation to perfore
1. Insert in linked list
2. Delete element form linked list
3. find length of linked list
4. Search element from linked list
5. exit
:"""))

        if (choise == 1):
            data, pos = input("\nenter value and position of element to add:").split()
            op.insert(int(data), int(pos))
            ll.disp()

        elif(choise == 2):
            value = int(input("\nenter value to delete:"))
            op.delete(ll, value)
            ll.disp()

        elif(choise == 3):
            print("length of linked list is:", op.length())

        elif(choise ==4):
            sr = int(input("enter value to search:"))
            l = op.length()
            op.search(sr, l)

        elif (choise == 5):
            break
        else:
            print("Please enter valid option")

        i = input("enter 1 to repeat, or any other key to exit:")
    
