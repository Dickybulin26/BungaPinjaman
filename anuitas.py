
from module import moduleAnuitas as ma

soal = """
            ibu eli meminjam uang di bank BTN sebesar 300 juta rupiah. Bank BTN memberikan
            bunga sebesar 8.1% per tahun. bu eli akan mencicil pinjaman tersebut selama 10 tahun
            tentukan:
                    (A). berapa besar angsuran yang harus dibayar bu eli setiap bulannya?
                    (B). berapa besarnya bunga dan angsuran pokok yang harus dibayarkan bu eli 
                         pada bulan terakhir?
        """

diket = """ 
            M0 = 300.000
            i = 8.1% / bulan = 0.081% / tahun
            n = 10 tahun -> 120 bulan

            A = (M * i * (1 + i)**n) / ((1 + i)**n - 1)
        """

print(ma.MencariAnuitas(modalAwal=250000000,bungaBulanan=7.2,jangka=120))

print(ma.MencariAnuitas(modalAwal=80000000,bungaBulanan=4.8,jangka=48))

"""
        Anuitas : A = an * Bn
        A = (M * i * (1 + i)**n) / ((1 + i)**n - 1)

"""

print(ma.MencariAnuitas(modalAwal=10000000,bungaBulanan=1.5,jangka=10))