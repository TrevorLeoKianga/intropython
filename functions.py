import email


def motto():
    print("this is our motto")


motto()
motto()
motto()


def vision():
    print("this s who we are")


vision()
vision()


def add():
    x = 15
    y = 30
    z = x + y
    print(z)


add()
add()
add()


def average(x, y, z):
    avg = (x + y + z) / 3
    print("your average is " + str(average))


def bmiCalc(weight, height):
    bmi = weight / pow(height, 2)
    if bmi < 18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal weight")
    elif bmi <= 34:
        print("Over Weight")
    else:
        print("Obese")


bmiCalc(65, 1.5)


def gradingsystem(marks):
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
        print("A++++++++++++++++++++++++++++++++")


gradingsystem(97)


def login(email, password):
    if user@example.com == email:
        print("correct")
    elif user123 == password:
        print("correct")
    else:
        print("incorrect")

login(email, password)
