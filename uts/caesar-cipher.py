def decrypt(chiper,key):
    result = ""
    for i in range(len(chiper)):
        if(chiper[i].isupper()):
            result += chr((ord(chiper[i]) - key + 65) % 26 + 65)
        else:
            result += chr((ord(chiper[i]) - key + 97) % 26 + 97)
            
    return result
chiper = "DWWDFNDWRQFH" #Plaintext = "ATTACKATONCE"
key = 3
print("Chiper: " + chiper)
print("Key: " + str(key))
print("Decrypt: " + decrypt(chiper,key))