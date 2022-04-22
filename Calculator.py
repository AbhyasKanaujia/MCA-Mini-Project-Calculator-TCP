from tkinter import *
import socket

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=60, borderwidth=4,
          state='disabled', disabledbackground='white', disabledforeground='black')
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

ResultLabel =  Label(root,text = "", justify = 'left', anchor = 'w')
ResultLabel.grid(row = 1, column = 0, columnspan = 5, padx=10, pady=10)


def getResultFromServer(expression):
    host = socket.gethostname()
    print("Sending Request to Server: ", expression)
    port = 5000
    client = socket.socket()
    client.connect((host, port))
    client.send(expression.encode())

    result = client.recv(1024).decode()
    print("Received From Server: ", result)

    client.close()

    return result
    # e.delete(0, END)
    # e.insert(0, result)


# def button_click(number):
#     e.config(state='normal')
#     if number == 'clear':
#         e.delete(0, END)
#     elif number == '=':
#         if e.get() != "":
#             getResultFromServer(e.get())
#     else:
#         e.insert(END, str(number))
#     e.config(state='disabled')

# if any operator
operator = False

def equal_click():
    e.config(state = 'normal')
    if e.get() != "":
        ans = getResultFromServer(e.get())

    ResultLabel.config(text = "")
    e.delete(0,END)
    e.insert(0, ans)
    e.config(state = 'disabled')
    global operator 
    operator = False

def digit_click(number):

    e.config(state = 'normal')
    e.insert(END, str(number))
    e.config(state = 'disable')
    
    if operator != False:
        ans = getResultFromServer(e.get())
        ResultLabel.config(text = ans)

def clear_click():

    e.config(state = 'normal')
    e.delete(0, END)
    e.config(state = 'disable')

    ResultLabel.config(text = "")
    global operator 
    operator = False

def operator_click(symbol):

    e.config(state = 'normal')
    e.insert(END, str(symbol))
    e.config(state = 'disable')
    
    if symbol != '.':
        global operator 
        operator = True


        

button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: digit_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: digit_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: digit_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: digit_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: digit_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: digit_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: digit_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: digit_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: digit_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: digit_click(0))

button_decimal = Button(root, text=".", padx=40, pady=20,
                        command=lambda: operator_click('.'))

button_add = Button(root, text="+", padx=40, pady=20,
                    command=lambda: operator_click('+'), bg='#E1D5E9')
button_multiply = Button(root, text="*", padx=40, pady=20,
                         command=lambda: operator_click('*'), bg='#E1D5E9')
button_divide = Button(root, text="/", padx=40, pady=20,
                       command=lambda: operator_click('/'), bg='#E1D5E9')
button_subtract = Button(root, text="-", padx=40, pady=20,
                         command=lambda: operator_click('-'), bg='#E1D5E9')

button_equal = Button(root, text="=", padx=40, pady=20,
                      command=equal_click, bg='#8C28DA')
button_clear = Button(root, text="Clear", padx=180,
                      pady=20, command=clear_click, bg='#FEB92D')

# place button on screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_decimal.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_clear.grid(row=6, column=0, columnspan=4)

root.mainloop()
