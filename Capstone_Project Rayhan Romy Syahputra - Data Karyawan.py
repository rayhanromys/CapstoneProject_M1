#Daftar Menu
#Data set yang merupakan ditcionary di dalam list
karyawan = [
    {'NIK' : '25081', 'Nama' : 'Sunaryo', 'Gender' : 'L', 'Umur': 25, 'Posisi' : 'Mechanical Engineer'},
    {'NIK' : '25082', 'Nama' : 'Sukarmini', 'Gender' : 'P', 'Umur': 38, 'Posisi' : 'Data Analyst'},
    {'NIK' : '25083', 'Nama' : 'Sulaiman', 'Gender' : 'L', 'Umur': 35, 'Posisi' : 'Data Scientist'},
    {'NIK' : '25084', 'Nama' : 'Supinah', 'Gender' : 'P', 'Umur': 28, 'Posisi' : 'Data Engineer'},
    {'NIK' : '25085', 'Nama' : 'Suromi', 'Gender' : 'L', 'Umur': 22, 'Posisi' : 'Biotechnologist'}
    ] 

#Menampilkan data karyawan, setiap looping akan menampilkan setiap baris
def data_karyawan(): 
    print('Data Karyawan:\n')
    for j,i in enumerate(karyawan):
        print(f"{j+1}. NIK: {i['NIK']}, Nama: {i['Nama']}, Gender: {i['Gender']}, Umur: {i['Umur']}, Posisi: {i['Posisi']}")

def menu_utama():
    print('''
========= Data Karyawan Perusahaan "PT. MAJU MUNDUR"=========

1. Report Data Karyawan Perusahaan "PT. MAJU MAJU MUNDUR"
2. Menambahkan Data Karyawan
3. Mengubah Data Karyawan
4. Menghapus Data Karyawan Karyawan
5. Exit
''')
    pilihan_menu = input('Pilih Menu [1-5]: ')
    if pilihan_menu == '1':
        menu_report()
    elif pilihan_menu == '2':
        menu_tambah()
    elif pilihan_menu == '3':
        menu_ubah()
    elif pilihan_menu == '4':
        menu_hapus()
    elif pilihan_menu == '5':
        print ('\nTerimakasih Sudah Mengakses Data Karyawan "PT. MAJU MUNDUR"')
        exit()
    else:
        menu_utama()
    
#Menu 1
def menu_report():
    while True:
        print ('''
========= Data Record Karyawan Perusahaan "PT. MAJU MUNDUR"=========\n
1. Report Seluruh Data Karyawan
2. Report Data Karyawan Tertentu
3. Kembali Ke Menu Utama''')
        
        pilihan_submenu_1 = input('\nPilih Menu [1-3]: ')
        if pilihan_submenu_1 == '1':            
            data_karyawan()

        elif pilihan_submenu_1 == '2':
            if len(karyawan) == 0:
                print('\nData Karyawan Kosong') #Jika Data Habis
            elif (len(karyawan)) != 0:
                NIK_Karyawan = input('\nMasukkan NIK [5 Digit]: ')
                print (f'Karyawan dengan NIK: {NIK_Karyawan}')
                
                list_NIK = []
                for i in range (len(karyawan)):
                    list_NIK.append(karyawan[i]['NIK']) #Memasukan NIK baru kedalam list
                if NIK_Karyawan in list_NIK:
                    print(f"{list_NIK.index(NIK_Karyawan) + 1}. NIK: {NIK_Karyawan}, Nama: {karyawan[list_NIK.index(NIK_Karyawan)]['Nama']}, Gender: {karyawan[list_NIK.index(NIK_Karyawan)]['Gender']} , Umur: {karyawan[list_NIK.index(NIK_Karyawan)]['Umur']}, Posisi: {karyawan[list_NIK.index(NIK_Karyawan)]['Posisi']}\n")
                else:
                    print (f'Data Karyawan dengan NIK {NIK_Karyawan} tidak tersedia') #Kalau Tidak Ada NIK
               
        elif pilihan_submenu_1 == '3':
            menu_utama()
        else:
            print('Masukkan Angka Yang Benar!')
            continue

            
