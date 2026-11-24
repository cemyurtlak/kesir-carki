# Devam Notları

## Çalışma kuralları
- Her değişiklikten sonra `GELISTIRME_GUNLUGU.md`'ye yeni aşama eklenir (en yeni üstte), gerekirse `README.md` ve bu dosya güncellenir.
- Arayüz metinleri ve kod içindeki değişken adları **Türkçe**dir; bu düzen korunmalı.
- Uygulama **tek HTML dosyası** + `lib/three.min.js` olarak kalmalı (okulda çift tıkla, internetsiz açılabilsin).
- `govde.html`, paylaşım bağlantısında yayınlanan gövdedir. `index.html` değiştirilirse aynı değişiklik `govde.html`'ye de yapılmalı (fark yalnızca `<!DOCTYPE>/<head>/<body>` sarmalayıcısı).

## Teknik kararlar ve nedenleri
- **Three.js r149 (UMD, `three.min.js`)**: `<script>` ile yüklenebilen son sürümlerden; modül/sunucu gerektirmez, `file://` ile açılır. Yerel dosya yoksa jsDelivr CDN'den yüklenir.
- **Renk yönetimi**: `outputEncoding` kullanılmıyor; renkler hex değerleriyle birebir görünsün diye (sRGB açıkken dilimler soluk çıkıyordu).
- **Sesler Web Audio ile sentezleniyor**: ses dosyası taşımaya gerek yok, çevrimdışı çalışır. Tarayıcı kuralı gereği ses ilk dokunuştan sonra başlar.
- **Konfeti ayrı 2B canvas'ta**: soru katmanının üstünde görünsün diye 3B sahneye değil, en üst katmana çiziliyor.
- **Soru katmanı HTML ile**: akıllı tahtada büyük ve net yazı için kesirler 3B değil, HTML/CSS ile (pay/çizgi/payda) çiziliyor.
- **Şık benzersizliği**: şıklar değerce karşılaştırılır (2/4 ile 1/2 aynı sayılır). "En sade hâl" ve "bileşik kesir" sorularında yazım biçimi karşılaştırılır; aynı değerli ama sadeleşmemiş kesir bilinçli yanlış şık olarak eklenebilir.
- **El takibi için MediaPipe Hands (eski "solutions" sürümü)**: model dosyaları npm paketinin içinde geliyor; böylece tamamen çevrimdışı kullanılabiliyor. Yeni `tasks-vision` paketi modeli Google sunucusundan indirmeyi gerektiriyordu. `modelComplexity:0` (hafif model) seçildi; akıllı tahtalarda hız için. `selfieMode:true` ile görüntü ve koordinatlar ayna çevrilmiş geliyor.
- **file:// sınırı**: Tarayıcı, çift tıkla açılan sayfanın yanındaki `.wasm/.data` dosyalarını okumaya izin vermiyor. Bu yüzden `file://` açılışta el takibi dosyaları jsDelivr'den yükleniyor; tamamen çevrimdışı kullanım için `baslat.bat` → `sunucu.py` var (Python `http.server`, 127.0.0.1, port 8771'den başlayıp ilk boş port). `localhost` güvenli kaynak sayıldığı için kamera izni orada da çalışır.
- **Projeye özel port + boş port arama (Aşama 4)**: Diğer projeler de 8765 gibi ortak portlar kullanınca yanlış proje açılıyordu. `sunucu.py` dolu portu atlar, Windows'ta `SO_EXCLUSIVEADDRUSE` kullanır (Python'un varsayılan `allow_reuse_address` ayarı Windows'ta dolu porta ikinci bağlanmaya izin veriyordu), `no-store` ile önbelleği kapatır. Not: port değişirse tarayıcıdaki kayıtlı ayarlar (seviye, ses) o adres için sıfırdan başlar.
- **Seçme yöntemi = bekleme (dwell)**: Çimdik hareketi çocuklarda ve uzaktan güvenilmez olduğu için parmağı 1,1 sn tutma seçildi.
- **Paylaşım bağlantısında kamera kullanılamaz**: claude.ai bağlantısı kamera iznini engelliyor; el ile oynama yalnızca bilgisayardaki dosyadan çalışır. Bağlantıda düğmeye basılınca uyarı çıkar.
- **Robot köpek ayrı sahne, aynı renderer**: İkinci bir WebGL bağlamı açmamak için `Kopek.sahne`/`Kopek.kamera` aynı `renderer` ile çiziliyor; köpek modunda çark sahnesi çizilmiyor (akıllı tahtada performans). Köpek modunda `durum.asama='kopek'`, böylece `cevir()` ve klavye/el ile çevirme kendiliğinden kapalı.
- **Köpek yüzü = canvas dokusu**: Kavisli küre parçası (SphereGeometry phi/theta aralığı) üstüne 512×256 canvas; ifade değişince yeniden çiziliyor (her karede değil).
- **Okşama ölçümü 2B ekranda**: Başın merkezi ve yarıçapı her seferinde 3B'den ekrana izdüşürülüyor (`basEkran`). İmleç başın 1,4 yarıçapı içindeyse ve hareket ediyorsa okşama sayılıyor. Fare, dokunuş ve iki el ayrı kaynak (`kay`) olarak tutuluyor.
- **Kalpler konfeti canvas'ında**: Okşama kalpleri 2B üst katmanda (`kalp()`, `kalpCiz()`); arkadaki süzülen kalpler 3B sprite.
- **Yayın = GitHub Pages (Aşama 5)**: depo `cemyurtlak/kesir-carki` (herkese açık; Pages ücretsiz planda yalnızca açık depoda çalışır), adres https://cemyurtlak.github.io/kesir-carki/ . Değişiklikten sonra değişen dosyalar depoya da yüklenmeli (bu oturumda Chrome'daki GitHub "Upload files" sayfasıyla yüklendi; tek seferde en fazla ~10 MB). Klasörün bulunduğu yolu `lib/...` korunmalı.
- **Parmakla tutup çevirme fiziği (Aşama 5)**: Bırakma hızı ω (rad/sn) → süre T = 2,2 + 0,19·|ω| sn (en çok 9 sn), açı Δ = ω·T/4. Dönüş eğrisi 1−(1−p)^4 olduğu için başlangıç hızı 4Δ/T = ω; yani çark parmaktan çıktığı hızla devam eder, sıçrama olmaz. Hedef dilim sona göre `ibreAltindaki(son)` ile bulunur (hile yok). Eşik `SURUKLE_MIN_HIZ` = 6 rad/sn. Hız, son 180 ms'deki örneklerden; parmak bırakmadan 220 ms'den uzun beklediyse 0.
- **Neden olay zaman damgası + getCoalescedEvents**: Zayıf telefonlarda kare hızı düşünce tarayıcı dokunma hareketlerini birleştirir; yalnız son olayı ölçmek hızı yanlış (genelde 0) çıkarıyordu.
- **Dikey ekran**: `max-aspect-ratio:1/1` veya 760px altında şıklar kartın altına 2x2 dizilir.

