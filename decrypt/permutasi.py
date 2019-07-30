ciphertext = "n etk5skd aiirk raatgorpif"
tabel = []

for i in range(len(ciphertext)):
    # Jika i adalah kelipatan 6 maka akan displit dan i menjadi awal 
    if i % 6 == 0:
        # Menambahkan ke tabel
        tabel.append(ciphertext[i:i+6])

print(tabel)

for j in range(len(tabel)):
    # Jika tabel mempunyai panjang = 6 maka pindah posisi
    if len(tabel[j]) == 6:
        # Posisi : 5-1-3-2-4-0
        plaintext = tabel[j][5] + tabel[j][1] + tabel[j][3] + tabel[j][2] + tabel[j][4] + tabel[j][0]
        print(plaintext, end='')
    # Jika tabel mempunyai panjang = 1 maka tidak diubah posisinya
    elif len(tabel[j]) == 1:
        plaintext = tabel[j]
        print(plaintext, end='')
    # Jika tabel mempunyai panjang = 2 maka pindah posisi 
    elif len(tabel[j]) == 2:
        # Posisi : 1-0
        plaintext = tabel[j][1] + tabel[j][0]
        print(plaintext, end='')
    # Jika tabel mempunyai panjang = 3 maka pindah posisi
    elif len(tabel[j]) == 3:
        # Posisi : 2-1-0
        plaintext = tabel[j][2] + tabel[j][1] + tabel[j][0]
        print(plaintext, end='')
    # Jika tabel mempunyai panjang = 4 maka pindah posisi
    elif len(tabel[j]) == 4:
        # Posisi : 3-1-2-0
        plaintext = tabel[j][3] + tabel[j][1] + tabel[j][2] + tabel[j][0]
        print(plaintext, end='')
    # Jika tabel mempunyai panjang = 5 maka pindah posisi
    elif len(tabel[j] == 5):
        # Posisi : 4-3-2-1-0
        plaintext = tabel[j][4] + tabel[j][3] + tabel[j][2] + tabel[j][1] + tabel[j][0]
        print(plaintext, end='')
