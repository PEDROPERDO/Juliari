# Binary Search - Intersection of Two Array

from typing import List

def intersection_double_array(nums_one : List[int], nums_two : List[int]) -> List[int]:
  """
  >>> intersection_double_array([1, 2, 2, 1], [2, 2])
  [2]

  >>> intersection_double_array([4, 9, 5], [9, 4, 9, 8, 4])
  [9, 4]
  
  >>> intersection_double_array([-1, 2, -3, 4, -5], [2, -3, 4])
  [2, -3, 4]

  >>> intersection_double_array([1, 1, 1, 2, 2, 2], [1, 1, 2, 2])
  [1, 2]
  """
  nums_one = set(nums_one)
  nums_two = set(nums_two)
  return list(nums_one & nums_two)

if __name__ == "__main__":
  import doctest
  doctest.testmod()
