import random
import time
import os
import sys
cnsts=(23522,45.252,6904,19487,0.48121)
def guid():
    def gettime():
        return (int(time.time()*cnsts[2])*cnsts[0]+int((time.time()**cnsts[4])*cnsts[1])*cnsts[3])%(36**7)
    def cvtb36(c):
        cst='0123456789abcdefghijklmnopqrstuvwxyz'
        b=''
        for i in range(7):
            b+=cst[c%36]
            c=c//36
        return b[::-1]
    def rndst(l):
        s=''
        for i in range(l):
            s+=random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
        return s
    return rndst(6)+';'+cvtb36(gettime())+'-'+rndst(15)+'('+rndst(4)+')'
def _int(w):
    def flt(x):
        if int(x)>100000:
            return true
        return abs(int(float(x))-float(x))>1e-7
    if(w=='version' or w=='ver' or w=='Version'):
        return 100001
    elif int(w)==-1:
        return 0
    elif flt(w):
        return -114514
    else:
        return int(w)
if __name__=='__main__':
    try:
        q=_int(input("guid_36 generator\nHow many guid_36s?(type 'version','ver' or 'Version' to show version) "))
        if q<=0:
            raise Exception
        elif q==100001:
            print("guid_36 generator release-0.1.0")
        else:
            for i in range(q):
                print(guid())
    except Exception:
        print('Number of guid_36s MUST be a positive integer that isn\'t greater than 100000!')
