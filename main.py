# Imports all from Tkinter GUI package
from tkinter import *

# Initialization
app = Tk()
weight = IntVar(None)
he = IntVar(None)
b = IntVar(None)
age = IntVar(None)
gender = IntVar(None)

# Calculates the BMI with user-given data and puts user in one of three categories
# Also checks if entered value for height is not zero
def calculate_bmi():
    try:
        re = float(weight.get()) / (float(height.get()) * float(height.get()))
        b.set(re)
    except ZeroDivisionError:
        weight.set(None)
        he.set(None)
        b.set(None)
        return
    if re <= 18.4:
      resLabelText.set ("You are underweight.")
    elif re <= 24.9:
         resLabelText.set("You are healthy.")
    elif re <= 29.9:
          resLabelText.set("You are over weight.")
    elif re <= 34.9:
           resLabelText.set("You are severely over weight.")
    elif re <= 39.9:
          resLabelText.set("You are obese.")
    else:
         resLabelText.set("You are severely obese.")


    return


# Sets size and title
app.geometry("400x400")
app.title("Ideal Body Mass Index")
app.config(bg = "blue")

# Label and text
ageLabelText = StringVar()
ageLabelText.set("Enter your age: ")
massLabel = Label(app, textvariable=ageLabelText)
massLabel.pack()

mass = Entry(app, textvariable= age)
mass.pack()

genderLabelText = StringVar()
genderLabelText.set("Enter your gender: ")
massLabel = Label(app, textvariable=genderLabelText)
massLabel.pack()

mass = Entry(app, textvariable= gender)
mass.pack()

mLabelText = StringVar()
mLabelText.set("Enter your weight in kg: ")
massLabel = Label(app, textvariable=mLabelText)
massLabel.pack()

mass = Entry(app, textvariable=weight)
mass.pack()

# Label and text box for height
hLabelText = StringVar()
hLabelText.set("Enter your height in m: ")
heightLabel = Label(app, textvariable=hLabelText)
heightLabel.pack()

height = Entry(app, textvariable=he)
height.pack()

# Button and label and textbox for BMI calculation
button = Button(app, text="Calculate BMI", command=calculate_bmi)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Your BMI is: ")
bmiLabel = Label(app, textvariable=bmiLabelText)
bmiLabel.pack()

bmi = Entry(app, textvariable=b)
bmi.pack()
resLabelText = StringVar()
resLabelText.set(" and you are categorised as: ")
resLabel = Label(app, textvariable=resLabelText)
resLabel.pack()

# Starts the GUI
app.mainloop()
