"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        value = int(input("Enter a number: "))
        finished = True
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
