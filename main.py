#Stick System master 3.10
from os import *

class Msg:
    def __init__ (self,msg):
        self.info = msg
    def change_msg (self,new_msg):
        self.info = new_msg
    def print (self):
        print('\033[34mI:\033[0m'+self.msg)
def print_i (msg):
    n_class=Msg(msg)
    n_class.print()


class W_msg:
    def __init__ (self,w_msg):
        self.info = w_msg
    def change_msg (self,new_w_msg):
        self.info = new_w_msg
    def print (self):
        print('\033[31mW:\033[0m'+self.info)
def print_w (w_msg):
    n_class=W_msg(w_msg)
    n_class.print()


def print_e (msg):
    print('\033[34m'+msg+'\033[0m')


def cls ():
    system('cls')
print_e('Sitck System master 3.10')
print_e('On Sitck Kernel 3.50')
def input_user ():
    info=input('[Cloud@Stick]->')
    return info
def jisuanqi ():
    w_1=0
    def jia ():
        q1 = int(eval(input('输入第一个加数>')))
        q2 = int(eval(input('输入第二个加数>')))
        q3 = q1+q2
        print('{}+{}={}'.format(q1,q2,q3))
    def jian ():
        q1 = int(eval(input('输入 被减数>')))
        q2 = int(eval(input('输入 减数>')))
        q3 = q1-q2
        print('{}-{}={}'.format(q1, q2, q3))
    def cheng ():
        q1 = int(eval(input('输入第一个乘数>')))
        q2 = int(eval(input('输入第二个乘数>')))
        q3 = q1 * q2
        print('{}x{}={}'.format(q1, q2, q3))
    def chu ():
        q1 = int(eval(input('输入 被除数>')))
        q2 = int(eval(input('输入 除数>')))
        q3 = q1 / q2
        print('{}/{}={}'.format(q1, q2, q3))
    print('计算器 V3.10')
    print('Stick System.io.')
    print('功能： 1.加 2.减 3.乘 4.除')
    while w_1 == 0:
        user_1=input('输入功能>')
        if user_1 == '1':
            jia()
        elif user_1 == '2':
            jian()
        elif user_1 == '3':
            cheng()
        elif user_1 == '4':
            chu()
        else:
            print('请重新输入！')
def up_data_log ():
    log='''
    更新日志
    2022/12/11 V3.10
    发布内核 3.50
    发布 Shell 3.10
    '''
    print(log)
