age = 17
if age < 18:
    print("TRUE")
else:
    print("FALSE")

x = 10
y = 20
if x < y and y > 15:
    print("TRUE")
else:
    print("FALSE")

if x < y or y > 50:
    print("TRUE")
else:
    print("FALSE")
marks = 100
if marks < 40:
    print("E ")
elif marks < 50:
    print("D ")
elif marks < 60:
    print("C ")
elif marks < 70:
    print("B")
elif marks < 80:
     print("A")
else:
    print("A+")


bettingnumber = 0
if bettingnumber == 1:
    print("you won a car!!")
elif bettingnumber == 2:
     print("you won a phone!!")
elif bettingnumber == 3:
    print("you won a cow!!")
elif bettingnumber == 4:
    print("you won 4 cows!!")
elif bettingnumber == 5:
     print("you won 10 cows!!")
else:
    print("Please Enter A number From 1 - 5 to BET !!")

weight = 70
height = 1.8
BodyMassIndex = weight / (height * height)
print(BodyMassIndex)

if BodyMassIndex < 18:
    print("Underweight")
elif BodyMassIndex <= 18 :
    print("Normal weight")
elif BodyMassIndex <= 29:
    print("Over Weight")
else:
    print("Obese")

p= 1500
r = 5
t = 3

interest = p * r * t
print(interest/100)
if interest < 2000:
    print("scam")
elif interest < 3000:
    print("bad loan")
else:
    print("good loan")



