# 1. Ask for student's name
name = input("Enter student name")

# 2. Ask for marks in three subjects
math = float(input("Enter Math marks:"))
english = float(input("Enter English marks:"))
python = float(input("Enter Python marks:"))

# 3. Check invalid marks
if(math < 0 or math > 100 or english < 0 or english > 100 or python < 0 or python > 100):
  print("Invalid marks")
else:
 # 4. Calculate average marks
  average = (math + english + python) / 3

# 5. Determine final grade
if average >= 80:
  grade = "A+"
elif average >= 70:
  grade = "A"
elif average >= 60:
  grade = "A-"
elif average >= 50:
  grade = "B"
elif average >= 40:
  grade = "C"
else:
  grade = "F"

# 6. Display final result
print(f"Student Name: {name}")
print(f"Average Marks: {average:.2f}")
print(f"Final Grade: {grade}")





