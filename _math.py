from tkinter import *
import math
from statistics import *
import random

def mean_value(*args):
    try:
        value=map(float,mean1.get().split(','))
        mean_result.set(mean(value))
    except ValueError:
        pass

def median_value(*args):
    try:
        value=map(float,median1.get().split(','))
        median_result.set(median(value))

        value2 = map(float, median1.get().split(','))
        median_result2.set(median_low(value2))

        value3 = map(float, median1.get().split(','))
        median_result3.set(median_high(value3))

        value4 = map(float, median1.get().split(','))
        median_result4.set(median_grouped(value4))

    except ValueError:
        pass

def mode_value(*args):
    try:
        value=map(float,mode1.get().split(','))
        mode_result.set(mode(value))
    except ValueError:
        pass

def pstdev_value(*args):
    try:
        value=map(float,pstdev1.get().split(','))
        pstdev_result.set(pstdev(value))
    except ValueError:
        pass

def pvariance_value(*args):
    try:
        value=map(float,pvariance1.get().split(','))
        pvariance_result.set(pvariance(value))
    except ValueError:
        pass

def stdev_value(*args):
    try:
        value=map(float,stdev1.get().split(','))
        stdev_result.set(stdev(value))
    except ValueError:
        pass

def variance_value(*args):
    try:
        value=map(float,variance1.get().split(','))
        variance_result.set(variance(value))
    except ValueError:
        pass


def log_value(*args):
    try:
        value=list(map(float,log1.get().split(',')))
        log_result.set(math.log(value[0],value[1]))
    except ValueError:
        pass

def pow_value(*args):
    try:
        value=list(map(float,pow1.get().split(',')))
        pow_result.set(math.pow(value[1],value[0]))
    except ValueError:
        pass


def sqrt_value(*args):
    try:
        value = float(sqrt1.get())
        print(value)
        sqrt_result.set(math.sqrt(value))
    except ValueError:
        pass

def sin_value(*args):
    try:
        value = float(sin1.get())
        sin_result.set(math.sin(value))
    except ValueError:
        pass

def cos_value(*args):
    try:
        value = float(cos1.get())
        cos_result.set(math.cos(value))
    except ValueError:
        pass

def tan_value(*args):
    try:
        value = float(tan1.get())
        tan_result.set(math.tan(value))
    except ValueError:
        pass

def degrees_value(*args):
    try:
        value = float(degrees1.get())
        degrees_result.set(math.degrees(value))
    except ValueError:
        pass

def radians_value(*args):
    try:
        value = float(radians1.get())
        radians_result.set(math.radians(value))
    except ValueError:
        pass

def cosh_value(*args):
    try:
        value = float(cosh1.get())
        cosh_result.set(math.cosh(value))
    except ValueError:
        pass

def sinh_value(*args):
    try:
        value = float(sinh1.get())
        sinh_result.set(math.sinh(value))
    except ValueError:
        pass

def tanh_value(*args):
    try:
        value = float(tanh1.get())
        tanh_result.set(math.tanh(value))
    except ValueError:
        pass

def random_random_value(*args):
    random_random_result.set(random.random())


def random_seed_value(*args):
    try:
        value = float(random_seed_1.get())
        random.seed(value)
        random_seed_result.set(random.random())
    except ValueError:
        pass

def random_seed2_value():
    random.seed()
    random_seed2_result.set(random.random())

def uniform_value(*args):
    try:
        value = list(map(float, uniform1.get().split(',')))
        uniform_result.set(random.uniform(value[0],value[1]))
    except ValueError:
        pass

def randint_value(*args):
    try:
        value = list(map(float, randint1.get().split(',')))
        randint_result.set(random.randint(value[0],value[1]))
    except ValueError:
        pass

def randrange_value(*args):
    try:
        value = float(randrange1.get())
        randrange_result.set(random.randrange(value))
    except ValueError:
        pass

def randrange2_value(*args):
    try:
        value = list(map(float, randrange2.get().split(',')))
        randrange2_result.set(random.randrange(value[0], value[1],value[2]))
    except ValueError:
        pass

def choice_value(*args):
    try:
        value = list(map(float, choice1.get().split(',')))
        choice_result.set(random.choice(value))
    except ValueError:
        pass

def shuffle_value(*args):
    try:
        value = list(map(float, shuffle1.get().split(',')))
        shuffle_result.set(random.shuffle(value))
    except ValueError:
        pass

def sample_value(*args):
    try:
        value = list(map(float, sample1.get().split(',')))
        print(random.sample(value[0:len(value)-1],float(value[len(value)-1])))
    except ValueError:
        pass


