import re

# On the first look, going off the line "You may need to test the string against
# multiple regex patterns...", you might think to try something like this:
lowercaseRegex = re.compile(r'[a-z]')
uppercaseRegex = re.compile(r'[A-Z]')
digitRegex = re.compile(r'\d')
# We'll call this Solution1

# Solution2
# Let's put it all together and make sure it's at least 8 characters long
allTogetherRegex = re.compile(r'^[a-zA-Z\d]{8,}$')  # Solution2

# Solution3
# EXTRA CREDIT: Read about lookahead assertions
# https://docs.python.org/3.9/howto/regex.html#lookahead-assertions
lookaheadRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
# ^ We are using positive lookahead here


def isPasswordStrong(password):
    # Solution1
    # Lets use the findall method to create a few lists
    # We can use those lists together to make sure we have at least 8 chars
    lower = lowercaseRegex.findall(password)
    upper = uppercaseRegex.findall(password)
    digit = digitRegex.findall(password)

    count = 0
    if not (lower and upper and digit):
        return False
    else:
        count += len(lower)
        count += len(upper)
        count += len(digit)

        if count < 8:
            return False

    # There are massive problems with Solution1. Can you think of what they are?
    # Hint: Try entering special characters (~!@#$%^&*()-+_=,.<>/?) or even spaces

    # Solution2
    allTogether = allTogetherRegex.search(password)
    if not allTogether:
        return False

    # Solution3
    lookahead = lookaheadRegex.search(password)
    if not lookahead:
        return False

    return True


password = input('Input a password to test its strength: ')
strong = isPasswordStrong(password)

if strong:
    print('This password is strong 💪')
else:
    print('This password needs to hit the gym, lawyer up, and delete tiktok')
