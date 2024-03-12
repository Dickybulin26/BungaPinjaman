import module.moduleBunga as mb


soal =  """
            Pada awal bulan ditahun 2019 ibu Ely menabung di bank sebesar
            Rp.500.000. Bank ini diberi bunga majemuk sebesar 0.5% per bulan.
            Tentukan jumlah tabungan ibu Ely pada akhir tahun.
        """

diket = """ 
            M0 = 500.000
            i = 0.5% / bulan = 6% / tahun
            n = 1 tahun -> 12 bulan

            Mn = M0 * (1 + i)
        """

print(mb.MencariModaln(500000, 0.005))

print(mb.MencariModalAwal(35400000, 3, 72))

print(mb.MencariBunga(20000000,20960000,4))

print(mb.MencariJangka(
    modalAwal=25000000, 
    modalN=30000000, 
    bungaBulanan=2.5
    ))

print(mb.MencariJangka(
    modalAwal=25000000,
    modalN=30000000,
    bungaBulanan=2.5, 
    tipe="tahun"
    ))


print(mb.MencariModalAwal(10000,10))

print(mb.MencariModaln(modalAwal=20000000,bungaBulanan=5,jangka=60))

print(mb.MencariModaln(modalAwal=75_000_000,bungaBulanan=5,jangka=168,tipe="majemuk"))