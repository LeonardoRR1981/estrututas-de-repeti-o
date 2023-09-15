pessoas = 0
total = 0
soma_idade =0
while True:
 idade = input('Qual sua idade? ')
 
 if (idade == 'sair'):
    break 
 idade = int(idade)
     
 if (idade < 3):
    preco = 0
    print('O ingresso de de graça!!')
    pessoas += 1
    total += 0
    soma_idade += idade
    
 elif (idade <= 12):
    preco = 15
    print('O ingresso custa R$ 15')
    pessoas += 1
    total += 15
    soma_idade += idade
    
 elif (idade > 12):
    preco = 30
    print('O ingresso custa R$ 30')  
    pessoas += 1
    total += 30
    soma_idade += idade
    
print('O total de pessaos que compraram ingresso foram de {}'.format(pessoas))

print('O valor total a se pagar e R$ {:.2F}'.format(total))

print('A media de idade é de {:.2f}'.format(soma_idade / pessoas))
     
     

 
 
    

    
    