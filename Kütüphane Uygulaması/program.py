from modules import *

print("""****************************************

Kütüphane Programına Hoşgeldiniz.

İşlemler:

1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Sayısını Yükselt

Çıkmak için "q" ya basın.


****************************************""")

kütüphane = Kütüphane()

while(True):
    print(50*"\n")
    işlem = input("Yapacağınız işlem:")

    if işlem == 'q':
        print(2*"\n")
        print("Program sonlandırılıyor.")
        break

    elif işlem == '1':
        print(2*"\n")
        kütüphane.kitapları_goster()

    elif işlem == '2':
        print(2*"\n")
        isim = input("Hangi kitabı istiyorsunuz:")
        print("Kitap sorgulanıyor...")
        time.sleep
        print(2*"\n")
        kütüphane.kitap_sorgula(isim)



    elif işlem == '3':
        print(2*"\n")
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı:"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("\n")
        print("Kitap ekleniyor.")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")



    elif işlem == '4':
        print(2*"\n")
        isim = input("Hangi kitabı silmek istiyorsunuz:")

        cevap = input("{} isimli kitabı silmek istediğinizden emin misiniz? (E/H)".format(isim))
        if cevap == "e":
            print("Kitap siliniyor.")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi.")

 
            

    elif işlem == '5':
        print(2*"\n")
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz:")
        print("Baskı yükseltiliyor.")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi.")
    
    else:
        print(2*"\n")
        print("Geçersiz işlem girdiniz. ({})".format(işlem))

        
        
