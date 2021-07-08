import sys

def Calc_CLI():
    if sys.argv[1] == '':
        print('消遣我？后面跟上你的身高！！SB')

    elif sys.argv[1] == '[你的身高]':
        print('\r\n请不要把名字也抄上，屑屑！\r\n')

    else:
        Height = sys.argv[1]
        print ('\r\n' + '    ' + '你的身高是' + Height + 'cm' + '\r\n')

Calc_CLI()