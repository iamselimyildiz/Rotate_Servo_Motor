# Rotate_Servo_Motor

1)Komut İstemini aç (Command Prompt), içerisine `pip install pyfirmata` yaz ve Enter'a bas.  
2) Ardunio inidirilir ve kurulur.`https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE`  
3)Ardinuo yu aç ve üst bardan Tools/Library Manager kısmına girip `firmata` diye arat.  
![1](https://github.com/iamselimyildiz/Rotate_Servo_Motor_Ardunio/assets/94224409/d1412f3b-27b4-4d91-9109-85495f1eb9b9)  
4)Şimdi sıra Ardunio ile Servo motor (ben SV90 modelini kulandım)' ı bağlamaya geldi.  
Kabloların takılacağı soketler:` Kırmızı:5V,Turuncu:-5 ve Siyah:Topraklama(GND)`.    
(Tabi servo'nun kollarını vidalamayı unutmayın.)  
![ardunio_ve_servo_bağlantı](https://github.com/iamselimyildiz/Rotate_Servo_Motor_Ardunio/assets/94224409/c57ce6d5-7ea2-4b6c-a73d-0145d1d7215b)  
5)Kablo bağlamaları yapıldıktan sonra güç kablosunu(power cord) Ardunio'ya bağlayın.  Şu aşamada PC-ARDUNIO-SERVO bağlantısı yapılmış olmalı.  
6)Ardunio ya kütüphane yükleme: Yukarıdaki bardan `File/Examples/Firmata/Standart Firmata` yı bul.   
![Ekran Görüntüsü (167)](https://github.com/iamselimyildiz/Rotate_Servo_Motor_Ardunio/assets/94224409/f8e4903e-dd68-4e0e-9fe8-3e15b3b86775)  
7)Yeni pencerede açılan kodu üstteki `Upload(-->)` tuşu ile Ardunio ya yükle.   
Eğer sorunla karşılaşırsan select board ile diğer portları dene.  
![InkedEkran Görüntüsü (168)](https://github.com/iamselimyildiz/Rotate_Servo_Motor_Ardunio/assets/94224409/99e102c7-5f58-4495-b942-d1d38c3e6e73)  
8) Son aşama, hangi portta olduğumuzu yazacağımız python koduna yapıştıralım. Benim durumumda `COM3`  
![Ekran Görüntüsü (169)](https://github.com/iamselimyildiz/Rotate_Servo_Motor_Ardunio/assets/94224409/df41b475-d2c1-47f0-9966-e6774661d0fe)  
9) Kod editörünü aç ve `Port="COM3"` yazan kısma kendi portunu aynı formatta yaz.  
Repodaki `1.py` adındaki python uzantılı dosyadaki kodu kullan ve yazarken anlamaya çalış.  
![SharedScreenshot](https://github.com/iamselimyildiz/Rotate_Servo_Motor_Ardunio/assets/94224409/ea17b4bd-d283-4f7d-9930-556de74272b6)





