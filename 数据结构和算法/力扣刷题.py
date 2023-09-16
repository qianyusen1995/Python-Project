class Solution:
  """两数之和 Leecode 1"""
  def twoSum(self, nums: list[int], target: int) -> list[int]:
      idx = {}  # 创建一个空哈希表（字典）
      for j, x in enumerate(nums):  # x=nums[j]
          if target - x in idx:  # 在左边找nums[i]，满足 nums[i]+x=target
              #print ([target-x, x])
              return [idx[target - x], j]  # 返回两个数的下标
          idx[x] = j  # 保存 nums[j] 和 j
          #print(idx)
solver = Solution()
# 调用 twoSum 方法，并传入参数 nums 和 target
result = solver.twoSum(nums=[2,3,4], target=6) #{2:0, 7:1, 11:2, 15:3}
print(result)  # Output: [0, 1]


class Solution:
      def problemName(self, s: str) -> int:
            x, y = ...,...
            start = 0
            for end in range(len(s)):
                  x = new_x
                  if condition:
                        y = new_y


