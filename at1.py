while True:
    try:
        a=int(input("digite um numero:"))
        
    except ValueError:
        print("digite um numero inteiro")
        continue
    if a == 0:
        print("seu numero é zero")
    elif a < 0:
        print("seu numero é negativo")
    else:
        print("seu numero é positivo")
