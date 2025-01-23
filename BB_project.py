import random

def introduction():
    """Provides a brief introduction explaining the program."""
    print("Welcome to the Python Q&A Program!")
    print("This program will keep asking you questions until you type 'exit'.")
    print("At the end, it will tell you how many questions you answered.")

def closing_statement(count):
    """Prints a closing statement showing how many questions were answered."""
    print(f"\nYou answered a total of {count} questions. Thanks for participating!")

def ask_questions(questions):
    """Asks a list of questions and allows retry from failure point."""
    count = 0
    index = 0

    while True:
        question, correct_answer = questions[index]
        user_input = input(f"{question} ").strip().lower()

        if user_input == "exit":
            print("Haha, nice try! No escape here. Let's continue.")
            continue  # Force the user to answer

        if user_input != correct_answer.lower():
            print("WRONG! Back to square one, genius.")
            choice = input("Retry or chicken out? ('retry' or 'exit'): ").lower()
            if choice == "exit":
                print("Haha, no escaping! Back to it!")
            else:
                print("Back to it!")
            index = 0  # Restart from the first question
        else:
            index += 1
            count += 1  # Increment the counter

        if index >= len(questions):
            break  # Exit the loop when all questions are answered

    return count

def main():
    """Main function to execute the program logic."""
    introduction()

    easy_questions = [
        ("What color is the sky on a clear day?", "blue"),
        ("How many legs does a spider have?", "8"),
        ("What sound does a dog make? (Hint: Woof!)", "woof"),
        ("What is 1 + 1? (Think really hard!)", "2"),
        ("Which fruit is yellow and monkeys love it?", "banana")
    ]

    simple_programming_questions = [
        ("What is the output of 2 + 2 in Python?", "4"),
        ("Which keyword is used to define a function in Python?", "def"),
        ("What data type is this: [1, 2, 3]?", "list"),
        ("What is the keyword to import libraries in Python?", "import"),
        ("What does 'print()' do? (Hint: It shows stuff)", "display text")
    ]

    # Ask easy questions first
    print("\nAnswer these ridiculously easy questions first:")
    easy_count = ask_questions(easy_questions)

    # Ask programming questions next
    print("\nNow for some simple programming questions:")
    programming_count = ask_questions(simple_programming_questions)

    # Final hard question
    hard_question = "What is the meaning of life, the universe, and everything? (Hint: Just hit Enter and hope!)"
    answer = input(hard_question + " ")
    if answer.strip() == "":
        print("Damn, you got lucky... or you cheated!")
    else:
        print("I don't even know the answer, so I didn’t expect you to know either. Nice try, though!")

    total_count = easy_count + programming_count  # Sum up total questions answered
    closing_statement(total_count)

if __name__ == "__main__":
    main()


