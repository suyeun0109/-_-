cards1=["i","water","drink"]
cards2=["want","to"]
goal=["i","want","to","drink","water"]

n=len(goal)
while goal:
    if cards1 and goal[0]==cards1[0]:
        goal.pop(0)
        cards1.pop(0)
    elif cards2 and goal[0]==cards2[0]:
        goal.pop(0)
        cards2.pop(0)
    else:
        break

if goal==[]:
    print("Yes")
else:
    print("No")