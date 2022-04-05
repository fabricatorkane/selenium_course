assert abs(-42) == 42

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
print(index)
if index != -1:    # возвращает индекс первого вхождения подстроки в строку и -1, если подстрока не найдена
    print(f'Substring found at index {index}')
