daftarBuku = [
    {
        'Judul' : 'Twilight',
        'Tahun' : '2022',
        'Pengarang' : 'Stephenie Meyer',
        'Penerbit' : 'Gramedia',
        'Genre' : 'Fiksi'
    },
    {
        'Judul' : 'Heat Transfer',
        'Tahun' : '1997',
        'Pengarang' : 'Yunus A. Cengel',
        'Penerbit' : 'McGrow-Hill',
        'Genre' : 'Pengetahuan'
    },
    {
        'Judul' : 'Filosofi Teras',
        'Tahun' : '2018',
        'Pengarang' : 'Henry Manampiring',
        'Penerbit' : 'Kompas Media',
        'Genre' :'Non Fiksi'
    },
]

#HALAMAN AWAL PERPUSTAKAAN
def perpus() :
    while True :
        print('SELAMAT DATANG DI PERPUSTAKAAN BAHAGIA')
        print('''List Menu :
              1. Daftar Buku yang Tersedia
              2. Program Donasi Buku
              3. Meminjam Buku
              4. Mengembalikan Buku Pinjaman
              5. Mengubah Data Buku
              6. Keluar Program''')
        inputMenu = int(input('Pilih Menu yang ingin Ditampilkan : '))
        if inputMenu == 1 :
            readBuku()
        elif inputMenu == 2 :
            donasiBuku()
        elif inputMenu == 3 :
            pinjamBuku()
        elif inputMenu == 4 :
            balikinBuku()
        elif inputMenu == 5 :
            updateData()
        elif inputMenu == 6 :
            print('Terima Kasih Telah Berkunjung ke Perpustakaan Bahagia')
            break
        else :
            print('Nomor yang Anda Masukan Salah! Masukan Nomor yang Sesuai')
            break

#FUNGSI MENAMPILKAN TABEL LIST BUKU
def tabelBuku() :
    print('--------------------------------------------------------------------------------------')
    print('Index\t|Judul \t\t|Tahun\t|Pengarang \t\t|Penerbit\t|Genre')
    print('--------------------------------------------------------------------------------------')
    for i,buku in enumerate(daftarBuku) :
        print(f"{i}\t|{buku['Judul']}\t|{buku['Tahun']}\t|{buku['Pengarang']}\t|{buku['Penerbit']}\t|{buku['Genre']}")
    print('--------------------------------------------------------------------------------------')


#FUNGSI 1 : MENAMPILKAN DAFTAR BUKU
def readBuku() :
    print('SELAMAT DATANG DI PERPUSTAKAAN BAHAGIA')
    while True:
        print('''List Menu :
              1. Menampilkan Daftar Buku yang Tersedia
              2. Keluar dari Menu''' )
        inputRead = int(input('Pilih Menu yang ingin Ditampilkan : '))

        if inputRead == 1 :
            print('Daftar Menu')
            tabelBuku()
        elif inputRead == 2 :
            exitRead = input('Apakah anda ingin kembali ke menu utama? (ya/tidak) : ')
            if exitRead.lower() == 'tidak' :
                print('SILAKAN PILIH MENU DIBAWAH INI')
            else :
                break

#FUNGSI 2 : MENAMBAHKAN DATA (CREATE DATA) - DONASI BUKU
def donasiBuku() :
    while True :
        print('AYO DONASI BUKU :)')
        print('''List Menu :
              1. Menambahkan Data Buku yang ingin Didonasikan
              2. Keluar dari Menu''' )
        inputDonasi = int(input('Pilih Menu yang ingin Ditampilkan : '))

        if inputDonasi == 1 :
            detailBuku = input('Masukan Judul Buku yang ingin Didonasikan : ')
            for i,buku in enumerate(daftarBuku) :
                a = (daftarBuku[i]['Judul'])
                if detailBuku == a :
                    print('Buku sudah tersedia')
                    break
                else :
                    print('Baik, Silakan Lengkapi Data Buku Dibawah Ini')
                    JudulBuku = input('Masukan Judul Buku : ')
                    TahunBuku = input('Masukan Tahun Buku : ')
                    PengarangBuku = input('Masukan Nama Pengarang Buku : ')
                    PenerbitBuku = input('Masukan Nama Penerbit Buku : ')
                    GenreBuku = input('Masukan Genre Buku : ')

                    simpanData = input('Apakah Data ingin Disimpan? (ya/tidak) : ')
                    if simpanData.lower() == 'ya' :
                        daftarBuku.append({
                            'Judul' : JudulBuku,
                            'Tahun' : TahunBuku,
                            'Pengarang' : PengarangBuku,
                            'Penerbit' : PenerbitBuku,
                            'Genre' : GenreBuku
                        })
                        print('Data Berhasil Disimpan')
                        tabelBuku()
                        break
                    elif simpanData.lower() == 'tidak' :
                        print('Data Tidak Disimpan')
                        break

        elif inputDonasi == 2 :
            exitDonasi = input('Apakah anda ingin kembali ke menu utama? (ya/tidak) : ')
            if exitDonasi.lower() == 'tidak' :
                print('SILAKAN PILIH MENU DIBAWAH INI')
            elif exitDonasi.lower() == 'ya' :
                break


