# -*- coding: utf-8 -*-
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
criptografada = []
cont = 0

print('_________________________________##CRIPTOGRAFIA:##_________________________________\n')
print('Programa para criptografar e descriptografar mensagens. Baseado na cifra de Cesar!')
print('___________________________________________________________________________________\n\n')

entrada = input("Digite a mensagem: ") #Frase a ser criptografada ou descriptografada
entrada = entrada.upper() #transformando entrada em caixa alta

print("\nDeseja criptografar ou descriptografar? ") #ação para saber se a mensagem sera criptografada ou descriptografada
acao = input("Digite 'c' para criptografar ou 'd' para descriptografar: ")
acao = acao.lower() #transformando entrada em caixa baixa

if acao != 'c' and acao != 'd': #condição para verificar se a 'acao' atende aos requisitos
    while acao != 'c' and acao != 'd': #loop prende o usuario até que a condição seja atendida
        print("\nOpção inválida! ")
        acao = input("Digite 'c' para criptografar ou 'd' para descriptografar: ")
        acao = acao.lower()

modif = int(input("\nDigite um modificador de 0 até 26: ")) #variavel para modificar a posição das letras equivalentes; ex: se 1 -> 'A' = 'B'

if modif > 26 or modif < 0: #condição para verificar se 'modif' não é maior que o alfabeto
    while modif > 26 or modif <0 : #loop prende o usuario até que a condição seja atendida
        print('\nNão é possivel utilizar o valor! ')
        modif = int(input("Digite novamente um modificador de 0 até 26: "))

if acao == 'c': #se entrada = 'c', a mensagem será criptografada
    for i in entrada:
        if i in alfabeto:
            cont = alfabeto.index(i) #se i estiver no alfabeto, cont recebe a posição da letra no alfabeto
            posicaoEntrada = cont + modif #trocará a letra equivalente pela letra na posição + o modificador
            if posicaoEntrada > len(alfabeto): #se a posição ultrapassar o numero de letras do alfabeto, ele começará de novo
                posicaoEntrada = posicaoEntrada - len(alfabeto)
    
            criptografada.append(alfabeto[posicaoEntrada]) #adiciona à mensagem final a letra na posição
    
        else: #caracteres diferentes de letras não passarão pelo processo, serão adicionados diretamente.
            criptografada.append(i)

if acao == 'd': #se entrada = 'd', a mensagem será descriptografada
    for i in entrada:
        if i in alfabeto:
            cont = alfabeto.index(i) #se i estiver no alfabeto, cont recebe a posição da letra no alfabeto
            posicaoEntrada = cont - modif #trocará a letra equivalente pela letra na posição - o modificador (pois é a ação reversa a de criptografar)
            if posicaoEntrada < 0: #se a posição for menor que 0, ele começará da ultima letra, z.
                posicaoEntrada = posicaoEntrada + len(alfabeto)
    
            criptografada.append(alfabeto[posicaoEntrada]) #adiciona à mensagem final a letra na posição
    
        else:
            criptografada.append(i)

print('\n\n__________________________________##RESULTADO:##___________________________________\n')

print("Mensagem criptografada: ", ''.join(criptografada)) #parametro .join junta os itens na lista pelo definido entre os apostrofes; ex: se passasemos a lista [A,P,S] pelo '&'.join, imprimiria: A&P&S
print('\n___________________________________________________________________________________\n')