def get_arr():
    length= int(input("length of first line: "))
    while(True):
        if length%2!=0 and length >= 3:
            arr=["*"]*length
            return arr,length
        else:
            length=int(input("odd and larger than 2 numbers are valid only :"))
def dimond(arr,length):
        j=int(length/2+1/2)
        for i in range(length):
            arr2=arr.copy()
            j=int(length/2+1/2)+1
            arr2[j-i:j+i]=" "
            # arr[j:-i]=" "
            line=''.join(arr2)
            print (line)
def liner(arr):
    length = len(arr)
    for i in range(length):
        str=arr.copy()
        str[i]="*"
        str[length-1-i]="*"
        line=''.join(str)
        print(line)
arr,length=get_arr()
dimond(arr,length)
exit()
