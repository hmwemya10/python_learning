with open('./about.txt','w') as file : #default is read(), add 'w' to change write()
    file.write('hmmk')
    file.write('\n20 yrs old')

##after doing other task

with open('./about.txt','w') as file : 
    file.write('overwritten')

with open('./about.txt','a') as file : 
    file.write('added other sentences not overwritten')

lists = ['\n hmmk','\n 20 yrs', '\n hello']
with open('./about.txt','a') as file : 
    file.writelines(lists)

