class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        combined = sorted(nums1 + nums2)

        o = len(combined)

        if o % 2 == 1:
            return combined[o // 2]
        else:
            mid1 = o // 2
            mid2 = mid1 - 1
            return (combined[mid1] + combined[mid2]) / 2.0
