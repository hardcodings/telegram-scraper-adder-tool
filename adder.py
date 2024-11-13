from telethon import TelegramClient, errors
import csv

# Telegram API credentials (from my.telegram.org)
api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API Hash
phone_number = 'YOUR_PHONE_NUMBER'  # Your phone number with country code

# The target group or channel to add users to
target_group_username = 'TARGET_GROUP_OR_CHANNEL_USERNAME'  # Replace with the target group's username

# Create the Telegram client and save session automatically
client = TelegramClient('session_name', api_id, api_hash)

async def add_users_to_group():
    # Connect and log in
    await client.start(phone_number)

    # Get the target group or channel entity
    target_group = await client.get_entity(target_group_username)

    # Read the users from the file
    with open('users.txt', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        users = [row for row in reader]

    # Loop through each user and try to add them to the group
    for user in users:
        user_id = user[0]
        username = user[1]

        try:
            # Add the user to the group
            if username != "None":
                user_entity = await client.get_input_entity(username)
                await client(InviteToChannelRequest(target_group, [user_entity]))
                print(f"Added {username} to {target_group.title}")
            else:
                print(f"Skipping {user_id} because they have no username.")
        
        except errors.UserPrivacyRestrictedError:
            print(f"Cannot add {username} due to privacy settings.")
        except errors.FloodWaitError as e:
            print(f"Flood wait error. Sleeping for {e.seconds} seconds.")
            time.sleep(e.seconds)
        except Exception as e:
            print(f"Failed to add {username}: {str(e)}")

# Run the async function
with client:
    client.loop.run_until_complete(add_users_to_group())
