given_string = input().lower()
count = 0
given_words = ["sand", "water", "fish", "sun"]

for word in given_words:
    num = given_string.find(word)
    while num != -1:
        count += 1
        num = given_string.find(word, num + 1)

print(count)