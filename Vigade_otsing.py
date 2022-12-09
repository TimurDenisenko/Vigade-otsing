from math import * #поменял немного модуль сделав его более удобным для использования дабы не писать math.funktsioon()

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #добавил тип данных float чтобы использовать переменные в формулах и поменял кавычки на привычные
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=sqrt(2*a**2) #изменил math.funtktsioon на sqrt и сделал правильную формулу диагонали квадрата - умножил на 2 возвел в квадрат
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #убрал лишнюю скобку в конце
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #добавил тип данных float для дальнейшего использования в формулах
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #добавил тип данных float для дальнейшего использования в формулах
S=b*c
print("Ristküliku pindala", S) #добавил кавычки и поменял их на привычные 
P=2*(b+c) #добавил знак умножения после 2
print("Ristküliku ümbermõõt", P)
di=sqrt((b**2+c**2)) #изменил math.funtktsioon на sqrt и сделал правильную формулу
print("Ristküliku diagonaal", round(di,1)) #добавил скобку в конце и сделал правильное округление по заданию
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus =>")) #добавил тип данных float для последующего применения в формулах
d=2*r #поставил знак умножения между 2 и r
print("Ringi läbimõõt", d) #добавил запятую между текстом и переменной
S=pi*r**2 #поправил формулу - r вместо умножения возвел в квадрат
print("Ringi pindala", round(S,2)) #добавил правильное округление в соответствие с заданием
C=2*pi*r #добавил знак умножения между 2 и числом Пи
print("Ringjoone pikkus", round(C,2)) #добавил правильное округление в соответствие с заданием
