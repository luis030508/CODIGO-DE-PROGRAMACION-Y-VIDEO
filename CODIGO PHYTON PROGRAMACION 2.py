thon 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "coright", "credits" or "license()" for more information.
>>> #BIENVENIDA
>>> a= ("BIENVENIDOS AL JUEGO DEL AHORCADO")
>>> print ("bienvenidos al juego del ahorcado")
bienvenidos al juego del ahorcado
>>> #NOMBRE DE USUARIO
>>> b= ("CAMPO PARA INGRESAR NOMBRE DE USUARIO")
>>> print ("nombre de usuario")
nombre de usuario
>>> 
>>> #DIFICULTAD DEL JUEGO
>>> c= ("OPCION PARA ELEGIR DIFICULTAD DEL JUEGO")
>>> print ("dificultad del juego")
dificultad en el juego
>>> 
>>> #TIEMPO
>>> d= ("ELEGIR EL TIEMPO QUE SE DESEA PARA JUGAR")
>>> print ("seleccionar tiempo de juego")
seleccionar tiempo de juego
>>> 
>>> #INICIO DEL JUEGO
>>> e= ("Inicio del juego")
>>> print ("Buena suerte")
Buena suerte
>>> Buena suerte
SyntaxError: incomplete input
>>> 
>>> #FIN DEL JUEGO
>>> f= ("Mucho exito a la siguiente partida")
>>> g= ("Muy bien hecho, lo has logrado")
>>> print ("Mucho exito a la siguiente partida")
Mucho exito a la siguiente partida
>>> print ("Muy bien hecho, lo has logrado")
Muy bien hecho, lo has logrado



import time 
nombre=input (" ¿Cual es tu nombre? ")
print (" Bienvenido, "+nombre, " Llego el momento de iniciar el ahoracado ")
time.sleep(1)
print (" Es momento de jugar ")
palabra=" periodico "
tuacierto= ""
intentos=4


while intentos > 0 :
    errores=0
    for letra in palabra:
       if letra in tuacierto:
         print( letra, end="")
       else :
        print("-" , end="")
        errores+=1
    if errores==0:
        print(" Lo has logrado, sigue asi ") 
        break

    tuletra=input(" inserta una letra ")
    tupalabra += tuletra
    if tuletra not in palabra : 
        intentos-=1
        print("incorrecto")
        print(" te quedan ",+intentos," intentos ")
    if intentos == 0:
        print(" suerte a la proxima, no lo has logrado ")
else:
    print("agradecido por tu participacion")            



