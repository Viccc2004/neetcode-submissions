class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # A set only keeps unique elements
        unique_elements = set(nums)
        return len(unique_elements) < len(nums)