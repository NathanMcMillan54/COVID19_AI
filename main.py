from datetime import date
import os
import cv2


def lookForFace():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_defualt.xml')

    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            askQuestion()
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('Look for human face', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()


currentDate = date.today()


def askQuestion():
    # ask person questions
    print("Type in lowercase")
    question = input("Have you been in contact with anybody who has COVID19? ")

    # ask person question
    if question == 'yes':
        ask4Symptoms()
    elif question == 'ya':
        ask4Symptoms()
    elif question == 'i dont know':
        ask4Symptoms()
    elif question == 'no':
        print("Good")
    elif question == 'check-for-&-update':
        confirm = input("Confirm: ")
        if confirm == "01111001 01100101 01110011":
            os.system('git pull')
            exit()
        else:
            print("Incorrect confirmation code")
            exit()
    else:
        print("Enter yes or no")
        askQuestion()


# talk about how flu and COVID19 symptoms are similar
def talkAboutFlu():
    print("COVID19 symptoms are similar to flu symptoms, you should also get tested for the flu.")
    exit()


# ask if a person has COVID19 symptoms
def possiblePositiveCase():
    pPC = open("possiblePositiveCase.txt", "r+")
    pPC.read()
    lines = ["\nA positive case"]
    pPC.writelines(currentDate.strftime("%d/%m/%Y"))
    pPC.writelines(lines)
    pPC.read()
    exit()


def possibleNegativeCase():
    pNC = open("possibleNegativeCase.txt", "r+")
    pNC.read()
    lines = ["\nA negative case"]
    pNC.writelines(currentDate.strftime("%d/%m/%Y"))
    pNC.writelines(lines)
    pNC.read()
    exit()


def ask4Symptoms():
    symptoms = input("Have you had difficulty breathing, or had a fever? ")
    if symptoms == 'yes':
        print("Get tested or quarantine")
        possiblePositiveCase()
        talkAboutFlu()
    elif symptoms == 'ya':
        print("Get tested or quarantine")
        possiblePositiveCase()
        talkAboutFlu()
    elif symptoms == 'no':
        print("Ok, you probably don't need to be tested")
        possibleNegativeCase()
    else:
        print("Enter yes or no")
        ask4Symptoms()


lookForFace()
