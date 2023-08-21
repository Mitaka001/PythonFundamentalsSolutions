text = input().split()

added_words = [word for word in text if len(word) % 2 == 0]
print("\n".join(added_words))
