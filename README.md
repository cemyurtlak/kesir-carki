# Kesir Çarkı

Ortaokul (5-7. sınıf) öğrencileri için **3 boyutlu, sesli ve efektli kesir yarışması**.
Çark döner, durduğu dilimin konusundan rastgele bir kesir sorusu gelir. Dört şık ekranın köşelerinde (A-B-C-D) çıkar, öğrenci doğru şıkka dokunur.
Bilgisayar, tablet ve akıllı tahtada çalışır. Kurulum gerekmez.

## Telefondan / internetten açma
**Adres:** https://cemyurtlak.github.io/kesir-carki/
Telefonda, tablette ya da herhangi bir bilgisayarda bu bağlantıyı açmak yeterli. Tarayıcı menüsünden **"Ana ekrana ekle"** denirse uygulama gibi simgesiyle tam ekran açılır.
- Çarkı **parmağınla tutup hızlıca çevir ve bırak**: ne kadar hızlı bırakırsan o kadar çok döner, parmağının hareketine göre kendiliğinden yavaşlayıp durur. Kısa dokunuş da çevirir.
- Bu adres güvenli (https) olduğu için **El ile oyna** (ön kamera) telefonda da kullanılabilir.

## Çalıştırma
**En iyi yol (el ile oynama dahil, internetsiz):** `baslat.bat` dosyasına çift tıklayın. Bilgisayarda Python yüklü olmalıdır. Küçük bir yerel sunucu açılır ve oyun tarayıcıda `http://127.0.0.1:8771` adresinde başlar (bu port doluysa bir sonraki boş port kullanılır; adres siyah pencerede yazar). Başka bir projenin sunucusu açık olsa bile karışmaz. Oyun bitene kadar siyah pencereyi kapatmayın.

**Hızlı yol:** `index.html` dosyasına çift tıklayın (Chrome, Edge veya Safari önerilir). Bu şekilde açınca "El ile oyna" özelliği için internet gerekir.

1. Dosyaları klasör yapısını bozmadan taşıyın.
2. `lib/three.min.js` dosyası `index.html` ile aynı klasör yapısında durmalıdır. Bu sayede **internet olmadan da** çalışır.
   (İnternet varsa yazı tipleri daha güzel görünür; yoksa sistem yazı tipi kullanılır.)
3. Akıllı tahtada sağ üstteki **tam ekran** düğmesine basın.

## Nasıl oynanır
- **ÇEVİR!** düğmesine, çarkın kendisine ya da klavyede **boşluk** tuşuna basın.
- Ya da çarkı parmakla/fareyle **tutup çevirip bırakın**: çark parmağı takip eder, bırakınca o hızla döner. Yavaş bırakılırsa dönmez ("Daha hızlı çevir!").
- Çark durunca soru gelir. Şıklar: dokunarak ya da klavyede **A/B/C/D** veya **1/2/3/4** ile seçilir.
- Cevaptan sonra doğru şık yeşil yanar, altta **çözüm adımları** görünür. **Devam** ile çarka dönülür.

## El ile oynama (kamera)
Üst şeritteki **El ile oyna** düğmesine basın ve kamera iznini verin. Sol altta kamera görüntüsü ve algılanan el iskeleti görünür.
- **Çarkı çevirmek:** Elinizi çarkın üzerinden **hızlıca** geçirin (sağa, sola, yukarı ya da aşağı). El ne kadar hızlıysa çark o kadar çok tur atar (3 ile 12 tur). Dönüş yönü elin hareket yönüne göredir; örneğin çarkın üstünde sağa kaydırınca saat yönünde döner.
- **Şık seçmek:** İşaret parmağınızın ucu ekranda renkli bir imleç olarak görünür. İmleci bir şıkkın üstünde yaklaşık **1 saniye** tutun; halka dolunca şık seçilir. **Devam**, **ÇEVİR!** ve seviye düğmeleri de aynı şekilde seçilebilir.
- İki el aynı anda algılanır (mavi ve pembe imleç). Kameraya 1-2 metre uzaktan, iyi ışıkta durmak en iyi sonucu verir.
- Dokunmatik ekranda ya da fareyle çarkı **tutup sürükleyip bırakmak** da hıza göre çevirir (çark parmağı takip eder).

