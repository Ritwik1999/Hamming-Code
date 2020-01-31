# The following script demonstrates the generation of Hamming Code for any length of the message to be transmitted

# calculate number of redundancy bits required
def calc_no_of_red_bits(m):
    r = 1
    while(True):
        if (2**r) >= m + r + 1:
            break
        else:
            r += 1
    return r

# make positions for redundancy bits within the message
def insert_red_pos(msg_list, r):
    pos = 0
    msg_pos = 0
    new_msg_list = [0 for i in range(len(msg_list) + r)]
    for i in range(len(new_msg_list)):
        if i + 1 == (2**pos):
            pos += 1
            new_msg_list[i] = 'r'
        else:
            new_msg_list[i] = msg_list[msg_pos]
            msg_pos += 1
    return new_msg_list

# Calculate the redundancy bit
def calc_xor(msg, value):
    arr = []
    for i in range(len(msg)):
        if (i+1 & (1 << value) == 1 << value) and msg[i] != 'r':
            arr.append(msg[i])
    bit = int(arr[0])
    for i in range(1, len(arr)):
        bit = bit ^ int(arr[i])
    return str(bit)

# Insert the redundancy bit
def add_red_bits(msg, r):
    for i in range(r):
        bit = calc_xor(msg, i)
        msg[(2**i) - 1] = bit
    print("The code to be transmitted is: " + (''.join(msg))[::-1])


msg = input('Enter the data: ')
no_of_red_bits = calc_no_of_red_bits(len(msg))
length_msg = insert_red_pos(list(msg[::-1]), no_of_red_bits)
new_msg = add_red_bits(length_msg, no_of_red_bits)
