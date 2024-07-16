from prettytable import PrettyTable

list_ban = [
        {'kode':4101,'merek':'GT Radial','nama':'Champiro','tipe':'ECO','ukuran_ban':'15/205/65','stock':7,'harga':651000},
        {'kode':2301,'merek':'Bridgestone','nama':'Dueler','tipe':'M/T','ukuran_ban':'17/225/70','stock':5,'harga':2500000},
        {'kode':1301,'merek':'Achilles','nama':'Desert','tipe':'M/T','ukuran_ban':'16/215/65','stock':6,'harga':1310000}, 
        {'kode':5201,'merek':'Yokohama','nama':'Geolandar','tipe':'A/T','ukuran_ban':'16/215/70','stock':8,'harga':2300000},
        {'kode':2101,'merek':'Bridgestone','nama':'Techno','tipe':'ECO','ukuran_ban':'15/195/60','stock':4,'harga':867000},
        {'kode':3201,'merek':'Dunlop','nama':'Grandtrek','tipe':'A/T','ukuran_ban':'17/265/65','stock':3,'harga':1225000},
        {'kode':4201,'merek':'GT Radial','nama':'Savero','tipe':'A/T','ukuran_ban':'18/235/60','stock':5,'harga':1500000},
        {'kode':3101,'merek':'Dunlop','nama':'Enasave','tipe':'Eco','ukuran_ban':'15/185/65','stock':6,'harga':645000}
]

def menu():
    print('''
                 Selamat Datang di Ban Shop!   ''')
    print('''        
             +=================================+  
             |    *      Menu Utama      *     | 
             +=================================+  
             | 1. Menampilkan Daftar Ban       |
             | 2. Menambahkan Ban              |
             | 3. Menghapus Ban                |
             | 4. Mengupdate Stock Ban         |
             | 5. Membeli Ban                  |
             | 6. Exit Program                 |
             +=================================+''')

