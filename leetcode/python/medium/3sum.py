#! /usr/bin/python

def threeSum(nums):

	pos_nums = []
	neg_nums = []
	sol = []
	for i in nums:
		if i < 0:
			neg_nums.append(i)
		else:
			pos_nums.append(i)
	
	if pos_nums.count(0) > 3:
		sol.append([0,0,0])

	if len(pos_nums) > 1:
		for i in range(0, len(pos_nums) - 1):
			for j in range(i+1, len(pos_nums)):
				if -(pos_nums[i] + pos_nums[j]) in neg_nums:
					sol1 = [pos_nums[i], pos_nums[j], -(pos_nums[i] + pos_nums[j])]
					if sorted(sol1) not in sol:
						sol.append(sorted(sol1))

	if len(neg_nums) > 1:	
		for i in range(0, len(neg_nums) - 1):
			for j in range(i+1, len(neg_nums)):
				if -(neg_nums[i] + neg_nums[j]) in pos_nums:
					sol1 = [neg_nums[i], neg_nums[j], -(neg_nums[i] + neg_nums[j])]
					if sorted(sol1) not in sol:
						sol.append(sorted(sol1))

	return sol

	

nums = [0,0,0]
print nums
print threeSum(nums)			

"""

        :type nums: List[int]

        :rtype: List[List[int]]

        """
