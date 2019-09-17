import re


def PW_check(string):
    msg = []
    if len(string) < 8:
        msg.append("Input more than 8 strings.")
    if not check_Upper.search(string):
        msg.append("Input 1 or more uppercase letters.")
    if not check_num.search(string):
        msg.append("Input 1 or more numbers.")
    if not check_sign.search(string):
        msg.append("Input 1 or more symbols." + "  Example:" + r"!#%&'()*+,/:;<=>?@_`{}~")
    if len(msg) == 0:
        return True
    else:
        [print(i) for i in msg]
        return False


try:
    check_num = re.compile(r'\d')
    check_sign = re.compile(r"[!#%&'()*+,/:;<=>?@_`{}~]")
    check_Upper = re.compile(r'[A-Z]')
    judge = ''

    while not judge:
        word = input("Input PassWord \nPassWord:")
        judge = PW_check(word)

finally:
    print("end")