def menu_read():                    
    while True:
        print('''  
        +=======================================================+      
        |           *      Menu Daftar Ban      *               |
        +=======================================================+              
        | 1. Menampilkan seluruh daftar ban                     |
        | 2. Menampilkan daftar ban berdasarkan kode ban        |
        | 3. Menampilkan daftar ban berdasarkan merek           |
        | 4. Menampilkan daftar ban berdasarkan ukuran ring     |
        | 5. Menu utama                                         |
        +=======================================================+''')
        pilihan = input('Masukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 5:
                break
            elif pilihan == 1:
                sub_menu_read()
            elif pilihan == 2:
                data_kode()
            elif pilihan == 3:
                data_merek()
            elif pilihan == 4:
                data_ring()
            else:
                print('\nMohon masukkan pilihan menu yang tersedia.\n\n')    
        else:
            print('\nMasukkan angka Menu yang ingin dijalankan.\n\n')

def tabel():                        # menampilkan daftar ban (utama)
    for i in range(len(list_ban)):
        for j in range(i+1,len(list_ban)):
            if(list_ban[i]['ukuran_ban']>list_ban[j]['ukuran_ban']):
                list_ban[i]['ukuran_ban'],list_ban[j]['ukuran_ban']=list_ban[j]['ukuran_ban'],list_ban[i]['ukuran_ban']
    print('\nDaftar Ban\n') 
    tabel = PrettyTable()
    tabel.field_names = ['No','Kode','Merek','Nama','Tipe','Ukuran Ban','Stock','Harga']
    for i in range(len(list_ban)):
        tabel.add_row([i+1,list_ban[i]['kode'],list_ban[i]['merek'],list_ban[i]['nama'],list_ban[i]['tipe'],list_ban[i]['ukuran_ban'],list_ban[i]['stock'],list_ban[i]['harga']])
    tabel.align = 'c'
    print(tabel)

def tabel_harga():                        # menampilkan daftar ban (utama)
    for i in range(len(list_ban)):
        for j in range(i+1,len(list_ban)):
            if(list_ban[i]['harga']<list_ban[j]['harga']):
                list_ban[i]['harga'],list_ban[j]['harga']=list_ban[j]['harga'],list_ban[i]['harga']
    print('\nDaftar Ban\n') 
    tabel = PrettyTable()
    tabel.field_names = ['No','Kode','Merek','Nama','Tipe','Ukuran Ban','Stock','Harga']
    for i in range(len(list_ban)):
        tabel.add_row([i+1,list_ban[i]['kode'],list_ban[i]['merek'],list_ban[i]['nama'],list_ban[i]['tipe'],list_ban[i]['ukuran_ban'],list_ban[i]['stock'],list_ban[i]['harga']])
    tabel.align = 'c'
    print(tabel)

def tabel_stock():                        # menampilkan daftar ban (utama)
    for i in range(len(list_ban)):
        for j in range(i+1,len(list_ban)):
            if(list_ban[i]['stock']<list_ban[j]['stock']):
                list_ban[i]['stock'],list_ban[j]['stock']=list_ban[j]['stock'],list_ban[i]['stock']
    print('\nDaftar Ban\n') 
    tabel = PrettyTable()
    tabel.field_names = ['No','Kode','Merek','Nama','Tipe','Ukuran Ban','Stock','Harga']
    for i in range(len(list_ban)):
        tabel.add_row([i+1,list_ban[i]['kode'],list_ban[i]['merek'],list_ban[i]['nama'],list_ban[i]['tipe'],list_ban[i]['ukuran_ban'],list_ban[i]['stock'],list_ban[i]['harga']])
    tabel.align = 'c'
    print(tabel)

def sub_menu_read():
    while True:
        print('''  
        +===================================================+
        |             *     Daftar Ban     *                |
        +---------------------------------------------------+
        | 1. Daftar ban urut berdasarkan ukuran ring        |
        | 2. Daftar ban urut berdasarkan harga              |
        | 3. Daftar ban urut berdasarkan stock              |
        | 4. Menu daftar ban                                |
        +===================================================+''')
        pilihan = input('Masukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 4:
                break
            elif pilihan == 1:
                tabel()
            elif pilihan == 2:
                tabel_harga()
            elif pilihan == 3:
                tabel_stock()
            else:
                print('\nMohon masukkan pilihan menu yang tersedia.\n\n')    
        else:
            print('\nMasukkan angka Menu yang ingin dijalankan.\n\n')

def data_kode():                    # Menampilkan data berdasarkan kode ban
    while True:
        tampil=input('Masukkan kode ban yang ingin ditampilkan: ')
        if tampil.isdigit():
            tampil=int(tampil)
            found = False
            for i in list_ban:
                if i['kode'] == tampil:
                    found = True
                    tabelsementara.append(i)
                    tabel_sementara()
                    tabelsementara.clear()
                    break
            if not found:
                print(f'\nProduk dengan kode {tampil} tidak ada.')
            break

def data_merek():
    while True:
        merek_cari = input('Masukkan merek yang ingin dicari: ').capitalize()
        if merek_cari.isalpha():
            merek_cari=str(merek_cari)
            found = False
            for i in range(len(list_ban)):
                if list_ban[i]['merek'] == merek_cari:
                    found = True
                    tabelsementara.append(list_ban[i])
                    continue
            if not found:
                print(f'\nProduk dengan merek {merek_cari} tidak ada.')
            break
        else:
            print('\nMohon masukkan merek ban dengan benar.')
    tabel_sementara()
    tabelsementara.clear()

def data_ring():
    while True:
        ring_cari = input('Masukkan ukuran ring yang ingin dicari: ').capitalize()
        if ring_cari.isdigit():
            ring_cari=int(ring_cari)
            found = False
            for i in range(len(list_ban)):
                ring=list_ban[i]['ukuran_ban']
                ring_split=int(ring.split('/')[0])
                if ring_split == ring_cari:
                    found = True
                    tabelsementara.append(list_ban[i])
                    continue
            if not found:
                print(f'\nProduk dengan ukuran ring {ring_cari} tidak ada.')
            break
        else:
            print('\nMohon masukkan ukuran ring dalam bilangan bulat.')
    tabel_sementara()
    tabelsementara.clear()

tabelsementara=[]
def tabel_sementara():                  # Menampilkan data yang akan dihapus
    table = PrettyTable()
    table.field_names = ['Kode','Merek','Nama','Tipe','Ukuran Ban','Stock','Harga']
    for i in tabelsementara:
        table.add_row([i['kode'], i['merek'], i['nama'], i['tipe'], i['ukuran_ban'], i['stock'], i['harga']])
    table.align = 'c'
    print(table)

def menu_tambah():                    # Menampilkan menu tambah
    tabel()
    while True:
        print('''  
        +============================+     
        |   *    Menu Tambah    *    |
        +============================+               
        | 1. Menambah produk ban     |
        | 2. Menu utama              |
        +============================+     ''')
        pilihan = input('Masukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 2:
                break
            elif pilihan == 1:
                add_part()
            else:
                print('\nMasukkan pilihan menu yang tersedia.')
        else:
            print('\nMohon masukkan pilihan menu yang tersedia yang berupa bilangan bulat.')

def add_part():                         # Menambah produk dengan input, menampilkan tabel dari produk yang akan ditambah dan checker
    while True:
        kode_tambah = input('\nMasukkkan kode produk ban: ')
        if kode_tambah.isdigit():
            kode_tambah=int(kode_tambah)
            found = False
            for i in range(len(list_ban)):
                if list_ban[i]['kode'] == kode_tambah:
                    found = True
                    print('\nKode ban yang dimasukkan sudah tersedia.')
                    return
            if not found:
                break
            if found:
                break
        else:
            print('\nMohon masukkan kode ban dalam bilangan bulat.')
    while True:
        merek_tambah = input('\nMasukkkan merek produk ban: ').capitalize()
        valid = True
        for char in merek_tambah:
            if not (char.isalpha() or char == ' '):
                valid = False
                break
        if valid:
            break
        elif valid and ' ' in tipe_tambah:
            break
        else:
            print('Masukkan tipe ban dengan benar.')
            
    while True:
        nama_tambah = input('\nMasukkkan nama produk ban: ').capitalize()
        if nama_tambah.isalpha():
            nama_tambah=str(nama_tambah)
            break
        else:
            print('Masukkan nama dengan benar.')

    while True:
        tipe_tambah = input('\nMasukkkan tipe ban (A/T, M/T, RADIAL, ECO): ').upper()
        valid = True
        for char in tipe_tambah:
            if not (char.isalpha() or char == '/'):
                valid = False
                break
            elif len(tipe_tambah) <3:
                valid = False
                break
        if valid:
            break
        elif valid and '/' in tipe_tambah:
            break
        else:
            print('Masukkan tipe ban dengan benar.')

    while True:
        print(f"\nContoh ukuran ban: {list_ban[i]['ukuran_ban']}")
        ukuran_ban_tambah = input('Masukkan ukuran ban: ')
        valid = True
        for char in ukuran_ban_tambah:
            if not (char.isdigit() or char == '/'):
                valid = False
                break
        if valid and '/' in ukuran_ban_tambah:
            break
        else:
            print('Mohon masukkan ukuran ban dengan benar.')

    while True:
        stock_tambah = input('\nMasukkkan stock ban: ')
        if stock_tambah.isdigit():
            stock_tambah=int(stock_tambah)
            if stock_tambah < 0:
                print('Mohon masukkan stock dengan jumlah yang benar.')
            else:
                break

    while True:
        harga_tambah =input('Masukkkan harga ban : ')
        if harga_tambah.isdigit():
            harga_tambah=int(harga_tambah)
            if harga_tambah < 0:
                print('Mohon masukkan stock dengan jumlah yang benar.')
            else:
                break
    tabelsementara.append({'kode':kode_tambah,'merek':merek_tambah,'nama':nama_tambah,'tipe':tipe_tambah,'ukuran_ban':ukuran_ban_tambah,'stock':stock_tambah,'harga':harga_tambah})
    tabel_sementara()
    while True:
        choice = str(input('\nApakah anda ingin menambahkan produk ini? (Y/T): ')).upper()
        if choice == 'Y':
            list_ban.append({'kode':kode_tambah,'merek':merek_tambah,'nama':nama_tambah,'tipe':tipe_tambah,'ukuran_ban':ukuran_ban_tambah,'stock':stock_tambah,'harga':harga_tambah})
            print(f'\nProduk telah ditambahkan.')
            tabelsementara.pop()
            tabel()
            break
        elif choice == 'T':
            print(f'\nProduk batal ditambah.')
            tabelsementara.pop()
            break    
        else:
            print('\nMohon masukkan Y untuk ya, dan T untuk tidak.')
        break


def menu_update():                 
    while True:
        print('''
        +===========================+        
        |    *   Menu Update   *    |
        +===========================+              
        | 1. Merubah produk ban     |
        | 2. Menu utama             |
        +===========================+        ''')
        pilihan = input('Masukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 2:
                break
            elif pilihan == 1:
                update_part()
            else:
                print('\nMasukkan pilihan menu yang tersedia.')
        else:
            print('\nMohon masukkan pilihan menu yang tersedia yang berupa bilangan bulat.')

def update_part():
    tabel()
    while True:
        kode_update = input('Masukkan kode ban yang ingin dirubah: ')
        if kode_update.isdigit():
            kode_update=int(kode_update)
            found = False
            for i in range(len(list_ban)):
                if list_ban[i]['kode'] == kode_update:
                    found = True
                    tabelsementara.append(list_ban[i])
                    tabel_sementara()
                    while True:
                        choice = str(input("\nApakah anda ingin merubah stock produk ini? (Y/T): ")).upper()
                        if choice == 'Y':
                            sub_menu_update(i)
                            break
                        elif choice == 'T':
                            tabelsementara.pop()
                            print(f'\nProduk dengan kode {kode_update} batal diubah.')
                            break    
                        else:
                            print('\nMohon masukkan Y untuk ya, dan T untuk tidak.')
                    break
            if not found:
                print(f'\nProduk dengan kode {kode_update} tidak tersedia.')
            break
        else:
            print('\nMohon masukkan pilihan menu yang tersedia yang berupa bilangan bulat.')


def sub_menu_update(i):
    while True:
        tabel_sementara()
        print('''
        +=====================+        
        |  *  Menu Update  *  |
        +=====================+
        | 1. Stock            |
        | 2. Harga            |
        | 3. Menu update      |
        +=====================+      ''')
        pilihan = input('Masukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 3:
                tabelsementara.pop()
                break
            elif pilihan == 1:
                while True:
                    inp_stock = input('Masukkan jumlah stock yang baru: ')
                    if inp_stock.isdigit():
                        inp_stock = int(inp_stock)
                        if inp_stock < 0:
                            print('Masukkan jumlah stock yang positif.')
                        else:
                            while True:
                                choice = str(input('\nApakah anda ingin merubah stock produk ini? (Y/T): ')).upper()
                                if choice == 'Y':
                                    list_ban[i]['stock']=inp_stock
                                    print(f'\nStock berhasil dirubah.')
                                    break
                                elif choice == 'T':
                                    print(f'\nStock batal dirubah.')
                                    break    
                                else:
                                    print('\nMohon masukkan Y untuk ya, dan T untuk tidak.')
                            break
                    else:
                        print('Masukkan jumlah stock dalam bentuk angka.')
            elif pilihan == 2:
                while True:
                    inp_harga = input('Masukkan harga yang baru: ')
                    if inp_harga.isdigit():
                        inp_harga = int(inp_harga)
                        if inp_harga < 0:
                            print('Masukkan harga dengan benar.')
                        else:
                            while True:
                                choice = str(input('\nApakah anda ingin merubah stock produk ini? (Y/T): ')).upper()
                                if choice == 'Y':
                                    list_ban[i]['harga']=inp_harga
                                    print(f'\nStock berhasil dirubah.')
                                    tabel()
                                    break
                                elif choice == 'T':
                                    print(f'\nStock batal dirubah.')
                                    break    
                                else:
                                    print('\nMohon masukkan Y untuk ya, dan T untuk tidak.')
                            break
                    else:
                        print('Masukkan jumlah stock dalam bentuk angka.')
            else:
                print('\nMasukkan pilihan menu yang tersedia.')

def menu_delete():                 
    while True:
        print('''
        +=======================================+        
        |           *  Menu Hapus  *            |
        +---------------------------------------+      
        | 1. Hapus berdasarkan kode ban         |
        | 2. Hapus berdasarkan kategori         |
        | 3. Menu utama                         | 
        +=======================================+     
              ''')
        pilihan = input('Masukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 3:
                break
            elif pilihan == 1:
                hapus_kode()
            elif pilihan == 2:
                hapus_kategori()
            else:
                print('\nMasukkan pilihan menu yang tersedia.')
        else:
            print('\nMohon masukkan pilihan menu yang tersedia yang berupa bilangan bulat.')

def hapus_kode():
    while True:
        tabel()
        hapus = input('Masukkan kode ban yang ingin dihapus: ')
        if hapus.isdigit():
            hapus=int(hapus)
            found = False
            for i in range(len(list_ban)):
                if list_ban[i]['kode'] == hapus:
                    found = True
                    tabelsementara.append(list_ban[i])
                    tabel_sementara()
                    while True:
                        choice = str(input("\nApakah anda ingin menghapus produk ini? (Y/T): ")).upper()
                        if choice == 'Y':
                            list_ban.remove(list_ban[i])
                            print(f'\nProduk dengan kode {hapus} telah dihapus.')
                            tabel()
                            break
                        elif choice == 'T':
                            print(f'\nProduk dengan kode {hapus} batal dihapus.')
                            tabelsementara.pop()
                            break    
                        else:
                            print('\nMohon masukkan Y untuk ya, dan T untuk tidak.')
                    break
            if not found:
                print(f'\nProduk dengan kode {hapus} tidak ada.')
            break
        else:
            print('\nMohon masukkan kode ban dalam bilangan bulat.')

def hapus_kategori():
    while True:
        input_merek = input('\nMasukkkan merek produk ban: ').capitalize()
        if input_merek.isalpha() or input_merek == '':
            break
        else:
            print('Mohon masukkan merek dengan benar.')

    while True:
        input_tipe = input('\nMasukkkan tipe ban (A/T, M/T, RADIAL, ECO): ').upper()
        valid = True
        for char in input_tipe:
            if not (char.isalpha() or char == '/'):
                valid = False
                break
            elif len(input_tipe) <3:
                valid = False
                break
        if valid:
            break
        elif valid and '/' in input_tipe:
            break
        elif input_tipe == '':
            break
        else:
            print('Masukkan tipe ban dengan benar.')

    tabelindex=[]
    for i in range(len(list_ban)):
        if list_ban[i]['merek'] == input_merek and list_ban[i]['tipe'] == input_tipe:
            tabelindex.append(list_ban[i])
        elif list_ban[i]['merek'] == input_merek and input_tipe == '' :
            tabelindex.append(list_ban[i])
        elif input_merek == '' and list_ban[i]['tipe'] == input_tipe:
            tabelindex.append(list_ban[i])
    if len(tabelindex)==0:
        print('Anda tidak memasukan nama merek atau nama tipe.')
    else:
        tabelsementara.extend(tabelindex)
        tabelindex.clear()
        checker()


def checker():
    while True:
        tabel_sementara()
        choice = str(input('\nApakah anda ingin menghapus produk ini? (Y/T): ')).upper()
        if choice == 'Y':
            for i in tabelsementara:
                if i in list_ban:
                    list_ban.remove(i)
            print(f'\nProduk telah dihapus.')
        elif choice == 'T':
            print(f'\nProduk batal dihapus.')
        else:
            print('\nMohon masukkan Y untuk ya, dan T untuk tidak.')
        tabelsementara.clear()
        break

keranjang=[]
def tabel_keranjang():                  # Menampilkan data yang akan dihapus
    table = PrettyTable()
    table.field_names = ['Kode','Merek','Nama','Tipe','Ukuran Ban','Stock','Harga','Total']
    for item in keranjang:
        table.add_row([item['kode'], item['merek'], item['nama'], item['tipe'], item['ukuran_ban'], item['stock'], item['harga'], item['harga_total']])
    table.align = 'c'
    print(table)

def menu_beli():                 
    while True:
        print('''
        +=====================+        
        |   *  Menu Beli  *   |
        +---------------------+      
        | 1. Pembelian        |
        | 2. Pembayaran       |
        | 3. Menu utama       | 
        +=====================+     ''')
        pilihan = input('Masukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 3:
                break
            elif pilihan == 1:
                part_beli()
            elif pilihan == 2:
                part_bayar()
            else:
                print('\nMasukkan pilihan menu yang tersedia.')
        else:
            print('\nMohon masukkan pilihan menu yang tersedia yang berupa bilangan bulat.')

def part_beli():
    tabel()
    kodebeli = input('\nMasukkan kode ban yang ingin dibeli : ')
    while(True):
        if kodebeli.isdigit():
            kodebeli=int(kodebeli)
            found = False
            for i in range(len(list_ban)):
                if list_ban[i]['kode'] == kodebeli:
                    found = True
                    while True:
                        inp_jumlah=input('Masukkan jumlah yang akan dibeli: ')
                        if inp_jumlah.isdigit():
                            inp_jumlah=int(inp_jumlah)
                            if inp_jumlah < 0:
                                print('Masukkan jumlah yang akan dibeli dengan benar.')
                                break
                            elif inp_jumlah>list_ban[i]['stock']:
                                print('Jumlah stock tidak mencukupi.')
                                break
                            else:
                                keranjang_beli=list_ban[i].copy()
                                keranjang_beli['harga_total']=  inp_jumlah*list_ban[i]['harga']
                                keranjang_beli['stock']= inp_jumlah
                                list_ban[i]['stock']=list_ban[i]['stock'] - inp_jumlah
                                keranjang.append(keranjang_beli)
                                tabel_keranjang()
                            break
                        else:
                            print('\nMohon masukkan jumlah yang akan dibeli dalam bilangan bulat.')
                    break
            if not found:
                print(f'\nProduk dengan kode {kodebeli} tidak tersedia.')
            break
        else:
            print('\nMohon masukkan pilihan menu yang tersedia yang berupa bilangan bulat.')
            break

def part_bayar():
    if not keranjang:
        print('Tidak ada produk dalam keranjang.')
        return
    tabel_keranjang()
    total_harga=0
    for i in range(len(keranjang)):
        total_harga+=keranjang[i]['harga_total']
    print(f'Jumlah yang harus dibayarkan sebesar: {total_harga}')
    while True:
        bayar = input('\nMasukkan jumlah uang : ')
        if bayar.isdigit():
            bayar=int(bayar)
            if bayar < total_harga:
                print(f'\nUang anda kurang.')
            elif bayar > total_harga:
                print(f'\nTerima Kasih\nUang kembali anda : {bayar-total_harga}')
                keranjang.clear()
                break
            else:
                print('\nTerima Kasih')
                keranjang.clear()
                break
        print('\nMohon masukkan jumlah uang berupa angka.')

def main():
    while True:
        menu()
        pilihan = input('\nMasukkan angka Menu yang ingin dijalankan : ')
        if pilihan.isdigit():
            pilihan=int(pilihan)
            if pilihan == 6:
                while True:
                    tutup=str(input('\nApakah anda ingin menutup aplikasi? (Y/T) ')).upper()
                    if tutup== 'Y' or tutup == 'T':
                        break
                    else:
                        print('\nMohon masukkan Y untuk ya, dan T untuk tidak.')
                if tutup == 'Y':
                    print('\nAplikasi ditutup.')
                    break
                else:
                    print('\nAplikasi batal ditutup.')
            elif pilihan == 1:
                menu_read()     # sort  by, filter
            elif pilihan == 2:
                menu_tambah()
            elif pilihan == 3:
                menu_delete()   # delete berdasarkan merek/
            elif pilihan == 4:
                menu_update()
            elif pilihan == 5:
                menu_beli()
            else:
                print('\nMohon masukkan angka menu yang tersedia.')
        else:
            print('\nMohon masukkan angka menu yang tersedia.')

if __name__=='__main__':
    main()