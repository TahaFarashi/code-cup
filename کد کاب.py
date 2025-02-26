def check_tickets(t, c):
    results = []
    for i in c:
        n = list(map(int, i[0]))  
        r = list(map(int, i[1]))
        p = list(map(int, i[2]))
        R = int(map(i[3][0]))
        
        ostani = False
        for i in range(6):  
            if n[i] >= 7 and r[i] == 1 and p[i] >= 2:
                ostani = True
                break  
        keshvary= R <= 40 

        if ostani or keshvary:
            results.append("YES")
        else:
            results.append("NO")

    return results
t = int(input().strip())
c= [ [input().strip().split() for _ in range(4)] for _ in range(t) ]
for result in check_tickets(t, c):
    print(result)