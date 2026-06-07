# Password Strength Checker 🔐
A Python command-line tool that checks the strength of a password and gives real-time suggestions to make it stronger.

## Features
- Checks password length
- Detects uppercase, lowercase, numbers and special characters
- Gives suggestions on what's missing
- Scores password as Weak, Medium or Strong
- Checks against 10,000 most common passwords
- Keeps prompting until a strong password is entered

## How to Run
1. Clone the repository
   git clone https://github.com/deekshitha0x/password-strength-checker.git
2. Navigate to the folder
   cd password-strength-checker
3. Run the script
   python password_checker.py

## Example Output
enter the password: password123
too common!
enter the password: hello
password is too short
enter the password: Hello@123
password is of good length
strength: strong

## Technologies Used
- Python 3
- `string` module
  
## Author
Deekshitha — [GitHub](https://github.com/deekshitha0x)
