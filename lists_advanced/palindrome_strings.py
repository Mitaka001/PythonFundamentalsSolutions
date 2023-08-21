words = input().split()
palindrome = input()
words_list = []

palindrome_words = [words_list.append(word) for word in words if word == word[::-1]]
print(words_list)
print(f"Found palindrome {words_list.count(palindrome)} times")
