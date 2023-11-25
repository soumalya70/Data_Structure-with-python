def placementlelo(n, m, dealer, x): 
    dealer.sort(reverse=True)
    x.sort(reverse=True) 
    #Telegram - @PLACEMENTLELO 
    S=0

    i = 0

#Telegram - @PLACEMENTLELO

    for d in dealer:

        while i < m and x[i][1] > d[1]: 
            i += 1

            if i < m and x[i][0] >= d[0]: 
                S+= 1 
                i += 1

#Telegram - @PLACEMENTLELO 
    return S
#Telegram - @PLACEMENTLELO

n, m = map(int, input().split())

dealer =[tuple(map(int, input().split())) for _ in range(n)] 
x = [tuple(map(int, input().split())) for _ in range(m)]

#Telegram - @PLACEMENTLELO

ans = placementlelo(n, m, dealer, x) 
ans+=1
print(ans, end="")

