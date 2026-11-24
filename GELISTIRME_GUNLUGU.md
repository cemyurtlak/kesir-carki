# Geliştirme Günlüğü
(En yeni aşama en üstte)

---

## Aşama 5 — Telefonda çalışan GitHub bağlantısı + parmakla tutup çevirme
**Tarih:** 24.11.2026

**İstek:** Proje telefonda çalışacak şekilde GitHub linki hâline getirilsin. Parmakla dokunarak döndürme güzel çalışsın.

**Yapılanlar:**
- **Parmakla tutup çevirme (yeniden yazıldı):** Çarkın üstüne dokunup sürükleyince çark parmağı birebir takip ediyor (tıkırtı ve ibre sallanması dahil). Bırakınca, son ~180 ms'deki açısal hızla dönmeye devam edip kendiliğinden yavaşlıyor. Dönüş eğrisi bırakma hızıyla kesintisiz eşleşiyor (hız ne kadar yüksekse o kadar çok tur ve uzun süre; 40 rad/sn'de ~14 tur, en fazla 9 sn). Durduğu dilim bu hareketten çıkıyor, önceden seçilmiyor. Yavaş bırakılırsa çark dönmüyor ve "Daha hızlı çevir!" uyarısı çıkıyor. Kısa dokunuş eskisi gibi normal çeviriyor; çarkın dışında kaydırma eski kaydırarak çevirme davranışını koruyor.
- Yavaş telefonlarda tarayıcının birleştirdiği dokunma hareketleri (`getCoalescedEvents`) tek tek işleniyor, zamanlar olay zaman damgasından alınıyor; böylece hız doğru ölçülüyor. Sürüklerken çarkın boştaki yavaş dönüşü duruyor.
- **Telefon düzeni:** 560 px altında üst şerit 2 satıra indi (El ile oyna ve Robot Köpek yalnızca simge, tam ekran düğmesi gizli; iPhone desteklemiyor). Dik ekranda çark ekran genişliğini dolduracak kadar büyüdü (390 px telefonda yarıçap 122 → 166 px). Bilgi balonunun taşması düzeltildi.
- **Ana ekrana eklenebilir:** `manifest.json`, `ikon.png` (512×512 çark simgesi), `theme-color` ve Apple web-app etiketleri eklendi; "Ana ekrana ekle" ile uygulama gibi tam ekran açılıyor.
- **GitHub Pages:** `cemyurtlak/kesir-carki` deposu açıldı, tüm dosyalar yüklendi, Pages yayını açıldı: https://cemyurtlak.github.io/kesir-carki/ . Bu adres https olduğu için telefonda kamera ile "El ile oyna" da çalışabiliyor (el takibi dosyaları depodaki `lib/mediapipe/`'den yükleniyor).

**Değişen dosyalar:** `index.html`, `govde.html`, `manifest.json` (yeni), `ikon.png` (yeni), `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md`

**Test durumu:**
- Chromium telefon öykünmesi (390×844 ve 360×740, dokunmatik), gerçek dokunma olaylarıyla: yavaş sürükleme → çark parmağı takip etti (1,22 rad), dönmedi, uyarı çıktı ✔. Hızlı fırlatma (15 rad/sn) → 3 tur, 5,1 sn, ibrenin gösterdiği "Karşılaştır" diliminde durdu ve o konunun sorusu geldi ✔. Kısa dokunuş → normal çevirdi ✔. Yatay taşma yok, konsolda hata yok.
- Robot köpek ekranı telefonda düzgün görünüyor.
- Gerçek bir telefonda henüz denenmedi.

---

## Aşama 4 — baslat.bat başka projeyi açıyordu (düzeltme)
**Tarih:** 02.11.2026

**İstek:** baslat.bat çalıştırınca başka bir proje açılıyor.

**Sebep:** Eski `baslat.bat` her zaman `localhost:8765` adresini kullanıyordu. Bilgisayarda başka bir projenin sunucusu aynı portta açık kaldığında tarayıcı o projeyi gösteriyordu. Windows'ta Python sunucusu dolu porta da bağlanabildiği için hata da vermiyordu. Tarayıcının aynı adresteki eski sayfayı önbellekten getirmesi de aynı sonucu doğurabiliyordu.

