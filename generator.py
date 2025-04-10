custom_words = ['red', 'green', 'yellow', 'pink', 'blue']
from random import randint

def randomSentenceGenerator(word) :
    randomIndex = randint(0,len(custom_words)-1)
    return f'{custom_words[randomIndex]} {word}'


with open('./text.txt') as file:
    parag = file.read()
    word_list = parag.split() #['&asdf', 'asdf']
    setence_list = list(map(randomSentenceGenerator,word_list))
    paraCount = int(input('paragraph count :'))

    for count in range(paraCount):
        with open('./generator.txt', 'a') as writefile :
            writefile.write(''.join(setence_list)+'\n\n')



