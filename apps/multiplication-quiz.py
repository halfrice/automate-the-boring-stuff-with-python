import random, math, time

success = [
    'Correct!',
    'Good Answer!',
    'Nice!',
    "You've got it!",
    'Smart!',
    'Outstanding!',
]

fail = [
    'Fail...',
    'Disappointed in you...',
    "C'mon man!",
    'Really?!..',
    "That's not it, dummy.",
    "Don't be stupid.",
]


def grade(numOfCorrect, numOfQuestions):
    grades = {10: 'A', 9: 'A-', 8: 'B', 7: 'C', 6: 'D'}
    grade = ''

    score = math.ceil((10 * numOfCorrect) / numOfQuestions)
    if score in grades.keys():
        grade = grades[numOfCorrect]
    else:
        grade = 'F'

    return grade


def quiz(n):
    # Create multiplication questions
    questions = []
    for i in range(n):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        questions.append([a, b])

    print(f'Multiplication Quiz. {len(questions)} questions.')
    rsg = ['Ready', 'Set', 'Go!']
    for i in range(len(rsg)):
        print(f'{rsg[i]}', end='\n')
        time.sleep(0.25)

    # The quiz loop
    score = 0
    while True:
        for i, q in enumerate(questions):  # i = index, q = question
            userAnswer = ''
            attempt = 1
            startTime = time.time()
            elapsedTime = 0

            # Get an answer from user
            while type(userAnswer) is not int:
                # Allow max 3 attempts
                if attempt > 3:
                    print('Too many attempts. Moving on...')
                    break

                # Get user input
                userAnswer = input(f'{q[0]} x {q[1]}: ')

                # Calculate the elapsed time
                elapsedTime = time.time() - startTime
                if elapsedTime >= 8:
                    print('Too much time has passed. Fail...')
                    break

                # Typecast user's answer to an integer
                try:
                    userAnswer = int(userAnswer)
                except ValueError:
                    print('Please enter a number: ')
                    userAnswer = ''

                attempt += 1

            # Evaluate the user's answer
            if type(userAnswer) is int and elapsedTime < 8:
                answer = q[0] * q[1]

                if userAnswer == answer:
                    print(f'{success[random.randint(0, len(success) - 1)]}')
                    score += 1
                else:
                    print(f'{fail[random.randint(0, len(fail) - 1)]}')

            # Wait one second between questions
            time.sleep(1)

        # After all the questions have been asked, break out of the quiz loop
        break

    # Display results to the user
    print('\nReport Card')
    print(f'Grade: {grade(score, len(questions))}')
    print(f'Score: {score}/{n}')


quiz(10)
