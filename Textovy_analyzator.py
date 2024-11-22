# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Marek Pošmura
# email: m.posmura@seznam.cz


import textwrap
from getpass import getpass
from task_template import TEXTS

line = 40 * "-"

users = {
          "bob": "123",
          "ann": "pass123",
          "mike": "password123",
          "liz": "pass123",
         }

# LOGIN - WHILE SMYČKA DOKUD NEZADÁ ODPOVÍDAJÍCÍ ÚDAJE
login = False

while not login:
  username = input("Username: ")
  password = getpass("Password: ") # metoda getpass zajistí nezobrazení hesla při zadání
  print(line)
  if users.get(username) == password:
    login = True
    print(f"Welcome to the app, {username.capitalize()}.\nWe have {len(TEXTS)} texts to be analyzed.", line, sep="\n")
  else:
    print("Unregistered user or wrong password.\nTry again.", line, sep="\n")


# VYBRÁNÍ SPRÁVNÉHO TEXTU - S CYKLEM WHILE
first_text = 1
last_text = int(len(TEXTS))
correct_num = False

while not correct_num:
  chosen_number = input(f"Enter a number between {first_text} and {last_text} to select:\n\
If you want to analyze your own text, type '0':\n\
If you want to quit program, type: 'Q': ")
  print(line)
  if chosen_number.lower().strip() == 'q': # OŠETŘENÍ ROZDÍLNÉ VELIKOSTI A PŘÍPADNÝCH MEZER NAVÍC
    print("Terminating the program...", line, sep="\n")
    quit()

# UMOŽNÍ UŽAVATELI ANALYZOVAT SVŮJ VLASTNÍ TEXT
  elif chosen_number == "0":
    new_text = input("Add your text to analyze:\n")
    print(line, "Your new text is:", textwrap.fill(new_text, width=40), line, sep="\n")
    TEXTS.append(new_text)
    chosen_text = TEXTS[-1]
    break

  elif chosen_number.isnumeric() is False:
    print(f"You didn´t choose number.\nTry again.", line, sep="\n")

  elif int(chosen_number) < first_text or int(chosen_number) > last_text:
    print(f"You didn´t choose number between {first_text} and {last_text}.\nTry again.", line, sep="\n")

  else:
    print(f"You selected number: {chosen_number}", line, sep="\n")
    chosen_text = TEXTS[int(chosen_number) - 1]
    correct_num = True

# SMYČKA PRO ZJIŠTĚNÉ VŠECH ZNAKŮ, O KTERÉ JE POTŘEBA TEXT OČISTIT
characters = []

for symbol in chosen_text:
  if not symbol.isalnum() and symbol not in characters and symbol != " ":
    characters.append(symbol)

# SMYČKA VYTVOŘÍ LIST OČIŠTĚNÝCH SLOV
clean_text = []

for word in chosen_text.split():
  clean_word = word.strip("".join(characters))
  clean_text.append(clean_word)

# SMYČKA PROVEDE POŽADOVANÉ ANALÝZY
words = []
titlecase = []
uppercase = []
lowercase = []
numeric = []
sum_of_num = []
length = {}

for word in clean_text:
  if word.isalnum():
    words.append(word)

  if word.istitle():
    titlecase.append(word)

  if word.isupper() and word.isalpha():
    uppercase.append(word)

  if word.islower():
    lowercase.append(word)

  if word.isnumeric():
    numeric.append(int(word))
    sum_of_num = sum(numeric)

# PODMÍNKA POČÍTÁ POČET SLOV PODLE JEJICH DÉLKY
  if len(word) not in length:
    length[len(word)] = 1
  else:
    length[len(word)] += 1


# VYPÍŠE VÝSLEDEK ANALÝZY + KONTROLA MNOŽNÉHO ČÍSLA (NA MNOŽNÁ ČÍSLA DEFINOVAT VLASTNÍ FUNKCI???)
print(f"There {'are' if len(words) > 1 else 'is'} {len(words)} {'words' if len(words) > 1 else 'word'} in the selected text.")
print(f"There {'are' if len(titlecase) > 1 else 'is'} {len(titlecase)} titlecase {'words' if len(titlecase) > 1 else 'word'}.")
print(f"There {'are' if len(uppercase) > 1 else 'is'} {len(uppercase)} uppercase {'words' if len(uppercase) > 1 else 'word'}.")
print(f"There {'are' if len(lowercase) > 1 else 'is'} {len(lowercase)} lowercase {'words' if len(lowercase) > 1 else 'word'}.")
print(f"There {'are' if len(numeric) > 1 else 'is'} {len(numeric)} numeric {'strings' if len(numeric) > 1 else 'string'}.")
print(f"The sum of all the numbers: {sum_of_num}.", line, sep = "\n")


# VYKRESLENÍ GRAFU, GRAF SE ROZŠIŘUJE PODLE NEJVETŠÍHO POČTU SLOV
max_value = int(max(length.values()))

print("LEN|", "OCCURENCES".center(max_value), "  |NR.", sep="")
print(line)

for key, value in sorted(length.items()):
    print(f"{str(key).rjust(3)}| {'*'*(int(value))} {'|'.rjust(max_value - int(value) + 1)}{str(value)}")
print(line)



