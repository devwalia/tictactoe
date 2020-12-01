t = int(input())
for _ in range(t):
    line = input()
    even = ""
    odd = ""

    for i, c in enumerate(line):

        if (i%2 & i) == 0:
            even+= c
        else:
            odd +=c

 print(even, odd)
