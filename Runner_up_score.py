# The task is to identify the second-highest score from a list of given scores.

n = int(input())
arr = set(map(int, input().split()))

a = max(arr)
arr.remove(a)
print(max(arr))