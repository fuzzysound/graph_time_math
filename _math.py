from tkinter import *
from tkinter import ttk
from math import *
from statistics import *
from random import *

root=Tk()
root.title("Project")

combo_frame = ttk.Frame(root)
combo_frame.grid(column=0, row=0)

input_frame = ttk.Frame(root)
input_frame.grid(column=1, row=0)

output_frame = ttk.Frame(root)
output_frame.grid(column=1, row=1)

button_frame = ttk.Frame(root)
button_frame.grid(column=1, row=2)

input_value_1 = StringVar()
input_value_2 = StringVar()

def float_to_int(num):
    if num.is_integer():
        return int(num)
    else:
        return round(num, 3)

def int_check(num):
    if isinstance(num, float):
        return float_to_int(num)
    if isinstance(num, list):
        return list(map(float_to_int, num))

def _seed():
    if input_value_1.get():
        seed(float(input_value_1.get()))
    else:
        seed()

def comboselect(input_value_1, input_value_2):
    for widget in input_frame.winfo_children():
        widget.destroy()
    if combo.get() == 'random':
        seed_entry = Entry(input_frame, width=20, textvariable=input_value_1)
        seed_entry.grid(column=1, row=1)
        Label(input_frame, text='(').grid(column=0, row=1, sticky=E)
        Label(input_frame, text=')').grid(column=2, row=1)
        seed_button = Button(input_frame, text = 'Set Seed', command = _seed)
        seed_button.grid(column=3, row=1)
    elif combo.get() == 'sample':
        list_entry = Entry(input_frame, width=20, textvariable=input_value_1)
        value_entry = Entry(input_frame, width=20, textvariable=input_value_2)
        list_entry.grid(column=1, row=1)
        Label(input_frame, text='(').grid(column=0, row=1, sticky=E)
        Label(input_frame, text=',').grid(column=2, row=1)
        value_entry.grid(column=1, row=2)
        Label(input_frame, text=')').grid(column=2, row=2)
    else:
        entry = Entry(input_frame, width=20, textvariable=input_value_1)
        entry.grid(column=1, row=1)
        Label(input_frame, text='(').grid(column=0, row=1, sticky=E)
        Label(input_frame, text=')').grid(column=2, row=1)
    Label(output_frame, text='=').grid(column=0, row=0)

    button['command'] = calculate

def calculate():
    try:
        if combo.get() == 'random':
            cal_result = random()
            cal_result = int_check(cal_result)
            output_value.set(cal_result)
        elif combo.get() == 'shuffle':
            value = list(map(float, input_value_1.get().split(',')))
            shuffle(value)
            value = int_check(value)
            output_value.set(value)
        elif combo.get() == 'sample':
            population = list(map(float, input_value_1.get().split(',')))
            num_sample = int(input_value_2.get())
            cal_result = sample(population, num_sample)
            cal_result = int_check(cal_result)
            output_value.set(cal_result)
        else:
            try:
                value = list(map(float, input_value_1.get().split(',')))
                cal_result = eval(combo.get() + '(' + str(value) + ')')
                cal_result = int_check(cal_result)
                output_value.set(cal_result)
            except:
                try:
                    value = list(map(float , input_value_1.get().split(',')))
                    cal_result = eval(combo.get() + '(*' + str(value) + ')')
                    cal_result = int_check(cal_result)
                    output_value.set(cal_result)
                except:
                    pass
    except:
        pass

def _comboselect(event):
    comboselect(input_value_1, input_value_2)

combo = ttk.Combobox(combo_frame)
combo.bind('<<ComboboxSelected>>', _comboselect)




combo.set('Select a function...')
combo['values'] = ('mean', 'median', 'mode', 'pstdev', 'pvariance', 'stdev', 'variance', 'ceil', 'floor', 'fabs',
                   'factorial', 'fmod', 'log', 'pow', 'sqrt', 'sin', 'cos', 'tan', 'degrees', 'radians', 'cosh',
                   'sinh', 'tanh', 'random', 'seed', 'uniform', 'randint', 'randrange', 'choice', 'shuffle', 'sample')
combo.pack()


output_value = StringVar()
result = Label(output_frame, textvariable=output_value, font='Helvetica 20 bold')
result.grid(column=1, row=0, padx=15)

button = ttk.Button(button_frame, text='Calculate')
button.pack()

root.mainloop()
