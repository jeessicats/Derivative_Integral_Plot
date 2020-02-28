linha = '+-' * 50
titulo = "Programa de Cálculo"
nome = "Jéssica Teixeira dos Santos"

print(linha)
print(titulo.center(100))
print(linha)

print(nome.rjust(100))

from math import sin, cos, exp, pi
import matplotlib.pyplot as plt
import sys

def h():
    return 0.0001

def graf_cos():
    plt.title("Cosseno", fontsize=16)

    i = 0
    y = []
    x = []

    while -10*pi < i < 10*pi:
        y.append(cos(i))
        x.append(i)
        i = i + 0.1

    plt.plot(x, y, color="blue")
    plt.show()

    return 10

def deri_cos():
    x = int(input("Digite um ponto no qual deseja calcular a derivada de cos(x): "))
    derivada = (-cos(x + 2 * h()) + 8 * cos(x + h()) - 8 * cos(x - h()) + cos(x - 2 * h())) / (12 * h())
    print("\nA derivada de cos(x) no ponto",x,"será: ",derivada,"\n")

    return 10

def inte_cos():
    a = int(input("Insira um valor inicial para a integral: "))
    b = int(input("Insira um valor final para a integral: "))
    n = 100
    delta = (b - a)/n
    integral = 0

    x = []
    y = []

    for i in range(n + 1):
        x.append(i*delta + a)
        y.append(cos(x[i]))

    for i in range(1, n):
        fator = 4
        if (i%2 == 0):
            fator = 2
        integral += fator*y[i]

    integral += y[0] + y[n]
    integral *= delta/3.0

    print("\nO valor da integral sera: ",integral,"\n")

    return 10

def graf_sin():
    plt.title("Seno", fontsize=16)

    i = 0
    y = []
    x = []

    while -10*pi < i < 10*pi:
        y.append(sin(i))
        x.append(i)
        i = i + 0.1

    plt.plot(x, y, color="green")
    plt.show()

    return 10

def deri_sin():
    x = int(input("Digite um ponto no qual deseja calcular a derivada de sen(x): "))
    derivada = (-sin(x + 2 * h()) + 8 * sin(x + h()) - 8 * sin(x - h()) + sin(x - 2 * h())) / (12 * h())
    print("\nA derivada de sen(x) no ponto",x,"será: ",derivada,"\n")

    return 10

def inte_sin():
    a = int(input("Insira um valor inicial para a integral: "))
    b = int(input("Insira um valor final para a integral: "))
    n = 100
    delta = (b - a)/n
    integral = 0

    x = []
    y = []

    for i in range(n + 1):
        x.append(i * delta + a)
        y.append(sin(x[i]))

    for i in range(1, n):
        fator = 4
        if (i % 2 == 0):
            fator = 2
        integral += fator*y[i]

    integral += y[0] + y[n]
    integral *= delta/3.0

    print("\nO valor da integral sen(x) é: ",integral,"\n")

    return 10

def graf_exp():
    plt.title("Exponencial", fontsize=16)

    i = 0
    y = []
    x = []

    while -10*pi < i < 10*pi:
        y.append(exp(i))
        x.append(i)
        i = i + 0.1

    plt.plot(x, y, color="red")
    plt.show()

    return 10

def deri_exp():
    x = int(input("Digite um ponto no qual deseja calcular a derivada de exp(x): "))
    derivada = (-exp(x + 2 * h()) + 8 * exp(x + h()) - 8 * exp(x - h()) + exp(x - 2 * h())) / (12 * h())
    print("\nA derivada de exp(x) no ponto",x,"será: ",derivada,"\n")

    return 10

def inte_exp():
    a = int(input("Insira um valor inicial para a integral: "))
    b = int(input("Insira um valor final para a integral: "))
    n = 100
    delta = (b - a)/n
    integral = 0

    x = []
    y = []

    for i in range(n + 1):
        x.append(i * delta + a)
        y.append(exp(x[i]))

    for i in range(1, n):
        fator = 4
        if (i % 2 == 0):
            fator = 2
        integral += fator * y[i]

    integral += y[0] + y[n]
    integral *= delta/3.0

    print("\nO valor da integral sera: ",integral,"\n")

    return 10

while (1):

    while(1):
        função = int(input("Digite 1, 2 ou 3 para escolher uma das seguintes funções:\n1. cos(x)\n2. sen(x)\n3. exp(x)\nOu -1 para sair.\n"))  # 1 para seno, 2 para cosseno e 3 para exponencial
        if(função >= 4 or função < -1 or função == 0):
            print("\nDigite um valor válido!\n")
        elif (função == -1):
            sys.exit()
        else:
            break

    calculo = int(input("O que você gostaria de fazer com está função?\n1. Plotar um gráfico desta função.\n2. Calcular a derivada deste função.\n3. Calcular a integral desta função.\n"))

    if (função == 1):
        if (calculo == 1):
            função = graf_cos()
        elif (calculo == 2):
            função = deri_cos()
        elif (calculo == 3):
            função = inte_cos()
        else:
            print("\nDigite um valor válido!\n")
            calculo = int(input("O que você gostaria de fazer com está função?\n1. Plotar um gráfico desta função.\n2. Calcular a derivada deste função.\n3. Calcular a integral desta função.\n"))

    elif (função == 2):
        if (calculo == 1):
            função = graf_sin()
        elif (calculo == 2):
            função = deri_sin()
        elif (calculo == 3):
            função = inte_sin()
        else:
            print("\nDigite um valor válido!\n")
            calculo = int(input("O que você gostaria de fazer com está função?\n1. Plotar um gráfico desta função.\n2. Calcular a derivada deste função.\n3. Calcular a integral desta função.\n"))

    elif (função == 3):
        if (calculo == 1):
            função = graf_exp()
        elif (calculo == 2):
            função = deri_exp()
        elif (calculo == 3):
            função = inte_exp()
        else:
            print("\nDigite um valor válido!\n")
            calculo = int(input("O que você gostaria de fazer com está função?\n1. Plotar um gráfico desta função.\n2. Calcular a derivada deste função.\n3. Calcular a integral desta função.\n"))

    else:
        print("\nDigite um valor válido!\n")
        função = int(input("Digite 1, 2 ou 3 para escolher uma das seguintes funções:\n1. cos(x)\n2. sen(x)\n3. exp(x)\n"))  # 1 para seno, 2 para cosseno e 3 para exponencial