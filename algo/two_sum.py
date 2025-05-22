from typing import List, Dict


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return the indices of the two numbers such that they add up to `target`.

    Approach
    --------
    Single-pass hash-map:
      • iterate once, keeping a map {value: index}
      • on each element `n`, look for `target − n` in the map
      • if found, return the stored index and current index

    Complexity
    ----------
    Time : O(n)    – one pass over the list
    Space: O(n)    – hash-map grows with input size
    """
    index_map: Dict[int, int] = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in index_map:  # complement seen earlier
            return [index_map[diff], i]
        index_map[n] = i  # remember current value’s index
    return []  # no solution found
