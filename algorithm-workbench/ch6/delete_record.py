# A file exists on the disk named students.txt
# The file contains several records, and each record
# contains two fields: student's name and final exam score
# Write code that deletes the record containing
# "John Perz" as the student name

def main():

    # Create a bool variable to use as a flag
    found = False

    # Get the student to delete
    search = input('What is the Student\'s name? ')

    # Open original students.txt file
    students_file = open('students.txt', 'r')

    # Open temporary file
    temp_file = open('temp.txt', 'w')

    # Read the first record's name field
    name = students_file.readline()

    # Read rest of the file
    while name != '':
        # Read grade field
        grade = float(students_file.readline())

        # If this is not record to delete, write to temp file
        if name != search:
            # Write record to temp file
            temp_file.write(name + '\n')
            temp_file.write(str(grade) + '\n')
        else:
            # Set flag to true
            found = True

        # Read
    temp = file.read
