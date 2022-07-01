import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.geometry('450x400')
win.title('CALCULATOR')
expression=''
#---------------------------op() function to disable all op button to disable state------------------------

#========================================op() function start=======================================

def btn_click(arg):
    global expression
    #e1_var.set(ard)
    expression=expression+arg
    e1_var.set(expression)


    if expression[0] in ['+','/','*']: # if user press +,/,* at start
        expression=str(0)+arg
        e1_var.set(expression)

# if user try to press consective operator
    if expression[len(expression)-1] in ['+','/','*','-'] and expression[len(expression)-2] in ['+','/','*','-']:
        expression=expression[:len(expression)-2]+str(arg)
        e1_var.set(expression)

    # if arg=='.':
    #     dot.config(state='disabled')
    #
    # if arg in['+','/','*','-']:
    #     dot.config(state='normal')


def clear_click():
    global expression,e1_var
    expression=''
    e1_var.set('')


def clear_1():
    global expression
    expression=expression[0:len(expression)-1]
    e1_var.set(expression)

    # if expression[len(expression)-1] in ['+','/','*','-']:
    #     for i in [plus,div,mul,minus,eql]:
    #         i.config(state='disabled')
    #
    # if expression[len(expression)-1] not in ['+','/','*','-']:
    #     for i in [plus,div,mul,minus,eql]:




def eql_click():
    global expression
    if expression[len(expression)-1]=='0' and expression[len(expression)-2]=='/':
        messagebox.showinfo('DIVIDE BY 0 ERROR','divide by 0 is not possible')
        expression=''
        e1_var.set(expression)
    else:
        expression=str(eval(expression))
        e1_var.set(expression)

#==============================end of eql_click button code==============================

#-------------------------------designing code---------------------------------

#ROW 1

e1_var=tk.StringVar()
e1=tk.Entry(win,width=28,textvariable=e1_var,bd=3,font=('elephant',15),state='disabled',justify='right')
e1.place(x=0,y=0)

#ROW 2
cancel=tk.Button(win,text='AC',width=15,height=2,command=clear_click,fg='red',font=('elephant',10),bg='#57DD15')
cancel.place(x=0,y=30)
cancel_c=tk.Button(win,text='C',width=13,height=2,command=clear_1,fg='red',font=('elephant',10),bg='#57DD15')
cancel_c.place(x=140,y=30)
div=tk.Button(win,text='/',width=22,height=2,command=lambda:btn_click('/'),bg='#57DD15')
div.place(x=265,y=30)

#ROW 3
seven=tk.Button(win,text='7',width=14,height=2,command=lambda:btn_click('7'),bg='#57DD15')
seven.place(x=0,y=70)
eight=tk.Button(win,text='8',width=14,height=2,command=lambda:btn_click('8'),bg='#57DD15')
eight.place(x=107,y=70)
nine=tk.Button(win,text='9',width=14,height=2,command=lambda:btn_click('9'),bg='#57DD15')
nine.place(x=214,y=70)
mul=tk.Button(win,text='*',width=14,height=2,command=lambda:btn_click('*'),bg='#57DD15')
mul.place(x=321,y=70)

#ROW 4
four=tk.Button(win,text='4',width=14,height=2,command=lambda:btn_click('4'),bg='#57DD15')
four.place(x=0,y=110)
five=tk.Button(win,text='5',width=14,height=2,command=lambda:btn_click('5'),bg='#57DD15')
five.place(x=107,y=110)
six=tk.Button(win,text='6',width=14,height=2,command=lambda:btn_click('6'),bg='#57DD15')
six.place(x=214,y=110)
minus=tk.Button(win,text='-',width=14,height=2,command=lambda:btn_click('-'),bg='#57DD15')
minus.place(x=321,y=110)

#ROW 5
one=tk.Button(win,text='1',width=14,height=2,command=lambda:btn_click('1'),bg='#57DD15')
one.place(x=0,y=150)
two=tk.Button(win,text='2',width=14,height=2,command=lambda:btn_click('2'),bg='#57DD15')
two.place(x=107,y=150)
three=tk.Button(win,text='3',width=14,height=2,command=lambda:btn_click('3'),bg='#57DD15')
three.place(x=214,y=150)
plus=tk.Button(win,text='+',width=14,height=2,command=lambda:btn_click('+'),bg='#57DD15')
plus.place(x=321,y=150)

zero=tk.Button(win,text='0',width=30,height=2,command=lambda:btn_click('0'),bg='#57DD15')
zero.place(x=0,y=190)
dot=tk.Button(win,text='.',width=14,height=2,command=lambda:btn_click('.'),bg='#57DD15')
dot.place(x=214,y=190)
eql=tk.Button(win,text='=',width=14,height=2,command=eql_click,bg='#57DD15')
eql.place(x=321,y=190)
#=================================designing code END==========================================

#======================bing all button to set bg on mouse hover============================

one.bind("<Enter>",lambda e: one.config(bg="#DDF5F0"))
one.bind("<Leave>",lambda e: one.config(bg="#57DD15"))
two.bind("<Enter>",lambda e: two.config(bg="#DDF5F0"))
two.bind("<Leave>",lambda e: two.config(bg="#57DD15"))
three.bind("<Enter>",lambda e: three.config(bg="#DDF5F0"))
three.bind("<Leave>",lambda e: three.config(bg="#57DD15"))
four.bind("<Enter>",lambda e: four.config(bg="#DDF5F0"))
four.bind("<Leave>",lambda e: four.config(bg="#57DD15"))

five.bind("<Enter>",lambda e: five.config(bg="#DDF5F0"))
five.bind("<Leave>",lambda e: five.config(bg="#57DD15"))
six.bind("<Enter>",lambda e: six.config(bg="#DDF5F0"))
six.bind("<Leave>",lambda e: six.config(bg="#57DD15"))
seven.bind("<Enter>",lambda e: seven.config(bg="#DDF5F0"))
seven.bind("<Leave>",lambda e: seven.config(bg="#57DD15"))
eight.bind("<Enter>",lambda e: eight.config(bg="#DDF5F0"))
eight.bind("<Leave>",lambda e: eight.config(bg="#57DD15"))

win.mainloop()

