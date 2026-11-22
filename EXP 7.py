import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Rohan", 20, "BTech"])
    writer.writerow(["Preeti", 21, "BCA"])
    writer.writerow(["Anshul", 19, "BTech"])

print("CSV file created")
