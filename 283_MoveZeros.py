class Solution(object):
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

# zero is the first index of the zero in the array
# It is kind of odd to initialize it to 0,
# but zero will be incremented until zero is found, so it is okay
# example : [5,0,1,0,3,12]
# i = 0, [5,0,1,0,3,12], zero = 1
# i = 1, [5,0,1,0,3,12], zero = 1
# i = 2, [5,1,0,0,3,12], zero = 2
# i = 3, [5,1,0,0,3,12], zero = 2
# i = 4, [5,1,3,0,0,12], zero = 3
# i = 5, [5,1,3,12,0,0], zero = 4

# i went through normally till len(nums), O(n)
# space complexity, O(1)
