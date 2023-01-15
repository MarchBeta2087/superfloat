import sys
import copy
def setmaxdigits(x):
    try:
        sys.set_int_max_str_digits(x)
        return 0
    except:
        return 1
setmaxdigits(2147483647)
sys.setrecursionlimit(2147483617)
DIVDIGITS=10
NTI=10 #牛顿迭代次数
TYI=10 #泰勒展开项数
class superfloat:
    def __init__(self,fa,ex=0):
        self.ex=int(ex)
        if type(fa)==int:
            while fa%10==0 and fa!=0:
                fa=fa//10
                self.ex+=1
            self.fa=fa
        elif type(fa)==float:
            fa=str(fa)
            if "e" not in fa:
                parti=fa.split(".")
                if len(parti)==1:
                    parti.append("0")
                maji=parti[0]
                minoi=parti[1]
                self.fa=int(str(str(maji)+str(minoi)))
                self.ex-=len(minoi)
            else:
                prefloat=fa.split("e")
                fasi=prefloat[0]
                expi=int(prefloat[1])
                self.ex+=expi
                parti=fasi.split(".")
                if len(parti)==1:
                    parti.append("0")
                maji=parti[0]
                minoi=parti[1]
                self.fa=int(str(str(maji)+str(minoi)))
                self.ex-=len(minoi)
            while self.fa%10==0 and self.fa!=0:
                self.fa=self.fa//10
                self.ex+=1
        elif type(fa)==str:
            if "e" not in fa:
                parti=fa.split(".")
                if len(parti)==1:
                    parti.append("0")
                maji=parti[0]
                minoi=parti[1]
                self.fa=int(str(str(maji)+str(minoi)))
                self.ex-=len(minoi)
            else:
                prefloat=fa.split("e")
                fasi=prefloat[0]
                expi=int(prefloat[1])
                self.ex+=expi
                parti=fasi.split(".")
                if len(parti)==1:
                    parti.append("0")
                maji=parti[0]
                minoi=parti[1]
                self.fa=int(str(str(maji)+str(minoi)))
                self.ex-=len(minoi)
            while self.fa%10==0 and self.fa!=0:
                self.fa=self.fa//10
                self.ex+=1
        else:
            self.fa=0
        if self.fa==0:
            self.ex==0
        while self.fa%10==0 and self.fa!=0:
            self.fa=self.fa//10
            self.ex+=1
    def __str__(self):
        if self.ex>=0:
            return str(self.fa)+self.ex*"0"
        else:
            len1=len(str(abs(self.fa)))
            len2=-self.ex #把fa的最后-ex位用小数点和前面隔开
            if len1>len2: #整数fa的位数比-ex大则不需要补0
                faword=str(abs(self.fa))
                right1=faword[-len2::]
                left1=faword[0:-len2]
                return (self.fa<0)*"-"+left1+"."+right1
            else: #整数fa的位数小于等于-ex需要补0
                faword=str(abs(self.fa)).zfill(len2)
                zep="0."
                if self.fa<0:
                    zep="-0."
                return zep+faword
    def __int__(self):
        if self.ex>=0:
            return self.fa*(10**self.ex)
        else:
            return self.fa//(10**(-1*self.ex))
    def __float__(self):
        return float(self.fa)*(10**self.ex)
    def __add__(self,self2):
        if self.ex>=self2.ex:
            self.fa=self.fa*(10**(self.ex-self2.ex))
            smallex=self2.ex
        else:
            self2.fa=self2.fa*(10**(self2.ex-self.ex))
            smallex=self.ex
        return superfloat(self.fa+self2.fa,smallex)
    def __sub__(self3,self4):
        if self3.ex>=self4.ex:
            self3.fa=self3.fa*(10**(self3.ex-self4.ex))
            smallex=self4.ex
        else:
            self4.fa=self4.fa*(10**(self4.ex-self3.ex))
            smallex=self3.ex
        return superfloat(self3.fa-self4.fa,smallex)
    def __mul__(self5,self6):
        afa=self5.fa
        bfa=self6.fa
        tfa=copy.copy(afa*bfa)
        aexi=self5.ex
        bexi=self6.ex
        cexi=copy.copy(self5.ex+self6.ex)
        return superfloat(tfa,cexi)
    def __truediv__(self7,self8):
        if type(self7)!=superfloat:
            self7=superfloat(self7)
        if type(self8)!=superfloat:
            self8=superfloat(self8)
        TDIG=DIVDIGITS
        while abs(int(self7.fa//self8.fa))<1000:
            self7.fa=self7.fa*(10**TDIG)
            self7.ex-=TDIG
            TDIG=TDIG*2
        return superfloat((self7.fa)//(self8.fa),(self7.ex)-(self8.ex))
    def __floordiv__(self9,self10):
        if self9.ex>=self10.ex:
            self9.fa=self9.fa*(10**(self9.ex-self10.ex))
        else:
            self10.fa=self10.fa*(10**(self10.ex-self9.ex))
        return superfloat(self9.fa//self10.fa)
    def __mod__(self11,self12):
        return copy.copy(self11)-copy.copy(self12)*copy.copy(self11//self12)
def sqrt(x1):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    px1=x1
    oriex=x1.ex
    faex=len(str(x1.fa))-1
    sqself=superfloat(1,(oriex+faex)//2)
    for i in range(NTI):
        sqself=(sqself+x1/sqself)/superfloat(2,0)
        x1=px1
    return sqself
def scmp(x1,x2=superfloat(0,0)):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    if type(x2)!=superfloat:
        x2=superfloat(x2)
    remain=x1-x2
    if remain.fa<0:
        return -1
    elif remain.fa==0:
        return 0
    else:
        return 1
def floor(x1,d1=0):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    d1=int(d1)
    if x1.ex+d1<=0:
        lfa=x1.fa//(10**(-x1.ex-d1))
    else:
        lfa=x1.fa*(10**(x1.ex+d1))
    return superfloat(lfa,-d1)
def ceil(x1,d1=0):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    d1=int(d1)
    if x1.ex+d1<=0:
        lfa=x1.fa//(10**(-x1.ex-d1))
        if x1.fa%(10**(-x1.ex-d1))>0:
            lfa+=1
    else:
        lfa=x1.fa*(10**(x1.ex+d1))
    return superfloat(lfa,-d1)
def sround(x1,d1=0):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    d1=int(d1)
    if x1.ex+d1<=0:
        lfa=x1.fa//(10**(-x1.ex-d1))
        if ((x1.fa*2)//(10**(-x1.ex-d1)))%2==1:
            lfa+=1
    else:
        lfa=x1.fa*(10**(x1.ex+d1))
    return superfloat(lfa,-d1)
def fastpow(int1,pn):
    if pn>0:
        res1=1
        while pn:
            if pn%2:
                res1*=int1
            int1*=int1
            pn=pn>>1
        return res1
    elif pn<0:
        return superfloat(1,0)/fastpow(int1,-pn)
    elif pn==0:
        return 1
def intexppow(x1,p1=1):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    p1=int(p1)
    if p1>0:
        return superfloat(fastpow(x1.fa,p1),p1*x1.ex)
    elif p1==0:
        return superfloat(1,0)
    else:
        return superfloat(1,0)/intexppow(x1,-p1)
def zexp(x1):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    if x1!=0:
        gx1=x1
        EXI=copy.copy(superfloat(1,0))
        UEXI=copy.copy(EXI)
        for i in range(1,TYI+1):
            MU1=gx1/superfloat(i,0)
            UEXI=UEXI*MU1
            EXI+=UEXI #e的指数幂泰勒展开式：Σx^N/N! N=0
        return EXI
    else:
        return 1
e=zexp(1)
def exp(x1):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    intx1=int(x1//superfloat(1,0))
    remx1=x1%superfloat(1,0)
    if remx1.fa!=0:
        return intexppow(e,intx1)*zexp(remx1)
    else:
        return intexppow(e,intx1)
def ln(x1):
    if type(x1)!=superfloat:
        x1=superfloat(x1)
    sta1=superfloat(copy.copy(len(str(abs(x1.fa)))+x1.ex))*superfloat(23025851,-7)
    x2=sta1
    for i in range(NTI):
        x2temp=x2
        x2=x2temp+x1/exp(x2temp)-superfloat(1,0)
    return x2
def log(r1,ba=e):
    if type(r1)!=superfloat:
        r1=superfloat(r1)
    preln=ln(r1)
    if type(ba)!=superfloat:
        ba=superfloat(ba)
    postln=ln(ba)
    return preln/postln
def spow(ba1,ex1):
    if type(ba1)!=superfloat:
        ba1=superfloat(ba1)
    if type(ex1)!=superfloat:
        ex1=superfloat(ex1)
    return intexppow(ba1,floor(ex1))*exp(ln(ba1)*(ex1%superfloat(1)))
def sin(rad1):
    if type(rad1)!=superfloat:
        rad1=superfloat(rad1)
    va1=superfloat(0,0)
    va2=rad1
    for i in range(1,TYI+1): #正弦函数泰勒展开式 ∑(-1)^(N)*x^(2N+1)/(2N+1)! N=0
        va1+=va2
        va2=va2*superfloat(-1,0)*rad1*rad1/superfloat(2*i)/superfloat(2*i+1)
    return va1
def cos(rad2):
    if type(rad2)!=superfloat:
        rad2=superfloat(rad2)
    va3=superfloat(0,0)
    va4=superfloat(1,0)
    for i in range(1,TYI+1): #余弦函数泰勒展开式 ∑(-1)^(N)*x^(2N)/(2N)! N=0
        va3+=va4
        va4=va4*superfloat(-1,0)*rad2*rad2/superfloat(2*i)/superfloat(2*i-1)
    return va3
def tan(rad3):
    if type(rad3)!=superfloat:
        rad3=superfloat(rad3)
    return sin(rad3)/cos(rad3)
def cot(rad4):
    if type(rad4)!=superfloat:
        rad4=superfloat(rad4)
    return cos(rad4)/sin(rad4)
def sec(rad5):
    if type(rad5)!=superfloat:
        rad5=superfloat(rad5)
    return superfloat(1,0)/cos(rad5)
def csc(rad6):
    if type(rad6)!=superfloat:
        rad6=superfloat(rad6)
    return superfloat(1,0)/sin(rad6)
def gausspi(n01=8):
    n01=int(n01)
    Na=superfloat(1)
    Na2O=superfloat(1)/sqrt(2)
    Na2CO3=superfloat(25,-2)
    NaHCO3=superfloat(1)
    Na2Cr2O7=superfloat(0)
    Na2SiO3=superfloat(0)
    for i in range(n01):
        Na2O2=(copy.copy(Na)+copy.copy(Na2O))*superfloat(5,-1)
        NaCl=sqrt(Na)
        NaClO=sqrt(Na2O)
        Na2O=NaCl*NaClO
        Na2SO4=copy.copy(Na)-copy.copy(Na2O2)
        Na2CO3=copy.copy(Na2CO3)-NaHCO3*Na2SO4*Na2SO4
        NaHCO3=copy.copy(NaHCO3)*superfloat(2)
        Na=copy.copy(Na2O2)
        Na2SiO3=superfloat(str(copy.copy(Na)))
    Na2Cr2O7_1=superfloat(str(copy.copy(Na2SiO3)))
    Na2Cr2O7_2=copy.copy(Na2O)
    Na2Cr2O7=Na2Cr2O7_1+Na2Cr2O7_2
    return Na2Cr2O7*Na2Cr2O7*superfloat(25,-2)/Na2CO3
pi=gausspi()
def asin(v1):
    if type(v1)!=superfloat:
        v1=superfloat(v1)
    tian1=superfloat(1,0)
    di1=superfloat(1,0)
    ren1=v1
    kun1=superfloat(0,0)
    for i in range(1,TYI+1):
        qian1=copy.copy(tian1)*copy.copy(di1)*copy.copy(ren1)
        tian1*=superfloat(2*i-1,0)/superfloat(2*i,0)
        di1*=superfloat(2*i-1,0)/superfloat((2*i+1),0)
        ren1*=v1*v1
        kun1+=qian1
    return kun1
def acos(v2):
    if type(v2)!=superfloat:
        v2=superfloat(v2)
    return pi*superfloat(5,-1)-asin(v2)
def atan(v3):
    if type(v3)!=superfloat:
        v3=superfloat(v3)
    if scmp(copy.copy(v3),superfloat(0))==0:
        return 0
    elif scmp(copy.copy(v3)*copy.copy(v3),superfloat(1))==-1:
        vv1=superfloat(0,0)
        vv2=copy.copy(v3)
        for i in range(1,TYI+1):
            mua1=superfloat(-1,0)*copy.copy(v3)*copy.copy(v3)
            vv2=copy.copy(vv2)*copy.copy(mua1)*copy.copy(superfloat(2*i-1))/copy.copy(superfloat(2*i+1,0))
            vv1=copy.copy(vv1)+copy.copy(vv2)
        return vv1+v3
    elif scmp(copy.copy(v3),superfloat(1))==0:
        return pi*superfloat(25,-2)
    elif scmp(copy.copy(v3),superfloat(-1))==0:
        return pi*superfloat(-25,-2)
    elif scmp(copy.copy(v3),superfloat(1))==1:
        return pi*superfloat(5,-1)-atan(superfloat(1)/v3)
    else:
        return pi*superfloat(-5,-1)-atan(superfloat(1)/v3)
def acot(v4):
    if type(v4)!=superfloat:
        v4=superfloat(v4)
    if scmp(v4)==-1:
        return pi*superfloat(-5,-1)-atan(v4)
    else:
        return pi*superfloat(5,-1)-atan(v4)
def asec(v5):
    if type(v5)!=superfloat:
        v5=superfloat(v5)
    return acos(superfloat(1)/v5)
def acsc(v6):
    if type(v6)!=superfloat:
        v6=superfloat(v6)
    return asin(superfloat(1)/v6)
def sinh(v7):
    if type(v7)!=superfloat:
        v7=superfloat(v7)
    baby1=exp(v7)
    baby2=exp(superfloat(-1)*v7)
    return (baby1-baby2)*superfloat(5,-1)
def cosh(v8):
    if type(v8)!=superfloat:
        v8=superfloat(v8)
    baby3=exp(v8)
    baby4=exp(superfloat(-1)*v8)
    return (baby3+baby4)*superfloat(5,-1)
def tanh(v9):
    if type(v9)!=superfloat:
        v9=superfloat(v9)
    return sinh(v9)/cosh(v9)
def coth(v10):
    if type(v10)!=superfloat:
        v10=superfloat(v10)
    return cosh(v10)/sinh(v10)
def sech(v11):
    if type(v11)!=superfloat:
        v11=superfloat(v11)
    return superfloat(1)/cosh(v11)
def csch(v12):
    if type(v12)!=superfloat:
        v12=superfloat(v12)
    return superfloat(1)/sinh(v12)
def asinh(v13):
    if type(v13)!=superfloat:
        v13=superfloat(v13)
    return ln(v13+sqrt(v13*v13+superfloat(1)))
def acosh(v14):
    if type(v14)!=superfloat:
        v14=superfloat(v14)
    return ln(v14+sqrt(v14*v14-superfloat(1)))
def atanh(v15):
    if type(v15)!=superfloat:
        v15=superfloat(v15)
    return superfloat(5,-1)*(ln(superfloat(1)+v15)-ln(superfloat(1)-v15))
def acoth(v16):
    if type(v16)!=superfloat:
        v16=superfloat(v16)
    return superfloat(5,-1)*(ln(superfloat(1)+v16)-ln(v16-superfloat(1)))
def asech(v17):
    if type(v17)!=superfloat:
        v17=superfloat(v17)
    return acosh(superfloat(1)/v17)
def acsch(v18):
    if type(v18)!=superfloat:
        v18=superfloat(v18)
    return asinh(superfloat(1)/v18)
