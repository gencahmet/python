'''
x = int (input("bir sayı giriniz: "))

if x%2 == 0:
    print("çift")
print("bitti")
'''
'''
x = int(input("bir sayı giriniz: "))

while x < 0:
    print("sayı negatif, pozitif gir")
    x = int(input("bir sayı giriniz: "))

print("sayı pozitif ve " x "dir")
'''
''''
toplam =0
x=0
while x<=100:
    toplam +=x
    x +=1
print(toplam)
'''
'''
for c in "hey":
    print(c)
toplam =0
for x in range(101):
    toplam +=x
print(toplam)
'''
# gördüğümüz gibi break while ve for içinde kullanılıp dögüyü sonlandırıyor.
'''
for i in range(10):
    if i ==3:
        break
    print(i)
x=0
while x<10:
    print(x)
    x +=1

    if x ==3:
        break
'''
# continue fonkisyonu alt tarafa geçme loopun başına gidip tekrar başla diyor.
'''
for i in range(10):
    if i ==3:
        continue
    print(i)
x=-1
while x<10:
    x +=1
    if x ==3:
        continue
    print(x)
'''
'''
i=0    
notlar = [10, 20, 35, 67, 98]
# notlar = [ogrenci_1, ogrenci_2, ogrenci_3, ogrenci_4, ogrenci_5]
notlar [1] += 70 
for i in range(5):
    print(notlar[i])
    i +=1
notlar[0:3] = 80,95
print(notlar)
notlar[0:3] =[100]
print(notlar)
print(len(notlar))
notlar.append(75)
print(notlar)
notlar.extend([50,88])
print(notlar)
notlar.insert(3,77)
print(notlar)
notlar.remove(75)
print(notlar)
print(notlar.pop(1))
print(notlar.count(50))
print(notlar)
print(notlar.index(77))
notlar.reverse() # listeyi terse çevirir kalıcı olarak
print(notlar)
print(notlar[::-1])  # ters yazmayı sağlar kalıcı değil sadece yazar
print(sorted(notlar)) # küçükten büyüğe sıralama ama orjinal liste günvcellenmez hala aynı
print(notlar)
notlar.sort() # küçükten büyüğe kalıcı oldu.
print(notlar)
newlist = ["f","t","g","3"]
print(sorted(newlist))
'''
'''
konum = (42,25)
print(konum[1])
print(konum[0])
print(konum)
print(40 in konum)

newtuple = ([24,43,55],67,86)
newtuple[0][2]=13 # tuple içindeki liste değeri deişebilir.
print(newtuple)

x=2
y=3
(x,y)=(y,x)
print(x,y)
[x,y] = [y,x]
print(x,y)
'''
'''
isim = ["Ahmet", "Leyla","kübra","hacer","ümran"]
notlar = [88,92,97,100,89]
a = len(isim)
i=0
for i in range(a):
    print(isim[i], "adlı öğrencinin notu", notlar[i])
    i +=1
notu =  {"Ahmet": {"not": 90,"no":43},"leyla":{"not": 100,"no":23}, "ümran":{"not": 98,"no":63} }
print(notu["leyla"]["no"])
notu["Ahmet"]["not"] =83
notu["Kübra"] = 97,34
del notu["Ahmet"]
print(notu) 
'''
'''
mesage = "merhaba, nasılsın?"
s = set(mesage)
print(s) '''
'''
notlar = [90,72,81,77]
for e in notlar:
    print(e)
'''
'''
t = 0

for e in notlar:
    t += e
    
ortalama = t / len(notlar)

print(ortalama)
'''
'''
t = 0

for penguen in notlar:
    t += penguen
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)
'''
'''
for i in range(4):
    print("Iteration: ", i)

t = 0

for i in range(len(notlar)):
    t += notlar[i]
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)'''
'''
for i in range(len(notlar)):
    notlar[i] += 5
print(notlar)
'''
'''
for i in range(len(notlar)):
    
    if i == 1:
        continue
        
    notlar[i] += 5

print(notlar)'''
'''
x = int(input("Hangi sayıyı kontrol edeyim?:"))

l = [2,3,40,100,10,1]

for e in l:
    print(e) # iterasyon break ile çıkmış mı görelim mi diye
    if e == x:
        print("Buldum!!")
        break
'''
'''
d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}
d2 = {"student_1": 90, "student_2": 80, "student_3": 72}
for k in d:
    print(k)

for k in d:
    v = d[k]
    print(v)

for v in d.values():
    print(v)

for k in d2:
    value = d2[k]
    
    if value > 85:
        print(k)

for k,v in d.items():
    print("key değeri:", k, "value değeri:", v)
    '''
