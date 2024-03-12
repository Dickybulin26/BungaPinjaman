# Module Bunga Pinjaman
## Module Anuitas
- MencariAnuitas
	- Menghitung Anuitas (A)
			
		![enter image description here](https://soalfismat.com/wp-content/uploads/2020/05/Rumus-anuitas.png)
			
			Args: (float|int)
			modalAwal (float|int): Modal awal (M0)
			bungaBulanan (float|int): Bunga bulanan (i)
			jangka (float|int): Jangka waktu (n)
			Default Value = 12 (bulan | 1 tahun)
			Returns: (float|int) -> anuitas (A)
			
			bungaBulanan = bungaBulanan  /  100  /  12

			anuitas  = ((modalAwal  *  bungaBulanan) * ((1  +  bungaBulanan)**jangka)) / (((1  +  bungaBulanan)**jangka) -1 )
			return  f"Anuitas = {anuitas}"


## ModuleBunga
- MencariModalAkhir
	- MencariModaln
	
	![enter image description here](https://cdn-web.ruangguru.com/landing-pages/assets/hs/01-2.jpg)

		Fungsi untuk menghitung modal ke-n

		Args: (float|int)
		modalAwal (float|int): bunga awal (M0)
		bungaBulanan (float|int): bunga bulanan (i)
		Default Value = 12 (bulan | 1 tahun)
		jangka (float|int): jangka waktu (n)
		Returns: (float|int) -> Modal Ke-n (Mn)
		
		bungaBulanan  =  bungaBulanan  /  100  /  12
		modalN  =  modalAwal  * (1+ (jangka  *  bungaBulanan))
		return  f"Modal ke-{jangka} = {modalN}"

- Mencari Modal Awal
	- MencariModalAwal

			Fungsi untuk menghitung modal awal

			Args: (float|int)
			modalAwal (float|int): bunga awal (M0)
			bungaBulanan (float|int): bunga bulanan (i)
			Default Value = 12 (bulan | 1 tahun)
			jangka (float|int): jangka waktu (n)
			tipe (str): tipe bunga (tunggal | majemuk)
			Default Value = tunggal
			Returns: (float|int) -> Modal Ke-n (Mn)

			bungaBulanan  =  bungaBulanan  /  100  /  12
			if  (tipe  ==  "majemuk"):
			modalN  =  modalAwal  * (1+ ((jangka  *  bungaBulanan)**2))
			else:
			modalN  =  modalAwal  * (1+ (jangka  *  bungaBulanan))

			return  f"Modal ke-{jangka} = {modalN}"

## Contoh Soal

![enter image description here](https://media-public.colearn.id/thumbnail/M0052501E007_large.png)

    import  module.moduleBunga  as  mb
    print(mb.MencariModaln(modalAwal=75_000_000,bungaBulanan=5,jangka=168,tipe="majemuk"))

**HASIL:**

    Modal ke-168 = 111750000.0
    
