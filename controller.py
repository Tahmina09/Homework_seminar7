import view as v
import funcs as f 

def phone_button():
    menu_item = v.menu()
    if menu_item == "1":
        f.add_contact()
    elif menu_item == "2":
        print(f.del_contact())
    elif menu_item == "3":
        print(f.search_data())
    elif menu_item == "4":
        f.import_book()
    elif menu_item == "5":
        print(f.export_data())
    else:
        print('Такой команды не обнаружено. Попробуйте ещё раз!')