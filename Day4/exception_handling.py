try:
    f = open("Student_details.txt","r")
    print(f.read())

except FileNotFoundError:
    print("File not found!")

else:
    print("File read successfully")

finally:
    print("Process Completed!")
    