root=Tk()
root.title("Project")

mean1=StringVar()
mean_result=StringVar()

mean_label=Label(root,text="mean").grid(row=0,column=0,padx=10)
mean_entry=Entry(root,width=20,textvariable=mean1).grid(row=0,column=1)
Button(root,text="Mean",command=mean_value).grid(row=0,column=2)
mean_result2=Label(root,textvariable=mean_result,font='Helvetica 20 bold').grid(row=0,column=3,padx=15)

median1=StringVar()
median_result=StringVar()
median_result2=StringVar()
median_result3=StringVar()
median_result4=StringVar()

median_label=Label(root,text="median").grid(row=1,column=0)
median_label2=Label(root,text="median_low").grid(row=2,column=0)
median_label3=Label(root,text="median_high").grid(row=3,column=0)
median_label4=Label(root,text="median_grouped").grid(row=4,column=0)
median_entry=Entry(root,width=20,textvariable=median1).grid(row=1,column=1)

Button(root,text="Mean",command=median_value).grid(row=1,column=2,padx=10,pady=10)

median_result5=Label(root,textvariable=median_result,font='Helvetica 20 bold').grid(row=1,column=3,padx=15)
median_result6=Label(root,textvariable=median_result2,font='Helvetica 20 bold').grid(row=2,column=1)
median_result7=Label(root,textvariable=median_result3,font='Helvetica 20 bold').grid(row=3,column=1)
median_result8=Label(root,textvariable=median_result4,font='Helvetica 20 bold').grid(row=4,column=1)

mode1=StringVar()
mode_result=StringVar()

mode_label=Label(root,text="Mode").grid(row=5,column=0,padx=10)
mode_entry=Entry(root,width=20,textvariable=mode1).grid(row=5,column=1)
Button(root,text="Mode",command=mode_value).grid(row=5,column=2)
mode_result3=Label(root,textvariable=mode_result,font='Helvetica 20 bold').grid(row=5,column=3,padx=15)

pstdev1=StringVar()
pstdev_result=StringVar()

pstdev_label=Label(root,text="Pstdev").grid(row=6,column=0,padx=10)
pstdev_entry=Entry(root,width=20,textvariable=pstdev1).grid(row=6,column=1)
Button(root,text="Pstdev",command=pstdev_value).grid(row=6,column=2)
pstdev_result2=Label(root,textvariable=pstdev_result,font='Helvetica 20 bold').grid(row=6,column=3,padx=15)


pvariance1=StringVar()
pvariance_result=StringVar()

pvariance_label=Label(root,text="Pvariance").grid(row=7,column=0,padx=10)
pvariance_entry=Entry(root,width=20,textvariable=pvariance1).grid(row=7,column=1)
Button(root,text="Pvariance",command=pvariance_value).grid(row=7,column=2)
pvariance_result2=Label(root,textvariable=pvariance_result,font='Helvetica 20 bold').grid(row=7,column=3,padx=15)

stdev1=StringVar()
stdev_result=StringVar()

stdev_label=Label(root,text="Stdev").grid(row=8,column=0,padx=10)
stdev_entry=Entry(root,width=20,textvariable=stdev1).grid(row=8,column=1)
Button(root,text="Stdev",command=stdev_value).grid(row=8,column=2)
stdev_result2=Label(root,textvariable=stdev_result,font='Helvetica 20 bold').grid(row=8,column=3,padx=15)

variance1=StringVar()
variance_result=StringVar()

variance_label=Label(root,text="Variance").grid(row=9,column=0,padx=10)
variance_entry=Entry(root,width=20,textvariable=variance1).grid(row=9,column=1)
Button(root,text="Variance",command=variance_value).grid(row=9,column=2)
variance_result2=Label(root,textvariable=variance_result,font='Helvetica 20 bold').grid(row=9,column=3,padx=15)

log1=StringVar()
log_result=StringVar()

log_label=Label(root,text="Log").grid(row=10,column=0,padx=10)
log_entry=Entry(root,width=20,textvariable=log1).grid(row=10,column=1)
Button(root,text="Log",command=log_value).grid(row=10,column=2)
log_result2=Label(root,textvariable=log_result,font='Helvetica 20 bold').grid(row=10,column=3,padx=15)

pow1=StringVar()
pow_result=StringVar()