'''
s = "merhaba nasılsın ?"
print(s.split(" "))
'''
'''
s2 = "limon, portakal, elma"
print(s2.split(","))
'''


'''
l = ['limon', 'portakal', 'elma']
",".join(l)
'''
'''
squares = [i*i for i in range(1,11)]
print(squares)
odd_squares = [e for e in squares if e%2==1]
print(odd_squares)
square_dict = {e:e * e for e in range(1,11)}
print(square_dict)
print(square_dict[9])
m = [[j for j in range(7)] for _ in range(5)]
print(m)
new_m = []
for l in m:
    print(l)
    for e in l:
        new_m.append(e)
        print(e)
        '''
'''
x, y, *z, t = (4, 7, 11, 4, 21)
print(x)
print(y)
print(z)
print(t)
'''
'''
l = [(1,2), (10,20)]
for e in l:
    print(e)
print(type(l))
for e in l:
    a, b = e
    print(a)
    print(b)
    print("*********")
for a, b in l:
    print("tuple'ın ilk elemanı", a)
    print("tuple'ın ikinci elemanı", b)
    print("-----------------------------")
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']
for e in adlar:
    print(e)
for i, e in enumerate(adlar):
    print(i, "indexindeki eleman:", e)
for i, e in enumerate(adlar, start = 100):
    print(i, "lokasyonunda bulunan eleman:", e)
    '''
    
'''
    satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for i in range(len(maliyet)):
    s = satis[i]
    c = maliyet[i]
    
    kar = s - c
    print(f'Total profit: {kar}')

for s, c in zip(satis, maliyet):
    kar = s - c
    print(f'Total profit: {kar}')

'''
'''
keys = ['isim', 'soyad', 'ulke', 'is']
values = ['Denis', 'Walker', 'Turkey', 'data scientist']
d = {}
for k, v in zip(keys, values):
    d[k] = v
print(d)
'''


'''
def square(x):
    return x * x

print(square(2))

def square(x):
    
    res = x * x
    
    print("Square of " + str(x) + ": " + str(res))
    
    return res

square(4)

def f(x):
    
    l = []
    res = x * x 
    for i in range(10):
        res += 20
        l.append(res)
    return l

print(f(10))
'''
'''
def hello(end, start = "Hello"):
   
  print(start + " " + end)
hello("Denis")
hello("Denis","Hey")
'''
'''
def kare(x):
    return x**2
a = kare # a da fonksiyon oldu.
print(a(5))

def f2(x, f):
    return f(x) + 4
f2(3,kare)
print(f2(3,kare))
'''

# alt taraftaki fonksiyon çağırmalar çok önemli
'''
l = [1,2,3,4]
def apply(l, f):
    """
    l bir liste, 
    f listenin tüm elemanlarına uygulanacak fonksiyon
    sonunda listenin orijinali elemanlarına fonksiyonun uygulanmış haliyle güncellenir
    """
    
    n = len(l)
    
    for i in range(n):
        l[i] = f(l[i])

def kare(x):
    return x**2

apply(l, kare)
print(l)

def kup(x):
    return x**3

def apply_funcs(f_list, x):
    t = []
    for f in f_list:
        t.append(f(x))
        
    return t 

print(apply_funcs([kare, kup], 5))

'''
'''
a = 9_000_000_000 # alttan çizgiyi bilgisayar okumuyor sadece bizim okumamız için kolay oluyor.
print(a)
'''
'''
x=2
print(f"x in değeri {x}") # x i stringe çevirip toplama yapmak yerine başa f koyup tırnak arasına koyup süslü paranteze x değerini koyuyoruz.
'''
'''
def kare(x):
    return x**2

b = int(input("değer giriniz: "))
a = kare(b)
print(f"{b} nin karesi {kare(b)} dır")

'''


#n, m = map(int, input().split()) # map(int, input().splite()) tek line da 1 den fazla input almaya yarar.
'''n,m = [int(x) for x in input().split()]
l1 = []
l2 = []
l3 = []
l4 = []
counter = 0

for i in range(n):
    a = input()
    l1.append(a)
for i in range(m):
    b = input()
    l2.append(b)


for counter in range(m):
    for counter1 in range(n)
    if l2[counter] == l1[counter1]:
        l3.append(counter1+1)
    
    if l2[counter] == l1[counter1]:
        l4.append(counter1+1)

print(l3)
print(l4)
'''
'''
n, m = map(int, input().split())

from collections import defaultdict

l1 = defaultdict(list)
l2 = []

for i in range(n):
    l1[input()].append(i+1)


for x in range(m):
    l2.append(input())
    

for y in range(m):
    if l2[y] in l1:
        print(l1[l2[y]])
    else:
        print("-1")
'''