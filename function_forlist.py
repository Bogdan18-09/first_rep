
def new_list_for_happy():
    my_llist = []
    n = int(input("Введите длину списка чисел : "))
    for i in range(n):
        output_index_type = int(input(f'Выберите тип данных для {i+1} элемента 1-int 2-str 3-list 4-dict '))
        if output_index_type==1:
            enter_index=int(input(f"Введите ваше число : "))
            my_llist.append(enter_index)
        elif output_index_type == 2:
            enter_index=input(f'Введите вашу строку : ')
            my_llist.append(enter_index)
        elif output_index_type==3:
            enter_index=list(input(f'Введите ваш список : '))
            my_llist.append(enter_index)
    #     Выбор типа данных для dict key
        if output_index_type==4:
            select_type_key=int(input(f'Выберите тип данных для ключа 1-int 2-str 3-list: '))
            if select_type_key==1:
                _key=int(input('Введите ваше число : '))
            if select_type_key == 2:
                _key=input('Enter youre string : ')
            if select_type_key == 3:
                _key =list(input('Enter youre list : '))

            #     выбор типа данных для value
            select_value_type=int(input('enter types of value 1-int  2-str  3-list '))
            if select_value_type ==1:
                _value=int(input('Enter youre integer : '))
            if select_value_type == 2:
                _value=input('Enter youre string : ')
            if select_value_type == 3:
                _value=list(input('Enter youre list : '))            
            my_llist.append({_key : _value})
    print(my_llist)
new_list_for_happy()