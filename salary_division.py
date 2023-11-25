def money(n):
    t500 = 0
    t200 = 0
    t100 = 0
    t50 = 0
    t20 = 0
    t10 = 0
    t5 = 0
    t2 = 0
    t1 = 0
    
    while n > 0:
        if n >= 500:
            n = n - 500
            t500 += 1
        elif 200 <= n < 500:
            n = n - 200
            t200 += 1
        elif 100 <= n < 200:
            n = n - 100
            t100 += 1
        elif 50 <= n < 100:
            n = n - 50
            t50 += 1
        elif 20 <= n < 50:
            n = n - 20
            t20 += 1
        elif 10 <= n < 20:
            n = n - 10
            t10 += 1
        elif 5 <= n < 10:
            n = n - 5
            t5 += 1
        elif 2 <= n < 5:
            n = n - 2
            t2 += 1
        
    if n == 1:
        t1 = 1
    print(t500, t200, t100, t50, t20, t10, t5, t2, t1)

money(5000)
