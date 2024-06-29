# #some tricky trick ;)
# stars='*********************************************************************************************'
# length=int(input('input:'))
# while(length>0):
#     print(stars[0:length])
#     length-=1
n=int(input("n:"))
str=''
for i in range(n):
    str+=" "
def line(str):
    for i in range(n):
        str[i]="*"
        str[-1+i]="*"
        print(str)
line(str)
def is_prime(number):
    global prime_numbers
    for i in prime_numbers:
        if n