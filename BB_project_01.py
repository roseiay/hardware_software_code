print("Welcome to the Educational Background Program!")
print("This program will ask you about your educational background and summarize your responses.\n")

# Start by asking the user's name
name = input("Let's start with your name. What is your name? ")

# Ask if the user attended high school
attended_high_school = input(f"Hi {name}, did you attend high school? (yes/no): ").strip().lower()

if attended_high_school == "yes":
    # If yes, ask for the high school name
    high_school = input("What is the name of the high school you attended? ")
else:
    # If no, ask if they earned a GED instead
    got_ged = input("Did you earn a GED instead? (yes/no): ").strip().lower()
    if got_ged == "yes":
        high_school = "Earned a GED"
    else:
        # If neither high school nor GED, note it and provide encouragement
        high_school = "Did not attend high school or earn a GED"
        print("That's okay! There are many paths to success, and it's never too late to pursue your goals.")

# Ask if the user attended college
attended_college = input("Did you attend college? (yes/no): ").strip().lower()

if attended_college == "yes":
    # If yes, ask for the college name
    college = input("What is the name of the college you attended? ")
else:
    # If no, note it and provide encouragement
    college = "Did not attend college"
    print("That's completely fine! College isn't the only way to learn or succeed.")

# Summarize the user's responses
print("\nThank you for sharing your educational background! Here's what we learned about you:")
print(f"Name: {name}")
print(f"High School: {high_school}")
print(f"College: {college}")

# End with a personalized farewell
print(f"\nThanks for participating in this program! Best of luck on your journey ahead, {name}!")
