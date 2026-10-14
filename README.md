# kyrox-brand

Kyrox Studio logo dosyaları ve marka renk tanımları. Fair CRM, Fair Stand, kyrox.studio web sitesi ve diğer tüm işler logoyu ve renkleri buradan alır.

**Kurallar bu repoda değil.** Logonun nasıl kullanılacağı, renkler ve yazım kuralları için:
[kyrox-platform/standards/brand/BRAND_STANDARD.md](https://github.com/kyrox-studio/kyrox-platform/blob/main/standards/brand/BRAND_STANDARD.md)

Bu reponun neden var olduğu ve sınırları: [ADR-0010](https://github.com/kyrox-studio/kyrox-platform/blob/main/ecosystem/decisions/0010-brand-repository.md)

## İçerik

```
logo/
  svg/          Kaynak dosyalar (logo, sembol, yazı, profil, favicon)
  png/          Şeffaf zeminli PNG'ler, 1080 px profil görselleri, favicon boyutları
  favicon.ico
tokens/
  colors.css      Marka renkleri, CSS değişkeni olarak (--kyrox-*)
  typography.css  Yazı tipleri (Inter, Archivo) ve başlık sınıfları
  tokens.json     Renkler, fontlar ve boyut ölçeği, JSON olarak
kilavuz/
  logo-ailesi.html   Tüm versiyonların görsel örneği (tarayıcıda aç)
tools/          Logoyu vektör kaynaktan yeniden üreten betikler
```

## Logoyu güncellemek

Ürün repolarındaki logo dosyaları elle düzenlenmez. Logo değişecekse:

1. `tools/paths.json` veya `tools/build.py` güncellenir.
2. `tools/` altında `python3 build.py` (SVG) ve `python3 png.py` (PNG, Playwright + Chromium gerekir) çalıştırılır; çıktı `tools/out/` altına yazılır ve `logo/` altına kopyalanır.
3. Bu repoya PR açılır, ardından ürün repolarına ayrı PR'lar.

`.studio` yazısı Inter Medium fontuyla üretilir; yeniden üretmek için Inter'in kurulu olması gerekir.

Proje fotoğrafları, render'lar ve videolar bu repoya girmez.
