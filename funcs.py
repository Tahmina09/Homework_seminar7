def export_data():
    data_B = []
    with open('Telephone-Book.txt', 'r', encoding='utf-8') as file:
        data_B = file.read()
        list_cont = data_B.split("\n\n")
    return list_cont


def import_book():
    name = input('Введите имя файла, из которого импортируется телефонная книга - ')
    data = export_data()
    with open ('Telefon_Book.txt', 'a') as f:
        f.write(data_file + '\n\n')


def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    telephone = input('Введите телефон: ')    
    with open('Telephone-Book.txt', 'a', encoding= 'UTF - 8') as data:
        data.write(f'\n\n{surname} \n{name} \n{telephone}')
        

def search_data():
    data = export_data()
    data_list = []
    val = 1
    word = input('Введите имя или фамилию -> ')
    for line in data:
        if word in line:
            val = 0
            data_list.append(line)
            
    if val: print('Такого контакта нет!')
    return data_list
            

def del_contact():
    data = export_data()
    find = search_data()
    if find != []:
        if len(find) == 1:
            for i in range(len(data) - 1):
                if data[i] == find[0]:    
                    data.pop(i)
                    new_str = "\n\n".join(data)
                
                    with open('Telephone-Book.txt', 'w', encoding='utf-8') as file:
                        file.write(new_str)
                        break
        else:
            print('Найдено несколько контаков!')
            print(find)
            index_find = int(input('Введите индекс удаляемого контакта: '))

            if index_find >= 0:
                for i in range(len(data) - 1):
                    if data[i] == find[index_find]:    
                        data.pop(i)
                        new_str = "\n\n".join(data)
                
                with open('Telephone-Book.txt', 'w', encoding='utf-8') as file:
                    file.write(new_str)
        
    else:
        print('Контакт не найден!')
        
print(del_contact())