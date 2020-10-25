class Solution:
    def maxArea(self, height):
        left=0
        right = len(height) - 1  # 设定左右指针初始位置
        max_vol = (right - left) * min(height[left], height[right])  # 设定初始最大容量
        while left < right and right - left > 0:
            # 主要是要考虑是移动左指针还有右指针，什么情况下移动，想清楚这点问题就解决了
            # 移动短的边界，同时更新最大的容量
            if height[left] <= height[right]:
                left += 1
                max_vol = max(max_vol, (right - left) * min(height[left], height[right]))
            else:
                right -= 1
                max_vol = max(max_vol, (right - left) * min(height[left], height[right]))
        return max_vol