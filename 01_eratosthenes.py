# Sieve of Eratosthenes (Eratosthenovo síto)
def array_range(start, end):
    array = []
    for i in range(start, end):
        array = array + [i]
    return array
    
"""
>>> array_range(2, 10)
[2, 3, 4, 5, 6, 7, 8, 9]
"""
def is_multiple(x, y):
    return (x % y) == 0
    
"""
>>> is_multiple(4, 2)
True
>>> is_multiple(4, 3)
False
"""
def remove_multiples(num, array):
    result = []
    for el in array:
        if not is_multiple(el, num):
            result = result + [el]
        # print(el, result)
    return result
    
"""
>>> remove_multiples(2, [2, 3, 4, 5, 6, 7, 8, 9])
[3, 5, 7, 9]
"""
def get_primes(n):
    nums = array_range(2, n)
    primes = []
    while len(nums) != 0:
        prime = nums[0]
        primes = primes + [prime]
        nums = remove_multiples(prime, nums)
        # print(nums, primes)
    return primes
    
"""
>>> get_primes(10)
[2, 3, 5, 7]
"""
# Úkol 3.15
"""
>>> is_subarray([1, 2, 2], [2, 1, 1, 2, 4, 2])
True
>>> is_subarray([1, 1, 2], [1, 1, 2])
True
>>> is_subarray([1, 1, 2], [1, 2, 2])
False
>>> is_subarray([2, 1, 2], [1, 2, 2])
False
"""
