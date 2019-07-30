# Fungsi ini untuk melooping key sepanjang ciphertextnya
def generateKey(cipher_text, keyword): 
	keyword = list(keyword) 
	# Jika panjang cipher text == panjang keyword maka langsung menampilkan keyword
	if len(cipher_text) == len(keyword): 
		return(keyword) 
	else: 
		# Jika panjang cipher != panjang keyword maka lakukan perulangan hingga panjang keyword == panjang cipher
		for i in range(len(cipher_text) - len(keyword)): 
			keyword.append(keyword[i % len(keyword)]) 
	return("" . join(keyword)) 

# Fungsi ini untuk mendekripsi ciphertext sesuai dengan key
def decrypt(cipher_text, key):
	# Untuk menyimpan hasil dekripsi berupa array 
	original_text = [] 
	# Melakukan perulangan sepanjang panjang cipher
	for i in range(len(cipher_text)): 
		x = chr(((ord(cipher_text[i]) - ord(key[i]) + 26) % 26) + ord('A'))
		original_text.append(x) 
		# Mengubah array menjadi string
	return("" . join(original_text)) 
	

# Driver code / Input user
cipher_text = "XKSTRSUFMAG"
keyword = "ITENAS"
key = generateKey(cipher_text, keyword)
# Tampilan
print("Encrypt Text: " + cipher_text) 
print("Key : " + keyword)
print("Decrypted Text : " + decrypt(cipher_text, key))
# HASIL PLAINTEXT : PROGRAMMING

