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
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Use two-pointer technique to check for palindrome
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
