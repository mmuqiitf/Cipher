# Import Package
import sys
import numpy

def cipher_encryption():
   msg = input("Enter message: ").upper()
   msg = msg.replace(" ", "")
   # if message legth is odd number, append 0 at the end
   len_chk = 0
   if len(msg) % 2 != 0:
      msg += "0"
      len_chk = 1
   
   # msg to matrix
   row = 2
   col = int(len(msg)/2)
   msg2d = numpy.zeros((row,col), dtype=int) 

   itr1 = 0
   itr2 = 0
   for i in range(len(msg)):
      if i%2 == 0:
         msg2d[0][itr1] = int(ord(msg[i])-65)
         itr1 += 1
      else:
         msg2d[1][itr2] = int(ord(msg[i])-65)
         itr2 += 1
   # end for
   key = input("Enter 4 letter key strings: ").upper()
   key = key.replace(" ", "")

   # key 2x2
   key2d = numpy.zeros((2,2), dtype=int)
   itr3 = 0
   for i in range(2):
      for j in range(2):
         key2d[i][j] = ord(key[itr3])-65
         itr3 += 1
   
   # checking validity of the key
   # finding determinant
   determinant = (key2d[0][0] * key2d[1][1]) - (key2d[0][1] * key2d[1][0])
   determinant = determinant % 26

   # finding multipicative inverse
   mul_inverse = -1
   for i in range(26):
      temp_inverse = determinant * i
      if temp_inverse % 26 == 1:
         mul_inverse = i
         break
      else:
         continue
   # end for
   
   if mul_inverse == -1:
      print("Invalid key")
      sys.exit()
   
   encrypt_text = ""
   itr_count = int(len(msg)/2)
   if len_chk == 0:
      for i in range(itr_count):
         temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
         encrypt_text += chr((temp1 % 26) + 65)
         temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
         encrypt_text += chr((temp2 % 26) + 65)
      # end for
   else:
      for i in range(itr_count-1):
         temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
         encrypt_text += chr((temp1 % 26) + 65)
         temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
         encrypt_text += chr((temp2 % 26) + 65)
      # end for
   # end if else

   print("Encryption Text:" + encrypt_text)


def cipher_decryption():
    msg = input("Enter message: ").upper()
    msg = msg.replace(" ", "")

    # if message length is odd number, append 0 at the end
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # msg to matrix
    row = 2
    col = int(len(msg) / 2)
    msg2d = numpy.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i]) - 65)
            itr2 += 1
    # for

    key = input("Enter 4 letter Key String: ").upper()
    key = key.replace(" ", "")

    # key to 2x2
    key2d = numpy.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1
    # for

    # finding determinant
    determinant = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    determinant = determinant % 26

    # finding multiplicative inverse
    mul_inverse = -1
    for i in range(26):
        temp_inverse = determinant * i
        if temp_inverse % 26 == 1:
            mul_inverse = i
            break
        else:
            continue
    # for

    # adjugate matrix
    # swapping
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

    # changing signs
    key2d[0][1] *= -1
    key2d[1][0] *= -1

    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    # multiplying multiplicative inverse with adjugate matrix
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inverse

    # modulo
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    # cipher to plain
    decryp_text = ""
    itr_count = int(len(msg) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    # if else

    print("Decrypted Text: {}".format(decryp_text))





def main():
   choice = int(input("1. Encryption\n2.Decryption\nChoose(1,2): "))
   if choice == 1:
      print("-- Encryption --")
      cipher_encryption()
   elif choice == 2:
      print("-- Decryption --")
      cipher_decryption()
   else:
      print("Invalid Choice")

main()

# Chiper : APADZCJJJB
# Key : HILL
# Plain : short thing

# Cipher Algorithm

# Encryption
# 1. Convert message into pairs of 2 rows and multiple columns, number of columns is total length of message divided by 2
# 2. Take a 4 letter key and convert it into 2x2 matrix
# 3. Perform matrix multiplication between each row and column pair of message and 2x2 key matrix
# 4. Take modulo 26 of result to obtain cipher text letter

# Decryption
# 1. Convert message into pairs of 2 rows and multiple columns, number of columns is total length of message divided by 2
# 2. Take a 4 letter key and convert it into 2x2 matrix
# 3. Find determinant of the key matrix
# 4. find multiplicative inverse of the determinant ofkey matrix
# 5. find adjugate matrix of key matrix
# 6. multiply multiplicative inverse of determinant with adjugate matrix and take mod 26 of result
# 7. Perform matrix multiplication between each row and column pair of message and 2x2 key matrix
# 8. Take modulo 26 of result to obtain cipher text letter