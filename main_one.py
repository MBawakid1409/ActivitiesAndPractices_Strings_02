# Activities & Practices
# --------- [String] ---------
print("--------- [Strings] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
favorite_fruit = "blueberry"
print(len(favorite_fruit)) # 9
print(favorite_fruit[0]) # b
print(favorite_fruit[0]) # b
print(favorite_fruit[4:6]) # be
print(favorite_fruit[4:7]) # ber
print(favorite_fruit[3:8]) # eberr
print(favorite_fruit[2:9]) # ueberry
print(favorite_fruit[:4]) # blue
print(favorite_fruit[4:]) # berry
print("----------------------------------")
# Practise 02
print("Practise #02")
fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix
print(favorite_fruit) # blueberries
fruit_sentence = "My favorite fruit is " + favorite_fruit
print(fruit_sentence) # My favorite fruit is blueberries
print("----------------------------------")
# Practise 03
print("Practise #03")
first_name = "Julie"
last_name = "Blevins"
def account_generator(fName, lName):
    account_name = fName[:3] + lName[:3]
    return account_name

new_account = account_generator(first_name, last_name)
print(new_account) # JulBle
print("----------------------------------")
# Practise 04
print("Practise #04")
favorite_fruit = "blueberry"
# last_char = favorite_fruit[len(favorite_fruit)]
# print(last_char) # IndexError: string index out of range
last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char) # Output: y
length = len(favorite_fruit)
last_char = favorite_fruit[length-4:]
print(last_char) # Output: erry
print("----------------------------------")
# Practise 05
print("Practise #05")
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(fName, lName):
    account_name = fName[-3:] + lName[-3:]
    return account_name

temp_password = password_generator(first_name, last_name)
print(temp_password) # ikouki
print("----------------------------------")
# Practise 06
print("Practise #06")
# favorite_fruit = "blueberry"
print(favorite_fruit[-1]) # y
print(favorite_fruit[-2]) # r
print(favorite_fruit[-3:]) # rry
sentence0 = "daily life"
second_to_last = sentence0[-2]
print(second_to_last) # f
final_word = sentence0[-4:]
print(final_word) # life
print("----------------------------------")
# Practise 07
print("Practise #07")
first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R"
#print(first_name) # TypeError: 'str' object does not support item assignment
# Strings are Immutable
# We can use it to create other strings, but we cannot change the string itself.

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name) # Rob
print("----------------------------------")
# Practise 08
print("Practise #08")
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
print(favorite_fruit_conversation) # He said, "blueberries are my favorite!"
password = "theycallme\"crazy\"91"
print(password) # theycallme"crazy"91
print("----------------------------------")
# Practise 09
print("Practise #09")
def print_each_letter(word):
    for letter in word:
        print(letter)

favorite_color = "blue"
print_each_letter(favorite_color) # b l u e    
#print_each_letter("blue") # b l u e    
print("----------------------------------")
# Practise 10
print("Practise #10")
def get_length(word):
    counter = 0
    for letter in word:
        counter += 1
    return counter

function_test = get_length("HombaGomba")
print(function_test) # 10
print("----------------------------------")
# Practise 11
print("Practise #11")
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
    if character == "b":
        counter = counter + 1

print(counter) # 2
print("----------------------------------")
# Practise 12
print("Practise #12")
def letter_check(word, letter):
    for character in word:
        if letter == character:
            return True
    return False

test_function = letter_check("Listen to your voice", "O")
print(test_function) # False
test_function = letter_check("Listen to your voice", "o")
print(test_function) # True           
print("----------------------------------")
# Practise 13
print("Practise #13")
# letter in word
print("e" in "blueberry") # True
print("a" in "blueberry") # False
print("blue" in "blueberry") # True
print("blue" in "strawberry") # False
print("----------------------------------")
# Practise 14
print("Practise #14")
def contains(big_string, little_string):
    return little_string in big_string

function_test = contains("Watermelon", "melon")
print(function_test) # True
print("----------------------------------")
# Practise 15
print("Practise #15")
def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common

function_test = common_letters("watermelon", "melon")
print(function_test) # ['e', 'm', 'l', 'o', 'n']
print("----------------------------------")
# Practise 16
print("Practise #16")
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name

function_test = username_generator("Homba", "Gomba")
print(function_test) # HombGomb
print("----------------------------------")
# Practise 17
print("Practise #17")
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

function_test = password_generator("Funkey")
print(function_test) # yFunke
print("----------------------------------")
# Practise 18
print("Practise #18")
# String Methods
print('Hello world'.upper()) # HELLO WORLD
print('Hello world'.lower()) # hello world
print('Hello world'.title()) # Hello World
print('Hello world'.split()) # ['Hello', 'world']
print(' '.join(['Hello', 'world'])) # Hello world
print('Hello world'.replace('H', 'J')) # Jello world
print('   Hello world   '.strip()) # Hello world
print('{} {}'.format('Hello', 'world')) # Hello world
print("----------------------------------")

print("----------------------------------")
# Practise 19
print("Practise #19")

# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.

# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

print("----------------------------------")
# Practise 20
print("Practise #20")

# Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

def count_char_x(word, x):
  occurrences = 0
  for letter in word:
    if letter == x:
      occurrences += 1
  return occurrences

print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

print("----------------------------------")
# Practise 21
print("Practise #21")

# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.

# For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

print("----------------------------------")
# Practise 22
print("Practise #22")

# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

# For example, substring_between_letters("apple", "p", "e") should return "pl".

def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word

print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

print("----------------------------------")
# Practise 23
print("Practise #23")

# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words:
    if len(word) < x:
      return False
  return True

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

print("----------------------------------")
# Practise 24
print("Practise #24")

# Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.

# For example, the following three calls should all return True:
# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()


print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

print("----------------------------------")
# Practise 25
print("Practise #25")

# Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

print("----------------------------------")
# Practise 26
print("Practise #26")

# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print  

print("----------------------------------")
# Practise 27
print("Practise #27")

# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a  

print("----------------------------------")
# Practise 28
print("Practise #28")

# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn  
