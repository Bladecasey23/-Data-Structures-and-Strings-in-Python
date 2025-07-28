dict = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}
name = input("Enter the students name: ")
if name in dict.keys():
    print(f"{name} marks: ", dict[name])
else:
    print("students name doesn't exist")