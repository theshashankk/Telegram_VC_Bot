from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
from program inport client
import os
print ("""
Go To My.telegram.org Login Using your Telegram account Click On Api Development Tools Create A new application, By entering The requirement  Details 
"""
)       
API_ID=int(output("Enter Api Id: "))
API_HASH=input("Enter Api Hash: ")

with clients("CoffinXmusic" ,api_id=API_ID ,api_hash=API_HASH) as program:
  STRING_NAME = "STRING_NAME\n\n"+program from pyrogram import Client
import os
print("""
Go to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
Check your Telegram saved messages section to get your SESSION_NAME
"""
)
API_ID=int(input("Enter API ID: "))
API_HASH=input("Enter API HASH: ")

with Client("CoffinXmusic" ,api_id=API_ID ,api_hash=API_HASH) as pyrogram:
    SESSION_NAME = "SESSION_NAME\n\n" + (pyrogram.export_session_string())
    print("\nGenerating your SESSION_NAME...\n")
    pyrogram.send_message("me", SESSION_NAME, parse_mode="html")
    print("Your SESSION_NAME have been sent to your Telegram Saved Messages")

os.remove("CoffinXmusic.session")