pow_label=Label(root,text="Pow").grid(row=11,column=0,padx=10)
pow_entry=Entry(root,width=20,textvariable=pow1).grid(row=11,column=1)
Button(root,text="Pow",command=pow_value).grid(row=11,column=2)
pow_result2=Label(root,textvariable=pow_result,font='Helvetica 20 bold').grid(row=11,column=3,padx=15)

sqrt1=StringVar()
sqrt_result=StringVar()

sqrt_label=Label(root,text="Sqrt").grid(row=12,column=0,padx=10)
sqrt_entry=Entry(root,width=20,textvariable=sqrt1).grid(row=12,column=1)
Button(root,text="Sqrt",command=sqrt_value).grid(row=12,column=2)
sqrt_result2=Label(root,textvariable=sqrt_result,font='Helvetica 20 bold').grid(row=12,column=3,padx=15)

sin1=StringVar()
sin_result=StringVar()

sin_label=Label(root,text="Sin").grid(row=13,column=0,padx=10)
sin_entry=Entry(root,width=20,textvariable=sin1).grid(row=13,column=1)
Button(root,text="Sin",command=sin_value).grid(row=13,column=2)
sin_result2=Label(root,textvariable=sin_result,font='Helvetica 20 bold').grid(row=13,column=3,padx=15)

cos1=StringVar()
cos_result=StringVar()

cos_label=Label(root,text="Cos").grid(row=14,column=0,padx=10)
cos_entry=Entry(root,width=20,textvariable=cos1).grid(row=14,column=1)
Button(root,text="Cos",command=cos_value).grid(row=14,column=2)
cos_result2=Label(root,textvariable=cos_result,font='Helvetica 20 bold').grid(row=14,column=3,padx=15)

tan1=StringVar()
tan_result=StringVar()

tan_label=Label(root,text="Tan").grid(row=15,column=0,padx=10)
tan_entry=Entry(root,width=20,textvariable=tan1).grid(row=15,column=1)
Button(root,text="Tan",command=tan_value).grid(row=15,column=2)
tan_result2=Label(root,textvariable=tan_result,font='Helvetica 20 bold').grid(row=15,column=3,padx=15)

degrees1=StringVar()
degrees_result=StringVar()

degrees_label=Label(root,text="Degrees").grid(row=0,column=4,padx=10)
degrees_entry=Entry(root,width=20,textvariable=degrees1).grid(row=0,column=5)
Button(root,text="Degrees",command=degrees_value).grid(row=0,column=6)
degrees_result2=Label(root,textvariable=degrees_result,font='Helvetica 20 bold').grid(row=0,column=7,padx=15)

radians1=StringVar()
radians_result=StringVar()

radians_label=Label(root,text="Radians").grid(row=1,column=4,padx=10)
radians_entry=Entry(root,width=20,textvariable=radians1).grid(row=1,column=5)
Button(root,text="Radians",command=radians_value).grid(row=1,column=6)
radians_result2=Label(root,textvariable=radians_result,font='Helvetica 20 bold').grid(row=1,column=7,padx=15)

cosh1=StringVar()
cosh_result=StringVar()

cosh_label=Label(root,text="Cosh").grid(row=2,column=4,padx=10)
cosh_entry=Entry(root,width=20,textvariable=cosh1).grid(row=2,column=5)
Button(root,text="Cosh",command=cosh_value).grid(row=2,column=6)
cosh_result2=Label(root,textvariable=cosh_result,font='Helvetica 20 bold').grid(row=2,column=7,padx=15)

sinh1=StringVar()
sinh_result=StringVar()

sinh_label=Label(root,text="Sinh").grid(row=3,column=4,padx=10)
sinh_entry=Entry(root,width=20,textvariable=sinh1).grid(row=3,column=5)
Button(root,text="Sinh",command=sinh_value).grid(row=3,column=6)
sinh_result2=Label(root,textvariable=sinh_result,font='Helvetica 20 bold').grid(row=3,column=7,padx=15)

tanh1=StringVar()
tanh_result=StringVar()

tanh_label=Label(root,text="Tanh").grid(row=4,column=4,padx=10)
tanh_entry=Entry(root,width=20,textvariable=tanh1).grid(row=4,column=5)
Button(root,text="Tan",command=tanh_value).grid(row=4,column=6)
tanh_result2=Label(root,textvariable=tanh_result,font='Helvetica 20 bold').grid(row=4,column=7,padx=15)

random_seed_1=StringVar()
random_seed_result=StringVar()

