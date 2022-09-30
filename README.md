# Nyarlko-s-Android-Toolbox
<a href="https://github.com/ny4rlk0/Android-Toolbox-ADB/releases/download/v2.6/Android_Toolbox@nyarlko_v2.6.zip">İndir / Download v2.6</a>
<br><a href="https://github.com/ny4rlk0/Android-Toolbox-ADB/releases/download/v2.5/Android_Toolbox@nyarlko_v2.5.zip">İndir / Download v2.5</a>
<br>TR
---------------
<br>Hepsi bir arada android alet çantası. 
<br>Tüm apk'leri tek bir cihazda veya klasörde, usb veya wifi'den yedekleyin / geri yükleyin. ADB / USB ADB üzerinden Wifi /
<br>Fastboot / flash / kilit / kilit açma / silme / önyükleme kurtarma, çekirdeğe geçici önyükleme vb.
<br>Wifi Ters Kabuk 2 ayrı komut satırı olarak çalışır.
<br>Cihazınız fastboot modundaysa fastboot.exe'yi kullanır.
<br>Cihazınız ADB hata ayıklama modundaysa adb.exe'yi kullanır.
<br>USB'den cihaza, Wifi Reverse Shell'den de komut gönderebilirsiniz.
<br>* Not:
<br>ADB / FASTBOOT sürücülerinizi kurmayı unutmayınız...
<br>Programı her güncellediğimde ss'yi değiştirmek uğraştırıcı olmaya başladığı için ekran görüntüleri gerçek programdan farklı olabilir.
<br>Bu programın işlevlerinin çoğu ADB'in açık olmasını ve bir kısmı Önyükleyici (Bootloader) kilidinin açık olmasını gerektirir.
<br>Samsung telefonları Download Mode tek tuşla alabilirsiniz.
<br>
<br>Cihaz sürücülerini ADBDriversInstall.CMD'yi yönetici olarak açarak yükleyin.
<br>Rootlama Anlatımı Redmi Note 10S için
<br>Önyükleme kilidinizi Resmi yazılımla açın.
<br>Mevcut Firmware dosyanızdan images klasöründen boot.img telefonunuzun SD kartına kopyalayın.
<br>Cihazınızı Fastboot Moduna alın.
<br>TWRP recoveryi boot kısmına yükleyin.
<br>Cihazı yeniden başlatmadan Fastboot Menüsünden Recovery'e basın.
<br>TWRP açılınca boot kısmına ilk adımdaki boot.img flashlayın. Tek partitiona. 
<br>(Bunu yapmamızın sebebi cihaz twrp boot partitiona flashlı iken sadece TWRP boot ediyor. System'e boot etmiyor.)
<br>Userdata'yı yes yazarak formatlayın.
<br>System'i mount edin ve Magisk flashlayın.
<br>Cihazı yeniden başlatın.
<br>Not: Detaylı sistem kontrolü yaparken "com.mediatek.smartratswitch.service.apk" bir apk dosyası buldum.
<br><a href="https://www.reddit.com/r/Xiaomi/comments/qkfiy4/comment/ii3vkzl/?utm_source=share&utm_medium=web2x&context=3">Radio Accesss Technology Switch yani Ağ değişimini yapan bir apk bu.</a> 
<br>Özellikle belirtmek istedim çünkü kısaltması Remote Access Trojan ile karıştırılabilir.
<br>Ayrıca TWRP'den sideload'a basıp yazılım üzerinden istediğiniz .zip dosyasını TWRP'de ilerlemesini görerek yükleyebilirsiniz. Recovery/Fastboot romları gibi.
<br>
<br>EN
---------------
<br>Install drivers from ADBDriverInstall.CMD
<br>All in one android toolbox. Backup / Restore entire apks in single device or folder, from usb or wifi. Wifi over ADB / USB ADB / <br>Fastboot / flash /  lock / unlock / wipe / boot recovery , temp boot to kernel etc.
<br>Wifi Reverse Shell works as 2 seperate command line.
<br>If your device in fastboot mode it will use fastboot.exe
<br>If your device in ADB debugging mode it will use adb.exe
<br>You can send commands from USB to device, from Wifi Reverse Shell too.
<br>* Note:
<br>Don't forget to install your ADB / FASTBOOT drivers...
<br>Bring samsung phones to download mode with single click. *New: ~Waku ~Waku
<br>Screenshots may differ from actual program since it started to pain in the ass to change ss everytime i update program. 
 <br>* Screen Shots:
<p align="center">
    <img src="10.jpg">
    <img src="20.jpg">
