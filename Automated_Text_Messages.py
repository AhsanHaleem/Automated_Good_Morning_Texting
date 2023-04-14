from twilio.rest import Client
from pytz import timezone
import datetime
import time

# Twilio account credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
from_number = 'YOUR_TWILIO_PHONE_NUMBER'

# List of friends' phone numbers and their corresponding names
friends = {
    '+1123456789': 'Ahsan'
}

# Set the timezone to Eastern Standard Time (EST)
est_tz = timezone('US/Eastern')

# Infinite loop to keep checking the time
while True:
    now = datetime.datetime.now(est_tz)
    if now.hour == 11 and now.minute == 45:
        # Send "Good morning" text to each friend
        for to_number, name in friends.items():
            client = Client(account_sid, auth_token)
            message = f"Good morning, {name}!"
            try:
                client.messages.create(
                    body=message,
                    from_=from_number,
                    to=to_number
                )
                print(f"Sent 'Good morning' message to {name} at {to_number}")
                break
            except Exception as e:
                print(f"Failed to send 'Good morning' message to {name} at {to_number}: {e}")
    else:
        print("Waiting for 11:45 am EST...")
        time.sleep(30)  # Sleep for 30 seconds (1/2 minute) before checking the time again
