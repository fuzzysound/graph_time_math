from tkinter import *
from tkinter import ttk
from math import *
from statistics import *
from random import *
from functionHelps import helps # 함수 도움말을 가져오기 위해 import

# 입력된 숫자가 정수면 소숫점 아래를 제거하고, 그렇지 않으면 소숫점 셋째 자리까지 반올림하여 출력하는 함수
def float_to_int(num):
    if num.is_integer():
        return int(num)
    else:
        return round(num, 3)

# 입력으로 int type 변수가 들어올 경우 그대로 출력,입력으로 float type 변수가 들어올 경우 float_to_int 함수 적용해 출력,
# 입력으로 iterable한 객체가 들어올 경우 float_to_num 함수 map하여 출력하는 함수
def int_check(num):
    if isinstance(num, int):
        return num
    if isinstance(num, float):
        return float_to_int(num)
    if isinstance(num, list):
        return list(map(float_to_int, num))

# Set Seed 버튼에 bind하기 위한 함수
def _seed():
    if input_value_1.get(): # Entry에 특정 값이 입력되었을 경우
        seed(float(input_value_1.get())) # 해당 값으로 seed initialize
    else: # Entry가 빈칸일 경우
        seed()

# Combobox에 bind하기 위한 함수
def comboselect(input_value_1, input_value_2): # input_value_1과 input_value_2는 각각 entry

    # Combobox에서 선택을 바꿀 때마다 input_frame의 모든 요소들을 지운다
    for widget in input_frame.winfo_children():
        widget.destroy()

    # 선택된 함수에 따라 entry 생성
    if combo.get() == 'random': # 예외1: 선택된 함수가 random일 때
        seed_entry = Entry(input_frame, width=20, textvariable=input_value_1) # Seed가 입력될 entry
        seed_entry.grid(column=1, row=1)
        Label(input_frame, text='(').grid(column=0, row=1, sticky=E) # Entry 좌로 여는 괄호
        Label(input_frame, text=')').grid(column=2, row=1) # Entry 우로 닫는 괄호
        seed_button = Button(input_frame, text = 'Set Seed', command = _seed) # Set Seed 버튼 생성, _seed 함수와 bind
        seed_button.grid(column=3, row=1)
    elif combo.get() == 'sample': # 예외2: 선택된 함수가 sample일 때
        list_entry = Entry(input_frame, width=20, textvariable=input_value_1) # Population이 입력될 entry
        value_entry = Entry(input_frame, width=20, textvariable=input_value_2) # sample 수 값이 입력될 entry
        list_entry.grid(column=1, row=1)
        value_entry.grid(column=1, row=2)
        Label(input_frame, text='(').grid(column=0, row=1, sticky=E) # 첫번째 entry 좌로 여는 괄호
        Label(input_frame, text=',').grid(column=2, row=1) # 두 entry 사이 콤마
        Label(input_frame, text=')').grid(column=2, row=2) # 두번째 entry 우로 닫는 괄호
    else: # 그 외 모든 함수에 대해서 일괄 적용
        entry = Entry(input_frame, width=20, textvariable=input_value_1) # 입력값이 입력될 entry
        entry.grid(column=1, row=1)
        Label(input_frame, text='(').grid(column=0, row=1, sticky=E) # entry 좌로 여는 괄호
        Label(input_frame, text=')').grid(column=2, row=1) # entry 우로 닫는 괄호

    # helper canvas 삭제 및 새로 생성
    helper_canvas.delete('all') # 기존에 helper canvas가 존재할 경우 지운다
    margin = 10 # 테두리 여백
    helper_canvas.create_rectangle(margin, margin, width - margin, height - margin, outline='dimgray') # 테두리 상자 생성
    root_bg = root.cget('bg') # root 윈도우의 배경색 추출
    helper_canvas.create_rectangle(margin * 5 - 15, margin - 15, margin * 5 + 15, margin + 15, fill=root_bg,
                                   outline=root_bg) # Help 글자가 들어갈 만큼의 공간을 사각형으로 만든다. 일종의 꼼수.
    helper_canvas.create_text(margin * 5, margin, text='Help') # Help 글자 생성
    helper_canvas.create_text(width / 2, height / 2, text=helps[str(combo.get())],
                              width=width - 4 * margin) # 해당 함수에 해당하는 도움말을 helps에서 가져와서 띄운다

    # 그 외
    Label(output_frame, text='=').grid(column=0, row=0) # 출력값 왼쪽에 '=' 기호 띄우기
    button['command'] = calculate # Calculate 버튼에 calculate 함수 bind

