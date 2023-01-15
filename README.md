# superfloat v1.0
1.如何使用superfloat？ How to use superfloat?
下载superfloat.py，然后把superfloat.py复制到你要使用的Python代码所在文件夹。
然后创建你要使用的python代码文件，第一行输入import superfloat
若要创建一个类型为superfloat的变量，可以给变量赋值superfloat.superfloat(0)或者superfloat.superfloat(0,0)（0也可以换成其他数值）
支持superfloat与int、float、string的相互转换。
你还可以使用superfloat.py内部的三十三种函数进行运算。
Download superfloat.py, then, put superfloat.py into the folder where the python code you want to use in.
Then, create the python code files what you will use, input import superfloat in the first line.
To create a variable with type of superfloat, you can make the variable equals to superfloat.superfloat(0) or superfloat.superfloat(0,0), of course, you can replace 0 into other numbers.
It supports superfloat to and from int, float, string conversion.
You can also use 33 functions inside the superfloat.py to do the operation.

2.各种函数的介绍 Various of functions introuduction
Superfloat支持加减乘除运算，还支持33种函数，下面我们来看看各种函数的介绍。
Superfloat supports the calculating of addition, subtraction, multiplication and division, and 33 functions, let's look at introuductions of various of functions.

2.1 sqrt(x)
sqrt(x)返回值x的平方根。
sqrt(x) returns the arithmetic square root of the value x.

2.2 scmp(x1,x2)
scmp(x1,x2)用于比较x1与x2大小，如果x1>x2，返回1；如果x1=x2，返回0；如果x1<x2，返回-1。
x2默认值为0。
scmp(x1,x2) is used to compare x1 with x2, if x1 >x2, it returns 1; If x1=x2, it returns 0; If x1 <x2, it returns -1.
The default value of x2 is superfloat.superfloat(0).

2.3 floor(x,d)
floor(x,d)用于将x1向下取d1位小数。
d默认值为0。
floor(x,d) is used to take x down to d decimal places.
The default value for d is 0.

2.4 ceil(x1,d1)
ceil(x,d)用于将x向上取d位小数。
d默认值为0。
ceil(x,d) is used to take x up to d decimal places.
The default value for d is 0.

2.5 sround(x1,d1)
sround(x,d)用于将x四舍五入取d位小数。
d默认值为0。
sround(x,d) is used to round x to d decimal places.
The default value for d is 0.

2.6 exp(x)
exp(x)返回e的x次方。
exp(x) returns to the x power of e.

2.7 ln(x)
ln(x)返回x的自然对数。
ln(x) returns the natural logarithm of x.

2.8 log(x,y)
log(x,y)返回x以y为底的对数。
y默认值为superfloat.e
log(x,y) returns the logarithm of x in base y.
The default value is superfloat.e

2.9 spow(x,y)
spow(x,y)返回x的y次方。
spow(x,y) returns to the y power of x.

2.10 sin(r)
sin(r)返回r rad的正弦值。
sin(r) returns the sine of r rad.

2.11 cos(r)
cos(r)返回r rad的余弦值。
cos(r) returns the cosine of r rad.

2.12 tan(r)
tan(r)返回r rad的正切值。
tan(r) returns the tangent of r rad.

2.13 cot(r)
cot(r)返回r rad的余切值。
cot(r) returns the cotangent of r rad.

2.14 sec(r)
sec(r)返回r rad的正割值。
sec(r) returns the secant of r rad.

2.15 csc(r)
csc(r)返回r rad的余割值。
csc(r) returns the cosecant of r rad.

2.16 asin(v)
asin(v)返回方程sin(r rad)=v最接近0的解r。
asin(v) returns the solution r of the equation sin(r rad)=v closest to 0.

2.17 acos(v)
acos(v)返回方程cos(r rad)=v最接近pi/2的解r。
acos(v) returns the solution r of the equation cos(r rad)=v closest to pi/2.

2.18 atan(v)
atan(v)返回方程tan(r rad)=v最接近0的解r。
atan(v) returns the solution r of the equation tan(r rad)=v closest to 0.

2.19 acot(v)
acot(v)返回方程cot(r rad)=v最接近pi/2的解r。
acot(v) returns the solution r of the equation cot(r rad)=v closest to pi/2.

2.20 asec(v)
asec(v)返回方程sec(r rad)=v最接近pi/2的解r。
asec(v) returns the solution r of the equation sec(r rad)=v closest to pi/2.

2.21 acsc(v)
acsc(v)返回方程csc(r rad)=v最接近0的解r。
acsc(v) returns the solution r of the equation csc(r rad)=v closest to 0.

2.22 sinh(v)
sinh(v)=1/2(e^v-1/e^v)

2.23 cosh(v)
cosh(v)=1/2(e^v+1/e^v)

2.24 tanh(v)
tanh(v)=(e^v-1/e^v)/(e^v+1/e^v)

2.25 coth(v)
coth(v)=(e^v+1/e^v)/(e^v-1/e^v)

2.26 sech(v)
sech(v)=2/(e^v+1/e^v)

2.27 csch(v)
csch(v)=2/(e^v-1/e^v)

2.28 asinh(v)
asinh(v)返回方程sinh(w)=v的实数解w。
asinh(v) returns the real solution w of the equation sinh(w)=v.

2.29 acosh(v)
acosh(v)返回方程cosh(w)=v的实数解w。
acosh(v) returns the real solution w of the equation cosh(w)=v.

2.30 atanh(v)
atanh(v)返回方程tanh(w)=v的实数解w。
atanh(v) returns the real solution w of the equation tanh(w)=v.

2.31 acoth(v)
acoth(v)返回方程coth(w)=v的实数解w。
acoth(v) returns the real solution w of the equation coth(w)=v.

2.32 asech(v)
asech(v)返回方程sech(w)=v的实数解w。
asech(v) returns the real solution w of the equation sech(w)=v.

2.33 acsch(v)
acsch(v)返回方程csch(w)=v的实数解w。
acsch(v) returns the real solution w of the equation csch(w)=v.
