# 5 ekikdaarkrptgrfi&tn s ioa
ciphertext = '5 ekikdaarkrptgrfi&tn s ioa' # Masukan Plain Text
key = 3 # Memasukan Key
pembatas = '&' # Masukan pembatas

j = 1
tabel = []
temp = ""
plaintext = ""
switch = 1
# Tabel cipher
tabcipher = []
tabcipher += ciphertext

for i in range(len(tabcipher)):
  # Jika di dalam huruf pada tabel cipher adalah pembatas 
  if tabcipher[i] == pembatas:
    switch = 0
  # Jika di dalam huruf pada tabel cipher adalah bukan pembatas
  elif tabcipher[i] != pembatas:
    # Jika j sama dengan key
    if j == key:
      # Jika di dalam huruf selanjutnya adalah pembatas
      if tabcipher[i+1] == pembatas:
        tabel += " " + tabcipher[i]
        j = 2
      else:
        tabel += " " + tabcipher[i]
        j = 2
    # Jika switch = 0 maka huruf pada tabel cipher disimpan pada variabel temp
    elif switch == 0:
      temp += tabcipher[i]
    # Jika j != key
    else:
      # Jika huruf selanjutnya adalah pembatas
      if tabcipher[i+1] == pembatas:
        tabel += tabcipher[i] 
        j = 2
      else:
        tabel += tabcipher[i]
        j += 1

while (len(tabel) % key != 0):
  tabel.append(" ")

j = 0
for i in range (len(temp)):
  j += 1
  tabel[(j*key)-1] = temp[i]
for i in range (len(tabel)):
  plaintext += tabel[i]

print (plaintext)