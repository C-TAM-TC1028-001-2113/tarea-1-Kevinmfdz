def main():
    # escribe tu código abajo de esta línea
    mes_anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldo_final = (mes_anterior + ingresos - egresos - (cheques  * 13)) - ((mes_anterior + ingresos - egresos - (cheques * 13)) * 0.075) 

    print("El saldo final de la cuenta es:", saldo_final)


if __name__ == '__main__':
    main()