## Kod haritası (`index.html` içi)
| Bölüm | İçerik |
|---|---|
| `<style>` | Renk/yazı değişkenleri (`:root`), üst şerit, ÇEVİR düğmesi, soru katmanı, şıklar, kesir gösterimi (`.frac`), dikey ekran kuralları |
| `// <SORULAR>` … `// </SORULAR>` | Kesir matematiği (`gcd`, `sade`, `topla`…), HTML gösterimi (`kH`, `frac`), `secenekKur` (4 benzersiz şık), `URETICI` (8 konu × 3 seviye), `soruUret` |
| `Ses` nesnesi | Efektler (`tik`, `vuuu`, `dogru`, `yanlis`, `seri`…) ve `muzik()` döngüsü |
| `KAT` dizisi | Çarktaki 8 dilim: id, ad, sembol, renk (sıra = çarktaki sıra) |
| `sahneKur()` | 3B sahne: ışıklar, yıldızlar, süzülen semboller, çark dilimleri, jant, ampuller, göbek, ibre |
| `cevir()` / `donusBitti()` | Hedef dilimi seçip dönüş açısını hesaplar; durunca soruyu açar |
| `soruGoster()` / `cevapla()` / `devam()` | Soru akışı, süre, puan, geri bildirim |
| `konfeti()` / `dongu()` | Konfeti ve ana animasyon döngüsü |
| `donusYonu()` + `#sahne` pointer olayları | Çark dışında kaydırarak hıza göre çevirme |
| `Surukle`, `carkEkran`, `firlat`, `surukleBitir` | Çarkı parmakla tutup çevirme, bırakma hızıyla fırlatma (Aşama 5) |
| `El` nesnesi, `elModuAc/Kapat`, `elKare`, `elSonuc` | Kamera, MediaPipe Hands, önizleme çizimi, el hızıyla çevirme |
| `hedefBul` / `beklemeIsle` | Parmak imleci altında düğme bulma ve 1,1 sn bekleyince tıklama |
| `kalpYol` / `kalp` / `kalpCiz` | Uçuşan kalp parçacıkları (konfeti katmanında) |
| `Kopek` nesnesi, `kopekKur()` | Robot köpek sahnesi ve modeli (gövde, bacaklar, baş, yüz ekranı, kulaklar, kuyruk, zemin) |
| `kopekOksa` / `kopekDokun` / `basEkran` | Okşama algılama, mutluluk artışı, %100 kutlaması; dokununca havlama |
| `kopekGuncelle(now)` | Her kare: mutluluk azalması, kuyruk/baş/kulak/zıplama animasyonu, ışık rengi, ifade, alt panel |
| `kopekYuzCiz(ifade)` | Yüz ekranı: normal, uzgun, kirp, gulen, mutlu, kalp |
| `kopekAc` / `kopekKapat` | Köpek moduna giriş/çıkış |

