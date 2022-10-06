import re
import pyperclip

# Creating a regex for phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?            # area code (optional)
(\s | -)            # first seperator
\d\d\d            # first three digits
-            # seperator
\d\d\d\d            # last four digits
(((ext(\.)?\s) | x)            # extension word part (optional)
(\d {2,5}))?            # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email

emailRegex = re.compile(r'''
# something.+_@something.+_.com
[a-zA-Z0-9_.+]+            # name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name
''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone: # TO get the phone numbers from the list of tuples.
    allPhoneNumbers.append(phoneNumber[0])

# Copied the extracted phone and email to clipboard.
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
