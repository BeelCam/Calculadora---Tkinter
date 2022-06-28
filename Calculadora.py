from tkinter import *
from math import *

#VISUALIZAR LA OPERACION EN LA PANTALLA
def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
 
#CÁLCULO Y MUESTRA DE RESULTADOS.
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""
 
#LIMPIAR PANTALLA.
def limpiar():
    global operador
    operador=("")
    input_text.set("0")
 
 
ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("392x600")
#ventana.iconbitmap("calculadora.ico")

#Dimencion de los botones
anchoBoton = 8
altoBoton = 3
input_text=StringVar()
operador=""
 
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,justify="right")
Salida.place(x=10,y=60)
 
#AÑADIR BOTONES.
#CREAMOS NUESTROS BOTONES
Button(ventana,text="0",width=anchoBoton,height=altoBoton,command=lambda:btnClik(0),bg="light grey").place(x=17,y=180)
Button(ventana,text="1",width=anchoBoton,height=altoBoton,command=lambda:btnClik(1),bg="light grey").place(x=107,y=180)
Button(ventana,text="2",width=anchoBoton,height=altoBoton,command=lambda:btnClik(2),bg="light grey").place(x=197,y=180)
Button(ventana,text="3",width=anchoBoton,height=altoBoton,command=lambda:btnClik(3),bg="light grey").place(x=287,y=180)
Button(ventana,text="4",width=anchoBoton,height=altoBoton,command=lambda:btnClik(4),bg="light grey").place(x=17,y=240)
Button(ventana,text="5",width=anchoBoton,height=altoBoton,command=lambda:btnClik(5),bg="light grey").place(x=107,y=240)
Button(ventana,text="6",width=anchoBoton,height=altoBoton,command=lambda:btnClik(6),bg="light grey").place(x=197,y=240)
Button(ventana,text="7",width=anchoBoton,height=altoBoton,command=lambda:btnClik(7),bg="light grey").place(x=287,y=240)
Button(ventana,text="8",width=anchoBoton,height=altoBoton,command=lambda:btnClik(8),bg="light grey").place(x=17,y=300)
Button(ventana,text="9",width=anchoBoton,height=altoBoton,command=lambda:btnClik(9),bg="light grey").place(x=107,y=300)
Button(ventana,text="π",width=anchoBoton,height=altoBoton,command=lambda:btnClik("pi"), bd=1).place(x=197,y=300)
Button(ventana,text=",",width=anchoBoton,height=altoBoton,command=lambda:btnClik("."), bd=1).place(x=287,y=300)
Button(ventana,text="+",width=anchoBoton,height=altoBoton,command=lambda:btnClik("+"), bd=1).place(x=17,y=360)
Button(ventana,text="-",width=anchoBoton,height=altoBoton,command=lambda:btnClik("-"), bd=1).place(x=107,y=360)
Button(ventana,text="*",width=anchoBoton,height=altoBoton,command=lambda:btnClik("*"), bd=1).place(x=197,y=360)
Button(ventana,text="/",width=anchoBoton,height=altoBoton,command=lambda:btnClik("/"), bd=1).place(x=287,y=360)
Button(ventana,text="√",width=anchoBoton,height=altoBoton,command=lambda:btnClik("sqrt("), bd=1).place(x=17,y=420)
Button(ventana,text="(",width=anchoBoton,height=altoBoton,command=lambda:btnClik("("), bd=1).place(x=17,y=480)
Button(ventana,text=")",width=anchoBoton,height=altoBoton,command=lambda:btnClik(")"), bd=1).place(x=107,y=480)
Button(ventana,text="%",width=anchoBoton,height=altoBoton,command=lambda:btnClik("%"), bd=1).place(x=197,y=480)
Button(ventana,text="=",width=anchoBoton,height=altoBoton,command=resultado, bg = "red", bd=1).place(x=287,y=480)
Button(ventana,text="C",width=anchoBoton,height=altoBoton,command=limpiar, bd=1).place(x=107,y=420)
Button(ventana,text="EXP",width=anchoBoton,height=altoBoton,command=lambda:btnClik("**"), bd=1).place(x=197,y=420)
Button(ventana,text="In",width=anchoBoton,height=altoBoton,command=lambda:btnClik("log("), bd=1).place(x=287,y=420)
 
limpiar()
 
ventana.mainloop()