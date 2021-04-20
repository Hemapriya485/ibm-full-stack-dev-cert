# get a list of amstrong numbers within a given input range
def check_amstrong(num1,num2):
    List_of_amstrong=[]
    for x in range(num1+1,num2):
        n=0
        temp1=x
        temp2=x
        while(temp1>0):
            n=n+1
            temp1=int(temp1/10)
        ams=0
        while(temp2>0):
            rem=temp2%10
            ams=ams+(rem**n)
            temp2=int(temp2/10)
        if(ams==x):
            List_of_amstrong.append(x)
    return List_of_amstrong
num1=int(input("Enter upper limit:"))
num2=int(input("Enter lower limit:"))
print(num1,num2)
print(check_amstrong(num1,num2))
