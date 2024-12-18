# QuizQuestions/QuizAnswers CRUD Operations, Main Menu, and Quiz file
import self

import DBbase as db
import random


# quiz questions class  inherits  the 'DBbase' class
# We are using CRUD operations in our QUIZ MAKER project and used Exception Handling where ever possible
class QuizQuestions(db.DBbase):

    def __init__(self):
        """Constructor which tells what the DB name is"""
        super().__init__("quiz_maker.sqlite")

    def add_question(self, question):
        """ 'Create ': Inserts new values into the DB"""
        try:
            # 'INSERT' statement
            super().get_cursor.execute("INSERT or IGNORE INTO QuizQuestions (question) values(?);", (question,))
            # Commits changes to the DB, as long as no errors are produced
            super().get_connection.commit()
            # print statement
            print(f"Added {question} successfully.")
        except Exception as e:
            print("An error has occurred in 'QuizQuestions, add_question'.", e)

    def fetch_question(self, q_id=None, q_name=None):
        """ 'Read': Fetch values from the DB"""
        try:
            # Checks if q_id is not None; if it is not none then all records are fetched
            if q_id is not None:
                # SELECT * statement with 'fetchone' at the end
                return super().get_cursor.execute("SELECT * FROM QuizQuestions WHERE q_id = ?", (q_id,)).fetchone()
            elif q_name is not None:
                # SELECT * statement with 'fetchone' at the end which fetches specific question
                return super().get_cursor.execute("SELECT * FROM QuizQuestions WHERE question = ?",
                                                  (q_name,)).fetchone()
            else:
                # SELECT * statement with 'fetchall' at the end which fetches all the quiz questions
                return super().get_cursor.execute("SELECT * FROM QuizQuestions").fetchall()
        except Exception as e:
            print("An error has occurred in 'QuizQuestions, fetch_question'.", e)

    def update_question(self, q_id, question):
        """ 'Update': updates two parameters; the Primary Key and the question"""
        try:
            # 'execute' method takes the variables and replaces the SQL syntax question marks
            super().get_cursor.execute("UPDATE QuizQuestions SET question = ? WHERE q_id = ?;", (question, q_id))
            # Commits changes to the DB, as long as no errors are produced
            super().get_connection.commit()
            # print statement
            print(f"Updated record to {question} successfully.")
        except Exception as e:
            print("An error has occurred in 'QuizQuestions, update_question'.", e)

    def delete_question(self, q_id):
        """ 'Delete': deletes values from the DB"""
        try:
            # Delete statement
            super().get_cursor.execute("DELETE FROM QuizQuestions WHERE q_id = ?;", (q_id,))
            # Commits changes to the DB, as long as no errors are produced
            super().get_connection.commit()
            # print statement
            print(f"Deleted question ID {q_id} successfully.")
            return True
        except Exception as e:
            print("An error has occurred in 'QuizQuestions, delete_question'.", e)
            return False

    # ---------------------------------------------------------------------------------------------------

    def reset_database(self):
        """function that resets the 'QuizQuestions' table"""
        try:
            # Builds out the SQL code to DROP (if exists) and CREATE a table
            sql = """
            DROP TABLE IF EXISTS QuizQuestions;
            CREATE TABLE QuizQuestions (
                q_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                question text);
                        """
            # Executes the SQL syntax
            super().execute_script(sql)
            print("QuizQuestions table successfully created.")
        except Exception as e:
            print("An error occurred in 'QuizQuestions, reset_database'.", e)
        # 'finally' that accesses the super() and closes out the DB
        finally:
            super().close_db()


