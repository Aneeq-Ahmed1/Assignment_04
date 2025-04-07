# import random
# import time
# def naive_search(l, target):
#     for i in range(len(l)):
#         if l[i] == target:
#             return 1
#     return -1 


# def binary_search(l, target, low=None, high=None):
#     if low in None:
#         low = 0
#     if high is None:
#         high = len(l) - 1  

#     if high < low:
#         return -1      

#     midpoint = (len(l)) // 2

#     if l[midpoint] == target:
#         return midpoint
#     elif target < l[midpoint]:
#         return binary_search(l, target, low, midpoint-1 )
#     else:
#         return binary_search(l, target, midpoint+1, high)
    

# if __name__=='__main__':
#     l = [1,3,5,10,12]  
#     target = 10
#     print(naive_search(l, target))
#     print(binary_search(l, target))
  
#     length = 10000

#     sorted_list = set()
#     while len(sorted_list) < length
#         sorted_list.add(random.randint(-3*length, 3*length) ) 
#     sorted_list = sorted(list(sorted_list))
 
#     start = time.time()
#     for target in sorted_list:
#         naive_search(sorted_list, target)
#     end = time.time()
#     print("Naive search time" , (end - start/length, "seconds"))   








import random
import time

# Naive search (linear search)
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i  # return index, not 1
    return -1

# Binary search (recursive)
def binary_search(l, target, low=None, high=None):
    if low is None:  # ❌ Fixed: `in None` was invalid syntax
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2  # ❌ Fixed: should use `low` and `high`, not `len(l)`

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

# Main block
if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10

    print(f"Naive Search result: Index {naive_search(l, target)}")
    print(f"Binary Search result: Index {binary_search(l, target)}")

    # Create a large sorted list of unique integers
    length = 10000
    sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))  # ✅ Better and faster

    # Timing Naive Search
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time:", (end - start), "seconds")

    # Timing Binary Search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time:", (end - start), "seconds")
