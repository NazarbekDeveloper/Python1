# Python1

Ushbu loyiha Python dasturlash tilida yechilgan misollar saqlanadigan loyiha hisoblanadi

*Universitetda Python fanida berilgan vazifalar va misollar yechim kodlari hammasi shuyerda jamlanadi*
---
20.02.2026
Mavzu: Istisnolar bilan ishlash

Pythonda dasturda 2 xil xatolik bo'lishi mumkun:
1) Sintaksis xatolik - bu dasturni ishlatmaydigan xatolik turi hisoblanadi
Masalan: buyruqni xato yozish

if a > b # : qolib ketgan 
    print(a)
funksiyada xatolik
pint("salom") # r qolib ketgan 

2) RunTime error - bu xatolik bilan dastur ishlaydi, lekin o'sha xato qismi ishlagan paytda dasturda xatolik kelib chiqadi. Bu xatolik Istisno deb ataladi.
Masalan:

str = "hello"
a = int(str) # string turidagi so'zni intga o'tkazib bo'lmaydi
print(a) 

Bunday xatoliklarni oldini olish uchun Pythonda (try except) bloki mavjud.
Umumiy strukturasi:

try:
    amallar
excep([xatolik turi]):
    xatolik haqida xabar

Misol:

try:
    son = int(input())
    print(son)
except ValueError:
    print("Xato qiymat kiritildi")
print("Dastur tugadi")

---
Xatolik turlari asosiylari:

1) ValueError - a = int("hello")
2) ZeroDivisionError - a = 5, b = 0, a/b
3) Exception - umumiy xatolik

# Funksiya

Malum bir amalni dastur davomida qayta qayta ishlatishga yordam beruvchi narsa

Feunksiya (def) kalit so'zi orqali e'lon qilinadi.
Umumiy strukturasi:
--- 
def funksiyaNomi(parametrlar):
    #funksiya tanasi

Masalan:


def Display():
    print



Pythonda o'zgaruvchilarning ko'rinish sohasi mavjud bo'lib u 2 turga bo'linadi:
1) Global - butun dastur tarkibida ishlaydigan o'zgaruvchi
2) Lokal - faqat funksiya tarkibida ishlaydigan o'zgaruvchi.

Funksiya tarkibidagi o'zgaruvchini (global) kalit so'zi orqali globallashtiramiz

Masalan:
def Salom():
    global ism = "Sardor"
    print("salom ",ism)
def Xayr():
    print("xayir ",ism)


# Mavzu: Modullar

Dasturlashda stadart modullar mavjud, uning vazifasi: avvaldan tayyorlab qo'yilgan amallarni bajarish.

Masalan: Math moduli

Nostandart holatda elon qilinishi mumkun bo'lgan modul ham mavjud bo'lib.
U dasturchi tomonidan elon qilinadi.

Masalan: 

metod.py
 buyerda Sum(n); va Factorial(n); metodlari bor

misol.py
import metod as m
try:
    