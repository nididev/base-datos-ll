USERNAME = 'sistemas'
PASWORD = 'Abc123$'
INTENTOS_MAX = 3

intentos =0 
while intentos < INTENTOS_MAX:
    usuario = input ('Ingresa tu nombre de usuario')
    pasword = input ('Ingrese tu contrase: ')
    if usuario == USERNAME and pasword == PASWORD:
        print (f'Bienvenido{usuario}')
        break
    else: 
        intentos +1
        print (f'\nUsuario o contraseña incorrecto te queda {INTENTOS_MAX - 1}') 

else: 
    print('Se te han agotado los intentos')      
