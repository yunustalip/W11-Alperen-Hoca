"""
Created on Wed Dec  7 16:58:19 2022

@author: talip

Ödev1) Boş Copy Nedir? ".Copy" Nedir, yazdıktan sonra neleri değiştirir, neleri değiştirmez ?
DeepCopy Nedir? Shallow Copy Nedir? Bunlar oluşturduğumuz df'de neleri değiştirir?

Ödev2)e-01 yerine 0.78'i nasıl görebiliriz?

Ödev3)"np.Log()" doğal logoritma dediğimiz şekilde mi gelir yoksa log 2 tabanında mı gelir?

Ödev4)Yeo-Johnson çok büyük değerlerde uygulanamıyor mu? Neden Income değerlerindeki 
"10" olan değerimizi arttırdığımızda(1000 yaptığımızda) çıktımızda bozulmalar oluyor?

Cevap 1)  Direkt örnek üzerinden açıklama yapmak gerekirse
        Shallow copy örneği
            liste1 = [1,2,3]
            liste2 = copy.copy(liste1) olarak Shallow copy uygulayalım
            burda liste1 ve liste2nin bellekte tutulan idleri farklıdır. Eğer liste2ye yeni bir append yaparsak liste1 etkilenmez. AMA... 
            liste2 deki 1. değeri güncellediğimizde, liste1 deki 1. değerde güncellenir.
            Kısacası Shallow copy de birbirinin kopyası ama kısmen birbirine bağımlılık vardır.
        
        Deepcopyde ise
            Hem liste1 ve liste2nin bellekte tutulan idleri farklıdır. Hemde eğerki;
            liste1 deki 1. değeri güncellerseniz, liste2ye bir etkisi olmayacaktır. 
            birbirinin kopyası ama birbirinden tamamen bağımsız 2 liste olacaktır.
            
Cevap 2) 
"""
print( float(78e-2))
# 0.78
"""
Cevap 3)
np.log doğal logaritma olarak gelir yani e tabanında.

Cevap 4)
Yeo-Johnson dönüşümü veri setinde negatif ve sıfır değere sahip gözlemler olduğunda kullanışlıdır.
"""
