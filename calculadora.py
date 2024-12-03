import os
import time
import operator

def calculadora(num1: float, num2: float, operador: str) -> float:
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '%':
        result = num1 % num2
    elif operador == '^':
        result = num1 ** num2

    return result

def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    """Calcula o resultado de uma operação matematica básica.

    Parametros
    ----------
    num1 : float
        Primeiro operador.
    num2 : float
        Segundo operador.
    operador : str
        Operador da operacão. e34rt5vh n-
        Pode ser "+", "-", "*" o "/".

    Returns
    -------
    float
        Resultado da operação.

    Raises
    ------
    ValueError
        Se o operador não for "+", "-", "*" ou "/".
    """
    operacoes = {
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "*": lambda: num1 * num2,
        "/": lambda: num1 / num2,
        "%": lambda: num1 % num2,
        "^": lambda: num1 ** num2,
    }
    funcao = operacoes.get(operador)
    if funcao:
        return funcao()

    return float("nan")


def calculadora_v3(num1: float, num2: float, operador: str) -> float:
    operadores = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
        "^": operator.pow}

    if operador in operadores:
        return operadores[operador](num1, num2)

    return float("nan")


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            numero1: float = float(input('Introduza o primeiro número:'))
            numero2: float = float(input('Introduza o segundo número:'))
            operacao: str = input('Introduza a operação a realizar (+ - / *) ou (% ^):')
            print(f'O resultado: {calculadora_v2(numero1, numero2, operacao)}')
            print()
            cont: str = input('Deseja continuar? (s/n):').lower()
            if cont == 'n':
                break

        except ValueError:
            print('Dados inválidos!-> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossivel dividir por zero!-> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
