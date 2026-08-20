"""Write a Python program to find the longest consecutive increasing sequence in a tuple and display its elements.
Input:(3, 5, 7, 2, 4, 6, 8, 1, 9)
Output:(2, 4, 6, 8)"""

"""t = (3, 5, 7, 2, 4, 6, 8, 1, 9)

current = []
longest = []

for i in range(len(t) - 1):

    if t[i + 1] > t[i]:

        if len(current) == 0:
            current.append(t[i])

        current.append(t[i + 1])

    else:

        if len(current) > len(longest):
            longest = current.copy()

        current = []

if len(current) > len(longest):
    longest = current.copy()

print(tuple(longest))"""

""". Given a list of integers, write a Python program to find the contiguous (continuous) subarray that has the maximum sum and print that sum.
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6"""
"""nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = nums[0]
current_sum = nums[0]

for i in range(1, len(nums)):

    if current_sum < 0:
        current_sum = nums[i]
    else:
        current_sum = current_sum + nums[i]

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)"""


"""3.

A = {10, 20, 30, 40, 50}
B = {30, 40, 60, 70}

result = A ^ B

print(result)"""

