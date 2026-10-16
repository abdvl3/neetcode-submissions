class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # want biggest distance between bar
        # tallest bars

        h1 = 0
        h2 = len(heights) - 1
        vol = 0
        while h1 < h2:
            area = (h2 - h1) * min(heights[h1],heights[h2])
            vol = max(vol,area)
            if heights[h1] <= heights[h2]:
                h1 += 1
                
            else:
                h2 -= 1

        return vol
        

        

        