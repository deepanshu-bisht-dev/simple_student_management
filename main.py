student = {
    "Aarav Sharma": 88,
    "Vivaan Singh": 76,
    "Aditya Kumar": 92,
    "Vihaan Gupta": 65,
    "Arjun Yadav": 81,
    "Sai Reddy": 70,
    "Reyansh Mishra": 95,
    "Krishna Pandey": 58,
    "Ishaan Joshi": 73,
    "Shaurya Verma": 89,
    "Atharv Chauhan": 67,
    "Advik Tiwari": 84,
    "Pranav Saxena": 91,
    "Rudra Malik": 62,
    "Kabir Bisht": 78,
    "Ananya Rao": 96,
    "Diya Nair": 71,
    "Saanvi Iyer": 85,
    "Aadhya Patel": 60,
    "Myra Kapoor": 93,
    "Kiara Bhatt": 74,
    "Pari Choudhary": 87,
    "Anika Desai": 69,
    "Navya Menon": 80,
    "Riya Agarwal": 55,
    "Ira Khanna": 90,
    "Siya Thakur": 77,
    "Kavya Bansal": 83,
    "Aarohi Sinha": 66,
    "Avni Chopra": 94
}

while True:
    print("------STUDENT MANAGEMENT------")
    print("1. ADD STUDENT")
    print("2. VIEW STUDENT")
    print("3. CHECK RESULT")
    print("4. EXIT")

    choice = input("Enter your choice : (1,2,3,4)")


    # Add Student
    if choice == "1":
        name = input("Enter student name:")
        marks = int(input("Enter marks:"))
        student[name] = marks
        print(f"{name} successfully added!")

    # View Student
    elif choice == "2":
        for name, marks in student.items():
            print(name, ":", marks)

    # Check Result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student not found!")        
    
    # Exit
    elif choice == "4":
        print("Exited!")
        break

    else:
        print("Invalid inputs...!")