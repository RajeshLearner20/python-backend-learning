class InvalidAgeError(Exception):
    pass

def voters(age):
    if age<18:
        raise InvalidAgeError("Not Eligible for vote! ")

    else:
        print("you are eligible for vote")

try:
    age = int(input("Enter your age:"))
    voters(age)

except InvalidAgeError as e:
    print(e)

except ValueError:
    print("Please enter a valid numbers")
        
