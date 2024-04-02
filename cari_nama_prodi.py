def tentukan_prodi(nim):
    prodi = {
        '01' : 'prodi Teknik Elektronika',
        '02' : 'prodi Teknik Mesin',
        '03' : 'prodi Akuntansi',
        '04' : 'prodi Teknik Mesin',
        '07' : 'prodi Kebidanan',
        '08' : 'prodi Farmasi',
        '09' : 'prodi Teknik Informatika',
        '11' : 'prodi Akuntansi Sektor Publik',
        '12' : 'prodi Desain Komunikasi Visual',
        '13' : 'prodi Keprawatan'
    }


    kode_prodi = nim[2:4]
    if kode_prodi in prodi:
        return prodi[kode_prodi]
    else:
        return '(nama prodi tidak ditemukan)'

nama = input('Masukkan Nama Mahasiswa : ')
nim = input("Masukkan NIM Mahasiswa : ")
prodi = tentukan_prodi(nim)

print(f'Mahasiswa an.{nama} merupakan mahasiswa dari {prodi}')