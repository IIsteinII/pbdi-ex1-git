def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

def menu():
    while True:
        print("Escolha uma opção:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "0":
            break
        elif escolha in ["1", "2", "3", "4"]:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = somar(x, y)
            elif escolha == "2":
                resultado = subtrair(x, y)
            elif escolha == "3":
                resultado = multiplicar(x, y)
            elif escolha == "4":
                resultado = dividir(x, y)

            print(f"Resultado: {resultado}\n")

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()