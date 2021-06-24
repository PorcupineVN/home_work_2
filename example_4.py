prices=[20.14, 199.07, 292.48, 10.05, 937.49, 158.90, 427.99, 1050.68, 528.41, 612.50, 739.88]
print(prices)
for price in prices:
    price*=100
    r = int(price //100)
    kk = int(price%100)
    if kk < 10:
        kk = '0' + str(kk)
    print(f'{r} руб {kk} коп')
print('Адрес оригинального списка:', id(prices))
prices.sort()
print('Цены в порядке возрастания:', *prices)
print('Адрес отсортированного списка:', id(prices))
prices_reverse = list(reversed(prices))
print(*prices_reverse)
print('Пять самых дорогих товаров:', *prices[-5:])
