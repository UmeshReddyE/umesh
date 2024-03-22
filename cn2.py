# Python program to demonstrate
# hamming code


def calcRedundantBits(m):
	for i in range(m):
		if(2**i >= m + i + 1):
			return i

def posRedundantBits(data, r):

	# Redundancy bits are placed at the positions
	# which correspond to the power of 2.
	j = 0
	k = 1
	m = len(data)
	res = ''

	# If position is power of 2 then insert '0'
	# Else append the data
	for i in range(1, m + r+1):
		if(i == 2**j):
			res = res + '0'
			j += 1
		else:
			res = res + data[-1 * k]
			k += 1

	# The result is reversed since positions are
	# counted backwards. (m + r+1 ... 1)
	return res[::-1]


def calcParityBits(arr, r):
	n = len(arr)

	# For finding rth parity bit, iterate over
	# 0 to r - 1
	for i in range(r):
		val = 0
		for j in range(1, n + 1):

			# If position has 1 in ith significant
			# position then Bitwise OR the array value
			# to find parity bit value.
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])
				# -1 * j is given since array is reversed

		# String Concatenation
		# (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
		arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
	return arr


def detectError(arr, nr):
	n = len(arr)
	res = 0

	# Calculate parity bits again
	for i in range(nr):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])

		# Create a binary no by appending
		# parity bits together.

		res = res + val*(10**i)

	# Convert binary to decimal
	return int(str(res), 2)
def list_to_int(lst):
    sample_data=[]
    for i in lst:
        sample_data.append(int(i))
    return sample_data


def hamming_decode(received_data):
    if len(received_data) != 7:
        raise ValueError("Received data must be 7 bits long")
    s1 = received_data[0] ^ received_data[2] ^ received_data[4] ^ received_data[6]
    s2 = received_data[1] ^ received_data[2] ^ received_data[5] ^ received_data[6]
    s3 = received_data[3] ^ received_data[4] ^ received_data[5] ^ received_data[6]
    error_position = s1 + s2 * 2 + s3 * 4
    if error_position > 0:
        received_data[error_position - 1] ^= 1
    decoded_data = [received_data[2], received_data[4], received_data[5], received_data[6]]

    return decoded_data


# Enter the data to be transmitted
data = str(input("enter data :"))
print("Original Data is " + data)
# Calculate the no of Redundant Bits Required
m = len(data)
r = calcRedundantBits(m)

# Determine the positions of Redundant Bits
arr = posRedundantBits(data, r)

# Determine the parity bits
arr = calcParityBits(arr, r)

# Data to be transferred
print("Sender data transferred is " + arr) 

# Stimulate error in transmission by changing
# a bit value.
# 10101001110 -> 11101001110, error in 10th position.

arr = str(input("enter errorerd data:"))
print("Receiver Data is " + arr)
print("Error Data is " + arr)
correction = detectError(arr, r)
if(correction==0):
	print("There is no error in the received message.")
else:
	print("The position of error is ",len(arr)-correction+1,"from the left")
if arr[len(arr)-correction] == '1':
	arrlist = list(arr)
	arrlist[len(arr)-correction] = '0'
	arr = ''.join(arrlist)
else:
	arrlist = list(arr)
	arrlist[len(arr)-correction] = '1'
	arr = ''.join(arrlist)
print("Data after correcting error is " + arr)
received_data = list(arr)
received_data[2] = str(int(received_data[2]) ^ 1 ) # Flip one bit to simulate an error
sample_data = list_to_int(list(arr))
# print(sample_data)
decoded_data = hamming_decode(sample_data)
print("Decoded data:", data)