**Ayar değerleri (el modu, `elSonuc` içinde):** hareket penceresi 420 ms; çevirme eşiği mesafe > 0,28 (ekranın kısa kenarına göre) ve hız > 1,4/sn; güç = (hız − 1,4) / 3; iki dönüş arası 1500 ms; `BEKLEME` = 1100 ms; kamera eşlemesi x: 0,12–0,88, y: 0,10–0,80.

**Ayar değerleri (robot köpek, `Kopek` nesnesinin hemen altında):** `OKSAMA_HIZ`=3,5 (büyütürsen mutluluk daha çabuk dolar), `MUTLULUK_AZALMA`=3,5/sn (okşamadan 1,8 sn sonra başlar), `KOPEK_YON` gövde açısı, `KOPEK_BAS` baş açısı. Kamera uzaklığı `kopekBoyutla()` içinde.

Soru üreticiyi test etmek için `<SORULAR>` bloğu ayrı bir `.js` dosyasına kopyalanıp Node.js ile çok sayıda soru üretilebilir (her soruda 4 şık, tek doğru, benzersiz değer kontrolü).

## Bilinen sorunlar / sınırlar
- Parmakla çevirme gerçek telefonda henüz denenmedi; çok zor dönüyorsa `SURUKLE_MIN_HIZ` düşürülmeli.
- iPhone'da tam ekran düğmesi yok (Safari desteklemiyor); "Ana ekrana ekle" ile tam ekran açılır.
- GitHub sürümü bilgisayardaki klasörle otomatik eşitlenmez; değişiklikten sonra elle yüklenmeli.
- Çok eski akıllı tahtalarda (WebGL yoksa) uyarı mesajı çıkar; 3B olmayan yedek mod yok.
- İnternet yoksa "Baloo 2" yazı tipi yüklenmez, sistem yazı tipi kullanılır (çalışmayı etkilemez).
- Tarayıcı kuralı nedeniyle müzik/ses ilk dokunuştan önce çalmaz.
- El modu gerçek kamerayla henüz denenmedi; eşikler sınıf ortamında ayarlanmalı (çok hassas/az hassas olursa yukarıdaki değerler).
- Elin hangi imlece ait olduğu sıraya göre belirleniyor; iki el yer değiştirirse imleç renkleri yer değiştirebilir.
- Eski akıllı tahtalarda el takibi yavaş çalışabilir (saniyede az kare). Hareket penceresi bu yüzden geniş tutuldu.

- Robot köpek gerçek kamerayla henüz denenmedi; okşama çok zor/kolay dolarsa `OKSAMA_HIZ` ayarlanmalı.
- Köpek bölümünde hiç ses dosyası yok; havlama sentezle üretildiği için "robotik" duyuluyor (bilinçli).

## Sonraki adım fikirleri
- Robo'yu oyunla bağlamak: doğru cevaplarda Robo'ya "kemik/pil" kazanmak, seri yapınca Robo'nun sevinmesi.
- Robo'ya yeni hareketler: top getirme, "otur" komutu (el hareketiyle).
- El modu için ayar paneli (hassasiyet, bekleme süresi).
- İki takım modunda her takıma bir el/imleç rengi.
- **Takım modu**: sınıfı 2 takıma bölüp sırayla çevirme, takım puanları.
- Öğretmen için konu seçimi (ör. sadece toplama-çıkarma dilimleri).
- Kesir sorularına pasta/şerit modeli görseli eklemek.
- Oyun sonu özet ekranı (kaç soru, hangi konuda kaç doğru).
- Ondalık gösterim ve yüzde dilimi (7. sınıf).
