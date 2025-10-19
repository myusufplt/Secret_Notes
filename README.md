# Secret Notes - Şifreli Not Defteri Uygulaması

Python ve Tkinter ile geliştirilmiş, notlarınızı `cryptography` kütüphanesi ile şifreleyerek güvenli bir şekilde saklamanızı sağlayan basit bir masaüstü uygulamasıdır.

![Uygulama Ekran Görüntüsü](logo.png)

## Temel Özellikler

-   **Basit Arayüz:** Tkinter ile oluşturulmuş, herkesin kolayca kullanabileceği temiz bir arayüz.
-   **Güçlü Şifreleme:** Notları korumak için endüstri standardı olan Fernet (AES-128) şifrelemesi kullanılır.
-   **Benzersiz Anahtar:** Her not için tamamen rastgele ve tahmin edilemez yeni bir şifreleme anahtarı oluşturulur.
-   **Yerel Depolama:** Şifrelenmiş notlarınız, bilgisayarınızda `.txt` dosyaları olarak güvenle saklanır.

## Kullanılan Teknolojiler

-   Python 3
-   Tkinter (Python'un standart GUI kütüphanesi)
-   Cryptography Kütüphanesi

---

## Kurulum ve Çalıştırma

1.  **Gerekli kütüphaneyi yükleyin:**
    ```bash
    pip install cryptography
    ```

2.  **Uygulamayı başlatın:**
    Script'in bulunduğu klasörde terminali açın ve çalıştırın:
    ```bash
    python dosya_adin.py
    ```
    *(`dosya_adin.py` kısmını kendi dosya adınızla değiştirin.)*

3.  `logo.png` dosyasının ana script ile aynı klasörde olduğundan emin olun.

---

## Kullanım

### Not Şifreleme
1.  "Enter Your Title" alanına notunuz için bir başlık girin.
2.  "Enter Your Secret Note" alanına gizlemek istediğiniz metni yazın.
3.  **"Save And Encrypt"** butonuna tıklayın.
4.  Ekranda çıkan pop-up'taki **anahtarı kopyalayıp güvenli bir yere kaydedin.** Bu anahtar olmadan nota bir daha erişemezsiniz!

### Şifre Çözme
1.  Çözmek istediğiniz notun "Başlığını" girin.
2.  Daha önce kaydettiğiniz "Anahtarı" ilgili alana yapıştırın.
3.  **"Decrypt"** butonuna tıklayın. Notunuz ekranda görünecektir.
