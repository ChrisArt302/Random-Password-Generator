# Random Password Generator

import string, secrets

# Password set at 40 characters long
# Password variable set to empty string to add characters later on

password = ''
for i in range(10):
    j = secrets.choice(string.ascii_lowercase) # lowercase letter
    k = secrets.choice(string.punctuation) # punctuation
    l = secrets.choice(string.digits) # digits
    m = secrets.choice(string.ascii_uppercase) # uppercase letter
    password = password + j + k + l + m

print("\nHere is your randomly generated password: \n", "\n" + password)



