"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three key benefits of object orientation are abstraction, encapsulation,
   and polymorphism. Abstraction refers to the way that object orientation hides
   extraneous detail.

   Instead of writing every line of code needed for a process we'll repeat
   several times, for example, we can give it a name and invoke the method or
   function by name in the future--repeating just the name instead of multiple
   lines of code. The result is code that's easier to read and easier to
   maintain.

   Encapsulation describes the way object-oriented languages keep related data
   and operations together. Methods and attributes can be defined on classes.
   This, too, can make the code easier to scan, and it can help lower the
   likelihood of a variable name conflict arising.

   And polymorphism refers to the interchangeability of components (without the
   need for chains of conditionals)--achieved chiefly through subtyping.


2. What is a class?

   A class is a type (in the sense that e.g., list, str, and int are types). It
   can be used to instantiate objects of its type, and it may define its own
   attributes and methods.

3. What is an instance attribute?

   An instance attribute is the specific case of an attribute exhibited by an
   instance of the object's class.

4. What is a method?

   A method is a function defined on a class. The method can be called on any
   instance of the class; if the class is a parent class, the method will be
   applicable to instances of its subclasses as well.

5. What is an instance in object orientation?

   An instance is an occurrence of its class. It stands in relation to its class
   as, for example, "truck," "bus," and "car" do to "vehicle," or as "apple,"
   "berry," and "cherry" do to "fruit."

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attributes are defined on the class: instance attributes are specific
   to an individual instance. New instances of a class will automatically have
   any attributes defined on their class at the time of their instantiation.
   Afterward, though, these can be replaced by instance attributes, and
   further instance attributes can be added.

   In practice, it's best to avoid setting class attributes. However, you might
   do it if you have some attribute that all instances of your class share when
   they're first created. You might, for example, set a class attribute of
   "sold" that evaluates to False for the class ForSale class. If your inventory
   is at all diverse, you wouldn't want to set "price," for example, as a class
   attribute: it's likely to differ by product, so you'll want to use an
   instance attribute instead.

"""

# Parts 2 through 5:
# Create your classes and class methods

# Part 2

# 1. Student


class Student(object):
    """A person enrolled in a class"""

    def __init__(self, first_name, last_name, address):
        """Initializes attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

# 2. Question


class Question(object):
    """An interrogative statement and its answer."""

    def __init__(self, question, correct_answer):
        """Initializes attributes"""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Evaluates whether answer user supplied is the correct one"""
        print self.question
        entered_answer = raw_input("Enter your answer: ")
        if entered_answer == self.correct_answer:
            return True
        else:
            return False

# 3. Exam


class Exam(object):
    """A series of questions"""

    def __init__(self, name, questions):
        """Initializes attributes"""
        self.questions = []
        self.name = name

    def add_question(self, question, correct_answer):
        """Adds a new question and corresponding answer to the exam"""
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Tabulates score, where each correct answer is worth a point"""
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score = score + 1

        return float(score)


class Quiz(Exam):
    """An exam whose grade is 'pass' or 'fail' instead of a numeric score."""

    def administer(self):
        """Returns True if 50 percent or more of questions were answered
        correctly. Otherwise, returns False."""

        score = super(Quiz, self).administer()
        if score >= 50:
            return True
        else:
            return False


def take_test(exam, student):
    """Creates and grades an exam for a student and displays their score at the
    end."""

    student.score = exam.administer()
    print student.score


def example():
    example_test = Exam("Simple Test", [{'question':
                                         'What is the capital of Alberta?',
                                         'correct_answer': 'Edmonton'},
                                        {'question': 'Who is the author of Python?',
                                         'correct_answer': 'Guido Van Rossum'}
                                        ]
                        )  # Seems like initialization w/"[]" overrides these-^

    example_test.add_question("Who is Ubermelon's competition?", 'Sqysh')
    example_test.add_question("What is Balloonicorn's favorite color?", 'Sparkles')

    amber = Student("Amber", "Staab", "450 Sutter Street")

    take_test(example_test, amber)

example()
