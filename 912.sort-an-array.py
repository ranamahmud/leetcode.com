#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (62.63%)
# Likes:    258
# Dislikes: 181
# Total Accepted:    48.8K
# Total Submissions: 77.9K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
#
#
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
#
#
#

# @lc code=start


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high]
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
            pos = i + 1
            arr[high], arr[pos] = arr[pos], arr[high]
            return pos

        def quick_sort(arr, low, high):
            if low >= high:
                return
            p = partition(arr, low, high)
            quick_sort(arr, low, p-1)
            quick_sort(arr, p + 1, high)
        # Write your code here.
        low = 0
        high = len(nums) - 1
        quick_sort(nums, low, high)
        return nums

# @lc code=end
