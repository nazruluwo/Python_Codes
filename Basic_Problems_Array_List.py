# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']

def pair_sum(myList, sum):

    seen = set()
    output = set()

    for num in myList:
        target = sum - num
        if target not in seen:
            seen.add(num)
        else:
            #output.add((min(num, target), max(num, target)))
            tv= str(min(num, target)) + '+' + str(max(num, target))
            output.add(tv)

    return output


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

#SOLUTION - Duplicate Number O(n)
def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]

#Alternate Solution O(n^2)
def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example :

#Input: nums = [1,2,3,1]
#Output: true


def contains_duplicate(nums):
    seen = {}
    for i in nums:
       if seen.get(i):
            print('Duplicate Found')
            return True
       else:
            seen[i]=1
            
    return False

nums = [1,2,3,1]

print(contains_duplicate(nums))