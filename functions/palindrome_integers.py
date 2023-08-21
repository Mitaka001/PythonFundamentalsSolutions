def check_palindrome(numbers):
    if numbers == numbers[::-1]:
        return True
    return False

given_numbers = input().split(", ")
for number in given_numbers:
    print(check_palindrome(number))
