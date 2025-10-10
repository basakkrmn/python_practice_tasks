# Bir öğrenci not takip sistemi yazın.
# Program öğrenci bilgilerini (ad- soyad, vize notu, final notu) dictionary olarak saklasın.
# Tüm öğrencileri bir liste içinde tutsun.
# Ortalama hesaplayıp geçme/kalma durumunu belirlesin (vize %40, final %60, geçer not 50).
# Tüm öğrencileri ve durumlarını ekrana yazdırsın.

print("---Welcome to the student tracking system--- ")
students_list =[]
students_number =int(input("How many students do you want tp add?: \n"))

for i in range(students_number):
    name = input("Student's name: \n")
    surname = input("Student's surname: \n")
    midterm_grade = int(input("Midterm's grade: \n"))
    final_grade = int(input("Final's grade: \n"))
    student_gpa = (midterm_grade * 0.4) + (final_grade * 0.6)
    student = {"Name": f"{name}",
               "Surname": f"{surname}",
               "Midterm Grade": midterm_grade,
               "Final Grade": final_grade,
               "GPA":student_gpa,
               "Situation": ""}
    if student_gpa >= 50:
        student["Situation"] = "Passed"
    else:
        student["Situation"] = "Failed"

    students_list.append(student)

print(f"{'Name':<10} {'Surname':<10} {'Midterm':<7} {'Final':<6} {'GPA':<5} {'Situation'}")
print("-" * 55)

for student in students_list:
    print(f"{student['Name']:<10} {student['Surname']:<10} "
          f"{student['Midterm Grade']:<7} {student['Final Grade']:<6} "
          f"{student['GPA']:<5.2f} {student['Situation']}")