#  Calculate 버튼에 bind하기 위한 함수
def calculate():
    try:
        if combo.get() == 'random': # 예외1: 선택된 함수가 random일 때
            cal_result = random() # random 함수로 값 생성
            cal_result = int_check(cal_result) # int_check 함수 적용
            output_value.set(cal_result) # 출력
        elif combo.get() == 'shuffle': # 예외2: 선택된 함수가 shuffle일 때
            value = list(map(float, input_value_1.get().split(','))) # 입력값을 받아 콤마 단위로 분리한 다음 float화하여 list로 변환
            shuffle(value) # shuffle 함수는 아무것도 return하지 않기 때문에, 직접 return해 주어야 한다
            value = int_check(value) # int_check 함수 적용
            output_value.set(value) # 출력
        elif combo.get() == 'sample': # 예외3: 선택된 함수가 sample일 때
            population = list(map(float, input_value_1.get().split(','))) # Population. 입력값을 받아 콤마 단위로 분리한 다음 float화하여 list로 변환
            num_sample = int(input_value_2.get()) # Num. of samples. 입력값을 int화
            cal_result = sample(population, num_sample) # sample 함수 적용해 결과 추출
            cal_result = int_check(cal_result) # int_check 함수 적용
            output_value.set(cal_result) # 출력
        else: # 그 외 모든 함수에 대해서 일괄 적용
            try:
                value = list(map(float, input_value_1.get().split(','))) # 입력값을 받아 콤마 단위로 분리한 다음 float화하여 list로 변환
                cal_result = eval(combo.get() + '(' + str(value) + ')') # 입력값을 인수로 삼아 해당 함수 바로 실행해 결과 추출
                cal_result = int_check(cal_result) # int_check 함수 적용
                output_value.set(cal_result) # 출력
            except: # 인수로 iterable이 아닌 여러 변수를 받는 함수를 위한 예외문
                try:
                    value = list(map(float , input_value_1.get().split(','))) # 입력값을 받아 콤마 단위로 분리한 다음 float화하여 list로 변환
                    cal_result = eval(combo.get() + '(*' + str(value) + ')') # 입력값 앞에 asterisk를 붙여 unpack. 그 외 위와 동일
                    cal_result = int_check(cal_result) # int_check 함수 적용
                    output_value.set(cal_result) # 출력
                except:
                    pass # 입력값이 적절하지 않을 경우 pass
    except:
        pass # 입력값이 적절하지 않을 경우 pass

def _comboselect(event): # tkinter에서 widget에 함수를 bind할 경우 함수에 인수를 설정할 수 없으므로, 이를 우회하기 위한 꼼수
    comboselect(input_value_1, input_value_2) # input_value_1과 input_value_2를 인수로 받아 comboselect 함수 실행

# Root window와 내부 frame 설정
root=Tk() # root window 설정
root.title("Advanced Calculator") # 제목표시줄에 들어갈 제목

title_frame = ttk.Frame(root) # 가장 위에 표시될 프로그램 이름을 위한 frame 설정
title = Label(title_frame, text='Advanced Calculator', font=('Comic Sans MS', 25, 'bold'), fg='darkcyan') # Label 설정
title.pack()
title_frame.grid(column=0, row=0, columnspan=2, padx=30, pady=20)

combo_frame = ttk.Frame(root) # Combobox가 들어갈 frame 설정
combo = ttk.Combobox(combo_frame) # Combobox 생성
combo.bind('<<ComboboxSelected>>', _comboselect) # _comboselect 함수와 bind
combo.set('Select a function...') # 가장 처음에 combobox에 표시될 텍스트 설정
combo['values'] = ('mean', 'median', 'mode', 'pstdev', 'pvariance', 'stdev', 'variance', 'ceil', 'floor', 'fabs',
                   'factorial', 'fmod', 'log', 'pow', 'sqrt', 'sin', 'cos', 'tan', 'degrees', 'radians', 'cosh',
                   'sinh', 'tanh', 'random', 'uniform', 'randint', 'randrange', 'choice', 'shuffle', 'sample') # 선택지 설정
combo.pack()
combo_frame.grid(column=0, row=1, padx=5, pady=15, sticky=E)

input_frame = ttk.Frame(root) # 입력값 entry가 들어갈 frame 설정. 구체적인 entry 설정은 comboselect 함수에서 일어남.
input_frame.grid(column=1, row=1)

output_frame = ttk.Frame(root)  # 출력값 label이 들어갈 frame 설정.
output_value = StringVar() # 출력값이 할당될 전역변수 설정
result = Label(output_frame, textvariable=output_value, font='Helvetica 20 bold') # Label 생성
result.grid(column=1, row=0, padx=15)
output_frame.grid(column=1, row=2)

button_frame = ttk.Frame(root) # Calculate 버튼이 들어갈 frame 생성
button = ttk.Button(button_frame, text='Calculate') # Calculate 버튼 생성
button.pack()
button_frame.grid(column=1, row=3, pady=10)

helper_frame = ttk.Frame(root) # 함수 도움말이 들어갈 frame 설정.
width = 200
height = 200
helper_canvas = Canvas(helper_frame, width=width, height=height) # Canvas 생성. 캔버스 내부 설정은 comboselect 함수에서 일어남.
helper_canvas.pack()
helper_frame.grid(column=0, row=2, rowspan=3)

# 입력값이 할당될 전역변수 설정
input_value_1 = StringVar()
input_value_2 = StringVar()

# 프로그램 실행
root.mainloop()
