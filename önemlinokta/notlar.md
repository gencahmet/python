# Python

## stringler

- " " veya ' ' arasına yazılan şeyler stringtir.
- \n new line demek 
- \ arkasından glen şeyi dikkate alma demek. \' yani bu kesme işaretini string sonu veya başı algılama.
```python 
kim = "ahmet" 
print(kim)
print("ahmet")
```
- bıunlar aynı sonucu verir
```python
kim[0]
"Ahmet"[0]
len(kim)
len("Ahmet")
```
- aynı sonucu verir
- stringlerin içerisindeki değerler değiştirilemez. kim[0] =b olmaz
- kim[1:3] sonucu hm olarak çıkar 1. ve 2. indexi yazar. 
- kim [0:3:2] sonucu ise 0 dan 3 e kadar 2 atlayarak yaz yani Am olur.
- kim [100:0:-1] bu da 100. indexten yani en son indexten -1 olarak gel ve 0 a kadar yaz 0 dahil olmuyor dikkat!!
```python
a = "5"
int(a)
``` 
- stingi int değere çevirdik

```python
a = "5.5"
int(a)
float(a)
``` 
- string float şeklinde olduğu için int olmaz float a çevrilir.

## input
- x = input("bir sayı giriniz:") bu input fonksiyonu kullanıcıdan değer almak için kullanılır. ama aldığımız değer string olur onu tekrar int yapmamız lazım.
```python
x = input("bir sayı giriniz:") 
y = int(x)
print(y)
```
## yorum ekleme
 pytohda tek satır yorum ekleme # işareti ile yapılır.
 
 birden fazla satır için ''' sddasdadasd ''' şeklinde 3 tırnak arasına yazılabilir.

## boolean function 
- not true = false 
- a = true o zaman not a = false olur.
- a and b direkt and operatörü. (a>s) and (e>s)
- (a>s) or (e>s) . 
- short cicuit or değeri varsa ve 1 tane değerin true olduğunu biliyorsak gerisi önemli değil. 
- short circuit için örnekler ilk ikisinde hey bastırılmaz çünkü short circuitten direkt false ve true denir diğerlerinde bakılır.
- ama eğer and yerine & ve or yerine | kullanılarak short circuit önlenebilir ama printten dolayı hata alınabilir.

```python
(5 < 3) and print("hey")
(5 > 3) or print("hey")
(5 < 3) or print("hey")
(5 > 3) and print("hey")
```

## if,elif,else

``` python
x= int(input(bir sayı giriniz:))

if x%2 ==0
    print("girdiğiniz sayı çift sayıdır")

print("program sonlandı")
```

## for,while 
for da range belli while da doğru olana kadar. 

break -- döngüden çıkmak için kullanılır
continue fonkisyonu alt tarafa geçme loopun başına gidip tekrar başla diyor.

## list
verileri bir arada tutup istediğimizde verileri değiştirebilmek için.
list içinde string,int,float, list aynı ada hepsini tutabilir.

list[1:3] = [70] listede 1:3 indexleri yerine 70 eklendi
list.append() == listin sonuna değer eklenir 
list.extend([]) == listin sonuna 1 den fazla değer ekleme 
list.insert(index,deger) == istediğimiz indexe değer atıyoruz diğer değerler sağa kayıyor. 
list.remove(deger) == istediğimiz değeri siliyor. 
list.pop(index) değeri siliyor ve o değeri döndürüyor.
list.count == listede kaç defa bu değer görülmüş onu gösteriyor. 
### alising 
l2=l yaptık diyelim bundan sonra l değişince l2 de değişir çünkü l ve l2 kutuyu  gösteren etiketler.

ancak l2 = l.copy yaparsak l değişince l2 değişmez. 

## tuple
veriyi ayarladıktan sonra veri değişmez immutable listten farkı bu. ve listlerde köşeli parantez vardı tuple da normal parantez.

40 in list veya 40 in tuple ile liste tuple içinde 40 varsa true yoksa false döndürür.

## dictionary 
süslü parantez kullanılır ve indexle değil içinedki veri ile çağırılır. Aşağıdaki gibi. dictionary içinde key ve valueler istediğimiz type da olabilir birbirlerinden farklı da olabilirler ama list olamazlar.
notu =  {"Ahmet": 90,"leyla":100, "ümran":95 }
print(notu["leyla"])

## set 
süslü parantez olarak gösterilir, a= {5,3,2} ama 5 ten 2 tane koysak bile print yapınca 1 tane gözükür.

setler indexlenemez.
s.add(deger)
s.remove(deger)
s.discard(deger) remove gibi sadece error vermiyor
s1.differance(s2) cevap olarak seet çıkarır
s1-s2 buda differancı verir.
s1.symetric.dfiferance(s2) kesişim hariç tüm kümeyi verir.
s1.intersection(s2) kesişimi verir
s1.union(s2) birleşimi verir
s1.isdisjoint(s2) true false verir
s2.issubset(s1) s2 s1 in alt kümesiyse true değilse false
s1.issuperset(s2) üst kümesi mi için

## split

stringleri belirlibir kurala göre listeye çevirmek 
s = "merhaba nasılsın ?"
print(s.split(" "))
burada s stringini her boşlukta yeni eleman olarak böl demiş oluyoruz ve 3 elemanlı bir liste elde ediyoruz.

yani stringden liste gidiyor 

## join 
listten stringe döndürür.
l = ['limon', 'portakal', 'elma']
",".join(l)
list i stringe çevirir.

- enumerate() bize (index, element) olarak verecek.
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']
for e in adlar:
    print(e)
for i, e in enumerate(adlar):
    print(i, "indexindeki eleman:", e)
- enumerate() 0'dan başlamak zorunda değil, özellikle kaçtan başlayacağını belirtebiliriz.
for i, e in enumerate(adlar, start = 100):
    print(i, "lokasyonunda bulunan eleman:", e)

## zip()
- bu function ile farklı veri tipleri içinde paralel iterasyon yapmamızı sağlar.

- ayrıca bunu kullanarak dictionary yapabiliriz. 
  