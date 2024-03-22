import t11 as o
import numpy as np
arr = np.random.randint(1, 20, (5, 4))
print(arr)
n=0
while True and n is not 10:
    print("\t")
    print("\t1.Retrieve the last two row values\t\n\t2.Retrieve the sum of the second row values \t\n\t3.Display the max value index in the array. \t\n\t4.Add a new row \t\n\t5.Replace a specific value\t\n\t6.Identify how many values are less than given x\n\t7.Reshape the array into other possible shapes\n\t8.Convert the data type into float\n\t9.Identify unique values in the array\n\t10.EXIT()")
    print("\t")
    n=int(input("enter ur choice:"))
    if n==1:
        o.q1(arr)
    elif n==2:
        o.q2(arr)
    elif n==3:
        o.q3(arr)
    elif n==4:
        o.q4(arr)
    elif n==5:
        o.q5(arr)
    elif n==6:
        o.q6(arr)
    elif n==7:
        o.q7(arr)
    elif n==8:
        o.q8(arr)
    elif n==9:
        o.q9(arr)
