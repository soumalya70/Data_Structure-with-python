
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    stations = list(map(int, input().split()))

    # Calculate the minimum tank size
    tank = stations[0]
    last = x - stations[-1]

    if n > 1:
        for j in range(n - 1):
            tank = max(tank, stations[j + 1] - stations[j])

    print(max(last * 2, tank))
