# Write a function to find all pairs of an integer 
# array whose sum is equal to a given number. 
# Do not consider commutative pairs.

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