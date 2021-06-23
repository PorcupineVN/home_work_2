crew = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for man in crew:
    man_info = man.split()
    name = man_info[-1].capitalize()
    print(f'Привет, {name}!')