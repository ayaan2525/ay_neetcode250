class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Create a dictionary to map elements of nums1 to their indices
        nums1_dict = {num: idx for idx, num in enumerate(nums1)}

        # Initialize a stack to keep track of the next greater elements
        mono_stack = []
        for num in reversed(nums2):
            
            # For numbers in nums1, find their next greater element
            if num in nums1_dict:
                index = nums1_dict[num]
                
                # keep popping if top of the sack is smaller than current num
                while mono_stack and mono_stack[-1] < num:
                    mono_stack.pop()

                if mono_stack:
                    nums1[index] = mono_stack[-1]
                else:
                    nums1[index] = -1
                mono_stack.append(num)
            else:
                # # keep popping if top of the sack is smaller than current num to store next greater element at top
                while mono_stack and mono_stack[-1] < num:
                    mono_stack.pop()
                mono_stack.append(num)
        return nums1
    
"""
Question: https://leetcode.com/problems/next-greater-element-i/
Time complexity: O(n), n is the number of elements in nums2
Space complexity: O(m), for dictionary used to store nums1 element with indices
"""
            