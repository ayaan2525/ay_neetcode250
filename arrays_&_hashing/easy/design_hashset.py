class MyHashSet:

    def __init__(self):
        self.hashset = [-1]*1000001

    def add(self, key: int) -> None:
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        self.hashset[key] = -1

    def contains(self, key: int) -> bool:
        if self.hashset[key] == 1:
            return True
        else:
            return False
"""
Time complexity: O(1)
Space complexity: O(1000001), where 1000001 is the size of the map
Question: https://leetcode.com/problems/design-hashset/
"""