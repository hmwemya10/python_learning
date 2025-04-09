with open('./text.txt') as file:
    parag = file.read()

    ParaCount = int(input('para count: '))
    for count in range(ParaCount):
        with open('./generator.txt', 'a') as writefile :
            writefile.write(parag+'\n\n')

 