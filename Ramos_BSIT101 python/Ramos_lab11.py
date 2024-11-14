scores = []
passar = []

while True:
    grade = input ("Enter a grade (or stop to quit): ")
    
    if grade.lower()== 'stop':
        break
    elif not grade.isdigit():
        print("Invalid input. Please enter a number or stop to quit.")
    else:
        grade = int(grade)
        if (grade <= 40):
            print("Must be a typo")
            continue
        elif(grade >= 101):
            print("Must be a typo")
            continue
        scores.append(grade)
        if grade >= 75:
            passar.append(grade)
        
if scores:
    average = sum(scores) / len(scores)
    passedgrades = (len(passar)/ len(scores)) * 100
    print(f"Average score: {average:.2f}")
    print(f"Percentage of passed grades: {passedgrades:.2f}%")
    print(f"The student who have passed: {len(passar)} ")
    print(f"grades: {passar:} ")
else:
    print("where are the grades?")

