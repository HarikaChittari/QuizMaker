# This file includes the 'reset DB' function (reset the DB before importing data)
# This file reads a .CSV file and writes it to a .sqlite file

# Import packages
import DBbase as db
import csv


# Object class ->   QuizQuestions
class QuizQuestions:
    def __init__(self, row):
        """sets the columns for the "QuizQuestions" table"""
        self.q_id = row[0]
        self.question = row[2]


# PObject class ->   QuizAnswers
class QuizAnswers:
    def __init__(self, row):
        """sets the columns for the "QuizAnswers" table"""
        self.q_id = row[1]
        self.correct_answer = row[3]
        self.incorrect_answer_1 = row[4]
        self.incorrect_answer_2 = row[5]
        self.incorrect_answer_3 = row[6]


# Object class -> ClassDetails
class ClassDetails:
    # Username, Password
    def __init__(self, row):
        """sets the columns for the "ClassDetails" table"""
        self.id = row[0]
        self.student_id = row[1]
        self.password = row[2]


# This class specifically takes CSV and converts to sqlite
# We took this approach to make sure the files are clean and understandable

class CsvToSqlite(db.DBbase):

    def reset_database(self):
        try:
            sql = """
            DROP TABLE IF EXISTS QuizQuestions;
            DROP TABLE IF EXISTS QuizAnswers;
            DROP TABLE IF EXISTS ClassDetails;
            CREATE TABLE QuizQuestions (
                q_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                question text);
            CREATE TABLE QuizAnswers (
                    a_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    q_id INTEGER NOT NULL UNIQUE,
                    correct_answer text,
                    incorrect_answer_1 text,
                    incorrect_answer_2 text,
                    incorrect_answer_3 text);
                    
            CREATE TABLE ClassDetails(
                    id INTEGER PRIMARY KEY,
                    student_id TEXT UNIQUE,
                    password TEXT);
            
            """
            self.execute_script(sql)
        except Exception as ex:
            print("An error occurred in 'reset_database'.", ex)

    def read_data(self, file_name, data_class):
        self.data_list = []  # Empty list to be populated with data

        try:
            with open(file_name, "r") as records:
                csv_reader = csv.reader(records)
                next(records)  # Skips the first row of the CSV with the headers
                for row in csv_reader:  # Goes through the CSV file and parses the data
                    data = data_class(row)
                    self.data_list.append(data)
        except Exception as ex:
            print("An error occurred in 'read_data'.", ex)

        return self.data_list

    def save_to_database(self, data_list, table_name):
        print("Number of records to save: ", len(self.data_list))
        save = input("Continue? Type 'y' to continue, otherwise type 'n': ").lower()
        if save == "y":
            for item in self.data_list:
                # Inserts data into the DB using key/value pairs and SQL syntax
                try:
                    columns = ", ".join(item.__dict__.keys())
                    placeholders = ", ".join(["?" for _ in item.__dict__.values()])
                    values = tuple(item.__dict__.values())
                    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                    self.get_cursor.execute(query, values)
                    self.get_connection.commit()
                    print(f"Saved item {values} to {table_name}")
                except Exception as ex:
                    print("An error occurred in 'save_to_database'.", ex)
        else:
            print("Export to DB aborted.")


# Calls the CsvToSqlite class and uses the specified .sqlite file
quiz_questions_and_answers = CsvToSqlite("quiz_maker.sqlite")

# Imports and saves data to the "QuizQuestions" table
questions_list = quiz_questions_and_answers.read_data("quiz_questions.csv", QuizQuestions)
quiz_questions_and_answers.save_to_database(questions_list, "QuizQuestions")

# Imports and saves data to the "QuizAnswers" table
answers_list = quiz_questions_and_answers.read_data("quiz_questions.csv", QuizAnswers)
quiz_questions_and_answers.save_to_database(answers_list, "QuizAnswers")

# Imports and saves data to the "ClassDetails" table
class_details_list = quiz_questions_and_answers.read_data("Class_Details.csv", ClassDetails)
quiz_questions_and_answers.save_to_database(class_details_list, "ClassDetails")
