# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0
    left = [0] * len(height)
    right = [0] * len(height)
    left[0] = height[0]
    for i in range(1, len(height)):
        left[i] = max(left[i-1], height[i])
    right[-1] = height[-1]
    for i in range(len(height)-2, -1, -1):
        right[i] = max(right[i+1], height[i])
    return sum(min(left[i], right[i]) - height[i] for i in range(len(height)))

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))