from datetime import datetime as dt
import pandas as pd

menu = {
    "Daftar Menu": 
    [
      "TAS ", 
      "DOMPET",
      "TEMPAT TISSU",
      "KARPET",
    ],

    "Harga": 
    [
      "Rp. 30000", 
      "Rp. 15000", 
      "Rp. 10000",
      "Rp. 50000",
    ]
}

daftar_menu = pd.DataFrame(menu)

# Daftar Menu
lanjut = 1
# Jika kondisi benar, jalankan program
while lanjut == 1:
  ulang = 1
  # Jika kondisi benar, atau memilih "Y" jalankan program
  while ulang == 1 or ulang == "Y" or ulang == "y":
    ulang = 0
    print("="*40)
    print("KERAJINAN BUNGKUS KOPI".upper().center(40))
    print("="*40)
    print(daftar_menu)
    print("="*40)

    # List kosong untuk menampung data 
    kode_menu = []
    jumlah_order = []
    menu = []
    harga = []
    jumlah_harga = []

    # Input Pembeli
    pembeli = str(input("Nama Pembeli : "))
    # Input Banyak Jenis
    banyak_jenis = int(input("Ingin pesan berapa banyak : "))

    # Looping jumlah banyak jenis
    for i in range(banyak_jenis) :
      print(f"\nMenu ke - {i + 1}")
      # Input Kode Menu
      kode_menu.append(str(input("Kode Menu 0/1/2/3: ")))
      # Input Jumla h Order
      jumlah_order.append(int(input("Jumlah yang ingin dipesan: ")))
      print("")
      
      # Jika kode menu sama dengan TAS
      if kode_menu[i] == "0":
        menu.append("         TAS")
        harga.append("30000")
        jumlah_harga.append(int(harga[i]) * jumlah_order[i])
      # Jika kode menu sama dengan DOMPET
      elif kode_menu[i] == "1":
        menu.append("      DOMPET")
        harga.append("15000")
        jumlah_harga.append(int(harga[i]) * jumlah_order[i])
      # Jika kode menu sama dengan TISSU
      elif kode_menu[i] == "2":
        menu.append("TEMPAT TISSU")
        harga.append("10000")
        jumlah_harga.append(int(harga[i]) * jumlah_order[i])
      # Jika kode menu sama dengan TEMPAT TISSU
      elif kode_menu[i] == "3":
        menu.append("      KARPET")
        harga.append("50000")
        jumlah_harga.append(int(harga[i]) * jumlah_order[i])
      # Jika kode menu sama dengan KARPET
      # Jika kode tidak sama dengan kode menu
      else:
        print("Kode menu tidak tersedia, Silahkan mengisi kembali".upper())
        print("-"*40)
        print("")
        ulang = 1
        break

  # Output
  print("="*64)
  print("KERAJINAN BUNGKUS KOPI".upper().center(68))
  print("JAKARTA BARAT".upper().center(68))
  print("Project Dasar Pemrograman".upper().center(68))

  # Format tanggal & waktu
  now = dt.now()
  datetime = now.strftime("%a, %d %B %Y, %H:%M:%S %p")
  print("{:^68}".format(datetime))

  total_item = 0
  jumlah_bayar = 0

  # Looping List
  for a in range(banyak_jenis):
      data = {
          "Kode Menu" : kode_menu,
          "Nama Menu" : menu,
          "Jumlah Pesanan" : jumlah_order,
          "Jumlah Harga" : jumlah_harga
      }
      total_item = total_item + jumlah_order[a]
      jumlah_bayar = jumlah_bayar + jumlah_harga[a]

  list_menu = pd.DataFrame(data)
 
  print("")
  print("="*64)
  print(list_menu)
  print("="*64)
  print(f"Total Pembelian : \t\t\t{total_item} \t  {jumlah_bayar} ")
  print("="*64)
  # Pembeli
  print(f"Nama pembeli : {pembeli}")

  # Jumlah Bayar 
  total = jumlah_bayar 
 
  # Pembayaran
  ulang = 1 
  while ulang == 1:
      ulang = 0
      # Input Uang
      uang = int(input("Uang yang anda berikan : \t\t\tRp. "))
      if uang >= total :
          kembalian = uang - total
          print(f"Kembaliannya adalah : \t\t\t\tRp. {int(kembalian)}")
      elif uang <= total : 
          print("="*64)
          print("Uang tidak mencukupi, masukan nominal yang sesuai")
          ulang = 1
  # Penutup
  print("="*64)
  print("Terima kasih telah berbelanja\n".center(68)) 
  print("di toko Krebufe\n" .center(68) )
  # Input Ulang
  ulang = str(input("Apa ingin mengulang pesanan [Y/N] : "))
  lanjut = 1
  if ulang == "N" or ulang == "n":
      break
  print("")