class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = None
        while i != j:
            now_area = (j-i) * min(height[i], height[j])
            max_area = max(now_area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
