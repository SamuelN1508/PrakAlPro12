#  Meminta input jumlah kategori
n = int(input('Masukkan jumlah kategori : '))
data = {}

# Looping untuk memasukan nama kategori
for i in range(n):
    nama_kategori = input(f'Masukkan nama kategori ke-{i+1} : ')
    print(f'Masukkan 5 Aplikasi di Kategori {nama_kategori}')
    
    # Looping untuk memasukan nama aplikasi
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input(f'Nama Aplikasi ke-{j+1}: ')
        aplikasi.append(nama_aplikasi)
        
    # Memasukan aplikasi ke dalam kategori
    data[nama_kategori] = aplikasi
    
print()
print("Daftar Aplikasi")

# Menampilkan seluruh dictionary
for x in data:
    print(f'{x} = {data.get(x)}')

daftar_aplikasi_list = []

# ambil semua daftar aplikasi dari setiap kategori
for aplikasi in data.values():
    daftar_aplikasi_list.append(set(aplikasi))

# lakukan intersection ke semua set yang ada
hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
    
# Menampilkan aplikasi yang muncul di setiap kategori
print()
print(("Aplikasi yang hanya muncul di setiap kategori :"))
for x in hasil:
    print(x)
print()

set_app = set()

# Memasukan semua aplikasi ke dalam set
for x in data.values():
    for aplikasi in x:
        set_app.add(aplikasi)

satu = []
dua = []

# Looping setiap aplikasi untuk dihitung jumlah kemunculannya
for x in set_app:
    count = 0
    for kategori in data:
        # Jika didalam kategori tersebut ada aplikasi itu, maka count akan bertambah
        if x in data[kategori]:
            count += 1
    # Memasukan aplikasi ke dalam list sesuai jumlah kemunculannya
    if count == 2:
        dua.append(x)
    elif count == 1:
        satu.append(x)
        
# Print hasil
print("Aplikasi yang hanya muncul di satu kategori saja:")
for x in satu:
    print(x)

if n > 2:
    print("\nAplikasi yang hanya muncul tepat di dua kategori sekaligus:")
    for x in dua:
        print(x)