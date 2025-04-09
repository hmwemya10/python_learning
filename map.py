nums = [2,5,6,7,8,9,10]

#map(function,list) <- format

def mapFunction(num) : #num is from list(nums)
    return num*2

map(mapFunction,nums)
list(map(mapFunction,nums)) #<- map to list type casting
nums = list(map(mapFunction,nums))
print(nums) 



