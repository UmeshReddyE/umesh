
def Arithmetic_progression(arr):
    diff = arr[1] - arr[0]
    n = len(arr)

    for i in range(2, n):
        if arr[i] - arr[i - 1] != diff:
            return False
    return True

def Geometric_progression(arr):
	if len(arr) <= 1:
		return True
	ratio = arr[1]/float(arr[0])
	for i in range(1, len(arr)):
		if arr[i]/float(arr[i-1]) != ratio:
			return False
	return True
	

def Harmonic_progression(arr):
	n = len(arr)
	if (n == 1):
		return True
	rec = []
	for i in range(0, len(arr)):
		a = 1 / arr[i]
		rec.append(a)
	return(rec)
	rec.sort()
	d = rec[1] - rec[0]
	for i in range(2, n):
		if (rec[i] - rec[i-1] != d):
			return False
	return True
def Quadrant(x,y):
   if(x>0 and y>0):
       return("First quadrent")
   elif(x>0 and y<0):
       return("Second quadrent")
   elif(x<0 and y<0):
       return("Third quadrent")
   elif(x<0 and y>0):
       return("Fourth quadrent")
   else:
       pass
def Unsorted(arr):
   if arr is not sorted(arr):
       return True
   else:
       return False
def Sorted(arr):
   if arr==sorted(arr):
        return True
   else:
       return False
def Sqrt(num):
   return(num**0.5)
def Power(n1,n2):
    return (n1**n2)
def GCD(a, b):
	result = min(a, b)

	while result:
		if a % result == 0 and b % result == 0:
			break
		result -= 1
	return result

def Log(x,b):
   log_b = 2
   while x != int(round(b ** log_b)):
      log_b += 0.01
   return ((log_b))