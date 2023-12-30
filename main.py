# hello



meters = float(input("Введіть кількість метрів: "))


operation = input("Виберіть операцію (mile, inch, yard): ")


if operation == "mile":
    result = meters * 0.000621371
    print(f"{meters} метрів дорівнює {result} миль")
elif operation == "inch":
    result = meters * 39.3701
    print(f"{meters} метрів дорівнює {result} дюймів")
elif operation == "yard":
    result = meters * 1.09361
    print(f"{meters} метрів дорівнює {result} ярдів")
else:
    print("Невірна операція. Будь ласка, виберіть 'mile', 'inch' або 'yard'.")