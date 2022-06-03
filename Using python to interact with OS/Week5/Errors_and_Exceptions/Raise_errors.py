def validate_user(username, minlen):
    assert type(username) == str, "Username must be str"

    if minlen < 1:
        raise ValueError("Minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

print(validate_user(input("Введите логин: "), 5))