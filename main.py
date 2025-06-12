import pywhatkit
import datetime
import time
import csv

# Load contacts from CSV file
with open('contacts.csv', mode='r') as file:
    reader = csv.reader(file)
    contacts = [row[0] for row in reader]

message = "Hello! This is an automated message from Huzaifa."

# Send message to each contact
for contact in contacts:
    try:
        print(f"Sending to {contact}")
        pywhatkit.sendwhatmsg_instantly(
            contact,
            message,
            wait_time=15,       # Wait time before sending in seconds
            tab_close=False,    # Keep tab open
            close_time=15      # Optional: Close after 10 seconds
        )
        time.sleep(15)  # Wait between messages to avoid being blocked
    except Exception as e:
        print(f"Failed to send to {contact}: {e}")