**Yapılanlar:**
- Yeni `sunucu.py`: bu projeye ayrılan **8771** portundan başlayarak **boş** bir port arar (dolu portu bağlanma denemesiyle tespit eder, Windows'ta `SO_EXCLUSIVEADDRUSE` ile başka sunucunun portunu paylaşmaz), klasörü yalnızca `127.0.0.1`'de yayınlar ve tarayıcıyı o adreste açar.
- Sunucu `Cache-Control: no-store` gönderiyor; tarayıcı başka projenin eski sayfasını göstermez.
- `.wasm` dosyaları doğru türle (`application/wasm`) gönderiliyor.
- `baslat.bat` artık `sunucu.py`'yi çalıştırıyor (`python` yoksa `py`).

**Değişen dosyalar:** `baslat.bat`, `sunucu.py` (yeni), `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md`

**Test durumu:** 8771 portunu başka bir klasörün sunucusu tutarken `sunucu.py` çalıştırıldı: 8771 atlandı, 8772'de Kesir Çarkı açıldı (başlık doğru), diğer sunucu kendi sayfasını vermeye devam etti. Windows'ta henüz denenmedi.

---

## Aşama 3 — Robot köpek "Robo" bölümü
**Tarih:** 02.11.2026

**İstek:** Projeye ek olarak bir robot köpek bölümü olsun. Elimizle köpeğin başını okşayabilelim, köpek mutlu olsun, havada kalpler uçsun.

**Yapılanlar:**
- Üst şeride **Robot Köpek** düğmesi (pati simgesi) eklendi. Basınca çark yerine ayrı bir 3B sahne açılıyor (aynı çizim motoru, ikinci sahne). Çark dönerken ya da soru açıkken açılmıyor, uyarı veriyor.
- Three.js parçalarından robot köpek **Robo** yapıldı: beyaz gövde, parlayan şeritler, mavi yan paneller, 4 bacak, kırmızı tasma ve altın kalp künye, kulaklar, anten, ışıklı kuyruk, burun ve dil. Yüzü kavisli bir **ekran**; ifadeler (üzgün, normal, göz kırpma, gülen, okşanırken mutlu ^^ gözler, %100'de kalp gözler) canvas üzerine çiziliyor.
- **Okşama:** İmleç (fare, dokunmatik parmak ya da kameradaki işaret parmağı) başın üstünde hareket ettikçe mutluluk artıyor. Hareketsiz durmak okşama sayılmıyor. Okşanmayınca mutluluk yavaşça azalıyor.
- Mutluluk arttıkça: kuyruk daha hızlı ve geniş sallanıyor, ışıklar maviden pembeye dönüyor, %40 üstünde dil çıkıyor ve başın üstünden kendiliğinden kalpler uçuyor, %60 üstünde zıplayarak dans ediyor. Okşanırken başını ele sürtüyor, kulaklarını geriye yatırıyor.
- Okşadıkça elin olduğu yerden **kalpler uçuyor** (konfeti katmanına kalp parçacıkları eklendi). %100'de büyük kalp patlaması, taklalı zıplama, "ROBO ÇOK MUTLU!" yazısı ve havlama.
- Köpek imleci başıyla takip ediyor. Dokununca/tıklayınca havlayıp hopluyor.
- Alt panelde konuşma balonu (duruma göre değişen cümleler), kalpli mutluluk çubuğu ve **◀ Çarka dön** düğmesi var. Esc ile de çıkılıyor.
- Yeni sesler (Web Audio): `hav()` ve `mutluBip()`.
- El ile oynamada imleç, okşama için de kullanılıyor. Robot Köpek ve Çarka dön düğmeleri parmakla bekleyerek de seçilebiliyor.
- Çok yavaş kameralarda da okşama sayılsın diye iki imleç örneği arası 450 ms'ye kadar kabul ediliyor.

**Değişen dosyalar:** `index.html`, `govde.html`, `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md`

**Test durumu:**
- Chromium'da 1600×900 ve 820×1180 ekranlarda: köpek modu açıldı, fareyle başı okşanınca mutluluk %100'e çıktı, kalpler uçtu, kutlama çalıştı. Okşama bırakılınca mutluluk azaldı. Çarka dön sonrası boşluk tuşuyla çark normal döndü. Konsolda hata yok (yalnızca test ortamında yazı tipi indirilemedi).
- Sahte el verisiyle (saniyede ~8 kare): işaret parmağı başın üstünde gezdirilince mutluluk arttı, yüz "mutlu" ifadesine geçti.
- Gerçek kamerayla henüz denenmedi.

---

## Aşama 2 — Kamerayla el ile oynama
**Tarih:** 15.10.2026

**İstek:** Ek seçenek olarak kamera ile kişinin elleri algılansın. Kişi çarkın üzerinde çarkı döndürüyormuş gibi hareket yapınca el hızına bağlı olarak çark dönsün. Şıklar da elle seçilebilsin.

**Yapılanlar:**
- Üst şeride **El ile oyna** düğmesi eklendi. Kamera açılır, MediaPipe Hands ile en fazla 2 el algılanır. Sol altta ayna görüntüsü ve el iskeleti gösterilir (soru ekranında gizlenir).
- **El hızıyla çevirme:** Avuç merkezinin son ~0,42 sn'lik hareketi ölçülür. Ekranın kısa kenarının en az %28'i kadar ve hızlı bir hareket olursa çark döner. Hız, tur sayısını (3-12) ve dönüş süresini (3,4-7,2 sn) belirler. Yön, hareketin çark merkezine göre dönme yönünden hesaplanır. İki dönüş arasında 1,5 sn bekleme vardır.
- **Parmakla seçme:** İşaret parmağı ucu ekranda imleç olur (mavi/pembe, titremeyi azaltmak için yumuşatılmış). Şık, Devam, ÇEVİR ve seviye düğmeleri üstünde 1,1 sn bekleyince halka dolar ve tıklanır. Hedef beyaz çerçeveyle vurgulanır.
- Kameranın orta bölgesi tüm ekrana yayıldı; böylece köşelere uzanmak kolaylaştı.
- Dokunmatik ekran ve fare için **kaydırarak çevirme** eklendi (hız ve yön kaydırmadan hesaplanır, kısa dokunuş eskisi gibi normal çevirir).
- `cevir()` artık isteğe bağlı `{guc, yon}` alıyor.
- Çevrimdışı çalışma için MediaPipe Hands dosyaları `lib/mediapipe/` içine kondu. `index.html`'e çift tıklanırsa bu dosyalar tarayıcı kuralı gereği okunamadığı için internetten (jsDelivr) yüklenir.
- Yerel sunucuyla açmak için `baslat.bat` eklendi.
- Kamera izni verilmezse, kamera bulunamazsa ya da dosyalar yüklenemezse ekranda anlaşılır Türkçe uyarı çıkıyor.

**Değişen dosyalar:** `index.html`, `govde.html`, `baslat.bat` (yeni), `lib/mediapipe/*` (yeni), `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md`

**Test durumu:**
- Yerel sunucuda, Chromium'un sahte kamerasıyla: MediaPipe yerel dosyalardan yüklendi, el takibi "hazır" oldu, kamera önizlemesi çizildi, konsolda hata yok.
- Sahte el verisiyle: çarkın üstünde hızlı sağa kaydırma → saat yönünde 12,6 tur, 7,2 sn dönüş ✔. Parmağı A şıkkı üzerinde tutma → şık seçildi ✔. Yavaş el hareketi → çark dönmedi ✔.
- Gerçek kamerayla ve gerçek elle henüz denenmedi (eşik değerleri gerekirse sınıfta ayarlanmalı).

---

## Aşama 1 — İlk sürüm: 3B Kesir Çarkı
**Tarih:** 15.10.2026

**İstek:** Matematik projesi. Çark dönünce ortaokul seviyesinde kesir soruları gelsin, kenarlarda 4 şık çıksın, öğrenci doğru cevabı seçsin. Web uygulaması olsun; bilgisayar, tablet ve akıllı tahtada çalışsın. 3 boyutlu, renkli, efektli ve sesli olsun ("gören wow desin").

**Yapılanlar:**
- Three.js ile 3B sahne: 8 dilimli kabartmalı çark, altın jant, yanıp sönen 32 ampul, sallanan kırmızı ibre, göbek, arkada parıltı, yıldız alanı ve havada süzülen kesir sembolleri.
- Çark fiziği: 5-7 tur dönüp yavaşlayarak durur. Her dilim geçişinde "tık" sesi ve ibre sallanması. Kazanan dilim parlayıp öne çıkar.
- 8 konu için rastgele soru üretici (toplama, çıkarma, çarpma, bölme, denk kesir, karşılaştırma, kesir kadarı, tam sayılı kesir). Kolay/Orta/Zor seviyeleri.
- Yanlış şıklar tipik öğrenci hatalarından üretiliyor. Her soruda 4 farklı şık ve tek doğru cevap garanti.
- Soru ekranı: ortada soru kartı, 4 köşede renkli A-B-C-D şıkları (köşelerden uçarak gelir). Dikey ekranda 2x2 düzen.
- Doğru cevapta konfeti, fanfar, puan; seri 3/5/10'da büyük kutlama yazısı. Yanlışta sarsılma, doğru şıkkın gösterilmesi ve adım adım çözüm.
- Web Audio ile üretilen sesler (dosya gerekmez) ve isteğe bağlı arka plan müziği.
- Puan, seri, doğru/toplam sayacı; 40 sn süre seçeneği; tam ekran; klavye kısayolları.
- Seviye, ses ve süre tercihleri tarayıcıda hatırlanıyor.

**Değişen dosyalar:** `index.html`, `govde.html`, `lib/three.min.js`, `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md` (hepsi yeni)

**Test durumu:**
- Soru üretici Node.js ile 8 konu × 3 seviye × 4000 = 96.000 soru üretilerek test edildi: hepsinde 4 benzersiz şık ve tek doğru cevap var, hatalı değer çıkmadı.
- Chromium'da 1600×900 (yatay) ve 820×1180 (dikey tablet) ekranlarda açıldı, çark çevrildi, soru cevaplandı. Konsolda hata yok (yalnızca test ortamında yazı tipi indirilemedi).
- Bulunup düzeltilenler: `hidden` katmanların görünür kalması, çark renklerinin soluk çıkması, uzun dilim yazılarının taşması, "Tam Sayılı" sorularında bazen 3 şık çıkması.