#Menu 2
def menu_tambah():
    while True:
        print ('''
======== Menu Menambah Karyawan ========
1. Tambah Data Karyawan
2. Kembali Ke Menu Utama''')
        pilihan_submenu_2 = input('\nPilih Menu [1-2]: ')

        if pilihan_submenu_2 == '1':
            NIK_karyawan_baru = input('Masukkan NIK Karyawan (5 Digit Angka): ')
            if len (NIK_karyawan_baru) != 5:
                print ('NIK yang anda input tidak boleh lebih/kurang dari 5 digit!')
            elif len (NIK_karyawan_baru) == 5:
                for i in karyawan:
                    if i['NIK'] == NIK_karyawan_baru: #Kalau NIK Duplikat
                        print ('\nNIK sudah terpakai')
                        menu_tambah()
                else: #Kalau NIK Tidak Tersedia (Bisa diinput)
                    Nama_Baru = input('Masukkan Nama: ').capitalize()
                    Gender_Baru = input('Masukkan Gender: ').capitalize()
                    Umur_Baru = input ('Masukkan Umur: ')
                    Posisi_Baru = input ('Masukkan Posisi: ').capitalize()
                    while True:
                        konfirmasiMenu2 = input('Apakah Data jadi Ditambahkan (Y/N): ').capitalize()
                        if konfirmasiMenu2 == 'Y':
                            baris_baru = {'NIK':NIK_karyawan_baru, 'Nama' : Nama_Baru,  'Gender' : Gender_Baru, 'Umur' : Umur_Baru, 'Posisi' : Posisi_Baru}
                            karyawan.append(baris_baru)
                            print ('\nData Telah Tersimpan')
                            data_karyawan()
                            break
                        elif konfirmasiMenu2 == 'N':
                            menu_tambah()
                        else:
                            print ('\nMasukkan Hanya Y/N')
        elif pilihan_submenu_2 == '2':
            menu_utama()
        else:
            continue


#Menu3
def menu_ubah():
    while True:
        print ('''
======== Menu Mengubah Data Karyawan ========
1. Ubah Data Karyawan
2. Kembali Ke Menu Utama''')
        pilihan_submenu_3 = input('\nPilih Menu [1-2]: ')
        if pilihan_submenu_3 == '1':
            data_karyawan()
            Input_NIK = input('\nMasukkan NIK Karyawan: ')
            for i in karyawan:
                if Input_NIK == i['NIK']:
                    print (f"NIK: {i['NIK']}, Nama: {i['Nama']}, Gender: {i['Gender']}, Umur: {i['Umur']}, Posisi: {i['Posisi']}")
                    while True:
                        konfirmasi_ubah = input('Apakah Data Jadi Diubah (Y/N)? ').capitalize()
                        if konfirmasi_ubah == 'Y':
                            ubah_kolom = input('Pilih Kolom Yang Ingin Diubah (NIK, Nama, Gender, Umur, Posisi): ').lower()
                            if ubah_kolom == 'nik':
                                ubah_kolom = ubah_kolom.upper()
                            else:
                                ubah_kolom = ubah_kolom.capitalize()
                            ubah_isi = input(f'Masukkan {ubah_kolom} baru: ').capitalize()
                            while True:
                                konfirmasi_ubah2 = input('Apakah Data Jadi Diubah (Y/N)? ').capitalize()
                                if konfirmasi_ubah2 == 'Y':
                                    i[ubah_kolom] = ubah_isi
                                    print ('\nData Sudah Diubah')
                                    data_karyawan()
                                    menu_ubah()
                                elif konfirmasi_ubah2 == 'N':
                                    menu_ubah()
                                else:
                                    print ('\nMasukkan Y/N Saja!!')
                                
                        elif konfirmasi_ubah == 'N':
                            menu_ubah()
                        else:
                            print ('\nMasukkan Y/N Saja!!')
            else:
                print ('\nNIK tidak tersedia')
                menu_ubah()
        elif pilihan_submenu_3 == '2':
            menu_utama()
        else:
            continue

#Menu 4
def menu_hapus():
    while True:
        print ('''
======== Menu Menghapus Data Karyawan ========      
1. Hapus Data Karyawan
2. Kembali Ke Menu Utama''')
        pilihan_submenu_4 = input('\nPilih Menu [1-2]: ')
        if pilihan_submenu_4 == '1':

            if len(karyawan) == 0:
                print ('\nData Karyawan Kosong')
            elif len(karyawan) != 0:
                data_karyawan()
                hapus = input('\nMasukkan NIK yang mau dihapus: ')
                list_NIK = []
                for i in range (len(karyawan)):
                    list_NIK.append(karyawan[i]['NIK'])
                if hapus in list_NIK:
                    konfirmasi = input('\nTekan Y untuk menghapus atau N untuk membatalkan: ').capitalize()
                    if konfirmasi == 'Y':
                        del karyawan[list_NIK.index(hapus)]
                        data_karyawan()
                        print('\nData Karyawan Telah Dihapus')
                    elif konfirmasi == 'N':
                        print ('\nData tidak jadi dihapus')
                    else:
                        print('Masukkan Y/N')
                else:
                    print (f'\nNIK {hapus} tidak terserdia ')
        elif pilihan_submenu_4 == '2':
            menu_utama()
        else:
            continue

menu_utama()