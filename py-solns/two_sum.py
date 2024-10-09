class TwoSum(object):
    """Two Sum class"""
    def two_sum(self, nums, target):
        """returns indices of nums, sum to target."""
        sub_nums = []
        for num in nums:
            if num < target:
                sub_nums.append(num)
        for num in sub_nums:
            index_ar = []
            rem = target - num
            if rem in sub_nums:
                index_ar.append(num)
                index_ar.append(rem)
        index_arr = []
        for m in range(len(nums)):
            for num in index_ar:
                if num == nums[m]:
                    index_arr.append(m)
        return index_arr
