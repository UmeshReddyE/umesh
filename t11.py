import numpy as np
def q1(arr):
    print("Last row: ", arr[-1], "\nLast but one row: ", arr[-2])
def q2(self,arr):
    print("Sum of 2nd row values: ", sum(arr[3])) 
def q3(arr):
    maxi = np.where(arr == np.amax(arr))
    print("Maximum number is: ", np.amax(arr))
    print("They are at: ")
    print(*list(zip(maxi[0], maxi[1])), sep="\n")
def q4(arr):
    last = np.array(np.random.randint(1,5, (1, 4)))
    arr = np.append([arr], [[last]]).reshape(6, 4)
    print(arr)
def q5(arr):
    x, z = map(int, input("Enter a value to replace and replace with: ").split())
    arr[x == arr] = z
    print(arr)
def q6(arr):
    x = int(input("Enter the x value: "))
    print(arr[x > arr].size)
def q7(arr):
    s = arr.size
    print("All possible shapes of the array are: ")
    con = "Shape ({},{}):\n"
    for i in range(1, s):
     if s % i == 0:
      print(con.format(i, int(s / i)), arr.reshape(i, int(s / i)))
def q8(arr):
    arr=arr.astype("float64")
    print("After changing the datatype to float: \n",arr)
def q9(arr):
   print("Unique elements in the given array are: ",np.unique(arr))