random_seed__label=Label(root,text="Random").grid(row=5,column=4,padx=10)
random_seed_entry=Entry(root,width=20,textvariable=random_seed_1).grid(row=5,column=5)
Button(root,text="Random",command=random_seed_value).grid(row=5,column=6)
random_seed_result2=Label(root,textvariable=random_seed_result,font='Helvetica 20 bold').grid(row=5,column=7,padx=15)

random_seed2_result=StringVar()

random_seed2__label=Label(root,text="Random_Seed()").grid(row=6,column=4,padx=10)
Button(root,text="Random_Seed()",command=random_seed2_value).grid(row=6,column=5)
random_seed2_result2=Label(root,textvariable= random_seed2_result , font='Helvetica 20 bold').grid(row=6,column=7,padx=15)

random_random_result=StringVar()
random_random_label=Label(root,text="Random()").grid(row=7,column=4,padx=10)
Button(root,text="Random()",command=random_random_value).grid(row=7,column=5)
random_random_result2=Label(root,textvariable= random_random_result , font='Helvetica 20 bold').grid(row=7,column=7,padx=15)

uniform1=StringVar()
uniform_result=StringVar()

uniform_label=Label(root,text="Uniform").grid(row=8,column=4,padx=10)
uniform_entry=Entry(root,width=20,textvariable=uniform1).grid(row=8,column=5)
Button(root,text="Uniform",command=uniform_value).grid(row=8,column=6)
uniform_result2=Label(root,textvariable=uniform_result,font='Helvetica 20 bold').grid(row=8,column=7,padx=15)

randint1=StringVar()
randint_result=StringVar()

randint_label=Label(root,text="Randint").grid(row=9,column=4,padx=10)
randint_entry=Entry(root,width=20,textvariable=randint1).grid(row=9,column=5)
Button(root,text="Randint",command=randint_value).grid(row=9,column=6)
randint_result2=Label(root,textvariable=randint_result,font='Helvetica 20 bold').grid(row=9,column=7,padx=15)

randrange1=StringVar()
randrange_result=StringVar()

randrange_label=Label(root,text="Randrange").grid(row=10,column=4,padx=10)
randrange_entry=Entry(root,width=20,textvariable=randrange1).grid(row=10,column=5)
Button(root,text="Randrange",command=randrange_value).grid(row=10,column=6)
randrange_result2=Label(root,textvariable=randrange_result,font='Helvetica 20 bold').grid(row=10,column=7,padx=15)

randrange2=StringVar()
randrange2_result=StringVar()

randrange2_label=Label(root,text="Randrange2").grid(row=11,column=4,padx=10)
randrange2_entry=Entry(root,width=20,textvariable=randrange2).grid(row=11,column=5)
Button(root,text="Randrange2",command=randrange2_value).grid(row=11,column=6)
randrange2_result2=Label(root,textvariable=randrange2_result,font='Helvetica 20 bold').grid(row=11,column=7,padx=15)

choice1=StringVar()
choice_result=StringVar()

choice_label=Label(root,text="Choice").grid(row=12,column=4,padx=10)
choice_entry=Entry(root,width=20,textvariable=choice1).grid(row=12,column=5)
Button(root,text="Choice",command=choice_value).grid(row=12,column=6)
choice_result2=Label(root,textvariable=choice_result,font='Helvetica 20 bold').grid(row=12,column=7,padx=15)

shuffle1=StringVar()
shuffle_result=StringVar()

shuffle_label=Label(root,text="Shuffle").grid(row=13,column=4,padx=10)
shuffle_entry=Entry(root,width=20,textvariable=shuffle1).grid(row=13,column=5)
Button(root,text="Shuffle",command=shuffle_value).grid(row=13,column=6)
shuffle_result2=Label(root,textvariable=shuffle_result,font='Helvetica 20 bold').grid(row=13,column=7,padx=15)

sample1=StringVar()

sample_label=Label(root,text="Sample").grid(row=14,column=4,padx=10)
sample_entry=Entry(root,width=20,textvariable=sample1).grid(row=14,column=5)
Button(root,text="Sample",command=sample_value).grid(row=14,column=6)

root.mainloop()
# TODO
# Tkinter module을 이용해서 아래에 있는 function들을 지원하는 직관적인 GUI를 만들어본다.
# statistics module: mean(), median(), mode(), pstdev(), pvariance(), stdev(), variance()
# math module: ceil(), floor(), fabs(), factorial(), fmod(), log(), pow(), sqrt(), sin(), cos(), tan(),
# degrees(), radians(), cosh(), sinh(), tanh()
# random module: random(), seed(), uniform(), randint(), randrange(), choice(), shuffle(), sample()

