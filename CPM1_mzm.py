# ======================================================================================================================
### Inisiasi Data Awal -------------------------------------------------------------------------------------------------

list_dict_buku = [ 
    {
        'nomor': 1001, 
        'judul': 'Bumi Manusia', 
        'pengarang': 'Pramoedya Ananta Toer', 
        'penerbit': 'Lentera Dipantara', 
        'kategori': 'Roman'
    },
    {   
        'nomor': 1002, 
        'judul': 'Catatan Seorang Demonstran', 
        'pengarang': 'Soe Hok Gie', 
        'penerbit': 'LP3ES', 
        'kategori': 'Biografi'
    },
    {
        'nomor': 1003, 
        'judul': 'Atomic Habits', 
        'pengarang': 'James Clear', 
        'penerbit': 'Gramedia', 
        'kategori': 'Motivasi'
    }
]

list_dict_update = list_dict_buku.copy()
nomor = 0

# ======================================================================================================================
### Fungsi readData untuk menampilkan data baik seluruh maupun sebagian ------------------------------------------------

def readData() :
    print('''
    --------------Tampilkan Data---------------

    1. Tampilkan Seluruh Buku
    2. Tampilkan Buku Tertentu
    3. Kembali Ke Menu Utama
    ----------------------------------------
    ''')
    
    submenu = input('    Masukkan Sub Menu yang ingin dijalankan [1-3]: ')
    
    if submenu == '1' :
        if len(list_dict_update) == 0 :
            tidakAda()
            readData()
        else :
            print('\n    Daftar Buku :')
            for i, dict_update in enumerate(list_dict_update) :
                print(f"\t{i + 1}. Nomor : {dict_update['nomor']}, Judul : {dict_update['judul']}, Pengarang : {dict_update['pengarang']}, Penerbit : {dict_update['penerbit']}, Kategori : {dict_update['kategori']}")
            readData()   
    elif submenu == '2' :
        if len(list_dict_update) == 0 :
            tidakAda()
            readData()
        else :
            inputNomor()
            for dict_update in list_dict_update :
                if dict_update['nomor'] == nomor :
                    print(f"    Data Buku dengan Nomor : {nomor}")
                    print(f"\t1. Nomor : {dict_update['nomor']}, Judul : {dict_update['judul']}, Pengarang : {dict_update['pengarang']}, Penerbit : {dict_update['penerbit']}, Kategori : {dict_update['kategori']}")
                    break
            if dict_update['nomor'] != nomor :
                tidakAda()
            readData() 
    elif submenu == '3' :
        aplikasiPerpustakaan()
    else :
        pilihanSalah()
        readData()

# ======================================================================================================================
### Fungsi createData untuk menambahkan data ---------------------------------------------------------------------------

def createData() :
    print('''
    --------------Tambah Data---------------

    1. Tambahkan Daftar Buku
    2. Kembali Ke Menu Utama
    ----------------------------------------
    ''')
    
    submenu = input('    Masukkan Sub Menu yang ingin dijalankan [1-2]: ')
    
    if submenu == '1' :
        inputNomor()
        for dict_update in list_dict_update :
            if dict_update['nomor'] == nomor :
                print("    ***Data Sudah Ada***")
                break
        if dict_update['nomor'] != nomor :
            judul = input('    Masukkan Judul Buku : ')
            pengarang = input('    Masukkan Nama Pengarang : ')
            penerbit = input('    Masukkan Nama Penerbit : ')
            kategori = input('    Masukkan Kategori : ')

            simpan = input('    Apakah Data Akan Disimpan? (Y/N) : ').upper()

            if simpan == 'Y' :
                list_dict_update.append(
                {
                    'nomor': nomor, 
                    'judul': judul, 
                    'pengarang': pengarang, 
                    'penerbit': penerbit, 
                    'kategori': kategori
                }
                )
                print('    ***Data Tersimpan***')
        createData()
    elif submenu == '2' :
        aplikasiPerpustakaan()
    else :
        pilihanSalah()
        createData()

# ======================================================================================================================
### Fungsi updateData untuk mengubah data sesuai Nomor Buku dan Kolom/Keterangan ---------------------------------------

