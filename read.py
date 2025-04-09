# file = open('./text.txt')
# for line in file:
#     print(line)

# file.seek(0) #move to cursor to starting point

# lineLists = file.readlines()
# print(lineLists)


# file.seek(20)
# paragraph = file.read(100) # read only 100 characters
# print(paragraph)

# file.close() 

with open('./text.txt') as file :  # no need to use close()
    for line in file:
        print(line)

print('do other task')