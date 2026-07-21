class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_heights = [0] * n
        max_heights[-1] = height[-1]
        for i in range(n-2, -1, -1):
            max_heights[i] = max(height[i], max_heights[i+1])
        
        trapped_water = 0
        max_seen = 0
        for i in range(n-1):
            cur_height = height[i]
            bounding_height = min(max_seen, max_heights[i+1])
            trapped_water += max(0, bounding_height - cur_height)
            max_seen = max(max_seen, cur_height)
        return trapped_water



        
        