def quiz_game():
    questions = [
        {"question": "What's Japan's capital?",
         "options": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
         "answer": "C"},
        {"question": "Which planet is red?",
         "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
         "answer": "B"},
        {"question": "Biggest ocean?",
         "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
         "answer": "D"}
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your guess (A, B, C, or D): ").upper()

        if answer == q["answer"]:
            print("Yay! That's correct!")
            score += 1
        else:
            print("Oops! Correct answer was", q["answer"])

        print()

    print(f"Your total score: {score} out of {len(questions)}")

quiz_game()
