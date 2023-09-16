nome = input('Entre com seu nome: ')
senha = input('Entre com sua senha: ')

while (nome == senha):
    print('A senha não pode ser igual ao nome, tente de novo: ')
    nome = input('Entre com seu nome: ')
    senha = input('Entre com sua senha: ')
    continue
    
    if (nome != senha):
     break         
 
print('Acesso consedido.')