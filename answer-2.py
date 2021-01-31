# Python code to remove duplicate elements
def duplicate_removal(arr):
    if((len(arr)>=1) and (len(arr)<=1000000)):
        final_list = []
        for num in arr:
            if num not in final_list:
                final_list.append(num)
        return final_list
    else:
        return "out of bounds"
     
# Driver Code
arr = [1,2,3,4,4,2,1,5,1,4,5]
print(duplicate_removal(arr))

# simple solution could have been to just convert it to a set.

# for locating the duplicates of the array, we need to visit all the elements atleast once. As such, O(nlogn) time complexity is not possible at all.
