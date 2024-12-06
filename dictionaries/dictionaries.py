words_list = {}

with open("input.txt", "r") as file:
    text = file.read().lower()

words = text.split()

for word in words:
    if word in words_list:
        words_list[word] += 1
    else:
        words_list[word] = 1

for word, count in words_list.items():
    if count >= 3:
        print(f"{word}: {count}")

    
