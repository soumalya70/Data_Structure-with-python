'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format'''

'''The first line contains . The second line contains an array  A[]  of n integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score''' 
def quicksort(a, l, r):
    if r - l <= 1:
        return
    yellow = l + 1

    for green in range(l + 1, r):
        if a[green] <= a[l]:
            (a[yellow], a[green]) = (a[green], a[yellow])
            yellow = yellow + 1
    a[l], a[yellow - 1] = a[yellow - 1], a[l]
    quicksort(a, l, yellow - 1)
    quicksort(a, yellow, r)

arr = [int(x) for x in input().split()]
n=len(arr)
quicksort(arr, 0, n)
runner_up = None

for i in range(n - 2, -1, -1):  # Loop from the second-to-last element to the first element
    if arr[i] != arr[-1]:  # Check if the current element is different from the maximum element
        runner_up = arr[i]
        break

print(runner_up)