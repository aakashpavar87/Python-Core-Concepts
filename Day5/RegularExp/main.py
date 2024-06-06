import re

txt = " to teach python and javaScript to teach python and javaScript to teach python\n and javaScriptI love to teach python and javaScript\nI love to teach python and javaScript"
# ! It only matches first half or starting of line
match = re.match("I love to teach", txt, re.I)
print(match)


found = re.search("I love to", txt, re.M)
print(found)

all_found = re.findall("I love to", txt, re.M)
print(all_found)


newtxt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

mathced_replaced = re.sub(
    pattern="[Pp]ython", repl="JavaScript", string=newtxt, flags=re.I
)

splitted_lines = re.split("\n", newtxt, re.I)
print(splitted_lines)

pattern = r"[a-z].{16}"
print(re.match(pattern, "aakash@gmail.com", re.I))
