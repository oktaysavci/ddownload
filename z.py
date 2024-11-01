import requests
from urllib.parse import urlsplit
from os.path import basename

url = input("İndirmek istediğiniz dosyanın URL'sini girin: ")

# URL'den dosya adını al
dosya_adi = basename(urlsplit(url).path) or "indirilen_dosya.apk"

try:
    with requests.get(url, allow_redirects=True, stream=True, timeout=10) as response:
        response.raise_for_status()  # Hata olup olmadığını kontrol eder

        # Dosya indirme işlemi
        with open(dosya_adi, "wb") as dosya:
            toplam_boyut = int(response.headers.get('content-length', 0))
            indirilen_boyut = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    dosya.write(chunk)
                    indirilen_boyut += len(chunk)
                    # İlerleme yüzdesini yazdır
                    yuzde = (indirilen_boyut / toplam_boyut) * 100
                    print(f"\rİndirme durumu: %{yuzde:.2f}", end="")

    print(f"\n{dosya_adi} başarıyla indirildi.")
except Exception as e:
    print("Bir hata oluştu:", e)
