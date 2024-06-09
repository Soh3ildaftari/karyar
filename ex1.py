#child test
def child_check(age):
    if (age<=13):
        return True
    else:
        return False
age=input('give me your age:')
if child_check(int(age)):
    print('you are a child')
else:
    print('you\'r not a child')