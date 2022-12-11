import numpy as np

def P(b, total):
    return (b / total)
def A(n, m):
    b = (np.math.factorial(n)/np.math.factorial(n - m))
    return b
def fact(n, m):
    b = (np.math.factorial(n) * np.math.factorial(m-3))/(np.math.factorial(m)*np.math.factorial(n-3))
    return b
def dob_fact(a, p, m, n):
    b = (p / n) * fact(a, m)
    return b
def task1(b, br, r, bl):
    print("Завдання 1:")
    total = b + br + r + bl
    print("Ймовірність, що навмання взята коробка виявиться чорною =", round((P(b, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться коричневою =", round((P(br, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться червоною =", round((P(r, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться синьою =", round((P(bl, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться червоного або синього кольору =", (P(bl, total) + P(r, total)))
def task2(n, n1, m):
    print("\nЗавдання 2:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("Ймовірність, що серед навмання вибраних двох співробітників, хоча б один буде консультантом =", round(((A1 - A2) / A1), 2))
def task3(n, n1, m):
    print("\nЗавдання 3:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("Ймовірність, що серед вибраних фахівців буде принаймні один із родичів. =", round(((A1 - A2) / A1), 2))
def task4(p1, p2, p3, p4):
    print("\nЗавдання 4:")
    print("Ймовірність того, що цей товар призначений для п’ятого відділу =", round(((1 - (p1 + p2 + p3 + p4))), 2))
def task5(p1, a1):
    print("\nЗавдання 5:")
    print("Ймовірність прибуття двох розбіркових потягів по двох сусідніх коліях =", round((((p1/a1) * ((p1-1)/(a1-1)))), 2))
def task6(p1, p2):
    print("\nЗавдання 6:")
    print("Ймовірність того, що виготовлення виробу першого ґатунку даним станком =", round(((p1 * p2)), 2))
def task7(p1, p2, p3, p4, a1, a2, a3, a4, m, n):
    print("\nЗавдання 7:")
    b = dob_fact(a1, p1, m, n) + dob_fact(a2, p2, m, n) + dob_fact(a3, p3, m, n) + dob_fact(a4, p4, m, n)
    print("Ймовірність того, що цей студент підготовлений: \n\t\tа) відмінно = ", round((dob_fact(a1, p1, m, n) / b), 2))
    print("\t\tб) погано = ", round((dob_fact(a4, p4, m, n) / b), 3))
def task8(p1, p2, p3, a1, a2, a3):
    print("\nЗавдання 8:")
    print("Ймовірність того, що навмання взята деталь стандартна =", round((((p1*a1) + (p2*a2) + (p3*a3))), 2))
def task9(p1, p2, p3, a1, a2, a3):
    print("\nЗавдання 9:") #Формула Байєса
    print("Ймовірність того, що пацієнт був хворий на перитоніт =", round((((p2 * a2)/((p1 * a1) + (p2 * a2) + (p3 * a3)))), 2))
def task10(p1, p2, a1, a2):
    print("\nЗавдання 10:")
    print("Ймовірність того, що прилад зібраний фахівцем високої кваліфікації =", round((((p1 * a1) / ((p1 * a1) + (p2 * a2)))), 2))

task1(40, 26, 22, 12)
task2(10,2,2)
task3(10,8,3)
task4(0.15, 0.25, 0.2, 0.1)
task5(80, 120)
task6(0.9, 0.8)
task7(3, 4, 2, 1, 20, 16, 10, 5, 20, 10)
task8(0.4, 0.3, 0.3, 0.9, 0.95, 0.95)
task9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85)
task10(0.3, 0.7, 0.9, 0.8)