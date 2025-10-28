with open('student.txt' , 'w') as file:
    file.write("Rajesh 88\n")
    file.write("Dhanush 92\n")
    file.write("Kalai 79\n")    
    file.write("Deva 85\n")
    file.write("Vijay 95\n")

print("File 'student.txt' created and data written successfully.")

with open('Student.txt', 'r') as file:
    print("\nReading data from 'student.txt':\n")
    for line in file:
        name , marks = line.strip().split()
        marks = int(marks)
        if marks > 80:
            print(f"{name} has scored {marks } is above 801")