# # FUNGSI 3 : DELETE DATA - MEMINJAM BUKU
def pinjamBuku() :
    while True :
        print('MAU PINJAM BUKU YA??? AYO BOLEH BANGETTT :)')
        print('''Menu Pinjam Buku :
              1. Melakukan Peminjaman Buku
              2. Keluar dari Menu''' )
        inputPinjam = int(input('Pilih Menu yang ingin Ditampilkan : ')) 

        if inputPinjam == 1 :
            tabelBuku()
            indexPinjam = int(input('Masukan Index Buku yang ingin Dipinjam : '))
            if indexPinjam >= len(daftarBuku) :
                print('Index Buku yang Diinput Tidak Tersedia')
            elif indexPinjam < (len(daftarBuku)) :
                del daftarBuku[indexPinjam]
                print(f'index ke-{indexPinjam} sudah berhasil dipinjam')

        elif inputPinjam == 2 :
            exitPinjam = input('Apakah anda ingin kembali ke menu utama? (ya/tidak) : ')
            if exitPinjam.lower() == 'tidak' :
                print('SILAKAN PILIH MENU DIBAWAH INI')
                pinjamBuku()
            elif exitPinjam.lower() == 'ya' :
                break

#FUNGSI 4 : CREATE DATA 2 - MENGEMBALIKAN BUKU PINJAMAN
def balikinBuku() :
    while True :
        print('AYO AYO JANGAN LUPA DIBALIKIN YA BUKUNYA :)')
        print('''Menu Pengembalian Buku :
              1. Melakukan Pengembalian Buku
              2. Keluar dari Menu''' )
        inputBalikin = int(input('Pilih Menu yang ingin Ditampilkan : ')) 
        
        if inputBalikin == 1 :
            detailBalik = input('Masukan Judul Buku yang ingin Dikembalikan : ')
            for i,buku in enumerate(daftarBuku) :
                a = (daftarBuku[i]['Judul'])
                if detailBalik == a :
                    print('Buku sudah dikembalikan')
                    break
                else :
                    print('Baik, Silakan Lengkapi Data Buku Dibawah Ini')
                    JudulBuku = input('Masukan Judul Buku : ')
                    TahunBuku = input('Masukan Tahun Buku : ')
                    PengarangBuku = input('Masukan Nama Pengarang Buku : ')
                    PenerbitBuku = input('Masukan Nama Penerbit Buku : ')
                    GenreBuku = input('Masukan Genre Buku : ')

                    simpanData = input('Apakah Data ingin Disimpan? (ya/tidak) : ')
                    if simpanData.lower() == 'ya' :
                        daftarBuku.append({
                            'Judul' : JudulBuku,
                            'Tahun' : TahunBuku,
                            'Pengarang' : PengarangBuku,
                            'Penerbit' : PenerbitBuku,
                            'Genre' : GenreBuku
                        })
                        print('Data Berhasil Disimpan')
                        tabelBuku()
                        break
                    elif simpanData.lower() == 'tidak' :
                        print('Data Tidak Disimpan')
                        break

        elif inputBalikin == 2 :
            exitBalikin = input('Apakah anda ingin kembali ke menu utama? (ya/tidak) : ')
            if exitBalikin.lower() == 'tidak' :
                print('SILAKAN PILIH MENU DIBAWAH INI')
                balikinBuku()
            elif exitBalikin.lower() == 'ya' :
                break

# #FUNGSI 5 : UPDATE DATA BUKU 
def updateData() :
    while True :
        print('''Menu Ubah Data Buku :
              1. Melakukan Ubah Data Buku
              2. Keluar dari Menu''' )
        inputUpdate = int(input('Pilih Menu yang ingin Ditampilkan : ')) 

        if inputUpdate == 1 :
            tabelBuku()
            indexUpdate = int(input('Masukan Index Buku yang ingin Diubah : '))
            if indexUpdate >= len(daftarBuku) :
                print('Index Buku yang Diinput Tidak Tersedia')
            elif indexUpdate < (len(daftarBuku)) :
                buku = daftarBuku[indexUpdate]
                print(f"{indexUpdate}\t|{buku['Judul']}\t|{buku['Tahun']} \t\t|{buku['Pengarang']}\t|{buku['Penerbit']}\t|{buku['Genre']}")
            
            lanjutUpdate = input('Apakah anda yakin ingin mengubah data buku? (ya/tidak) : ')
            if lanjutUpdate.lower() == 'ya' :
                inputKolom = input('Masukan nama kolom yang diubah : ')
                if inputKolom in buku:
                    buku[inputKolom] = input(f"Masukan {inputKolom} buku yang baru: ")
                else:
                    print('Kolom yang diinput Tidak Tersedia')
                saveData = input('Simpan Perubahan Data? (ya/tidak) : ')
                if saveData.lower() == 'ya':
                    print('Data Sudah Diubah')
                    tabelBuku()
                    break
                elif saveData.lower() == 'tidak':
                    continue
            elif lanjutUpdate == 'tidak'.lower() :
                print('SILAKAN PILIH MENU DIBAWAH INI')
            
        elif inputUpdate == 2 :
            exitUpdate = input('Apakah anda ingin kembali ke menu utama? (ya/tidak) : ')
            if exitUpdate == 'tidak'.lower() :
                print('SILAKAN PILIH MENU DIBAWAH INI')
                updateData()
            elif exitUpdate == 'ya'.lower() :
                break
        
perpus()