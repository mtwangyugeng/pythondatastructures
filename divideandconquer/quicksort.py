def partition(nums, low, high):
    '''
    pick the value of nums[high] as pivot.
    throw all the values <= the pivot to the front
    then the pivot is on its sorted position. 
    (assuming the all values in nums[low : high + 1]
    are the only values that are smaller/ bigger
    than the pivot of the prevs recursion)

    @return: sorted pivot position
    '''
    pivot = nums[high]
    i = low - 1
    for j in range (low, high + 1):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    return i

def quicksort(nums, low, high): 
    ''' 
    Sorting with divide and conquer!
    '''
    if len(nums) == 1:
        return nums
    if (low < high):
        pi = partition(nums, low, high) # !important
        quicksort(nums, low, pi - 1)
        quicksort(nums, pi + 1, high)

nums = [1, 2, 3, 4, 6, 5, 0, 3, 0]
quicksort(nums, 0, len(nums)-1)
print(nums)