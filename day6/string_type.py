# Empty strings can be created using str() built-in fxn

s = str()  # Empty string
s = ""  # Empty string can also be created with empty quotes (single or double)

s = "I'm in broadway"  # This is a valid string
# s = 'I'm in broadway'  # This is an invalid string


# Escape Sequences is used to suppress the actual meaning of the character
# Some escape sequences are \', \n, \\, \b, \t, \r

a = 'I\'m in broadway'  # This is a valid string because of escape sequence \'
print(a)
a = "Hello\nWorld"  # \n breaks a line in the console
print(a)

a = "Hello\\\\\ \'World"  # \\ is an escape sequence that consider the \ only once
print(a)
a = "Hello\bWorld"  # \b  is an escape sequence that takes the cursor one space back.
# Here result is "HellWorld"
a = "Hello\tWorld"
print("Hellooooooo World\rBroad")  # \r is an escape sequence for carriage return. The string after the
# \r takes the cursor to the very beginning. Here the result will be Broadwayooo
print(a)



# Triple quoted strings are also possible in python

message = """Hello Im from broadway.
          And I'm learning Python """



