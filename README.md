# telegram-scraper-adder-tool
a tool that scrapes and add telegram users into groups and channels, both public and private

developer: https://t.me/profcoders

![tgm](https://github.com/user-attachments/assets/2b433cd1-3dd9-4ab7-b9e6-0ded7aafa5c2)

# ANALYSIS
- The script reads the users.txt file containing the users scraped from the previous script.
- It attempts to add those users to the specified group or channel. It handles common errors like privacy restrictions and rate limits (FloodWaitError).
- It uses the InviteToChannelRequest to add users to the group.

Developer: https://t.me/profcoders
# NOTES:
- Rate Limits: Telegram imposes restrictions on how many users you can add in a short period. If you encounter a FloodWaitError, you must respect the wait time or slow down your script.
- Privacy Settings: If a user has adding privacy restrictions (e.g., only allowing friends to add them to groups), the script will not be able to add them, and it will skip to the next user.
- Usernames: The script only attempts to add users with valid usernames, as Telegram primarily uses usernames for user interactions outside of contacts.

developer: https://t.me/profcoders
 
automated tool to scrape telegram users from a group and channel with auto forwarding feature and other features

TELEGRAM SCRAPER ADDER
TELEGRAM SCRAPER TOOL
TELEGRAM ADDER TOOL
TELEGRAM SCRAPING ADDING TOOL
TELEGRAM SCRAPER
TELEGRAM CHANNEL GROUP SCRAPER ADDER
TELEGRAM SCRAPER ADDER BOT
TELEGRAM CHANNEL SCRAPER 
TELEGRAM CHANNEL SCRAPER
TELEGRAM REPORT BAN TOOL
