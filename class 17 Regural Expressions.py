# regular Expressions in Python


# Simple Match:**
import re
pattern = r"apple"
text = "apple pie is delicious"
match = re.match(pattern, text)   # re.match() function checks if the pattern matches at the beginning of the string.
#print(re.match(pattern, text))
print(match.group())  # Output: "apple"

'''
This example demonstrates a basic match. The pattern r"apple" searches for the word "apple" in the
 given text. The re.match() function checks if the pattern matches at the beginning of the string
'''

# Case Insensitive Match:  It matches "apple" or "Apple" in the text.
import re
pattern = r"apple"
text = "Apple pie is delicious"
match = re.match(pattern, text, re.IGNORECASE)
print(match.group())  # Output: "Apple"


# Matching Numbers:**
import re
pattern = r"\d+"  # Match one or more digits
text = "There are 123 apples 12 324"
matches = re.findall(pattern, text)
print(matches)  # Output: ['123']
# r"\d+" matches one or more digits. The re.findall() function returns all occurrences of this pattern 
# in the given text.


# Matching Words:**
import re
pattern = r"\w+"  # Match one or more word characters
text = "Hello, world! 123"
matches = re.findall(pattern, text)
print(matches)  # Output: ['Hello', 'world']
'''
The pattern r"\w+" matches one or more word characters (letters, digits, or underscores). 
The re.findall() function returns all words in the text.
'''


# Splitting Text:**
import re
pattern = r"\s"  # Match whitespace characters
text = "Hello  world"
split_text = re.split(pattern, text)
print(split_text)  # Output: ['Hello', '', 'world']

'''
This example uses the pattern r"\s" to match whitespace characters. The re.split() function splits the
text using this pattern as a delimiter.
'''

# Substitution:**
import re
pattern = r"\d+"  # Match digits
text = "There are 123 apples"
substituted_text = re.sub(pattern, "many", text)
print(substituted_text)  # Output: "There are X apples"

'''
The pattern r"\d+" matches digits in the text. The re.sub() function substitutes all occurrences of 
this pattern with "X".
'''

# Matching Email Addresses:**
'''
The complex pattern r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}" is used to match email addresses.
 It captures valid email formats in the text.
'''
#asdam._A@gmail.com
import re
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
text = "Contact us at support@example.com"
matches = re.findall(pattern, text)
print(matches)  # Output: ['support@example.com']


if(re.findall(pattern, text)):
    print("Ask for password")
else:
    print("Enter a valid email")




# Matching Dates:**
'''
The pattern r"\d{2}-\d{2}-\d{4}" matches dates in the format "DD-MM-YYYY". 
The re.findall() function returns all occurrences of this pattern in the text.
'''
import re

pattern = r"\d{2}-\d{2}-\d{4}"
text = "Birthdate: 01-23-1990"
matches = re.findall(pattern, text)
print(matches)  # Output: ['01-23-1990']



# Negative Lookahead:**
'''
The pattern r"\b(?!not\b)\w+" uses a negative lookahead to match words that are not "not". 
The \b represents a word boundary.
'''
import re

pattern = r"\b(?!not\b)\w+"  # Match words that are not "not"
text = "This is not a test"
matches = re.findall(pattern, text)
print(matches)  # Output: ['This', 'is', 'a', 'test']


# Extracting HTML Tags:**
'''
The pattern r"<.*?>" matches HTML tags. It uses .*? to match any characters (including angle brackets) non-greedily. 
The re.findall() function returns all HTML tags in the text.
'''
import re

pattern = r"<.*?>"  # Match HTML tags
html_text = "<p>This is <strong>bold</strong> text.</p>"
tags = re.findall(pattern, html_text)
print(tags)  # Output: ['<p>', '<strong>', '</strong>', '</p>']
