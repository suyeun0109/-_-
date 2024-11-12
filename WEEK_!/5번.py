arr1=[
    [1,4],
    [3,2],
    [4,1]
]
arr2=[
    [3,3],
    [3,3]
]

arr=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        arr[i][j]+=arr1[i][j]*arr2[j][i]
        print(arr)