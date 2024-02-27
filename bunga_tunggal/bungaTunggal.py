
from module import moduleBungaTunggal as mbt


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

print(mbt.MencariModaln(500000, 0.005))

print(mbt.MencariModalAwal(35400000, 3, 72))

print(mbt.MencariBunga(20000000,20960000,4))

print(mbt.MencariJangka(
    modalAwal=25000000, 
    modalN=30000000, 
    bungaBulanan=2.5
    ))

print(mbt.MencariJangka(
    modalAwal=25000000,
    modalN=30000000,
    bungaBulanan=2.5, 
    tipe="tahun"
    ))

