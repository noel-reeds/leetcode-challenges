class TwoSum(object):
    """Two Sum class"""
    def two_sum(self, nums, target):
        nums_sum = 0
        presum = []
        for num in nums:
            nums_sum += num
            presum.append(nums_sum)
        if target in presum:
            indices = []
            index = 0
            for sums in presum:
                if sums <= target:
                    indices.append(index)
                    index += 1
        return indices
