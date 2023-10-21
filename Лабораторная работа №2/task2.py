money_capital: int = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_counter = 0  # Счетчик месяцев
while money_capital > 0:
    money_capital += salary
    money_capital -= spend
    spend += spend * increase
    if money_capital <= 0:
        print("Количество месяцев, которое можно протянуть без долгов:", month_counter)
    month_counter += 1
