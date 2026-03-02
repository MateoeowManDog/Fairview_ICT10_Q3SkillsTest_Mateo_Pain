from pyscript import document

def validate_account(event=None):
    output = document.getElementById("output")

    fullname = document.getElementById("fullname").value.strip()
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value.strip()
    #checks fullname capitalization
    if fullname != fullname.title():
        output.innerText = "Error: Full Name must use Proper Capitalization (Title Case)."
        return
    #checks userlength
    elif len(username) < 7:
        output.innerText = "Username must be at least 7 characters."
        return
    #checks password length
    elif len(password) < 10:
        output.innerText = "Password must be at least 10 characters."
        return
    #validation
    has_capital = any(c.isupper() for c in password)
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)

    if not (has_capital and has_letter and has_number):
        if not has_capital:
            output.innerText = "Password must contain a capital letter."
            return

        elif not has_letter:
            output.innerText = "Password must contain a letter."
            return

        elif not has_number:
            output.innerText = "Password must contain a number."
            return
    #if all of the conditions are met
    output.innerText = "Account successfully created!"