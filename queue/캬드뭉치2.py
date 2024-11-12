from collections import deque


def solutions(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:  # goal이 비어있지 않으면 계속 반복
        if cards1 and cards1[0] == goal[0]:  # cards1의 첫 번째 요소가 goal의 첫 번째와 같으면
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:  # cards2의 첫 번째 요소가 goal의 첫 번째와 같으면
            cards2.popleft()
            goal.popleft()
        else:
            break

    # goal이 빈 리스트라면 "Yes" 반환
    if goal == []:
        return "Yes"
    else:
        return "No"


# 테스트
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solutions(cards1, cards2, goal))  # 예상 출력: Yes

