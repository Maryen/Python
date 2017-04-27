import time
manual_list = [ ]
first_input = None

while first_input != 'add' or 'generate':  # Что если ввели неправильное ключевое слово 
        first_input = input('\n Input keyword \"add\" or \"generate\": ')
                
        if first_input == 'add':
            num_elements = int(input('\n Input number of element\'s in list: '))

            while num_elements > 0:  # Обеспечиваем ввод нужного количества данных
                elements = input('New element for the list: ')
                num_elements -= 1
                manual_list.append(elements)

            if len(manual_list) <= 0:  # Проверяем содержит ли лист данные
                print('List is empty or number of items less than zero!')
                manual_list.clear()
            else:
                print('\n Manual list consist of: ', manual_list)
                manual_list.clear()
          
        elif first_input == 'generate':
            range_from = int(input('\n Input number for starting the range: '))
            range_to = int(input('Input number for range up to: '))
            gen_list = [list for list in range(range_from, range_to)]  # range_to + 1)]

            if len(gen_list) <= 0: # Проверяем содержит ли лист данные
                print('List is empty or number of items less than zero!')
            else:
                print('\n Generate lits consist of: ', gen_list)

 

