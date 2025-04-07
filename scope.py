#global variable
name = "EMERALD"

def sayMyName() :
    #local variable
    global name
    name = "samantha"
    print(name) #local -> samantha, global -> samantha

sayMyName();

print(name) #global -> emerald, global overwrite -> samantha