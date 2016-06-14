class char:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_name(self, name):
        print('My name is {}'.format(name))
    def say_age(self, age):
        print('I am {}'.format(int(age)))
    def __int__(self):
       if int(self) < 18:
           print(' < 18')
       else:
           print(' > 18')
              

char_1 = char('alex','15')
char_2 = char('kate','13')

names = [] #для определения имени к кому обращаются

chars = [char_1, char_2]
for i in chars:
    names.append(i.name)

dialog = input('=>>')
for i in names:
    if i in dialog:
        for j in chars:
            if i == j.name:
                current_char = j #нужен для того что бы знать на ком исп сейнейм и тд


keys = {'name' :(current_char.say_name, current_char.name), 'age' : (current_char.say_age, current_char.age)}
for i in keys:
    if i in dialog:
        keys[i][0](keys[i][1])
        if i == 'age':
            print(keys[i][1])
"""
if i == 'age':
print(int(keys[i][1]) )   
"""        