class ClassDetails(db.DBbase):
    # Username, Password
    def __init__(self):
        """Constructor which tells what the DB name is"""
        super().__init__("quiz_maker.sqlite")

    def add_student_details(self, id, student_id, password):
        """ 'Create ': Inserts new values into the DB"""
        try:
            # 'INSERT' statement
            super().get_cursor.execute("""INSERT INTO ClassDetails
                        (id, student_id, password)
                            VALUES(?, ?, ?)""",
                                       (id, student_id, password))
            # print("Saved student to class: ", .student_id)
            # Commits changes to the DB, as long as no errors are produced
            super().get_connection.commit()
            # print statement
            print(f"Added {id, student_id, password} successfully.")
        except Exception as e:
            print("An error has occurred in 'Student Details, add_studentDetails'.", e)

    def fetch_student_details(self, id=None, student_id=None, password=None):
        """ 'Read': Fetch student values from the DB"""
        try:
            # Checks if student_id is not None; if it is not none then all records are fetched
            if id is not None:
                # SELECT * statement with 'fetchone' at the end
                return (super().get_cursor.execute("SELECT * FROM ClassDetails WHERE id = ?",
                                                   (id,)) .fetchone())
            elif student_id is not None:
                # SELECT * statement with 'fetchone' at the end which fetches specific question
                return super().get_cursor.execute("SELECT * FROM ClassDetails WHERE student_id = ?",
                                                  (student_id,)).fetchone()
            else:
                # SELECT * statement with 'fetchall' at the end which fetches all the quiz questions
                return super().get_cursor.execute("SELECT * FROM ClassDetails").fetchall()
        except Exception as e:
            print("An error has occurred in 'ClassDetails, fetch_student_details'.", e)

    def update_student_details(self, id, student_id, password):
        """ 'Update': updates two parameters; the Primary Key and the student_id"""
        try:
            # 'execute' method takes the variables and replaces the SQL syntax question marks
            super().get_cursor.execute("UPDATE ClassDetails SET student_id = ?, password = ? WHERE id = ?;",
                                       (student_id, password, id))
            # Commits changes to the DB, as long as no errors are produced
            super().get_connection.commit()
            # print statement
            print(f"Updated detail record to {student_id} successfully.")
            return True
        except Exception as e:
            print("An error has occurred in 'ClassDetails, update_student_details'.", e)
            return False

    def delete_student_details(self, id):
        """ 'Delete': deletes values from the DB"""
        try:
            # Delete statement
            super().get_cursor.execute("DELETE FROM ClassDetails WHERE id = ?;", (id,))
            # Commits changes to the DB, as long as no errors are produced
            super().get_connection.commit()
            # print statement
            print(f"Deleted question ID {id} successfully.")
            return True
        except Exception as e:
            print("An error has occurred in 'ClassDetails, delete_student_details'.", e)
            return False

    def reset_database(self):
        """function that resets the 'ClassDetails' table"""
        try:
            # Builds out the SQL code to DROP (if exists) and CREATE a table
            sql = """
                DROP TABLE IF EXISTS ClassDetails;
                CREATE TABLE ClassDetails(
                    id INTEGER PRIMARY KEY,
                    student_id TEXT UNIQUE,
                    password TEXT
                );"""

            # Executes the SQL syntax
            super().execute_script(sql)
            print("ClassDetails table successfully created.")
        except Exception as e:
            print("An error occurred in 'ClassDetails, reset_database'.", e)
        # 'finally' that accesses the super() and closes out the DB
        finally:
            super().close_db()


# 'QuizAnswers' class that inherits from the 'QuizQuestions' class
class QuizAnswers(QuizQuestions):
    def add_q_and_a(self, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3):
        """ 'C': adds new values into the DB"""
        try:
            # Adds the name of an item first from the 'QuizQuestions' table
            super().add_question(question)
        except Exception as e:
            print("An error occurred in 'QuizAnswers, add_q_and_a'-1.", e)
        # runs if no errors occur
        else:
            try:
                # gets the PK that was added. The 'fetch passes' in the ID or the question name, in this case we
                # don't know the q_id
                q_id = super().fetch_question(q_name=question)[0]
                # if the q_id exists in the DB
                if q_id is not None:
                    super().get_cursor.execute("""INSERT INTO QuizAnswers (q_id, correct_answer, incorrect_answer_1, 
                    incorrect_answer_2, incorrect_answer_3) VALUES(?,?,?,?,?);""", (
                        q_id, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3))
                    super().get_connection.commit()
                    print(f"QuizAnswers {question} added successfully")
                # if q_id is NOT Non
                else:
                    raise Exception("The id of the question name was not found.")
            except Exception as e:
                print("An error occurred in 'QuizAnswers, add_q_and_a'-2.", e)

    def fetch_answer(self, a_id=None):
        """ 'R': selects values from the DB"""
        try:
            if a_id is not None:
                # JOIN between 'QuizQuestions' and 'QuizAnswers' tables syntax
                ret_val = super().get_cursor.execute("""SELECT QuizAnswers.a_id, QuizAnswers.q_id, qq.question, 
                correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3 FROM QuizAnswers JOIN 
                QuizQuestions qq on QuizAnswers.q_id = qq.q_id WHERE QuizAnswers.a_id = ?;""", (a_id,)).fetchone()
                return ret_val
            else:
                return super().get_cursor.execute("""SELECT QuizAnswers.a_id, QuizAnswers.q_id, qq.question, 
                correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3 FROM QuizAnswers JOIN 
                QuizQuestions qq on QuizAnswers.q_id = qq.q_id;""").fetchall()
        except Exception as e:
            print("An error occurred in 'QuizAnswers, fetch_answer'.", e)

    def update_answer(self, a_id, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3):
        """ 'U': updates two parameters; the PK and the question"""
        try:
            super().get_cursor.execute(
                """UPDATE QuizAnswers SET correct_answer = ?, incorrect_answer_1 = ?, incorrect_answer_2 = ?, 
                incorrect_answer_3 = ? WHERE a_id = ?;""",
                (correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3, a_id))
            super().get_connection.commit()
            print(f"Updated QuizAnswers record {a_id} successfully.")
            # to indicate that things went well
            return True
        except Exception as e:
            print("An error occurred in 'QuizAnswers, update_answer'.", e)
            return False

    def delete_q_and_a(self, a_id):
        """ 'D': deletes values from the DB"""
        pass
        try:
            # Invoke fetch
            q_id = self.fetch_answer(a_id)[1]
            if q_id is not None:
                return_status = super().delete_question(q_id)
                super().get_connection.commit()
                if return_status is False:
                    raise Exception("Delete method in Questions failed. Delete aborted.")

        except Exception as e:
            print("An error occurred.", e)
        else:
            try:
                super().get_cursor.execute("""DELETE FROM QuizAnswers WHERE a_id = ?;""", (a_id,))
                super().get_connection.commit()
                print(f"Deleted answer ID {a_id} successfully.")
            except Exception as e:
                print("An error occurred 'QuizAnswers, delete_q_and_a'.", e)

    # ------------------END OF CRUD OPERATIONS------------------

    def reset_database(self):
        """Function that resets the 'QuizAnswers' table"""

        try:
            # Builds out the SQL code to DROP (if exists) and CREATE a table
            sql = """
                DROP TABLE IF EXISTS QuizAnswers;

                CREATE TABLE QuizAnswers (
                    a_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    q_id INTEGER NOT NULL UNIQUE,
                    correct_answer text,
                    incorrect_answer_1 text,
                    incorrect_answer_2 text,
                    incorrect_answer_3 text);
            """
            # Executes the SQL syntax
            super().execute_script(sql)
            print("QuizAnswers table successfully created.")

        except Exception as e:
            print("An error occurred in 'QuizAnswers, reset_database'.", e)
        # 'finally' that accesses the super() and closes out the DB
        finally:
            super().close_db()


