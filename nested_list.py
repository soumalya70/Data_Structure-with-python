if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    m = sorted(set([i[1] for i in records]))[1]
# print(m)
    records.sort()
    for n, s in records:
        if s == m:
            print(n)