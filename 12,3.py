# Tampilkan pesan error jika file tidak ditemukan/tidak bisa dibaca.
def cari_file(file):
    try:
        with open(file, 'r') as file:
            lines = file.read().lower()
            # Mengembalikan kalimat-kalimat dalam file
            return lines
    except:
        print(f"File '{file}' tidak dapat ditemukan/dibaca.")
        exit()

file1 = str(input("Masukkan nama file pertama: ")) # 12/1.txt
lines1 = cari_file(file1) 
file2 = str(input("Masukkan nama file kedua: ")) # 12/2.txt
lines2 = cari_file(file2)

# Mengsplit kalimat menjadi kata dan diubah menjadi set sehingga tidak berisikan kata berulang
kata1 = set(lines1.split())
kata2 = set(lines2.split())

# Digabung menjadi satu
kata = kata1.union(kata2)
print(kata)


    