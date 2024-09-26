import sys
n = int(sys.stdin.readline())
s = set()

for i in range(n):
    a = sys.stdin.readline().rstrip().split()

    if(len(a)==1):
        if(a[0] == "all"):
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    else:
        a, b = a[0], int(a[1])

        if(a=="add"):
            s.add(b)
        elif(a=="remove"):
            s.discard(b)
        elif(a=="toggle"):
            if (b in s):
                s.discard(b)
            else:
                s.add(b)
        else:
            print(1 if b in s else 0)