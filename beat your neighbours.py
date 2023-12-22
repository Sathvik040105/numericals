# def beat_your_neighbour(arr):
#     count = 4
#     if len(arr) == 1:
#         return (0,arr[0])
#     elif len(arr) > 1 and arr[0] > arr[1]:
#         return (0,arr[0])
#     elif len(arr) > 1 and arr[-1] > arr[-2]:
#         return (len(arr)-1,arr[-1])
#     for i in range(1,len(arr)-1):
#         if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#             print(count)
#             return(i,arr[i])
#         else:
#             count += 1
    
# print(beat_your_neighbour([9,11,21,14,11]))

#Time Complexity: O(n)
#No.of comparisons: 4 + (n-2) = n+2


def beat_your_neighbour_logn(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # If mid is a peak element, return mid.
        if (mid+1) > len(arr)-1 and arr[mid] > arr[mid - 1]:
            return (mid, arr[mid])
        elif mid-1 < 0 and arr[mid] > arr[mid + 1]:
            return (mid, arr[mid])
        elif arr[mid] > arr[mid - 1] and arr[mid] >= arr[mid + 1]:
            return (mid, arr[mid])

        # If mid is not a peak element and arr[mid - 1] > arr[mid], then the peak element must be on the left of mid.
        elif arr[mid - 1] > arr[mid]:
            high = mid

        # If mid is not a peak element and arr[mid + 1] > arr[mid], then the peak element must be on the right of mid.
        else:
            low = mid + 1

    return -1


print(beat_your_neighbour_logn([7,9,2,14,21,23,46]))
# print(beat_your_neighbour_logn([9,5,2,4,16,45]))
#Time Complexity: O(logn)
#No.of comparisons: logn + 2  
    
