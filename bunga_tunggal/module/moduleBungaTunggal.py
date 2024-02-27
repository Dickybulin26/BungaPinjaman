
#* MODUL UNTUK BUNGA TUNGGAL

def MencariModaln(modalAwal:int|float, bungaBulanan:int|float, jangka:int|float = 12):
    """
    Menghitung bunga tunggal

    Fungsi untuk menghitung modal ke-n

        Args: (float|int)
            modalAwal (float|int): bunga awal (M0)
            bungaBulanan (float|int): bunga bulanan (i)
                Default Value = 12 (bulan | 1 tahun)
            jangka (float|int): jangka waktu (n)

        Returns: (float|int) -> Modal Ke-n (Mn)
    """
    
    bungaBulanan = bungaBulanan / 100
    modalN = modalAwal * ((1 + bungaBulanan) ** jangka)
    return f"Modal ke-{jangka} = {modalN}"

def MencariModalAwal(modalN:int|float, bungaBulanan:int|float, jangka:int|float = 12):
    """
    Menghitung bunga tunggal

    Fungsi untuk menghitung modal awal

        Args: (float|int)
            modalAwal (float|int): bunga awal (M0)
            bungaBulanan (float|int): bunga bulanan (i) 
                Default Value = 12 (bulan | 1 tahun)
            jangka (float|int): jangka waktu dalam bentuk bulan (n)

        Returns: (float|int) -> Modal Awal (M0)
    """
    bungaBulanan = bungaBulanan / 100 / 12
    modalAwal = modalN / (1 +(jangka * bungaBulanan))
    return f"modal awalnya adalah = {modalAwal}"
    

def MencariBunga(modalAwal:int|float, modalN:int|float, jangka:int|float = 12):
    """
    Menghitung bunga tunggal

    Fungsi untuk menghitung bunga (i)

        Args: (float|int)
            modalAwal (float|int): Modal awal (M0)
            modalN (float|int): Modal ke-n (Mn)
            jangka (float|int): jangka waktu (n)
                Default Value = 12 (bulan | 1 tahun)
        Returns: (float|int) -> bunga (i)
    """
    bungaBulanan = (((modalN / modalAwal) - 1) / jangka) * 100
    return f"maka bunga bulanannya adalah = {bungaBulanan}% per bulan"   


def MencariJangka(
        modalAwal:int|float,
        modalN:int|float, 
        bungaBulanan:int|float = 12,
        tipe:str = "bulanan"):
    
            """
            Menghitung bunga tunggal

            Fungsi untuk menghitung jangka (n)

                Args: (float|int)
                    modalAwal (float|int): Modal awal (M0)
                    modalN (float|int): Modal ke-n (Mn)
                    bungaBulanan (float|int): bunga bulanan (i)
                        Default Value = 12 (bulan | 1 tahun)    
                    tipe (str): tipe jangka (n)
                        Default Value = bulanan
                Returns: (float|int) -> jangka waktu (bulan|tahun) (n)
            """
            bungaBulanan = bungaBulanan / 100 / 12
            jangka = ((modalN / modalAwal) - 1) / bungaBulanan

            if tipe == 'bulanan':
                return f"maka jangka waktu nya adalah = {round(jangka)} bulan"
            elif tipe == 'tahun':
                
                jangka = ((modalN / modalAwal) - 1) / bungaBulanan / 12
                return f"maka jangka waktu nya adalah = {round(jangka)} tahun"
        