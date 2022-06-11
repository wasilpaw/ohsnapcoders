my_str = input("Enter a few words: ")

words = my_str.split()

for word in words:
   word.lower()

words.sort()

for word in words:
   print(word)
