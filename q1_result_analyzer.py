# Analyze student result
def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    # grades
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
      
    # failed subs >40 in marks
    below_40 = []
    for i, mark in enumerate(marks):#marks >40 returns a list 
        if mark < 40:
            below_40.append(f"Subject {i + 1}")

    # print output 
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average:.2f}")#formats like total:300.0 ,average: 40.00
    print(f"Grade: {grade}")

    if below_40:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("No subjects below 40")

#my data
name = "Yashwanth"
roll = 156
marks = [81.5, 35.0, 39.0, 92.5, 79.0]

# call function
analyze_result(name, roll, marks)

analyze_result('Hari', 123, [20.0,40.0,50.0,39.0,29.0])
