#making stack using list and performing various stack operation


class stack_operation:
    def __init__ (self,element):
        self.element = element
        self.stack = [None]*self.element
        
    def get(self):
        for i in range(self.element):
            self.stack[i] = int(input("enter {} value:".format(i+1)))

    def display(self):
        print(self.stack)

    def find(self, f):
        for i in range(len(self.stack)):
            if(self.stack[i] == f):
                return "{} is found at {} place".format(f ,i+1)
                break
        return "element not found"

    def findmin(self):
        a = self.stack[0]
        for i in self.stack:
            if(i < a):
                a = i
        return a

    def findmax(self):
        a = self.stack[0]
        for i in self.stack:
            if (i > a):
                a = i
        return a


if __name__ == "__main__":
    element = int(input("enter no of element you want to add:"))

    l = stack_operation(element)

    l.get()
    l.display()

    x = 1;
    while(x == 1 ):
        choise = int(input("""enter operation you want to perform on given stack
1.find an enement
2.find minimum element
3.find maximum element
4.insert new element
5.delete laslt element
6.display stack
:"""))
    
        if (choise == 1):
            f = int(input("enter no you want to search:"))
            print(l.find(f))

        elif (choise == 2):
            print("minimum element is:",l.findmin())

        elif (choise == 3):
            print("maximum element is:",l.findmax())

        elif (choise == 4):
            l.stack.append(int(input("enter element to append:")))

        elif (choise == 5):
            l.stack.pop()

        elif (choise == 6):
            l.display()

        else:
            print("please enter valid choise")

        x = int(input("press 1 to go to main menu again, press any buttom to exit:"))
        
 
            
        
        
