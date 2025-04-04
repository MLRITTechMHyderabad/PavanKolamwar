def avg(students):
    avg=0
    for name, marks in students:
        average_marks = sum(marks) / len(marks)
        print(f"{name}'s average marks: {average_marks:.2f}")
        
        if average_marks>avg:
            top=name
            avg=average_marks
    print(f"{top}is highest avg grade: {avg:.2f}")
    
    #for student in students:
     #   print(student['alice'])
    
        
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]
name="Alice"
print(avg(students))      