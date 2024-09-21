from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        target = 0
        sorted_indexes = sorted(range(len(nums)), key=lambda x: nums[x])

        first_index = 0
        while first_index < len(sorted_indexes) - 2:
            if first_index == 0 or nums[sorted_indexes[first_index - 1]] != nums[sorted_indexes[first_index]]:
                left_index = first_index + 1
                right_index = len(sorted_indexes) - 1

                while left_index < right_index:
                    four_sum = nums[sorted_indexes[first_index]] + nums[sorted_indexes[left_index]] + nums[sorted_indexes[right_index]]
                    if four_sum < target:
                        left_index += 1
                    elif four_sum > target:
                        right_index -= 1
                    else:
                        result.append([nums[sorted_indexes[first_index]], nums[sorted_indexes[left_index]],
                                       nums[sorted_indexes[right_index]]])

                        increment = 1
                        while left_index + increment < right_index and nums[sorted_indexes[left_index]] == nums[
                            sorted_indexes[left_index + increment]]:
                            increment += 1
                        left_index += increment

                        decrement = 1
                        while right_index - decrement > left_index and nums[sorted_indexes[right_index]] == nums[
                            sorted_indexes[right_index - decrement]]:
                            decrement += 1
                        right_index -= decrement
            first_index += 1

        return result
