
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt (msg):

    #Find side length
    msg_length = len(msg)
    side_length = 0
    for i in range(100):
        if i**2 >= msg_length:
            side_length = i
            break

    msg_encrypted = ""
    for x in range(side_length):
        for y in range(side_length):
            try:
                #Returns the character at the apporiate index based on the formula below
                msg_encrypted = msg_encrypted + (msg[(side_length - y)*side_length - (side_length - x)])
            except:
                pass
    return msg_encrypted
            
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt (msg):

    #Find side length
    msg_length = len(msg)
    side_length = 0
    for i in range(100):
        if i**2 >= msg_length:
            side_length = i
            break

    msg_decrypted = ""
    for x in range(side_length):
        for y in range(side_length):
            try:
                #This is the same formula as encrypt, but the output is reversed
                msg_decrypted = (msg[(side_length - y)*side_length - (side_length - x)]) + msg_decrypted
            except:
                pass
    return msg_decrypted

def main():

  # read the two strings P and Q from standard imput
    cipher_in = ['gonewiththewind', 'osotvtnheitersec']
    decrypted_p = cipher_in[0]
    encrypted_q = cipher_in[1]

  # encrypt the string P
    encrypted_p = encrypt(decrypted_p)

  # decrypt the string Q
    descrypted_q = decrypt(encrypted_q)

  # print the encrypted string of P and the 
  # decrypted string of Q to standard out
    print(encrypted_p)
    print(descrypted_q)

if __name__ == "__main__":
  main()
