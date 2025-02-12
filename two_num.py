"""Author Anurag Kumar (mailto:anuragkumarak95@gmail.com)

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twoSum(nums, target):
    chk_map = {}
    for index, val in enumerate(nums):
        compl = target - val  #寻找互补数
        if compl in chk_map:
            indices = [chk_map[compl], index] # 如果在map里面，返回索引
            print(indices)
            return indices
        else:
            chk_map[val] = index #如果不在，直接加入对象
    return False

def test_twoSum():
    # 测试用例 1: 普通情况
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert twoSum(nums1, target1) == [0, 1], "Test case 1 failed"

    # 测试用例 2: 没有找到匹配的情况
    nums2 = [1, 2, 3, 4]
    target2 = 10
    assert twoSum(nums2, target2) == False, "Test case 2 failed"

    # 测试用例 3: 多个匹配，返回第一个找到的
    nums3 = [3, 2, 4, 6]
    target3 = 6
    assert twoSum(nums3, target3) == [1, 2], "Test case 3 failed"

    # 测试用例 4: 包含负数和零
    nums4 = [-3, 4, 3, 90]
    target4 = 0
    assert twoSum(nums4, target4) == [0, 2], "Test case 4 failed"

    print("All test cases passed!")

# 调用测试函数
test_twoSum()
