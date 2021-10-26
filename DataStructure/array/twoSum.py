'''
문제 : 두 수의 합
덧셈하여 타겟 숫자를 만들 수 있는 배열의 두 숫자 인덱스를 반환
'''


def brute_force(nums: list[int], t: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == t:
                return [i, j]


def in_solution(nums, t):
    for idx, num in enumerate(nums):
        complement = t - num

        if complement in nums[idx+1:]:
            return [idx, nums[idx+1:].index(complement)+(idx+1)]


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    t = int(input())

    print(brute_force(nums, t))
    print(in_solution(nums, t))
