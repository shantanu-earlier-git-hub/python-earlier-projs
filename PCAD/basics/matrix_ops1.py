"""
[[30 36 42]
 [66 81 96]]
[
    1*-1 + 2*-4 +3*-7, 1*-2 + 2*-5 +3*-8, 1*-3 + 2*-6 +3*-9 
    4*-1 + 5*-4 +6*-7, 4*-2 + 5*-5 +6*-8, 4*-3 + 5*-6 +6*-9
]

"""

result = [[0 for _ in range(3)] for _ in range(2)]

nums1 = [range(3), range(4, 7)]
nums2 = [range(1, 4), range(2, 5)]

for k in range(len(nums1)):
    for i in range(len(nums2[0])):
        for j in range(len(nums2)):
            result[k][i] += nums1[k][j] * nums2[j][i]

print(result)
