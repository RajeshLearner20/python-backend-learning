students = ['Rajesh', 'Dhanush', 'Kalai','Deva', 'Vijay']

marks = {'Rajesh': 85, 'Dhanush': 90, 'Kalai': 78, 'Deva': 88, 'Vijay': 92}

highest_scorer = max(marks, key=marks.get)
highest_mark = marks[highest_scorer]

print("Students Mark List")

for name,score in marks.items():
    print(f"{name}: {score}")

print("\nTop Performer")
print(f"The highest scorer is {highest_scorer} with a mark of {highest_mark}.")

