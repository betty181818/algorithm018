class Solution:
    def threeSum(self, nums: List[int]) :
        res = []
        size = len(nums)

        # 如果数组长度小于3，直接返回
        if size < 3:
            return res

        # 对数组进行排序
        nums = sorted(nums)

        # 依次选取排序后数组中的元素作为定值
        for i in range(len(nums)):
            # 如果定值超过0，返回结果
            if nums[i] > 0:
                break

            # 如果已经遍历过该定值，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 设置两个左右指针
            j, k = i + 1, len(nums) - 1

            # 如果左指针小于右指针
            while j < k:
                # 如果左指针已经遍历过该元素，跳过
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                # 如果右指针已经遍历过该元素，跳过
                if k < (size - 1) and nums[k] == nums[k + 1]:
                    k -= 1
                    continue

                sum = nums[i] + nums[j] + nums[k]

                # 当三数之和等于0，记录结果
                # 当三数之和小于0，左指针右移
                # 当三数之和大于0，右指针左移
                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1

        return res