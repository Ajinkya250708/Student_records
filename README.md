# Student_records
A Python-based command-line application to manage student records — add, view, search, update, delete, and analyze student data, all stored locally in a CSV file.

# Student Record Manager

👨‍🎓 A Python-based student record management system featuring student registration, record searching, updating, deletion, and class statistics using CSV file handling.

# 👨‍🎓 Student Record Manager

A **Python-based Student Record Management System** that allows users to add, view, search, update, and delete student records. The system also provides basic class statistics such as average, highest, and lowest marks.

Student records are stored locally in a CSV file, allowing the data to remain available even after the program is closed.

## ✨ Features

* 👤 **Add Student**

  * Add multiple student records at once.
  * Store the student's roll number, name, and marks.
  * Records are saved automatically to the CSV file.

* 📋 **Display All Students**

  * View all stored student records in a clean tabular format.
  * Displays roll number, student name, and marks.

* 🔍 **Search Student**

  * Search for a student using their roll number.
  * Displays the complete record when found.

* ✏️ **Update Student**

  * Update an existing student's name.
  * Update the student's marks.
  * Changes are automatically saved to the CSV file.

* 🗑️ **Delete Student**

  * Delete a student record using their roll number.
  * The updated records are saved automatically.

* 📊 **Class Statistics**

  * Display the total number of students.
  * Calculate the average marks.
  * Find the highest marks.
  * Display the highest scorer.
  * Find the lowest marks.
  * Display the lowest scorer.

* 💾 **Persistent Data**

  * Student records are stored in `student_record.csv`.
  * Data remains available when the program is run again.

## 📊 Class Statistics

The statistics section provides a quick overview of the class:

| Statistic | Description |
| --------- | ----------- |
| Total Students | Total number of students in the records |
| Average Marks | Average marks of all students |
| Highest Marks | Highest marks scored |
| Highest Scorer | Student with the highest marks |
| Lowest Marks | Lowest marks scored |
| Lowest Scorer | Student with the lowest marks |

## 🛠️ Technologies Used

* **Python 3**
* `csv` — stores and manages student records
* Functions — organizes different operations
* Loops — handles menus and multiple records
* File Handling — reads and updates the CSV file

## 📁 Project Structure

```text
Student_records/
│
├── student_record.py
├── student_record.csv
├── README.md
└── .gitignore
```

> `student_record.csv` is generated automatically when player data is saved. It does not need to exist before the first run.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ajinkya250708/Student_records.git
```

### 2. Navigate into the project

```bash
cd Student_records
```

### 3. Run the game

```bash
python "student_record.py"
```

Depending on your Python installation, you may need:

```bash
python3 "student_record.py"
```

## 🕹️ Main Menu

When the program starts, you will see:

```text
==============================================
           STUDENT RECORD SYSTEM
==============================================
1. Add Student
2. Display All Students
3. Search Student
4. Update Student
5. Delete Student
6. Class Statistics
7. Exit
==============================================
```

From here, users can manage student records, search for individual students, update information, delete records, or view class statistics.

## 💡 How It Works
The program stores student information in a CSV file in the form of:

```text
Roll Number, Name, Marks
```
When a student is added, their information is written to student_record.csv.

The program can then read the stored records to display, search, update, or delete student information.

The Class Statistics feature reads the marks of all students and calculates the average, highest marks, lowest marks, and corresponding student names.

##  📸 Sample Output

```text
================================================
              STUDENT RECORDS
================================================
R.No      Name                          Marks
------------------------------------------------
101         Bhavya Sehgal                 97.00
102         Harshit Gaur                  44.00
103         Dishit Maheshwari             78.00
================================================

```

## ⚠️ Important Notes

*  This project is designed as a Python learning and portfolio project.
*  Student records are stored locally using CSV file handling.
*  Do not store sensitive or real student information in the repository.
*  The `student_record.csv` file can be added to `.gitignore` if it contains personal data.

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ]  Add student grades and percentage calculation
* [ ]  Add sorting by marks
* [ ]  Add search by name
* [ ]  Add duplicate roll number detection
* [ ]  Improve input validation
* [ ]  Add a graphical user interface (GUI)
* [ ]  Add attendance management
* [ ]  Add more detailed student statistics
* [ ]  Use SQLite for database storage
* [ ]  Add unit tests


## 📜 License

This project is available for educational and personal use.
