class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # merge sort function
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        
        # merge function to combine two sorted arrays
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Append any remaining elements
            result.extend(left[i:])
            result.extend(right[j:])

            return result
        
        return merge_sort(nums)
    
    """
    Question: https://leetcode.com/problems/sort-an-array/
    Time Complexity: O(n log n), where n is the number of elements in the array.
    Space Complexity: O(n), due to the space used by the recursion stack and the merged
    
    """