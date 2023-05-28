# 1. Открывать файл (режим txt)
# 2. Создавать файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

#  Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
#  Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
#  для изменения и удаления данных.

# path = 'call.txt'
# data = open(path, 'w')
# for line in data:
#    print(line)
# data.close

def open_file_read(path):
   with open(path,'r') as file:
      main_list = file.readlines()
      main_list_str = [x.rstrip().split(':') for x in main_list]
   return main_list

print(open_file_read('Seminar8_HW\phones.txt')) 


def open_file_write(path, list_file):
   with open(path, 'w') as file:
      file.writelines([':'.join(x)+'\n' for x in list_file])
list_for_look = [['Ivanov''Ivan''165465''comments'], ['Petrov''Petr''665125''comments'], ['Sidorov''Grigoriy''798466''comments'], ['Frolov''Gennadiy''962145''comments'] ]
def look_list (list_for_look):
   print([' '.join(x) for x in list_for_look], end='\n')