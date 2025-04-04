def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)

    print("Dinero recibido:")
    print(money)

    Vuelto = money - expense
    Pesos = int(Vuelto)
    Centavos = int(round((Vuelto - Pesos)*100))

    print("\nVuelto\n")
    print(f"Pesos:\n{Pesos}")
    print(f"Centavos:\n{Centavos}")
change()