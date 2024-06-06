import re

# paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
# # print(re.findall("love", paragraph, re.I))

# splitted_words = re.split(" ", paragraph)
# frequent_words = []
# for word in splitted_words:
#     number_of_times = re.findall(word, paragraph).__len__()
#     frequent_words.append((number_of_times, word))

# print(max(frequent_words, key=lambda word: word[0]))


# txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction"
# digits = list(map(lambda num: int(num), re.findall("-?\d+", txt, re.I)))  # type: ignore
# print(max(digits) - min(digits))

# ! ? ==> 0 or 1 times
# ! . ==> 0 or Many times
# ! + ==> 1 or Many times


# def is_valid_variable(name):
#     pattern = r"^(?![0-9])[A-Za-z_]\w*$"
#     return bool(re.match(pattern, name))


# print(is_valid_variable("first_name"))

sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""

new_re = r"[$@#&*;!%]+"

simple_text = re.sub(new_re, "", sentence)
print(simple_text)

splitted_words_new = re.split(" ", re.sub(r"([.,?])?", "", simple_text))
print(splitted_words_new)

frequent_words_new = []

for word in splitted_words_new:
    number_of_times = re.findall(
        word, re.sub(r"([.,?])?", "", simple_text), re.IGNORECASE
    ).__len__()

    frequent_words_new.append((number_of_times, word))

print(max(frequent_words_new, key=lambda word: word[0]))
