"""
Implement a function that meets the specifications below.

def sum_digits(s):
    assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. 
    # Your code here
For example, sum_digits("a;35d4") returns 12.

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
"""
def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    sum=0
    get=0
    flag=0
    for i in s:
     get=ord(i)-48
     if(get>=0 and get<=9):
       sum+=get
       flag=1
    
    if flag!=1:
     raise ValueError()
    return sum
