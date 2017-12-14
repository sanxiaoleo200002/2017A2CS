#Leo Qiu Opt3

def groupSum(start,nums,target):
	if start+1 > len(nums):
		return target == 0

	return groupSum(start+1,nums,target) or groupSum(start+1,nums,target-nums[start])

def groupSum6(start,nums,target):
	if start+1 > len(nums):
		return target == 0

	if nums[start] == 6:
		return groupSum6(start+1,nums,target-6)
	return groupSum6(start+1,nums,target) or groupSum6(start+1,nums,target-nums[start])

def groupNoAdj(start,nums,target):
	if start+1 > len(nums):
		return target == 0

	return groupNoAdj(start+1,nums,target) or groupNoAdj(start+2,nums,target-nums[start])

def groupSum5(start,nums,target):
	if start+1 > len(nums):
		return target == 0 

	if nums[start]%5 == 0 and nums[start+1] == 1:
		return groupSum5(start+2,nums,target-nums[start])
	elif nums[start]%5 == 0:
		return groupSum5(start+1,nums,target-nums[start])
	return groupSum5(start+1,nums,target) or groupSum5(start+1,nums,target-nums[start])

def groupSumClump(start,nums,target):
	if start+1 > len(nums):
		return target == 0 

	if start < len(nums)-1: 
		if nums[start] == nums[start+1]:
			i = start
			while i < len(nums)-1 and nums[i] == nums[i+1]:
				i += 1
			i += 1
			return groupSumClump(i,nums,target) or groupSumClump(i,nums,target-(i-start)*nums[i-start])
	return groupSumClump(start+1,nums,target) or groupSumClump(start+1,nums,target-nums[start])


#print(11%5==0)
print(groupSum(0,[2,4,8],12))
print(groupSum6(0,[5,6,2],7))
print(groupNoAdj(0,[2,5,10,4],14))
print(groupSum5(0,[2,5,10,1],16))
print(groupSumClump(0,[2,4,4,4,3,4],15))
