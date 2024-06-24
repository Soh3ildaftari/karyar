def get_arr():
    length= int(input("length of first line: "))
    while(True):
        if length%2!=0 and length >= 3:
            arr=[" "]*length
            return arr
        else:
            length=int(input("odd and larger than 2 numbers are valid only :"))
def liner(arr):
    length = len(arr)
    for i in range(length):
        str=arr.copy()
        str[i]="*"
        str[length-1-i]="*"
        line=''.join(str)
        print(line)
arr=get_arr()
liner(arr)
exit()