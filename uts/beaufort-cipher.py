# Fungsi untuk membuat tabel Beaufort
def tabel_beaufort():
  tabel = []

  for i in range(26):
    tabel.append([])
  
  for baris in range(26):
    for kolom in range(26):
      # Jika baris kurang dari 65/A
      if (baris + 65) - kolom < 65:
        # pindah kembali ke A setelah Z
        # setelah baris pertama, setiap huruf akan bergeser ke kiri dengan satu posisi dibandingkan dengan baris di atasnya
        tabel[baris].append(chr((baris + 65) - kolom + 26 ))
      else:
        # setelah baris pertama, setiap huruf akan bergeser ke kiri dengan satu posisi dibandingkan dengan baris di atasnya
        tabel[baris].append(chr((baris + 65) - kolom ))
  return tabel

def cipher_key():
    cipher = input("masukan cipher: ").upper()
    key = input("masukan keyword: ").upper()
    # Untuk menyimpan perulangan key
    keymap = ""
    k = 0

    for i in range(len(cipher)):
      # Jika cipher mempunyai spasi maka keymap akan diberi spasi
        if ord(cipher[i]) == 32:
            keymap += " "
        else:
          # Perulangan key sehingga mempunyai panjang yang sama dengan cipher
            if k < len(key):
                keymap += key[k]
                k += 1
            else:
                k = 0
                keymap += key[k]
                k += 1
    # Membalikan nilai cipher dan keymap
    return cipher,keymap

def dekripsi(cipher,keymap):
  # Panggil tabel beaufort
  tabel = tabel_beaufort()
  plaintext = ""
  for i in range (len(cipher)):
    # Jika cipher == " " maka plaintext == " " 
    if ord(cipher[i]) == 32 :
      plaintext += " "
    else:
      # Mencocokkan baris dan kolom pada tabel
      kolom = ord(cipher[i]) - 65
      baris = ord(keymap[i]) - 65
      plaintext += tabel[baris][kolom]
  # Print dekrip 
  print(plaintext)


def main():
  cipher,keymap = cipher_key()
  dekripsi(cipher,keymap)

main()

# cipher :TCQHJSWHWAU
# plaintext: PROGRAMMING
# key:ITENAS
