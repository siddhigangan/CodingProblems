class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = {}
        for i in range(len(nums1)):
            if nums1[i] in arr1:
                arr1[nums1[i]] = arr1[nums1[i]] + 1
            else:
                arr1[nums1[i]] = 1

        arr2={}
        for i in range(len(nums2)):
            if nums2[i] in arr2:
                arr2[nums2[i]] = arr2[nums2[i]] + 1
            else:
                arr2[nums2[i]] = 1
        res = []
        if(len(nums1) < len(nums2)):
            for key,val in arr1.items():
                if (key in arr2):
                    a = min(val,arr2[key])
                    res.extend([key] * a)
                
        else:
            for key,val in arr2.items():
                if (key in arr1):
                    a = min(val,arr1[key])
                    res.extend([key] * a)
        return res