def updateData() :
    print('''
    --------------Ubah Data---------------

    1. Ubah Daftar Buku
    2. Kembali Ke Menu Utama
    ----------------------------------------
    ''')
    
    submenu = input('    Masukkan Sub Menu yang ingin dijalankan [1-2]: ')
    
    if submenu == '1' :
        inputNomor()
        nomor_awal = nomor
        keterangan = ''
        for dict_update in list_dict_update :
            if dict_update['nomor'] == nomor_awal :
                print(f"\t1. Nomor : {dict_update['nomor']}, Judul : {dict_update['judul']}, Pengarang : {dict_update['pengarang']}, Penerbit : {dict_update['penerbit']}, Kategori : {dict_update['kategori']}")
                
                # lanjut update                
                lanjut = input('    Tekan Y untuk Melanjutkan Update Data atau N jika Membatalkan Update Data (Y/N) : ').upper()
                if lanjut == 'Y' :
                    keterangan = input('    Masukkan Kolom/Keterangan yang Akan Di-Update [nomor, judul, pengarang, penerbit, kategori]: ').lower()
                    if keterangan in list_dict_update[0].keys() :
                        if keterangan == 'nomor':
                            inputNomor()
                            nilai_baru = nomor

                            # memastikan nomor unik/tidak ada duplikat
                            list_nomor = [dict_update['nomor'] for dict_update in list_dict_update]
                            while nilai_baru in list_nomor :
                                print("    ***Nomor Sudah Terpakai***")
                                inputNomor()
                                nilai_baru = nomor
                        else :
                            nilai_baru = input(f'    Masukkan {keterangan} baru : ')
                        
                        # update data
                        update = input('    Apakah Data akan di update? (Y/N) : ').upper()
                        if update == 'Y' :
                            dict_update[keterangan] = nilai_baru
                            print('    ***Data Terupdate***')
                    else :
                        pilihanSalah()
                break
        if keterangan != 'nomor' :
            if dict_update['nomor'] != nomor_awal :
                tidakAda()
        updateData()
    elif submenu == '2' :
        aplikasiPerpustakaan()
    else :
        pilihanSalah()
        updateData()

# ======================================================================================================================
### Fungsi deleteData untuk menghapus data sesuai nomor Buku -----------------------------------------------------------

def deleteData() :
    print('''
    --------------Hapus Data---------------

    1. Hapus Data
    2. Kembali Ke Menu Utama
    ----------------------------------------
    ''')
    
    submenu = input('    Masukkan Sub Menu yang ingin dijalankan [1-2]: ')
    
    if submenu == '1' :
        inputNomor()
        for id, dict_update in enumerate(list_dict_update) :
            if dict_update['nomor'] == nomor :
                hapus = input('    Apakah Data Akan Dihapus (Y/N) : ').upper()
                if hapus == 'Y' :
                    del list_dict_update[id]
                    print('    ***Data Deleted***')
                break
        if dict_update['nomor'] != nomor :
            tidakAda()
        deleteData()
    elif submenu == '2' :
        aplikasiPerpustakaan()
    else :
        pilihanSalah()
        deleteData()

# ======================================================================================================================
### Fungsi keluarProgram untuk pilihan Exit Program --------------------------------------------------------------------

def keluarProgram() :
    print('\n***Terima kasih. Sampai Jumpa Kembali!***')

# ======================================================================================================================
### Fungsi untuk perintah yang berulang --------------------------------------------------------------------------------

def inputNomor():
    while True :
        global nomor
        nomor = input('    Masukkan Nomor Buku : ')
        if nomor.isdigit() == True :
            nomor = int(nomor)
            break
        print('    ***Nomor Buku Harus Angka***')

def pilihanSalah() :
    print('\n    ***Pilihan Yang Anda Masukkan Salah!***')

def tidakAda() :
    print('\n    ***Data Tidak Tersedia***')

# ======================================================================================================================
### Fungsi Aplikasi Perpustakaan untuk Menampilkan Menu Utama dan Meminta User untuk Menginput Pilihan Menu ------------

def aplikasiPerpustakaan():
    print('''
============================================
Selamat Datang di Perpustakaan M. Zulfikar M

Daftar Menu Utama :
1. Menampilkan Daftar Buku
2. Menambah Daftar Buku
3. Mengupdate Daftar Buku
4. Menghapus Daftar Buku
5. Exit Program
============================================
    ''')

    pilihan = input('Masukkan Menu Utama yang ingin dijalankan [1-5]: ')
    
    if pilihan == '1' :
        readData()
    elif pilihan == '2' :
        createData()
    elif pilihan == '3' :
        updateData() 
    elif pilihan == '4' :
        deleteData() 
    elif pilihan == '5' :
        keluarProgram() 
    else :
        pilihanSalah()
        aplikasiPerpustakaan()

#=================================
aplikasiPerpustakaan()