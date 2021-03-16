s = input("Enter a string:")
print(f'Given String: {s}')
revstr = s[::-1]
print(f'Reversed String: {revstr}')


def is_palindrome(s, revstr):
    if revstr == s:
        return f"The supplied word is same if reversed"
    else:
        return f"Not same"


print(is_palindrome(s, revstr))