# a class for raising an exception when the user selects '2' in the quiz menu. This allows the program to exit the
# quiz menu and return to the program's main menu
class ReturnToMainMenuException(Exception):
    pass


def quiz(self):
    """Quiz function that prompts the user in a sub-menu, randomly selects questions from the 'quiz_question'
    database, quizzes the user, provides a score and grade once the quiz is completed, then prompts the user to
    re-take another quiz or return to the main menu """

    quiz_answers = QuizAnswers()
    return_to_menu = False  # Flag to control whether to return to the main menu

    while True:
        print("\nQuiz Menu")
        print("1. Take Quiz")
        print("2. Return to the main menu")
        choice = input("Select an option: ")

        if choice == "1":
            # Get a random question from the database
            student_id = str(input("Student ID: "))
            password = str(input("Password: "))

            # Check if student exists in the database
            class_details = ClassDetails()
            class_details.get_cursor.execute("SELECT id FROM ClassDetails WHERE student_id = ? AND password = ?",
                                             (student_id, password))
            result = class_details.get_cursor.fetchone()
            if result is None:
                print("Invalid username or password. Quiz aborted.")
                return
            print("The Student Details are valid . Quiz will start now.")
            question_data = quiz_answers.fetch_answer()  # Modify this to get a random question

            if not question_data:
                print("No questions available for the quiz.")
                continue

            score = 0
            total_questions = len(question_data)

            for random_question in question_data:
                # Extract question and answer information
                a_id, q_id, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3 = random_question

                print("\nQuestion:")
                print(question)

                # Present answer choices (you can randomize the order)
                answer_choices = [correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3]
                random.shuffle(answer_choices)

                for i, choice in enumerate(answer_choices):
                    print(f"{i + 1}. {choice}")

                while True:
                    user_choice = input("Select the correct answer (1-4) or type 'exit' to exit: ")

                    if user_choice.lower() == "exit":
                        print("Exiting the quiz.")
                        return_to_menu = True  # Set the flag to return to the main menu
                        break  # Exit the quiz

                    if user_choice.isdigit():
                        user_choice = int(user_choice)
                        if 1 <= user_choice <= 4:
                            break
                    print("Invalid input. Please enter a number between 1 and 4.")

                if return_to_menu:
                    break

                if answer_choices[user_choice - 1] == correct_answer:
                    score += 1

                    # Calculate the percentage and grade
                    score_percentage = (score / total_questions) * 100

                    if score_percentage >= 90:
                        grade = "A"
                    elif score_percentage >= 80:
                        grade = "B"
                    elif score_percentage >= 70:
                        grade = "C"
                    elif score_percentage >= 60:
                        grade = "D"
                    else:
                        grade = "F"

            # Display the final score and grade
            print(
                f"\nQuiz completed! You got {score}/{total_questions} questions right. Your score is {score_percentage:.2f}%")
            print(f"Your grade is: {grade}")
            print("Now returning to the quiz menu.")

        elif choice == "2":
            raise ReturnToMainMenuException

    return return_to_menu


