# распетатывает базу данных в консоли

def print_data(data):
     print("Фамилия;Имя;Отчечтво;Номер телефона\n")
     print(*data, sep="\n")