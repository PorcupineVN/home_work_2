# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(message)):
    count_digit = 0
    for j in range(len(message[i])):
        if message[i][j].isdigit():
            count_digit +=1
            index= j
    if count_digit==1:
        message[i] = message[i][:j] + '0' + message[i][j:]
        message[i] = (f'"{message[i]}"')
    elif count_digit > 1:
        message[i] = (f'"{message[i]}"')
print(*message)