# 🔐 Password Strength Meter & Auto-Generate Password

## 📌 Overview

This project is a **Password Strength Meter** with an integrated **Random Password Generator**. It allows users to evaluate the strength of their passwords based on security guidelines and generate **strong, random passwords**.

## 🚀 Features

✅ **Password Strength Meter** – Analyzes password security based on length, uppercase, lowercase, numbers, and special characters.  
✅ **Warnings & Suggestions** – Provides feedback on improving weak passwords.  
✅ **Random Password Generator** – Creates secure passwords with required complexity.  
✅ **Password History** – Displays the last 10 checked passwords.  
✅ **User-Friendly UI** – Built with **Streamlit** for an interactive experience.
c
## 🛠️ Technologies Used

- **Python** – Core programming language
- **Streamlit** – For building the interactive web app
- **Regex (re module)** – For password validation
- **Secrets module** – For generating random, strong passwords

## 📜 Installation & Setup

### 1️⃣ Install Dependencies

Make sure you have **Python 3.x** installed, then install the required package:

```sh
pip install streamlit
```

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/SarimArain99/password_strength_meter.git
cd password_strength_meter
```

### 3️⃣ Run the Application

```sh
streamlit run app.py
```

This will launch the Password Strength Meter in your browser.

## 🎯 How It Works

### 🔍 Password Strength Meter

1. Enter a password in the input field.
2. The app evaluates the password based on:
   - Length (minimum 8 characters)
   - Presence of uppercase letters (A-Z)
   - Presence of lowercase letters (a-z)
   - Inclusion of numbers (0-9)
   - Usage of special characters (@!#$\*& etc.)
3. The app displays a **warning message** for weak passwords.
4. Strong passwords receive a **success message**.

### 🔑 Random Password Generator

1. Click the **Generate Password** button.
2. A secure password is generated with:
   - At least 1 uppercase letter
   - At least 1 lowercase letter
   - At least 1 number
   - At least 1 special character
3. The generated password is displayed for use.

## 🔗 Future Enhancements

- ✅ Add a **progress bar** or **graph** for password strength visualization.
- ✅ Implement **integration with password managers** (Bitwarden, LastPass, etc.).
- ✅ Allow users to **store encrypted passwords securely**.
- ✅ Improve **UI/UX with better visuals**.

## 🤝 Contributing

Contributions are welcome! Feel free to **fork this repository** and submit a **pull request**.

## 🛡️ License

This project is **open-source** under the MIT License.

🔗 GitHub: [your-username](https://https://github.com/SarimArain99)
