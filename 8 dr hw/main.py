ball = int(input('ball kiriting: '))
if ball >= 90 and ball <=100:
    print("5")
elif ball >= 80 and ball <=89:
    print("4")
elif ball >= 70 and ball <=79:
    print("3")
elif ball >=0 and ball <=69:
    print("sizni bahoingiz juda kam")
else:
    print("son kriting")
son1 = int(input("son1 kiriting"))
son2 = int(input("son2 kiriting"))
son3 = int(input("son3 kiriting"))
result = max(son1,son2,son3)
print(result)