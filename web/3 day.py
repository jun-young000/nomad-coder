"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""
## 이 부분부터 숙제 시작
def add_to_dict(a={}, b="", c=""):
  if type(a) is not dict:
	  print(f"You need to send a dictionary. You sent: {type(a)}")
  elif not b or not c:
	  print("You need to send a word and a definition.")
  elif b in a:
	  print(f"{b} is already on the dictionary. Won't add.")
  else:
	  a[b] = c
	  print(f"{b} has been added.")

  

def get_from_dict(a={}, b=""):
  if type(a) is not dict:
	  print(f"You need to send a dictionary. You sent: {type(a)}")
  elif not b:
	  print("You need to send a word to search for.")	 
  elif not b in a:
	  print(f"{b} was not found in this dict.")
  else:
	  print(f"{b}: {a[b]}")

  

def update_word(a={}, b="", c=""):
  if type(a) is not dict:
	  print(f"You need to send a dictionary. You sent: {type(a)}")
  elif not b or not c:
	  print("You need to send a word and a definition to update.")	
  elif b in a:
	  a[b] = c
	  print(f"{b} has been updated to: {c}")


def delete_from_dict(a={}, b=""):
  if type(a) is not dict:
	  print(f"You need to send a dictionary. You sent: {type(a)}")
  elif not b:
	  print("You need to specify a word to delete.")	 
  elif not b in a:
	  print(f"{b} is not in this dict. Won't delete.")
  else:
	  del a[b]
	  print(f"{b} has been deleted.")


#####  니코's terther 답 추가및 설명
def add_to_dict(a_dict, word="", definition=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == '' or definition == '':
    print("You need to send a word and a definition.")
  else:
    if word in a_dict:
      print(f"{word} is already on the dictionary. Won't add.")
    else:
      a_dict[word] = definition
      print(word,"has been added.")


def get_from_dict(a_dict, word=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == '':
    print("You need to send a word to search for.")
  else:
    if word not in a_dict:
      print(f"{word} was not found in this dict.")
    else:
      print(f"{word}: {a_dict[word]}") 


def update_word(a_dict, word="", definition=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == "" or definition == "":
    print("You need to send a word and a definition to update.")
  else:
    if word not in a_dict:
      print(f"{word} is not on the dict. Can't update non-existing word.")
    else:
      a_dict[word] = definition
      print(word, "has been updated to:", definition)


def delete_from_dict(a_dict, word=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == "":
    print("You need to specify a word to delete.")
  else:
    if word not in a_dict:
      print(f"{word} is not in this dict. Won't delete.")
    else:
      del a_dict[word]
      print(f"{word} has been deleted.")


#에러 체크
#모든 함수들 안에는 에러 체크를 해주는 조건문이 들어가 있습니다.
#함수들은 딕셔너리(a_dict), 키 값(word), value값(definition) 순으로 인자를 받아옵니다. (함수 get_from_dict, delete_from_dict은 키 값까지만 받아옴)
#받아온 a_dict이 딕셔너리인지 확인하기 위해 if type(a_dict) is not dict : 라는 코드를 작성하여 a_dict 이 딕셔너리가 아니면 출력문을 사용하여 사용자에게 딕셔너리가 아니라고 알려주고 현재 a_dict 의 타입을 알려줍니다.
#a_dict이 딕셔너리인 것을 확인했다면 받아온 key값(word)과 value값(definition)이 비어있지 않은지 elif word == "" or definition == "" 와 같은 코드로 검사합니다.
#word 값과 definition 값 중 둘 중 하나라도 비어있다면 실행되는 조건문입니다.
#위의 두 조건문에 모두 걸리지 않고 통과했다면 모든 에러체크는 끝났습니다.

#add_to_dict(a_dict, word="", definition="")
#add_to_dict 함수는 딕셔너리에 새로운 값을 추가해주는 함수입니다.
#1번의 에러 체크 부분을 추가해줍니다.
#에러 체크를 무사히 통과하면 딕셔너리에 새로운 값을 추가해주고 만약 추가하려는 값이 이미 딕셔너리 안에 존재한다면 해당 값이 딕셔너리 안에 있다는 문장을 출력시켜주면 됩니다.
#if word in a_dict : 만약 딕셔너리 a_dict 안에 key값(word)이 이미 존재한다면 key 값이 중복되면 안 되므로 딕셔너리에 새로운 값을 추가할 수 없습니다.
#딕셔너리 안에 중복되는 key값이 없다면 드디어 새로운 값을 딕셔너리에 추가해줄 수 있습니다.
#a_dict[word] = definition 으로 a_dict 딕셔너리에 새로운 값을 추가해줄 수 있습니다.

#get_from_dict(a_dict, word="")
#get_from_dict 함수는 딕셔너리 안에 있는 값을 체크하여 만약 같은 key 값(word)이 존재한다면 그에 해당하는 key값과 value값을 출력해주는 함수입니다.
#마찬가지로 1번의 에러 체크를 모두 통과하면 if word not in a_dict: 조건문을 이용하여 딕셔너리 a_dict 안에 key 값(word)이 있는지 체크합니다.
#word랑 일치하는 key 값이 딕셔너리 a_dict 안에 존재한다면 print(f"{word}: {a_dict[word]}") 라는 코드를 작성하여 해당하는 key값과 value 값을 출력해줍니다.

#update_word(a_dict, word = "", definition = "")
#update_word 함수는 딕셔너리 a_dict 안에 있는 key 값 (word)에 해당하는 value 값 (definition)을 갱신시켜주는 함수입니다.
#마찬가지로 1번의 에러 체크를 모두 통과하면 if word not in a_dict: 조건문을 이용하여 딕셔너리 안에 key 값이 존재하지 않는지 체크합니다.
#key 값이 이미 존재하고 있어야 그 key 값에 해당하는 value 값을 수정할 수 있기 때문입니다.
#조건문을 이용해 딕셔너리 안에 해당 key값이 존재하고 있다면 a_dict[word] = definition 으로 해당 value 값을 갱신해줍니다.

#delete_from_dict(a_dict, word="")
#delete_from_dict 함수는 딕셔너리 a_dict 안에 있는 key 값(word)에 해당하는 정보를 삭제시키는 함수입니다.
#마찬가지로 1번의 에러 체크를 모두 통과하면 if word not in a_dict: 조건문을 이용하여 딕셔너리 안에 key 값이 존재하지 않는지 체크합니다.
#key 값이 이미 존재하고 있어야 그 key 값에 해당하는 모든 정보를 삭제할 수 있기 때문입니다.
#del a_dict[word] 를 이용하면 간단히 삭제할 수 있습니다.
























## 숙제끝
# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\