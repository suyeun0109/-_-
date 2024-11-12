N=5
K=2

queue=[]
for i in range(N):
    queue.append(i+1)

while len(queue)>1:
    for i in range(K-1):
        queue.append(queue.pop(0))
    queue.pop(0)

print(queue)