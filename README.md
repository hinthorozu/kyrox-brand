# Kyrox Studio — Marka

Kyrox Studio'nun logoları, marka kılavuzu ve ortak renk tanımları. Web sitesi, Fair CRM, Fair Stand ve tüm sosyal medya işleri logoyu ve renkleri buradan alır.

> **Precision meets Craft** · kyrox.studio

## İçerik

```
logo/
  svg/        Kaynak dosyalar. Web, matbaa, lazer kesim ve CNC için bunu kullan.
  png/        Şeffaf zeminli PNG'ler (logo 2400 px, sembol 1024 px),
              profil görselleri (1080 px) ve favicon boyutları
  favicon.ico
kilavuz/
  logo-ailesi.html   Logo versiyonları, renkler ve kullanım kuralları (tarayıcıda aç)
tokens/
  colors.css   Renkler, CSS değişkeni olarak
  tokens.json  Aynı renkler, JSON olarak
tools/         Logoyu vektör kaynaktan yeniden üreten betikler
```

## Hangi dosya nerede

| Kullanım | Dosya |
| --- | --- |
| Web sitesi, sunum, teklif, e-posta imzası | `logo/svg/kyrox-logo-renkli.svg` |
| Koyu zemin | `logo/svg/kyrox-logo-renkli-koyu-zemin.svg` |
| Tek renk baskı, lazer, ahşaba yakma | `kyrox-logo-siyah.svg` / `kyrox-logo-beyaz.svg` |
| Instagram ve LinkedIn profili | `logo/png/kyrox-profil-siyah-1080.png` |
| Web sitesi favicon'u | `logo/favicon.ico`, `logo/svg/favicon.svg`, `logo/png/apple-touch-icon-180.png` |

## Temel kurallar

- Bu düz logo markanın tek logosudur. Gölgeli, dokulu ya da 3D versiyon kullanılmaz.
- `.studio` her zaman küçük harf yazılır; domainin kendisini temsil eder.
- Logo esnetilmez, döndürülmez, parça renkleri değiştirilmez.
- En küçük boyut: ana logo ekranda 140 px / baskıda 35 mm, sembol 16 px / 8 mm.

Ayrıntılar için `kilavuz/logo-ailesi.html` dosyasını aç.

## Renkler

| Ad | Değer | Kullanım |
| --- | --- | --- |
| Çelik | `#B4B7BB` | Logo, açık zemin |
| Çelik, koyu zemin | `#C9CCD0` | Logo, siyah üzerinde |
| Ahşap | `#A2652C` | Logo |
| Deri | `#7B3B1D` | Logo |
| Mürekkep | `#0B0B0B` | Yazı ve koyu zemin |
| Kağıt | `#F5F3EF` | Açık zemin |
| Bakır | `#C47A3A` | Vurgu rengi |

Bir projede kullanmak için:

```html
<link rel="stylesheet" href="tokens/colors.css">
<style> .buton { background: var(--kyrox-copper); } </style>
```

## Logoyu yeniden üretmek

`tools/paths.json` logonun vektör şekillerini tutar. Bir renk ya da versiyon değişirse:

```bash
cd tools
python3 build.py   # SVG'leri out/svg/ altına yazar
python3 png.py     # PNG'leri out/png/ altına yazar (Playwright + Chromium gerekir)
```

`.studio` yazısı Inter Medium ile üretilir (`lc.py`, `textpath.py`); yeniden üretmek için Inter fontunun kurulu olması gerekir.

## Yol haritası

- [x] Logo ve logo ailesi
- [ ] Marka kılavuzu: renk paleti, fontlar, ses tonu
- [ ] Web sitesi (kyrox-website)
- [ ] Instagram ve LinkedIn şablonları
- [ ] İçerik takvimi

Proje fotoğrafları, render'lar ve videolar bu repoya girmez; onlar Google Drive'da durur.
