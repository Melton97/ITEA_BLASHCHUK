# Реализовать функцию bank, которая принимает следующие аргументы:
# сумма депозита, кол-во лет и процент.
# Результатом выполнения должна быть сумма по истечению депозита.
#git push

try:
    value_deposit = float(input('Введите сумму депозита:'))
    value_years = float(input('Введите количество лет:'))
    value_percent = float(input('Под какой процент желаете положить:'))
except (ValueError):
    print ('Введите пожалуйста число, а не строку!')
except (TypeError):
    print ('Введите пожалуйста корректное число!')


def bank(value_1, value_2, value_3):
    return value_1 + value_2*(value_1*(value_3/100))

result = bank(value_deposit, value_years, value_percent)

print (f'Ваша сумма по истечению срока: {result}')