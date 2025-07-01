#max subarray of size k
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 3
n = len(arr)

summ=sum(arr[:k])
maxi=summ
for i in range(k,n):
    summ=summ-arr[i-k]+arr[i]
    maxi=max(maxi,summ)
print(maxi)