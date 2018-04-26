class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1

        # 1. find the pivot by binary search approach - O(logN)
        pivot = self.findPivot(nums, 0, len(nums)-1)
        print(pivot)

        # 2-a. no pivot
        if pivot == -1:
            print('pattern 2-a')
            return self.BinarySearch(nums, 0, len(nums)-1, target)

        # 2-b. nums[pivot] == target
        if nums[pivot] == target:
            print('pattern 2-b')
            return pivot

        # 2-c. left part of the pivot
        if nums[0] <= target and target <= nums[pivot]:
            print('pattern 2-c')
            return self.BinarySearch(nums, 0, pivot, target)

        # 2-d. right part of the pivot
        if nums[(pivot+1)] <= target and target <= nums[-1]:
            print('pattern 2-d')
            return self.BinarySearch(nums, (pivot+1), len(nums)-1, target)

        return -1

    def findPivot(self, nums, left, right):
        # base case
        if left > right or len(nums) <= 1:
            return -1
        if left == right:
            return left

        # recursive
        mid = int((left + right)/2)

        # check if the mid is the pivot or not
        if left < mid and nums[mid-1] > nums[mid]:
            return mid-1
        if mid < right and nums[mid] > nums[mid+1]:
            return mid

        # if not, recursive
        if nums[left] >= nums[mid]:  # if pivot in this regeion
            return self.findPivot(nums, left, mid-1)
        elif nums[mid] >= nums[right]:  # if pivot in this regeion
            return self.findPivot(nums, mid+1, right)
        else:
            return -1

    def BinarySearch(self, nums, left, right, target):
        pivot = int((left + right)/2)
        print(nums)
        print(left, right, pivot)

        # check the true condition
        if left > right:
            return -1
        if target == nums[pivot]:
            return pivot

        # recursive
        if nums[pivot] < target:
            return self.BinarySearch(nums, pivot+1, right, target)
        elif target < nums[pivot]:
            return self.BinarySearch(nums, left, pivot-1, target)
