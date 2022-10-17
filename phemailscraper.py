#! python3
import re, pyperclip, os

# Define where you want it saved
def save_option():
    while True:
        save_option = input('Type "1" to save to a .txt file\n"2" to save to your clipboard\n"d" to delete the file\n"q" to quit: ')
        if save_option == '1':
            send_to_file()
            print('File saved to: ' + os.getcwd() + '\scraped info.txt')
        elif save_option == '2':
            send_to_clip()
            print('Results saved to your clipboard.')
        elif save_option == 'd':
            remove_file()
        elif save_option == 'q':
            quit()
        else:
            print('Enter a valid option.')
            continue

# regex for phone numbers
phone_regex = re.compile(r'''
# 555-555-5555, (555) 555-5555, 555-5555. 555-5555 ext 12345, ext. 12345, x12345
(
 ((\d\d\d) | (\(\d\d\d\)))?         # area code (optional)
 (\s | -)                           # first separator
 \d\d\d                             # first 3 digits
-                                   # separator
\d\d\d\d                            # last 4 digits
(((ext(\.)?\s) | x)                 # extension (optional)
 (\d{2,5}))?                        # extension number-part (optional)
)
''', re.VERBOSE)

# Regex for email addresses
email_regex = re.compile(r'''
                                    # some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+                     # name part
@                                   # @ symbol
[a-zA-Z0-9_.+]+                     # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from the text
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

# Copy the extracted email/phone to clipboard
results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)

def remove_file():
    os.unlink('scraped info.txt')
    print('File deleted.')

def send_to_clip():
    pyperclip.copy(results)

def send_to_file():
    scraped_results = open('scraped info.txt', 'a')
    scraped_results.write(results + '\n-----------------------------------------------------------------------------------')
    scraped_results.close()

save_option()
