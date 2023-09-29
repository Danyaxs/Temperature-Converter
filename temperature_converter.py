from rich.console import Console
from rich.table import Table
from rich import print

print('[bold][magenta][Добро пожаловать][/magenta] Это программа конвертирует градусы из одной величины в другую![/bold]')
def temperature_converter():
    print('[1] - Градус Кельвина')
    print('[2] - Градус Цельсия')
    print('[3] - Градус Фаренгейта')
    print('[4] - Градус Реомюра')
    print('[5] - Градус Ранкина')
    temp_num = int(input('Введите цифру, известной Вам величины, чтобы перевести её в другие единицы измерения: '))

    # Kelvin  Celsius  Fahrenheit  Reaumur  Rankin 
#############################################################################################################################################
    while True:
        if temp_num < 1 or temp_num > 5:
            print('[bold][red][Ошибка][/red] Введите цифру, исходя из предложенных значений выше[/bold]')
            temperature_converter()
        elif temp_num == 1:
            Kelvin = float(input('[Введите температуру] В градусах Кельвина: '))
            
            Celsius = round(Kelvin - 273.15, 2)
            Fahrenheit = round((9/5) * (Kelvin - 273.15) + 32, 2)
            Reaumur = round((Kelvin - 273.15) * (4/5), 2)
            Rankin = round(Kelvin * (9/5), 2)
            
            print()
            table = Table(title='Таблица конверсии температур из Кельвина в другие единицы измерения', title_style='bold red')

            table.add_column("Кельвины (K)", justify='center', style='#0000FF',)
            table.add_column("Градусы Цельсия (°C)", justify='center', style='#5b646e',)
            table.add_column("Градусы Фаренгейта (°F)", justify='center', style='#FF0000',)
            table.add_column("Градусы Реомюра (°Re)", justify='center', style='#008000',)
            table.add_column("Градусы Ранкина (°Ra)", justify='center', style='#0000FF',)

            table.add_row(str(Kelvin), str(Celsius), str(Fahrenheit), str(Reaumur), str(Rankin))
            
            console = Console()
            console.print(table)
#############################################################################################################################################
        elif temp_num == 2:
            Celsius = float(input('[Введите температуру] В градусах Цельсия: '))
            
            Kelvin = round(Celsius + 273.15, 2)
            Fahrenheit = round(Celsius * (9/5) + 32, 2)
            Reaumur = round(Celsius * (4/5), 2)
            Rankin = round((Celsius + 273.15) * (9/5), 2)
            
            print()
            table = Table(title='Таблица конверсии температур из Цельсия в другие единицы измерения', title_style='bold red')

            table.add_column("Градусы Цельсия (°C)", justify='center', style='#5b646e',)
            table.add_column("Кельвины (K)", justify='center', style='#0000FF',)
            table.add_column("Градусы Фаренгейта (°F)", justify='center', style='#FF0000',)
            table.add_column("Градусы Реомюра (°Re)", justify='center', style='#008000',)
            table.add_column("Градусы Ранкина (°Ra)", justify='center', style='#0000FF',)

            table.add_row(str(Celsius), str(Kelvin), str(Fahrenheit), str(Reaumur), str(Rankin))
            
            console = Console()
            console.print(table)
#############################################################################################################################################
        elif temp_num == 3:
            Fahrenheit = float(input('[Введите температуру] В градусах Фаренгейта: '))
            
            Kelvin = round((Fahrenheit - 32) * (5/9) + 273.15, 2)
            Celsius = round((Fahrenheit - 32) * (5/9), 2)
            Reaumur = round((Fahrenheit - 32) * (4/9), 2)
            Rankin = round(Fahrenheit + 459.67, 2)
            
            print()
            table = Table(title='Таблица конверсии температур из Фаренгейта в другие единицы измерения', title_style='bold red')
            
            table.add_column("Градусы Фаренгейта (°F)", justify='center', style='#FF0000',)
            table.add_column("Кельвины (K)", justify='center', style='#0000FF',)
            table.add_column("Градусы Цельсия (°C)", justify='center', style='#5b646e',)
            table.add_column("Градусы Реомюра (°Re)", justify='center', style='#008000',)
            table.add_column("Градусы Ранкина (°Ra)", justify='center', style='#0000FF',)

            table.add_row(str(Fahrenheit), str(Kelvin), str(Celsius), str(Reaumur), str(Rankin))
            
            console = Console()
            console.print(table)
#############################################################################################################################################
        elif temp_num == 4:
            Reaumur = float(input('[Введите температуру] В градусах Реомюра: '))
            
            Kelvin = round((Reaumur * (5/4)) + 273.15, 2)
            Celsius = round(Reaumur * (5/4), 2)
            Fahrenheit = round((Reaumur * (9/4)) + 32, 2)
            Rankin = round((Reaumur * (9/5)) + 491.67, 2)
            
            print()
            table = Table(title='Таблица конверсии температур из Реомюра в другие единицы измерения', title_style='bold red')

            table.add_column("Градусы Реомюра (°Re)", justify='center', style='#008000',)       
            table.add_column("Кельвины (K)", justify='center', style='#0000FF',)
            table.add_column("Градусы Цельсия (°C)", justify='center', style='#5b646e',)
            table.add_column("Градусы Фаренгейта (°F)", justify='center', style='#FF0000',)
            table.add_column("Градусы Ранкина (°Ra)", justify='center', style='#0000FF',)

            table.add_row(str(Reaumur), str(Kelvin), str(Celsius), str(Fahrenheit), str(Rankin))
            
            console = Console()
            console.print(table)
#############################################################################################################################################
        elif temp_num == 5:
            Rankin = float(input('[Введите температуру] В градусах Ранкина: '))
            
            Kelvin = round(Rankin * (5/9), 2)
            Celsius = round((Rankin - 491.67) * (5/9), 2)
            Fahrenheit = round((Rankin - 459.67), 2)
            Reaumur = round((Rankin - 491.67) * (4/9), 2)

            print()
            table = Table(title='Таблица конверсии температур из Ранкина в другие единицы измерения', title_style='bold red')
            
            table.add_column("Градусы Ранкина (°Ra)", justify='center', style='#0000FF',)
            table.add_column("Кельвины (K)", justify='center', style='#0000FF',)
            table.add_column("Градусы Цельсия (°C)", justify='center', style='#5b646e',)
            table.add_column("Градусы Фаренгейта (°F)", justify='center', style='#FF0000',)
            table.add_column("Градусы Реомюра (°Re)", justify='center', style='#008000',)       
            
            table.add_row(str(Rankin), str(Kelvin), str(Celsius), str(Fahrenheit), str(Reaumur))
            
            console = Console()
            console.print(table)
temperature_converter()