# 'Menu' class for an interactive menu
class Menu:

    def run(self):

        """Function for an interactive menu """
        # Dictionary for menu options
        menu_options = {"quiz": "Run the quiz program",
                        "get": "Get all quiz questions and answers and also Class Details",
                        "get_student": "Get all Class Details",
                        "getby": "Get quiz answer by answer ID and Class Details by Id",
                        "update": "Update quiz answers and also class details",
                        "add": "Add a quiz question and answers",
                        "add_student": "Add a Student Details",
                        "delete": "Delete a quiz question and answers",
                        "delete_student": "Delete student details",
                        "reset": "Reset database",
                        "exit": "Exit program"
                        }
        # print statement for a welcome
        print("Welcome to the Quiz program, please choose a selection")
        # empty variable
        user_selection = ""
        # While loop for accepting the user's input
        while user_selection != "exit":
            print("*** Option List ***")
            # for loop for printing the menu options
            for option in menu_options.items():
                print(option)

            user_selection = input("Select an option: ").lower()
            # Create an instance of the inventory
            quiz_answers = QuizAnswers()
            class_Details = ClassDetails()

            # if/else statements for user dictionary selections that will utilize 'fetch'
            if user_selection == "quiz":
                try:
                    quiz(self)
                except ReturnToMainMenuException:
                    pass

            elif user_selection == "get":
                results = quiz_answers.fetch_answer()
                for item in results:
                    print(item)
                input("Press return to continue.\n")

            elif user_selection == "get_student":
                results_class_details = class_Details.fetch_student_details()
                for item in results_class_details:
                    print(item)
                input("Press return to continue.\n")

            elif user_selection == "getby":
                a_id = input("Enter quiz answer ID: ")
                results = quiz_answers.fetch_answer(a_id)

                s_id = input("Enter the Student ID: ")
                student_results = class_Details.fetch_student_details(s_id)
                print(student_results)
                print(results)
                input("Press return to continue.\n")

            elif user_selection == "update":
                results = quiz_answers.fetch_answer()
                result_student_details = class_Details.fetch_student_details()

                for item in results:
                    print(item)
                a_id = input("Enter quiz answer ID: ")
                correct_answer = input("Enter correct answer: ")
                incorrect_answer_1 = input("Enter first incorrect answer: ")
                incorrect_answer_2 = input("Enter second incorrect answer: ")
                incorrect_answer_3 = input("Enter third incorrect answer: ")
                quiz_answers.update_answer(a_id, correct_answer, incorrect_answer_1, incorrect_answer_2,
                                           incorrect_answer_3)

                for item in result_student_details:
                    print(item)
                id = input("Enter the ID")
                s_id = input("Enter Student ID: ")
                password = input("Enter password: ")

                class_Details.update_student_details(id, s_id, password)
                print(class_Details.fetch_student_details(s_id))

                print(quiz_answers.fetch_answer(a_id))
                input("Press return to continue.\n")


            elif user_selection == "add":
                question = input("Enter question: ")
                correct_answer = input("Enter correct answer: ")
                incorrect_answer_1 = input("Enter first incorrect answer: ")
                incorrect_answer_2 = input("Enter second incorrect answer: ")
                incorrect_answer_3 = input("Enter third incorrect answer: ")
                quiz_answers.add_q_and_a(question, correct_answer, incorrect_answer_1, incorrect_answer_2,
                                         incorrect_answer_3)
                print("Done\n")
                input("Press return to continue.\n")

            elif user_selection == "add_student":
                id = input("Enter Unique Id: ")
                s_id = input("Enter student Id: ")
                password = input("Enter password: ")
                class_Details.add_student_details(id, s_id, password)
                print("Done\n")
                input("Press return to continue.\n")

            elif user_selection == "delete":
                a_id = input("Enter quiz answer ID: ")
                quiz_answers.delete_q_and_a(a_id)
                print("Done\n")
                input("Press return to continue.\n")

            elif user_selection == "delete_student":
                id = input("Enter student ID: ")
                class_Details.delete_student_details(id)
                print("Done\n")
                input("Press return to continue.\n")

            elif user_selection == "reset":
                confirm = input(
                    "This will delete all records in quiz_Questions and quiz_answers and student details; continue? (y/n) ").lower()
                if confirm == "y":
                    quiz_answers.reset_database()
                    classDetails = ClassDetails()
                    classDetails.reset_database()
                    questions = QuizQuestions()
                    questions.reset_database()
                    print("Reset complete.")
                    input("Press return to continue.\n")
                else:
                    print("Reset aborted.\n")
                    input("Press return to continue.\n")
            else:
                if user_selection != "exit":
                    print("Invalid selection, please try again.\n")


Menu.run(self)
