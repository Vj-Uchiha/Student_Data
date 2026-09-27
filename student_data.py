# PART 1: Create a dictionary of student records

student_data = {
    "id1": {
        "name": "Sara",
        "class": "V",
        "subject": "english, math, science"
    },
    "id2": {
        "name": "David",
        "class": "V",
        "subject": "english, math, science"
    },
    "id3": {
        "name": "Sara",
        "class": "V",
        "subject": "english, math, science"
    },
    "id4": {
        "name": "Surya",
        "class": "V",
        "subject": "english, coding, math"
    }
}


# PART 2: Display the original dictionary

print("===== ORIGINAL STUDENT RECORDS =====")
print(student_data)


# PART 3: Access values safely using get()

print("")
print("===== ACCESSING STUDENT RECORDS =====")

print("Details of id1:")
print(student_data.get("id1", "Not Found"))

print("")

print("Details of id5:")
print(student_data.get("id5", "Not Found"))


# PART 4: Add a new student record

student_data["id5"] = {
    "name": "Anaya",
    "class": "V",
    "subject": "english, art, science"
}

print("")
print("===== AFTER ADDING id5 =====")
print(student_data)


# PART 5: Update an existing student record

student_data["id2"]["subject"] = "english, math, coding"

print("")
print("===== AFTER UPDATING id2 SUBJECT =====")
print(student_data["id2"])


# PART 6: Remove duplicate records

cleaned_data = {}
seen_records = []

for student_id, details in student_data.items():

    # Create a combination of name, class and subject
    unique_key = (
        details["name"],
        details["class"],
        details["subject"]
    )

    # Keep only the first occurrence
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details

# Replace the original dictionary
student_data = cleaned_data

print("")
print("===== AFTER REMOVING DUPLICATE RECORDS =====")
print(student_data)


# PART 7: Remove id4 using pop()

removed_student = student_data.pop("id4", "Student not found")

print("")
print("===== REMOVED STUDENT =====")
print(removed_student)


# PART 8: Check the number of records

print("")
print("===== TOTAL STUDENT RECORDS =====")
print("Total student records left:", len(student_data))


# PART 9: Iterate through the final dictionary

print("")
print("===== FINAL STUDENT SUBJECT RECORDS =====")

for student_id, details in student_data.items():
    print(student_id, ":", details)

print("==========================================")
