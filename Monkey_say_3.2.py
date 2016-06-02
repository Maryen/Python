monkey_say = 'MyShecNameedeismyname'
alph = input('Enter key-word(empty input will end the input): ')

def check(alph):
    abc = []
    while alph:
        abc.append(alph)
        alph = input('Enter key-words: ')
    return abc
    
abc = list(check(alph))
print('Key-words are: ',abc)

abcd = list(map(lambda x: x.title(),abc))
abcd.extend(abc)
    
def monkey(abcd,monkey_say):    
    sh = [i for i in range(len(monkey_say))]
    for i in abcd:
        start = 0
        count = monkey_say.count(i)
        while count:
            j = monkey_say.find(i, start)
            start = j + 1
            sh.insert(j,i)
            count -= 1
            sh.pop(j+1)
    shh = list(filter(lambda x:str(x).isalpha(),sh))
    mystr = ' '.join(shh)
    return mystr
print(monkey(abcd,monkey_say))

