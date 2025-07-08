class MyHashMap:

    def __init__(self):
        self.map = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1    


"""
Time complexity: O(1)
Space complexity: O(1000001), where 1000001 is the size of the map
Question: https://leetcode.com/problems/design-hashmap/
"""