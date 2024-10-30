import requests

url = input("İndirmek istediğiniz dosyanın URL'sini girin: ")

dosya_adi = "indirilen_dosya.apk"  # İndirilen dosyanın adını burada belirleyebilirsin

try:
    response = requests.get(url, allow_redirects=True, stream=True)
    response.raise_for_status()  # Hata olup olmadığını kontrol eder
    
    # Dosyayı kaydediyoruz
    with open(dosya_adi, "wb") as dosya:
        for chunk in response.iter_content(chunk_size=8192):
            dosya.write(chunk)
    
    print(f"{dosya_adi} başarıyla indirildi.")
except Exception as e:
    print("Bir hata oluştu:", e)
  
