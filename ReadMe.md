# Email OTP Verification Using Python

## Functionality
1.`generate_otp()`:
- Generates a random 6-digit OTP (One Time Password).

2.`send_otp_email()`:
- Sends the generated OTP to the provided recipient email address using SMTP (Simple Mail Transfer Protocol).
- Uses the credentials (sender email and password) stored in the config module.

3.`otp_prompt()`:
- Prompts the user to enter the OTP.
- Validates the input to ensure it's a 6-digit numberic value.

4.`verify_otp()`:
- Compares the user input OTP with the generated OTP to verify if they match.
- Allows a maximum number of attempts (default is 3).

`main()`: Executes the OTP verification process.
- Calls `generate_otp()` to generate an OTP.
- Calls `send_otp_email()` to send the OTP to the recipient's email address.
- Calls `verify_otp()` to prompt the user to enter the OTP and verify the entered OTP.


## Dependencies:
- `smtplib`: python's smtplib module for sending emails and,
- `random`: random module for otp generation.


## How to Run:
1. Ensure you have Python installed on your system.

2. Set up the config.py file with the sender's email address and password, as well as the recipient's as shown in below cell.

```
#config.py
sender_email = "example@gmail.com"
email_password = "password"
recipient_email = "example@gmail.com"
```

3. Save the provided Python script as main.py.

4. Ensure the config.py file is in the same directory as main.py and contains the required credentials.

5. Open a terminal or command prompt.

6. Navigate to the directory containing the script. 

7. Run the script by executing the command: `$python main.py`

8. Follow the prompts to enter the OTP and verify access.


## Test Cases
Here are some test cases to ensure the system functions correctly under various scenarios:

1. **Correct OTP Entry:**
   - Generate an OTP.
   - Enter the correct OTP.
   - Expected Outcome: Access granted!

2. **Incorrect OTP Entry (Ones):**
   - Generate an OTP.
   - Enter an incorrect 6-digit numeric OTP.
   - Expected Outcome: Incorrect OTP, n attempts left.

3. **Incorrect OTP Entry (Max Attempts):**
   - Generate an OTP.
   - Enter incorrect 6-digit numeric OTP for all attempts.
   - Expected Outcome: You have exceeded maximum attempts. Access Denied!

4. **Invalid OTP Entry (Non-Digit Characters):**
   - Generate an OTP.
   - Enter alphabetic characters or special characters instead of digits.
   - Expected Outcome: Prompt for re-entry of OTP with an appropriate error message.

5. **Invalid OTP Entry (Incorrect Length):**
   - Generate an OTP.
   - Enter an OTP with fewer or more than 6 digits.
   - Expected Outcome: Prompt for re-entry of OTP with an appropriate error message.
