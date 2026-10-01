import json
from datetime import datetime

# Dosyadan görevleri yükleme fonksiyonu
def gorevleri_yukle():
    try:
        with open("gorevler.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return []

# Görevleri dosyaya kaydetme fonksiyonu
def gorevleri_kaydet(gorevler):
    with open("gorevler.json", "w", encoding="utf-8") as dosya:
        json.dump(gorevler, dosya, ensure_ascii=False, indent=4)

gorevler = gorevleri_yukle()

while True:
    print("\n=== Öğrenci Görev Takipçisi v1.0 ===")
    print("1 - Görev / Ödev Ekle")
    print("2 - Görevleri Listele")
    print("3 - Görevi Tamamlandı İşaretle")
    print("4 - Çıkış")

    secim = input("Seçtiğiniz işlemi giriniz: ")

    if secim == '1':
        baslik = input("Görev / Ödev Adı: ")
        tarih_str = input("Son Teslim Tarihi (YYYY-AA-GG, Örn: 2026-10-15): ")
        
        # Yeni görevi bir Sözlük (Dictionary) olarak hazırlıyoruz
        yeni_gorev = {
            "baslik": baslik,
            "tarih": tarih_str,
            "tamamlandi": False
        }
        
        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)
        print(f"'{baslik}' görevi başarıyla eklendi!")

    elif secim == '2':
        print("\n--- GÖREV LİSTESİ ---")
        if len(gorevler) == 0:
            print("Henüz kaydedilmiş bir görev yok!")
        else:
            for index, gorev in enumerate(gorevler, start=1):
                durum = "[X] Tamamlandı" if gorev["tamamlandi"] else "[ ] Bekliyor"
                print(f"{index}. {durum} - {gorev['baslik']} (Son Tarih: {gorev['tarih']})")

    elif secim == '3':
        if len(gorevler) == 0:
            print("Tamamlanacak görev yok!")
        else:
            print("\n--- Tamamlanacak Görevi Seçin ---")
            for index, gorev in enumerate(gorevler, start=1):
                durum = "[X]" if gorev["tamamlandi"] else "[ ]"
                print(f"{index}. {durum} {gorev['baslik']}")
            
            numara = int(input("Tamamlanan görevin numarasını girin: "))
            
            if 1 <= numara <= len(gorevler):
                gorevler[numara - 1]["tamamlandi"] = True
                gorevleri_kaydet(gorevler)
                print("Görev durumu 'Tamamlandı' olarak güncellendi!")
            else:
                print("Geçersiz görev numarası!")

    elif secim == '4':
        print("Çıkış yapılıyor... Derslerde başarılar!")
        break

    else:
        print("Geçersiz seçim! Lütfen 1-4 arasında bir sayı girin.")