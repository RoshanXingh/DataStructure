class quick_sort:
    def sort(self, arr):
        ln = len(arr)
        s = quick_sort()

       
        if (ln<=1):
            return arr

        else:
            left, right = [], []
            i, j = 0, ln-2
            p = arr.pop(ln-1)

            for item in arr:
                if (item<p):
                    left.append(item)
                else:
                    right.append(item)
            
            return s.sort(left) + [p] + s.sort(right)

                             

if __name__ == '__main__':
    arr = []
    arr = list(map(int, input("enter list element seperated by space:").split()))
    qs = quick_sort()
    print(qs.sort(arr))
