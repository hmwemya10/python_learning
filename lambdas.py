def add(n1,n2):
    return n1+n2

print(add(3,6))



add_lam = lambda n1,n2 : n1+n2

print(add_lam(5,1))

######### filter() function
nums = [1,2,3,4,5,6,7,8,9,10]



even_nums = list(filter(lambda num: (num%2 ==0 ),nums))
print(even_nums)


##### map function()

nums = list(map(lambda num: num*2,nums))
print(nums)