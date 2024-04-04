from tkinter import *
from tkinter import ttk

cor1 ="#1e1f1e"
cor2 ="#feffff"
cor3 ="#38576b"
cor4 ="#ECEFF1"
cor5 ="#FFAB40"


janela =Tk()
#titulo da janela
janela.title("Calculadora")
#definição da comprimento x altura
janela.geometry("235x310")
janela.config(bg=cor1)

#criação do frame superior
frame_tela = Frame(janela, width=235, height=50, bg= cor3)
frame_tela.grid(row=0, column= 0)

#criação do frame inferior
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column= 0)

# variavel todos valores
todos_valores = ""

#criando função para entrar os valores
def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    #passando valor para tela
    valor_texto.set(todos_valores)

#criando funcão para calular os valores de entrada
def calcular():

    global todos_valores
    resultado = eval(todos_valores) 
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)
    
#função limpa tela
def limpa_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")


#criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)

# criando botoes
#botão de "C" para limpar
b_1 = Button(frame_corpo, text="C", command=limpa_tela, width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_1.place(x=0, y=0)
#botão "%"
b_2 = Button(frame_corpo, text="%",  command= lambda: entrar_valores("%") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_2.place(x=118, y=0)
#botão "/"
b_3 = Button(frame_corpo, text="/", command= lambda: entrar_valores("/") ,width=5, height=2, bg=cor5, fg=cor2,  font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_3.place(x=177, y=0)

# criando botoes
#botão "7" 
b_4 = Button(frame_corpo, text="7", command= lambda: entrar_valores("7") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_4.place(x=0, y=52)
#botão "8"
b_5 = Button(frame_corpo, text="8", command= lambda: entrar_valores("8") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_5.place(x=59, y=52)
#botão "9"
b_6 = Button(frame_corpo, text="9", command= lambda: entrar_valores("9") , width=5, height=2, bg=cor4,  font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_6.place(x=118, y=52)
#botão "*"
b_7 = Button(frame_corpo, text="*", command= lambda: entrar_valores("*") ,width=5, height=2, bg=cor5, fg=cor2,  font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_7.place(x=177, y=52)

# criando botoes
#botão "4" 
b_8 = Button(frame_corpo, text="4", command= lambda: entrar_valores("4") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_8.place(x=0, y=104)
#botão "5"
b_9 = Button(frame_corpo, text="5", command= lambda: entrar_valores("5") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_9.place(x=59, y=104)
#botão "6"
b_10 = Button(frame_corpo, text="6", command= lambda: entrar_valores("6") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_10.place(x=118, y=104)
#botão "-"
b_11 = Button(frame_corpo, text="-", command= lambda: entrar_valores("-") , width=5, height=2, bg=cor5, fg=cor2,  font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_11.place(x=177, y=104)

# criando botoes
#botão "1" 
b_12 = Button(frame_corpo, text="1", command= lambda: entrar_valores("1") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_12.place(x=0, y=156)
#botão "2"
b_13 = Button(frame_corpo, text="2", command= lambda: entrar_valores("2") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_13.place(x=59, y=156)
#botão "3"
b_14 = Button(frame_corpo, text="3", command= lambda: entrar_valores("3") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_14.place(x=118, y=156)
#botão "+"
b_15 = Button(frame_corpo, text="+", command= lambda: entrar_valores("+") , width=5, height=2, bg=cor5, fg=cor2,  font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_15.place(x=177, y=156)

#botão "0" 
b_16 = Button(frame_corpo, text="0", command= lambda: entrar_valores("0") , width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_16.place(x=0, y=208)
#botão "."
b_17 = Button(frame_corpo, text=".", command= lambda: entrar_valores(".") , width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_17.place(x=118, y=208)
#botão "="
b_18 = Button(frame_corpo, text="=", command=calcular, width=5, height=2, bg=cor5, fg=cor2,  font=('ivy 13 bold'), relief=RAISED, overrelief= RIDGE)
b_18.place(x=177, y=208)



janela.mainloop()