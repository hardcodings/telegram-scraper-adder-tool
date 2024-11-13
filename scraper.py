from telethon import TelegramClient
import csv

# Telegram API credentials (from my.telegram.org)
api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API Hash
phone_number = 'YOUR_PHONE_NUMBER'  # Your phone number with country code

# The group or channel to scrape users from
group_username = 'GROUP_OR_CHANNEL_USERNAME'  # Replace with the group's username

# Create the Telegram client and save session automatically
client = TelegramClient('session_name', api_id, api_hash)

async def scrape_users():
    # Connect and log in
    await client.start(phone_number)

    # Get the group or channel entity
    group = await client.get_entity(group_username)

    # Get all participants of the group or channel
    participants = await client.get_participants(group)

    # Open the file to write the scraped users
    with open('users.txt', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['id', 'username', 'name'])

        # Write user details to the file
        for user in participants:
            if user.username:
                username = user.username
            else:
                username = "None"

            name = (user.first_name or '') + ' ' + (user.last_name or '')

            writer.writerow([user.id, username, name])

    print(f"Scraped {len(participants)} users from {group.title}")

# Run the async function
with client:
    client.loop.run_until_complete(scrape_users())
