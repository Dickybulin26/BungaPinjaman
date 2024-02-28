
#* MENCARI ANUITAS 

def MencariAnuitas(modalAwal:int|float, bungaBulanan:int|float, jangka:int|float = 12):
    """
    Menghitung anuitas (A)

        Args: (float|int)
            modalAwal (float|int): Modal awal (M0)
            bungaBulanan (float|int): Bunga bulanan (i)
            jangka (float|int): Jangka waktu (n)
                Default Value = 12 (bulan | 1 tahun)
        Returns: (float|int) -> anuitas (A)
    """

    bungaBulanan = bungaBulanan / 100 / 12
    anuitas = ((modalAwal * bungaBulanan) * ((1 + bungaBulanan)**jangka)) / (((1 + bungaBulanan)**jangka) -1 )
    return f"Anuitas = {anuitas}"