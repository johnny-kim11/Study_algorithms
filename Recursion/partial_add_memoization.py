### 부분합 문제 ###

num_list = [3, 2, 6, 5] # 주어진 숫자열
target_num = 14 # 목표 숫자

# Memoization을 위한 배열
memo = [[-1 for _ in range(target_num+1)] for _ in range(len(num_list)+1)]

# 1. 재귀함수 구현
# Input: 남은 숫자의 갯수, 남은 숫자의 합
def func(left_num, left_target):
    # 1-1. 남은 숫자가 없을 때
    if left_num == 0:
        if left_target == 0:
            return 1
        else:
            return 0
        
    # 1-2 남은 숫자가 있을 때
    # 1-2-1. 메모가 남아있을때
    if memo[left_num][left_target] != -1:
        return memo[left_num][left_target]
    
    # 1-2-2. 메모가 남아있지 않을때
    else:
        if func(left_num-1, left_target):
            memo[left_num][left_target] = 1
            return 1
        if  func(left_num-1, left_target-num_list[left_num-1]):
            memo[left_num][left_target] = 1
            print(num_list[left_num-1])
            return 1
        
    # 1-3. 
    memo[left_num][left_target] = 0
    
    return 0

if func(len(num_list), target_num):
    print("True")
else:
    print("False")
