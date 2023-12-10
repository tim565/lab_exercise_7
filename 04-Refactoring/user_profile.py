import re  # Regex


class UserProfileException(Exception):
    pass


def is_valid_name(name):
    return len(name) >= 3 and re.match("^[A-Za-z]*$", name)


def is_valid_age(age):
    return str(age).isnumeric() and 18 <= int(age) <= 120


def is_logged_in(login_status):
    return login_status


def check_name(name):
    if not is_valid_name(name):
        raise UserProfileException(f"Invalid name: {name}. Name should be at least 3 characters long and should only contain alphabetic characters.")


def check_age(age):
    if not is_valid_age(age):
        raise UserProfileException(f"Invalid age: {age}. Age should be a numeric value between 18 and 120.")


def check_country(country):
    countries = ["Germany", "Netherlands", "Austria", "Sweden"]
    in_valid_countries = country in countries

    if not in_valid_countries:
        raise UserProfileException(f"Invalid country: {country}. Our service is only available in {', '.join(countries)}.")


def check_login_status(login_status):
    if not is_logged_in(login_status):
        raise UserProfileException(f"User is not logged in. Cannot process.")


def check_user_profile(name, age, country, login_status):
    check_name(name)
    check_age(age)
    check_country(country)
    check_login_status(login_status)

    # If all conditions are met, return a success message.
    return f"User {name}'s profile is valid."


# Test the function with some sample data, and handle potential exceptions
try:
    print(check_user_profile("John", 34, "USA", True))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Ana", 15, "USA", False))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("", '52', "USA", True))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Carlos", 30, "Spain", True))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Emma", 22, "UK", False))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Rob3rt", 22, "UK", True))
except UserProfileException as e:
    print(e)
