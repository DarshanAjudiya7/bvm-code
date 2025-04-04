
marks1 = float(input("Enter marks for Subject 1 (out of 100): "))
marks2 = float(input("Enter marks for Subject 2 (out of 100): "))
marks3 = float(input("Enter marks for Subject 3 (out of 100): "))


if (0 <= marks1 <= 100) and (0 <= marks2 <= 100) and (0 <= marks3 <= 100):

   
    average = (marks1 + marks2 + marks3) / 3

    
    print(f"\nAverage Marks: {average:.2f}%")

    if average > 90:
        print("🎉 You qualify for a scholarship!")
        print("✅ Eligible for Admission")
    elif average > 75:
        print("✅ Eligible for Admission")
    else:
        print("❌ Not Eligible")
else:
    print("❌ Error: Marks should be between 0 and 100.")

