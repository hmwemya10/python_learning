#if you want to modify the specific items of list USE filter() 
nums = [1,2,3,4,5,6,7,8,9,10]


# filter(function,list)  <- format
def Even(num) :
    return(num%2 == 0)


filter(Even,nums)
even_nums = list(filter(Even,nums))
print(even_nums)


nums_e = [num for num in nums if(num%2 == 0)]
print(nums_e)


evenNums = []

for num in nums :
    if (num%2 == 0) :
        # print(num)
        evenNums.append(num)

print(evenNums)