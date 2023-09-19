"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        f = foo(x - 1)
        s = foo(x - 2)
        return f + s
    pass
  

def longest_run(mylist, key):
    longest_len = 0
    current_len = 0  
  
    for item in mylist:
        if item == key:
            current_len += 1
        else:
            if current_len > longest_len:
                longest_len = current_len
            current_len = 0

    if current_len > longest_len:
        longest_len = current_len

    return longest_len

  
  
  pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    def divide_and_conquer(left_size, right_size):
        if left_size == right_size:
            return (1 if mylist[left_size] == key else 0, 1)

        mid = (left_size + right_size) // 2

        left_result = divide_and_conquer(left_size, mid)
        right_result = divide_and_conquer(mid + 1, right_size)

        current_run = 0

        if mylist[mid] == key:
            current_run = left_result[1] + right_result[1]

        longest_size = max(left_result[0], right_result[0], current_run)

        return (longest_size, current_run)

    result = divide_and_conquer(0, len(mylist) - 1)
    return result[0]
pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


