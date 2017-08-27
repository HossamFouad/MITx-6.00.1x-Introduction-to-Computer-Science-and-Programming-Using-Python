"""
Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
"""
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
  i=1
  if k==0:
    return False
  while k>0:
    k-=i
    i+=1
  if k==0:
    return True
  else :
    return False
