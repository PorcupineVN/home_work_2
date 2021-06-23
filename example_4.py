import random
n_products = 20
prices=[round(random.uniform(0, 1000), 2) for i in range(n_products)]
print(prices)
for price in prices:
    r = int(price//1)
    kk = int((price%1)*100)
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
