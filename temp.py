def calcRedundantBits(m):
    for i in range(m):
        if 2 ** i >= m + i + 1:
            return i

def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''

    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])

        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])

        res = res + val * (10 ** i)

    return int(str(res), 2)

def list_to_int(lst):
    sample_data = []
    for i in lst:
        sample_data.append(int(i))
    return sample_data

def hamming_decode(received_data):
    n = len(received_data)
    r = calcRedundantBits(n)

    decoded_data = []

    # Error detection and correction logic
    error_detected = False
    for i in range(n):
        if i + 1 != 2 ** int(round(pow(2, i))):
            decoded_data.append(received_data[i])

    return decoded_data

# Main part of the code
data = str(input("Enter data: "))
print("Original Data is " + data)

m = len(data)
r = calcRedundantBits(m)
arr = posRedundantBits(data, r)
arr = calcParityBits(arr, r)

print("Sender data transferred is " + arr) 

arr = str(input("Enter erroneous data: "))
print("Receiver Data is " + arr)
print("Error Data is " + arr)

correction = detectError(arr, r)
if correction == 0:
    print("There is no error in the received message.")
else:
    print("The position of error is", len(arr) - correction + 1, "from the left")
    if arr[len(arr) - correction] == '1':
        arrlist = list(arr)
        arrlist[len(arr) - correction] = '0'
        arr = ''.join(arrlist)
    else:
        arrlist = list(arr)
        arrlist[len(arr) - correction] = '1'
        arr = ''.join(arrlist)

print("Data after correcting error is " + arr)

# Convert the string to a list of integers and perform decoding
received_data = list(arr)
received_data[2] = str(int(received_data[2]) ^ 1) # Flip one bit to simulate an error
sample_data = list_to_int(received_data)
decoded_data = hamming_decode(sample_data)
print("Decoded data:", decoded_data)
