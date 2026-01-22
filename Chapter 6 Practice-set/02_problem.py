marks_1 = int(input("Enter marks of subject 1: "))
marks_2 = int(input("Enter marks of subject 2: "))
marks_3 = int(input("Enter marks of subject 3: "))

avg_percentage = (marks_1 + marks_2 + marks_3)/3

if(marks_1 < 33 or marks_2 < 33 or marks_3 < 33):
    print("You have failed in one or more subjects.")
    print(f"Your overall percentage is {avg_percentage}")
    if (avg_percentage < 40):
        print(f'You failed in your examination as your overall percentage is low: {avg_percentage}')

else:
    print("You have passed the examination.")
    print(f"Your percentage {avg_percentage}")