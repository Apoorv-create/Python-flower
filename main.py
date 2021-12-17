from tkinter import *
root = Tk()

root.title("Fibonacci")
root.geometry('400x400')

label_series = Label(root, text = "Fibonacci series")
label_spiral = Label(root)
label_flower = Label(root)

def Fibonacci():
    num = 14
    first_number = 0
    second_number = 1
    counter = 1
    sum = 0

    while(counter <= num):
        label_series['text'] += str(sum) + " "
        counter = counter + 1
        first_number = second_number
        second_number = sum
        sum = first_number + second_number

        label_flower['text'] = "Flower is still blooming"
        label_spiral['text'] = "Spirals in the right direction are " + "Spirals in the left direction are - " + str(second_number) + ".\n Total number of the spirals are:  " + str(sum)

        btn = Button(root, text = "Show Fibonacci series : ", command=Fibonacci)
        btn.pack()

        label_spiral.pack()
        label_flower.pack()
        label_series.pack()