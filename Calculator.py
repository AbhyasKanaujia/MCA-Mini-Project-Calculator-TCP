# Import GUI and Socket libraries
from tkinter import *
import tkinter.font as tkFont
import socket

# create a GUI window
root = Tk()
# Set the title of the GUI window
root.title('Simple Calculator')
# Set font size to 12
tkFont.nametofont('TkDefaultFont').configure(size=12)


# Create Display
e = Entry(root, width=30, borderwidth=4,
          state='disabled', disabledbackground='white', disabledforeground='black', font='Courier 15 bold')
# Create Quick Result Label
ResultLabel = Label(root, text='', font='Courier',  justify='left')

# Check if expression is valid
# Invalid if last is operators and empty


def checkInvalid():
    exp = e.get()
    if exp == '':
        return True
    last_char = exp[-1]
    if last_char in ('+', '-', '*', '/', '%', '.'):
        return True
    return False

# Client code for getting result from server


def getResultFromServer(expression):
    # Attempt to get result from the server
    try:
        # get the hostname
        host = socket.gethostname()

        # Display message
        print('Sending Request to Server: ', expression)

        # get the port number
        port = 5000

        # get the instance of socket
        client = socket.socket()

        # connect to the server
        client.connect((host, port))

        # Encode and send the expression
        client.send(expression.encode())

        # get the result from server
        result = client.recv(1024).decode()

        # Display result
        print('Received From Server: ', result)

        # close the connection
        client.close()
    # If fail to get result from server then
    except Exception as e:
        # Display server unreachable message
        print('Server unreachable...')
        result = 'Server unreachable...'
    return result


# Global Variables

# if any operator
operator = 0
# If current number has decimal
decimal_status = False
# Sets result mode and input mode
ResultMode = False


# Handle when equal button is pressed
def equal_click():
    # Change to result mode
    global ResultMode

    # If expression is invalid then return
    if checkInvalid() == True:
        return

    # Get result from server when more than one operator
    global operator
    if operator >= 1:
        ans = getResultFromServer(e.get())
        if ans in ['Invalid Expression!!', 'Server unreachable...']:
            return

        # get result and update labels
        ResultLabel.config(text='')
        e.config(state='normal')
        e.delete(0, END)
        e.insert(0, ans)
        e.config(state='disabled')
        operator = 0

    # set display to result mode
    ResultMode = True


# Handle number button is pressed
def digit_click(number):
    # If result mode then clear
    if ResultMode == True and operator == 0:
        clear_click()

    # Append pressed number
    e.config(state='normal')
    e.insert(END, str(number))
    e.config(state='disable')

    # If valid then display result in label
    if operator != 0:
        ans = getResultFromServer(e.get())
        ResultLabel.config(text=ans)

# Handle Clear button is pressed


def clear_click():

    # set all flags to neutral state
    global decimal_status
    decimal_status = False

    # clear the display
    e.config(state='normal')
    e.delete(0, END)
    e.config(state='disable')

    # clear the label
    ResultLabel.config(text='')
    global operator

    # set other flags to netural state
    operator = 0
    global ResultMode
    ResultMode = False


# Handle Backspace button is pressed
def backspace_click():

    global operator
    global decimal_status
    exp = e.get()

    # nothing in entry
    if exp == '':
        return
    last_char = exp[-1]

    if last_char == '.':
        decimal_status = False
    # if last_char is operator
    if last_char in ('+', '-', '*', '/', '%'):
        operator = operator - 1

    # removing last character
    e.config(state='normal')
    if(len(e.get()) > 1):
        e.delete(len(e.get()) - 1, END)
    else:
        clear_click()
    e.config(state='disable')

    # getting removed string
    exp = e.get()
    if exp == '':
        return

    last_char = exp[-1]

    # checking if last character in operator
    if last_char in ('+', '-', '*', '/', '%'):
        # if single operator is left empty label
        if operator == 1:
            ResultLabel.config(text='')
        # calculating from string without last
        else:
            ans = getResultFromServer(exp[:-1])
            ResultLabel.config(text=ans)
    # normal calculating
    elif operator > 0:
        ans = getResultFromServer(exp)
        ResultLabel.config(text=ans)


# Handle if operation(+-/*%.) button is pressed
def operator_click(symbol):

    global decimal_status
    # If invalid then return
    if checkInvalid() == True:
        return

    # If decimal invalid then return
    if symbol == '.' and decimal_status == True:
        return

    # Append operator
    e.config(state='normal')
    e.insert(END, str(symbol))
    e.config(state='disable')

    # If operator then increment operator count
    if symbol != '.':
        global operator
        operator = operator + 1
        decimal_status = False
    else:
        # if decimal then set decimal status to true
        decimal_status = True


# Create Number Buttons
button_1 = Button(root, text='1', padx=40, pady=20,
                  command=lambda: digit_click(1))
button_2 = Button(root, text='2', padx=40, pady=20,
                  command=lambda: digit_click(2))
button_3 = Button(root, text='3', padx=40, pady=20,
                  command=lambda: digit_click(3))
button_4 = Button(root, text='4', padx=40, pady=20,
                  command=lambda: digit_click(4))
button_5 = Button(root, text='5', padx=40, pady=20,
                  command=lambda: digit_click(5))
button_6 = Button(root, text='6', padx=40, pady=20,
                  command=lambda: digit_click(6))
button_7 = Button(root, text='7', padx=40, pady=20,
                  command=lambda: digit_click(7))
button_8 = Button(root, text='8', padx=40, pady=20,
                  command=lambda: digit_click(8))
button_9 = Button(root, text='9', padx=40, pady=20,
                  command=lambda: digit_click(9))
button_0 = Button(root, text='0', padx=40, pady=20,
                  command=lambda: digit_click(0))

# Create decimal button
button_decimal = Button(root, text='.', padx=43, pady=20,
                        command=lambda: operator_click('.'))
# Create Operation Buttons
button_add = Button(root, text='+', padx=38, pady=20,
                    command=lambda: operator_click('+'), bg='#E1D5E9')
button_multiply = Button(root, text='*', padx=40, pady=20,
                         command=lambda: operator_click('*'), bg='#E1D5E9')
button_divide = Button(root, text='/', padx=40, pady=20,
                       command=lambda: operator_click('/'), bg='#E1D5E9')
button_subtract = Button(root, text='-', padx=40, pady=20,
                         command=lambda: operator_click('-'), bg='#E1D5E9')
button_modulus = Button(root, text='%', padx=38, pady=20,
                        command=lambda: operator_click('%'), bg='#E1D5E9')
# Create Function Buttons
button_equal = Button(root, text='=', padx=189, pady=20,
                      command=equal_click, bg='#8C28DA', fg='#ffffff')
button_clear = Button(root, text='Clear', padx=77,
                      pady=20, command=clear_click, bg='#FEB92D')
button_backspace = Button(root, text='<', padx=89, pady=20,
                          command=backspace_click, bg='#FFE3A3')

# place widgets on screen
# Place main display on row 1
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
# Place Quick Result on row 2
ResultLabel.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky='w')

# Place 7 8 9 and / on row 3
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

# Place 4 5 6 and * on row 4
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

# Place 1 2 3 and - on row 5
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

# Place . 0 % and + on row 6
button_decimal.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_modulus.grid(row=5, column=2)
button_add.grid(row=5, column=3)

# Place = and clear on row 7
button_equal.grid(row=6, column=0, columnspan=4)

# Place % and clear on row 8
button_clear.grid(row=7, column=0, columnspan=2)
button_backspace.grid(row=7, column=2, columnspan=2)

# Main GUI Event Loop
root.mainloop()
