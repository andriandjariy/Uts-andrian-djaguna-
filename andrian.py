status = False
batas = 4
buku = ["0.jago programen, harga : 30000 ||",
"1. jago python, harga :20000 ||", 
"2. jago OOP, harga : 250000 ||", 
"3. Desaign Website, harga : 40000 ||", 
"4. jago JavaScrep, Harga : 35000 ||",
"5. HTML5 dan CSS, harga : 15000 ||",
"6. PHP, harga : 90000 ||",
"7. fremawork codeignter, harga : 85000 ||",
"8. fremawork laravel, harga : 800000 ||",
"9. fremawork yi, harga, : 70000 ||",
"10. tutorial mySql, harga : 100000 ||"]
while batas > 0:
    a=int(input("pililah, jika beli tekan 1, dan jika ke admin tekan 2 :"))
    if a == 1:
        print("selamat datang pada aplikaso penjualan buku pada toko kami")
        print("----------------------------------------------------------")
        b = input("apakah anda mau membeli buku, jika iya tuliskan ya, jika tidak tuliskan tidak :")
        if b in ["ya", "YA", "Ya"]:
            print("berikut kami tamilkan judul judul buku sebagai berikut :")
            print("========================================================")
            for x in buku:
                print(x)
                print("----------------------------------------------------")
            pilih = int(input("masukan nomor buku di atas :"))
            if pilih == 0:
                harga = 30000
                print("----------------------------------------------------")
                print("buku yang anda beli : ",buku[0])
                print("====================================================")
                tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
                if tanya == "1":
                    harga = 50000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[0],buku[1])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "2":
                    harga = 55000
                    jum = 2
                    print("===================================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[0],buku[2])
                    print("===================================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif  tanya == "3":
                    harga = 70000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[0],buku[3])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "4":
                    harga = 65000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[0],buku[4])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "5":
                    harga = 45000
                    jum = 2
                    print("===================================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[0],buku[5])
                    print("===================================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "tidak":
                    harga = 30000
                    jum = 1
                    print("===================================================")
                    print("buku yang anda beli ::",buku[0])
                    print("----------------------------------------------------")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali) 
                    print("====================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                else:
                    print("anda masukan tidak sesuai yang kami perintahkan")
            elif pilih == 1:
                harga = 20000
                print("buku yang anda beli : \n",buku[1])
                print("====================================================")
                tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
                if tanya == "2":
                    harga = 45000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[1],buku[2])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "3":
                    harga = 60000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[1],buku[3])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif  tanya == "4":
                    harga = 55000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[1],buku[4])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "5":
                    harga = 35000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[1],buku[5])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "0":
                    harga = 50000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[1],buku[0])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "tidak":
                    harga = 20000
                    jum = 1
                    print("============================================")
                    print("buku yang anda beli ::",buku[1])
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                else:
                    print("anda masukan tidak sesuai yang kami perintahkan")
            elif pilih == 2:
                harga = 25000
                print("buku yang anda beli : \n",buku[2])
                print("====================================================")
                tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
                if tanya == "3":
                    harga = 65000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[2],buku[3])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "4":
                    harga = 60000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[2],buku[4])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif  tanya == "5":
                    harga = 40000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[2],buku[5])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "0":
                    harga = 55000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[2],buku[0])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "1":
                    harga = 45000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[2],buku[1])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "tidak":
                    harga = 25000
                    jum = 1
                    print("============================================")
                    print("buku yang anda beli ::",buku[2])
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("=================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                else:
                    print("anda masukan tidak sesuai yang kami perintahkan")
            elif pilih == 3:
                harga = 40000
                print("buku yang anda beli : \n",buku[3])
                print("====================================================")
                tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
                if tanya == "4":
                    harga = 35000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[3],buku[4])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "5":
                    harga = 55000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[3],buku[5])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif  tanya == "0":
                    harga = 60000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[3],buku[0])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "1":
                    harga = 60000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[3],buku[1])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "2":
                    harga = 65000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[3],buku[2])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "tidak":
                    harga = 40000
                    jum = 1
                    print("============================================")
                    print("buku yang anda beli ::",buku[3])
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                else:
                    print("anda masukan tidak sesuai yang kami perintahkan")
            elif pilih == 4:
                harga = 35000
                print("buku yang anda beli : \n",buku[4])
                print("====================================================")
                tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
                if tanya == "5":
                    harga = 50000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[4],buku[5])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "0":
                    harga = 65000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[4],buku[0])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif  tanya == "1":
                    harga = 55000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[4],buku[1])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "2":
                    harga = 55000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[4],buku[2])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "3":
                    harga = 75000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[4],buku[3])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "tidak":
                    harga = 35000
                    jum = 1
                    print("============================================")
                    print("buku yang anda beli ::",buku[4])
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                else:
                    print("anda masukan tidak sesuai yang kami perintahkan")
            elif pilih == 5:
                harga = 15000
                print("buku yang anda beli : \n",buku[5])
                print("====================================================")
                tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
                if tanya == "0":
                    harga = 45000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[5],buku[0])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                elif tanya == "1":
                    harga = 45000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[5],buku[1])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif  tanya == "2":
                    harga = 40000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[5],buku[2])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "3":
                    harga = 55000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[5],buku[3])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("==================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "4":
                    harga = 50000
                    jum = 2
                    print("============================================")
                    print("di batasi pembelian buku maxsimal dua buku ")
                    print("----------------------------------------------------")
                    print("buku yang anda beli ::",buku[5],buku[4])
                    print("============================================")
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("===================================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                elif tanya == "tidak":
                    harga = 15000
                    jum = 1
                    print("============================================")
                    print("buku yang anda beli ::",buku[5])
                    bayar = int(input("pembayaran :"))
                    kembali = bayar - harga
                    print("total pembeli :", jum)
                    print("pembayaran :", harga)
                    print("kembalian :", kembali)
                    print("============================================")
                    print("terima Kasih Anda Telah Membeli Buku Di Toko Kami")
                else:
                    print("anda masukan tidak sesuai yang kami perintahkan")
            else:
                print("angka yang anda masukan tidak tercantum dalah nomor buku")
                print("silahkan mulai kembali!")
        else:
            print("yang anda masukan tidak di anjurkan")
    elif a == 2:
        print("selamat datang admin pada aplikasi penjualan buku  pada Toko andrian")
        print("--------------------------------------------------------------------")
        print("inilah stok buku")
        print("--------------------------------------------------------------------")
        print(buku)
        print("===================================================================")
        print("jikan menambah tekan 1, jika mengubah tekan 2, dan jika menghapus tekan 3")
        print("------------------------------------------------------------------------")
        pilih = int(input("masukan pilihan :"))
        if pilih == 1:
            print("anda menambahkan stok buku, dengan format ikuti di bawah ini")
            print("------------------------------------------------------------------------")
            print("{nomor selanjutnya. nama buku, harga : diisi}")
            stok = str(input("masukan stok : "))
            print("------------------------------------------------------------------------")
            buku.append(stok)
            print(buku)
            print("=============================================")
            print("Anda Berhasil Menambahkan Stok Buku")
        elif pilih == 2:
            print("anda mengubah stok buku")
            print("------------------------------------------------------------------------")
            ubh = int(input("masukan nomor berapa yang ingin di ubah ? 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:"))
            print("------------------------------------------------------------------------")
            print("yang akan anda ubah :", buku[ubh])
            print("------------------------------------------------------------------------")
            print("format pengisian 'nmr, nama, harga ")
            print("------------------------------------------------------------------------")
            ganti = str(input("masukan nmr, nama buku dan harga buku yang anda gantikan:"))
            print("------------------------------------------------------------------------")
            buku[ubh]=ganti
            print("anda mengubah buku pertama dengan", ganti)
            print("------------------------------------------------------------------------")
            print(buku)
            print("=============================================")
            print("Anda Berhasil Mengubah Stok Buku")
        elif pilih == 3:
            print("anda ingin menghapus stok buku")
            hps = int(input("masukan nomor berapa yang ingin anda hapus 0,1,2,3,4,5,6, 7, 8, 9, 10 :"))
            print("------------------------------------------------------------------------")
            if hps == 0:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 1:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 2:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 3:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 4:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 5:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 6:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 7:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 8:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 9:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            elif hps == 10:
                del buku[hps]
                print(buku)
                print("--------------------------------------------------------------------")
                print("anda berhasil menghapus satu buku")
            else:
                print("anda masuka nomor yang tidak tersedia!")
                print("silahkan login kembali !")
    if not status:
        print("======================================================================================================================")
        print("Terimah Kasih Telam Mencoba Program Sederhana ANDRIAN DJAGUNA")
        print("SILAHKAN MENCOBA KEMBALI!")
        print("======================================================================================================================")
        batas = batas - 1
        continue
    else:
        break