def subsets(nums):
    res = []

    def backtrack(start, path):
        # record current subset
        res.append(path[:])

        # explore further choices
        for i in range(start, len(nums)):
            # choose nums[i]
            path.append(nums[i])

            # recurse with next index
            backtrack(i+1, path)

            # undo choice, backtrack
            path.pop()

        backtrack(0, [])
        return res