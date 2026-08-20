''''
nome = input('Digite seu nome: ')
cpf = input('Digite seu cpf: ')
idade = int(input('Digite sua idade:'))


print('Cadastro realizado com sucesso!')
print('Bem-vindo(a):', nome)
'''
''''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print('A soma dos números', num1, '+', num2, 'é:', soma)
print('A subtração dos números', num1, '-', num2, 'é:', subtracao)
print('A multiplicação dos números', num1, '*', num2, 'é:', multiplicacao)
print('A divisão dos números', num1, '/', num2, 'é:', divisao)
'''
''''
calculo1 = 10 + 2 * 10
calculo2 = (10 + 2) * 10

print(calculo1)
print(calculo2)
'''
'''''
soma = 5 + 2
print(soma)

subtracao = 5 - 2
print(subtracao)

multiplicacao = 5 * 2

divisao = 5 / 2
print(divisao)

mod = 5 % 2
print(mod)

divisaoexata = 5 // 2
print(divisaoexata)
'''
''''
idade=int(input('Digite sua idade: '))

print('Se passou 365 dias.')
idade = idade + 1

print('Sua idade hoje é de:', idade)
'''
'''''
tentativas = 3

print('Erro ao logar, você tem', tentativas - 1, 'tentativas para logar.')

tentativas = tentativas - 1
'''

#EXERCÍCIO 1

#FAÇA UM ALGORITMO PARA CALCULAR QUANTAS FERRADURAS SÃO NECESSÁRIAS PARA EQUIPAR TODOS OS CAVALOS DE UM HARAS.
''''
cavalos = int(input('Digite a quantidade de cavalos do haras: '))
print('São necessárias {} ferraduras para equipar todos os cavalos.'.format(cavalos * 4))
'''
#EXERCÍCIO 2

''''
Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos
dias de vida ela possui.
Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma
pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída:
MARIA, VOCÊ JÁ VIVEU 6935 DIAS.
'''
''''
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print('{} VOCÊ JÁ VIVEU {} DIAS.'.format(nome, idade * 365))
'''
#EXERCÍCIO 3

''''
A padaria Hotpão vende uma certa quantidade de pães franceses e uma
quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$
1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães
e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total
arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base
nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e
depois calcular os dados solicitados.
'''
'''''
paes = int(input('Digite a quantidade de pães vendidos: '))
broas = int(input('Digite a quantidade de broas vendidas: '))
total_arrecadado = (paes * 0.12) + (broas * 1.50)
poupanca = float(total_arrecadado * 0.10)

print('O total arrecadado foi de: R${} e o valor a ser guardado na poupança é de: R${:.2f}'.format(total_arrecadado, (poupanca)))


#EXERCÍCIO 4

''
O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.
Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos)
e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.
'''
'''
peso = float(input('Digite o peso do prato em quilos: '))
valor_a_pagar = peso * 12

print('O valor a pagar é de: R${}'.format(valor_a_pagar))

#EXERCÍCIO 5

'
Entrar com o dia e o mês de uma data e informar quantos dias se passaram
desde o início do ano.
Esqueça a questão dos anos bissextos e considere sempre que um mês possui
30 dias.

'''
dia=int(input('Que dia é hoje?: '))
mes=int(input('Que mês é hoje?: '))
print('Se passaram {} dias desde o início do ano.' .format((mes-1)*30+dia))
