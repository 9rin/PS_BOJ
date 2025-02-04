c = 0
while 1:
    c += 1
    n = list(map(int,input().split()))
    if n[0] == 0 :
        break
    if n[0] % 2 == 0 :
        res = "{:.1f}".format((n[n[0]//2] + n[(n[0]//2) + 1]) / 2)
        print(f"Case {c}: {res}")
    else:
        res = "{:.1f}".format(n[n[0]//2 + 1])
        print(f"Case {c}: {res}")