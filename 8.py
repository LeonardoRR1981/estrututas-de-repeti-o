print('+ Adicão')
print('- Subitração')
print('* Mutiplicação')
print('/ Divisão')


op = input('Qual operação deseja fazer? ')
if (op =='+' or op == '-' or op == '*' or op == '/' ):
   v1 = int(input('Digite um valor: '))
   v2 = int(input('Digite outro valor: '))

if(op == '+'):
  print('{} + {} = {}'.format(v1, v2, v1 + v2))
  
elif(op == '-'):
    print('{} - {} = {}'.format(v1, v2, v1 - v2))

elif(op == '*'):
      print('{} * {} = {}'.format(v1, v2, v1 * v2))   

elif(op == '/'):
    print('{} / {} = {}'.format(v1, v2, v1 / v2))
       
else:
    print('Inválido')

print('Saindo do programa')
        
       
       
    
