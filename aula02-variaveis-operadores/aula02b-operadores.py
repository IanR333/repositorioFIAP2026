from sympy import false

num1 = 5
num2 = 2
print(type(num1), type (num2))

resultado_op = num1 / num2
print(resultado_op, type(resultado_op))

#OPERADORES DE ATRIBUIÇAO

num = 15
print() #pule uma linha
print(num)

num=num+2
print(num)

num+= 2
print(num)

#OPERADORES RELACIONAIS
# >
#<

print(6>6) # retorna um valor bool

idade = 20
print(idade >= 21 )

logado = false
print(logado,type (logado))

maior_idade = idade >= 18
print(maior_idade, type (maior_idade))

# strings

nome1 = "marcos"
nome2 = "marcos"

print(nome1.upper() == nome2.upper())




