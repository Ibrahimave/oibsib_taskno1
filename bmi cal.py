weight = float(input("enter your weight in kg:"))
height = float(input("enter your height in cm"))

height_in_meters = height / 100
bmi = weight / (height_in_meters**2)

print("your BMI is:", bmi)

if bmi < 19.5:
  print("you're underweight")
elif 19.5 <= bmi < 25:
  print("you're a normal weight")
elif 25 <= bmi < 30:
  print("you're overweight")
else:
  print("you're obese")
