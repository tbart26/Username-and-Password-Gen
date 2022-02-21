# Tyler's username and password generator.
# This tool generates a new user's username and temporary password, based on their legal name.

first_name = "Tyler"
last_name = "Bartley"


# This is the function for the username. It takes the first three letters of the
# user's first name, and the first four letters of their last name to make their
# username. If the user's first or last name is less than 3 or 4 letters,
# their username becomes their entire name. This can be tuned to just use a longer
# version of their last name, though.
def username_generator(first_name, last_name):
    un_first = first_name[:3]
    un_last = last_name[:4]
    new_username = un_first + un_last
    short_name_response = first_name + last_name
    if len(first_name) < 3 or len(last_name) < 3:
        return short_name_response
    else:
        return new_username


# This is the password generator function. It starts with an empty string, then
# iterates through the user's username, and shifts each letter to the right,
# starting from the last letter of their name. So TylBart will become tTylBar.
def password_generator(username):
    password = ""
    for letters in range(0, len(username)):
        password += username[letters - 1]
    return password

# Outputting the username and password from the variables defined at the start of the program.
# This is a pretty basic script, but it gets the job done.

username = username_generator(first_name, last_name)
password = password_generator(username)

print(username)
print(password)

# This generator is the result of CodeAcademy's last page in the "Strings" lesson, at the
# start of the second half of the "Learn Python 3" skill path. It was definitely a little bit
# harder than I think it really needed to be, and the hints weren't the most helpful. I felt
# a little stupid writing this script because I actually had to look at the solution code to
# see what exactly they were looking for. I didn't reuse their code, though, and as a result of
# that the program isn't as efficient as it could be, but I would rather lose efficiency than
# copy someone else's work. Working with the basics of string iteration wasn't that bad,
# but getting to the bits where you need to generate the password really brought me the most trouble.
# Username generation was the hardest bit, but now I know how to shift letters to the right,
# so everything's a learning experience.
