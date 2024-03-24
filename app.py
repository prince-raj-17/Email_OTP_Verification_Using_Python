import config
import random
import smtplib

# Function to generate a 6-digit OTP randomly
def generate_otp():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

# Function to send OTP to the user's email address
def send_otp_email(recipient_email, msg):
    sender_email = config.sender_email
    email_password = config.email_password

    # Define and login to server
    print("Setting up server........\n")
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls() 
    server.login(sender_email, email_password) 
    print("Loged in succefully!\n")

    # Send email to recepient with otp
    server.sendmail(sender_email, recipient_email, msg)
    print("OTP sent!\n")
    server.quit()

# Function to prompt user to enter OTP
def otp_prompt():
    while True:
        try:
            user_input = input("Please enter the 6-digit OTP: ")
            if len(user_input) != 6:
                raise ValueError("OTP must be exactly 6 digits")
            if not user_input.isdigit():
                raise ValueError("OTP must contain only numeric digits")
            return user_input
        except ValueError as ve:
            print("Error: ",ve)

# Function to verify OTP
def verify_otp(otp):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        user_input = otp_prompt()
        if user_input == otp:
            print("Access granted!")
            return True
        else:
            print(f"Incorrect OTP, {max_attempts - attempts -1} attempts left.")
            attempts += 1
    print("You have exceeded maximum attempts.\nAccess Denied!")
    return False

            
# Function to execute the OTP verification process
def main():
    otp = generate_otp()

    recipient_email = config.recipient_email
    msg = f"Subject: OTP Verification\n\nYour 6-digit otp is: {otp}"
    send_otp_email(recipient_email, msg)

    verify_otp(otp)

if __name__ == "__main__":
    main()