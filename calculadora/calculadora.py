#Define a função "calculadora" que recebe a operação e dois numeros
def calculadora(operacao, num1, num2):
    #verifica se a operação escolhida é uma soma
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else: 
        return "operação inválida"
    
print("*"*30)
print('Calculadora em python'.upper())
print("*"*30)

print('Insira os numeros e a operação desejada: ')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

operacao = input('Digite a operação desejada:\n + para somar\n - subtrair \n * multiplicar \n / dividir \n')

#chama a função calculadora passando os paramentros necessarios 
# e guardando o resultado
resultado = calculadora(operacao, num1, num2)

#imprime a operação e o resultado formatados com duas casas decimais
print(f'{num1} {operacao} {num2} = {round(resultado,2)}')


    

    