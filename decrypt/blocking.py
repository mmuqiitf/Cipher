table = []

def divide(block,cipher):
  if block > cipher:
    result= (block+cipher)//cipher
  else:
    result= (block+cipher)//block
  return result

ciphertext = input("masukan pesan:").upper()
block = input("masukan banyak block:")
plaintext= " "
m_row = 0
m_column = 0

for row in range(int(block)):
  table.append([])

for alphabet in ciphertext:
    if m_column < divide(int(block),len(ciphertext)):
      table[m_row].append(alphabet)
      m_column += 1
    else:
      m_column = 0
      m_row += 1
      table[m_row].append(alphabet)
      m_column += 1
     
for column in range(len(table)):
  if len(table[column]) != divide(int(block),len(ciphertext)):
    table[column].append(" ")

for column in range(divide(int(block),len(ciphertext))):
  for row in range(int(block)):
    if row < (int(block)):
      plaintext += table[row][column]
    else:
      plaintext += " "

for column in table:
      for row in column:
          print(row, end=" | ")
      print(end="\n")

print("Plaintext: " + plaintext)