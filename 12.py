nome = input('Nome de usuário com 4 caracteres ou mais: ')

while len(nome) <= 3:
    print('Nome invalido.')
    nome = input('Nome de usuário com 4 caracteres ou mais: ')
    
    if (len(nome) >= 4):
     print('Nome valido')
     continue
    
idade = int(input('Qual sua idade? '))

while (idade > 150 ):
    print('Idade invalida.')
    idade = int(input('Qual sua idade? '))
    
    if (idade >= 0 and idade <= 150):
      print('Idade valida.')
      continue        
         
sal = float(input('Quanto é seu salario? '))   

while (sal <= 0):
    print('Salario invalido')   
    sal = float(input('Quanto é seu salario? '))   
    
    if (sal >= 1):
        print('Salario valido')
        continue
    
sexo = input(('Qual seu sexo? (f) ou (m): '))    
    
if (sexo == 'f'):
    print('Sexo feminino.')
     
elif (sexo == 'm'):
    print('Sexo masculino')   
    
estado = input('Qual seu estado civil? (s), (c), (v), (d): ')

if (estado == 's'):
    print('Solteiro')
    
elif (estado == 'c'):
    print('Casado')
    
elif (estado == 'v'):
    print('Viuvo')

elif (estado == 'd'):
    print('Divorsiado')
    

    
    
    
    
    
    
    
    
    