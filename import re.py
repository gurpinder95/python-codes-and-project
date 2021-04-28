import re
string = "I AM NOT YELLING . she said which is not true"
print(string)
new = re.sub("[A-Z]", "", string)
print(new)
new = re.sub("[a-z]", "", string)
print(new)
new = re.sub("[.]", "", string)
print(new)
new = re.sub("[.,'\'a-z]", "", string)
print(new)
new = re.sub("[.,'\' a-z A-Z]", "", string)
print(new)