## Robot köpek Robo
Üst şeritteki **Robot Köpek** (pati) düğmesine basın. Ekrana 3 boyutlu robot köpek Robo gelir.
- **Başını okşayın:** Fareyi, parmağınızı ya da kamerada işaret parmağınızı (El ile oyna açıksa) Robo'nun başının üstünde ileri geri gezdirin.
- Okşadıkça mutluluk çubuğu dolar, kalpler uçar, kuyruk hızlanır, ışıkları pembeleşir, gülümser ve dans eder. %100 olunca kalp gözlerle takla atıp havlar.
- Okşamayı bırakınca yavaş yavaş mutluluğu azalır; uzun süre sevilmezse üzülür.
- Robo'ya dokunun/tıklayın: havlar ve hoplar.
- **◀ Çarka dön** düğmesi ya da **Esc** ile oyuna dönülür. (Çark dönerken veya soru açıkken köpek bölümü açılmaz.)

## Çarkın dilimleri (8 konu)
| Dilim | Soru türü |
|---|---|
| Toplama | Kesirlerle toplama (eşit / katlı / farklı paydalar) |
| Çıkarma | Kesirlerle çıkarma |
| Çarpma | Kesir × kesir, doğal sayı × kesir |
| Bölme | Kesir ÷ kesir, doğal sayı ile bölme |
| Denk Kesir | En sade hâl bulma, kutudaki sayıyı bulma (genişletme) |
| Karşılaştır | Dört kesirden en büyüğü / en küçüğü |
| Kesir Kadarı | "48'in 3/4'ü", günlük hayat problemleri, tamamını bulma |
| Tam Sayılı | Tam sayılı ↔ bileşik kesir dönüşümü |

Sorular her seferinde **yeniden üretilir** (sınırsız soru). Yanlış şıklar öğrencilerin sık yaptığı hatalardan seçilir (ör. payları ve paydaları ayrı ayrı toplamak).

## Ayarlar (üst şerit)
- **Kolay / Orta / Zor**: sayı aralıkları ve soru türleri değişir. Puan: 10 / 15 / 20.
- **Saat**: 40 saniyelik süre sınırı (açıkken kalan süre bonus puan getirir).
- **El ile oyna**: kamerayla el takibi (yukarıya bakın).
- **Robot Köpek**: Robo'yu sevme bölümü (yukarıya bakın).
- **Hoparlör**: ses efektleri. **Nota**: arka plan müziği.
- **Seri**: art arda 3+ doğruda +5 bonus ve büyük kutlama.

## Dosya yapısı
```
index.html            Uygulamanın tamamı (görünüm + 3B çark + robot köpek + soru üretici + sesler)
govde.html            Aynı uygulamanın paylaşım bağlantısı için kullanılan gövdesi (index.html'den türetilir)
baslat.bat            Windows'ta sunucu.py'yi çalıştırıp oyunu başlatır (el ile oynama için önerilen yol)
sunucu.py             Boş port bulan yerel sunucu (8771'den başlar), tarayıcıyı açar
lib/three.min.js      Three.js r149 (3B grafik kütüphanesi, çevrimdışı kullanım için)
lib/mediapipe/        MediaPipe Hands 0.4.1675469240 (el takibi modeli ve dosyaları, çevrimdışı kullanım için)
manifest.json         "Ana ekrana ekle" için uygulama bilgisi
ikon.png              Uygulama simgesi (512×512)
.nojekyll             GitHub Pages dosyaları olduğu gibi sunsun
README.md             Bu dosya
GELISTIRME_GUNLUGU.md Aşama aşama geliştirme kaydı
DEVAM_NOTLARI.md      Kurallar, teknik kararlar, kod haritası, sonraki adımlar
```
