import re
import secrets
import string
import streamlit as st

# ✅ Set up the Streamlit page configuration
st.set_page_config(
    page_title="Password Strength Meter", page_icon="🔐", layout="centered"
)

# ✅ Page Title and Subtitle
st.title("🔒 Master Your Password Power")
st.subheader("🔍 Design, Evaluate, Validate, and Fortify Your Digital Keys")

# ✅ Password input field with a placeholder and hidden input type
userInput = st.text_input(
    "Enter Your Password",
    placeholder="Must be at least 8 characters with A-Z, a-z, 0-9 & special characters (@!#$%^&*)",
    type="password",
)

# ✅ Function to check password strength
def userPasswordStrength(password):
    """
    This function evaluates the strength of a password based on:
    - Length (at least 8 characters)
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Numbers (0-9)
    - Special characters (@!#$*&)
    """

    # ✅ Password strength levels
    remarks = {0: "Very Weak", 1: "Weak", 2: "Medium", 3: "Strong", 4: "Very Strong"}
    score = 0  # Initialize score

    # ✅ Step 1: Check if the password is at least 8 characters long
    if len(password) >= 8:
        score += 1
    else:
        st.warning(
            f"⚠️ **{remarks[0]}** - Password is too short! It should be at least 8 characters long. (Score: {score})"
        )
        return

    # ✅ Step 2: Check if the password contains at least one uppercase letter (A-Z)
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        st.warning(
            f"⚠️ **{remarks[1]}** - Password should contain at least 1 uppercase letter (A-Z). (Score: {score})"
        )
        return

    # ✅ Step 3: Check if the password contains at least one lowercase letter (a-z)
    if re.search(r"[a-z]", password):
        score += 1
    else:
        st.warning(
            f"🔴 **{remarks[2]}** - Password should contain at least 1 lowercase letter (a-z). Try adding numbers and special characters for extra security. 🔐 (Score: {score})"
        )
        return

    # ✅ Step 4: Check if the password contains at least one number (0-9)
    if re.search(r"\d", password):
        score += 1
    else:
        st.warning(
            f"🟠 **{remarks[3]}** - Password should contain at least 1 number (0-9). Try adding a number to enhance security. 🔢 (Score: {score})"
        )
        return

    # ✅ Step 5: Check if the password contains at least one special character (@!#$*&)
    if re.search(r"[@!#$%^&*()_+={}\[\]:;\"'<>,.?/~`\\|-]", password):
        score += 1
    else:
        st.warning(
            f"⚠️ Your password is strong, but adding a special character (@!#$%^&*()_+={{}}[]:;\"'<>,.?/~`\\|-) will make it even better! (Score: {score})"
        )
        return

    # ✅ If all conditions are met, display a success message
    st.success(
        f"✅ **{remarks[4]}** - Great job! Your password is strong and secure. (🎯 Your Password Score is: {score})"
    )
    st.write(f"🔐 Your Password: **{password}**")
    st.write("---")

    # ✅ Store password history
    if "Passwords" not in st.session_state:
        st.session_state["Passwords"] = []

    # ✅ Add new password to history if it hasn't been checked before
    if userInput and userInput not in st.session_state["Passwords"]:
        st.session_state["Passwords"].append(userInput)

    # ✅ Show a warning if the password has already been checked
    elif userInput in st.session_state["Passwords"]:
        st.warning("⚠️ **Warning:** You have already checked this password before.")

    # ✅ Maintain only the last 10 checked passwords
    if len(st.session_state["Passwords"]) > 10:
        st.session_state["Passwords"].pop(0)

    # ✅ Display last 10 checked passwords
    st.subheader("🔐 History of Last 10 Passwords:")
    for i, pswd in enumerate(reversed(st.session_state["Passwords"])):
        st.text(f"{i+1}. {pswd}")

    st.download_button(
        "Download Password History",
        data="\n".join(st.session_state["Passwords"]),
        file_name="password_history.txt",
        mime="text/plain",
    )


# ✅ Run the password strength checker when the user inputs a password
if userInput:
    userPasswordStrength(userInput)
st.markdown("\n---\n")


# ✅ Strong Password Generator
st.header("Strong Password Generator")
st.write("Don't want to create your own password? Try our generator below!")


def generate_secure_password(length=8):
    """Generate a strong password that includes at least one uppercase, one lowercase, one digit, and one special character."""

    if length < 8:
        raise ValueError(
            "Password length must be at least 8 to include all required character types."
        )

    # Required characters (one from each category)
    upper = secrets.choice(string.ascii_uppercase)  # At least one uppercase letter
    lower = secrets.choice(string.ascii_lowercase)  # At least one lowercase letter
    digit = secrets.choice(string.digits)  # At least one number
    special = secrets.choice(string.punctuation)  # At least one special character

    # Remaining characters randomly chosen from all allowed characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_length = length - 4  # Remaining after adding required characters

    password_list = [upper, lower, digit, special] + [
        secrets.choice(all_characters) for _ in range(remaining_length)
    ]

    # Shuffle to remove any predictable order
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


lengthOfPassword = st.number_input(
    "Password Length", min_value=8, max_value=20, value=8
)

if st.button("Generate New Password"):
    st.write(f"🔐 Secure Password:  **{generate_secure_password(lengthOfPassword)}**")
