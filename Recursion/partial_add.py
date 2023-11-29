### 부분합 문제 ###

num_list = [3, 2, 6, 5] # 주어진 숫자열
target_num = 14 # 목표 숫자

# 1. 재귀함수 구현
# Input: 남은 숫자의 갯수, 남은 숫자의 합
def func(left_num, left_target):
    print(left_num, left_target)
    # 1-1. 남은 숫자가 없을 때
    if left_num == 0:
        # 1-1-1. 남은 숫자의 합이 0일때
        if left_target == 0:
            return True
        else:
            return False
        
    # 1-2 남은 숫자가 있을 때
    if func(left_num-1, left_target):
        return True
    if  func(left_num-1, left_target-num_list[left_num-1]):
        print(num_list[left_num-1])
        return True
    
    return False

print(func(len(num_list), target_num))