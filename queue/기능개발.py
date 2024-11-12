import math

progresses=[93,30,55]
speeds=[1,30,5]
count=0
queue=[]
answer=[]
for i in range(len(progresses)):
    queue.append(math.ceil((100-progresses[i])/speeds[i]))

max_data=queue[0]
for i in range(len(queue)):
    if queue[i]<=max_data:
        count+=1
    else:
        answer.append(count)
        count=1
        max_data=queue[i]

answer.append(count)
print(answer)