def hamming_encode(data):
    # Ensure the data length is 4 bits
    if len(data) != 4:
        raise ValueError("Input data must be 4 bits long")

    # Calculate parity bits
    p1 = data[0] ^ data[1] ^ data[3]
    p2 = data[0] ^ data[2] ^ data[3]
    p3 = data[1] ^ data[2] ^ data[3]

    # Create the encoded word
    encoded_data = [p1, p2, data[0], p3, data[1], data[2], data[3]]

    return encoded_data

def hamming_decode(received_data):
    # Ensure the received data length is 7 bits
    if len(received_data) != 7:
        raise ValueError("Received data must be 7 bits long")

    # Calculate syndrome bits
    s1 = received_data[0] ^ received_data[2] ^ received_data[4] ^ received_data[6]
    s2 = received_data[1] ^ received_data[2] ^ received_data[5] ^ received_data[6]
    s3 = received_data[3] ^ received_data[4] ^ received_data[5] ^ received_data[6]

    # Calculate error position
    error_position = s1 + s2 * 2 + s3 * 4

    # Correct the error
    if error_position > 0:
        received_data[error_position - 1] ^= 1

    # Extract the original data
    decoded_data = [received_data[2], received_data[4], received_data[5], received_data[6]]

    return decoded_data

# Demonstration
data = [0, 0, 1, 1]  # 4-bit data
encoded_data = hamming_encode(data)
print("Encoded data:", encoded_data)

# Introducing an error in the received data
received_data = list(encoded_data)
received_data[2] ^= 1  # Flip one bit to simulate an error
decoded_data = hamming_decode(received_data)
print("Decoded data:", decoded_data)