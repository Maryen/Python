monkey_say = 'MyShecnameedeis'
abc = list({'my', 'name', 'is'})

def monkey(abc,monkey_say):

    abcd = list(map(lambda x: x.title(),abc))
    abc.extend(abcd)
    general_list = list(map(lambda x: monkey_say.partition(x),abc))

    """
general_list - создает список с кортежами из 3 элементов
semi_list - должен найти обработать список убрав слова не входящие в abc
но не ищет по картежу, а преобразование general_list в строку через join(лист)
не работает если внутри листа есть картеж.
    """

    semi_list = list(map(lambda x: general_list.find(x),abc)) 
    
    return semi_list
    
                        
print(monkey(abc,monkey_say))




# можно сделать через s.coun('a', [start:end])

