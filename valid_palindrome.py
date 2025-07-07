# using recursion:
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    if len(s) <= 1:
        return True
    if s[0].lower() == s[-1].lower():
        return is_palindrome(s[1:-1])
    return False


# however recursion method fails for too long string as it may exceed maximum recursion limit
def is_palindrome_two_pointers(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    ns = ''
    for char in s:
        if 'a' <= char.lower() <= 'z' or "0" <= char <= "9":
            ns += char.lower()
    # Use two-pointer technique to check for palindrome
    left, right = 0, len(ns) - 1

    while left < right:
        if ns[left] != ns[right]:
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome_two_pointers('0P'))
print(is_palindrome_two_pointers('race a car'))
print(is_palindrome_two_pointers('A man, a plan, a canal: Panama'))
