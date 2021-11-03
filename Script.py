class script(object):
    START_TXT = """<b>𝗛𝗘𝗟𝗟𝗢 {},

𝗜 𝗔𝗠 𝗦𝗨𝗣𝗘𝗥 𝗔𝗨𝗧𝗢 𝗙𝗜𝗟𝗧𝗘𝗥 𝗕𝗢𝗧..𝗜 𝗖𝗔𝗡 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗚𝗿𝗼𝘂𝗽𝘀....\n\n𝗝𝗨𝗦𝗧 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗪𝗜𝗧𝗛 𝗔𝗗𝗠𝗜𝗡 𝗥𝗜𝗚𝗛𝗧𝗦 𝗔𝗡𝗗 𝗘𝗡𝗝𝗢𝗬 😍\n\n👨‍💻 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : <a href='https://telegram.dog/KOT_FREE_DE_LA_HOYA_OFF'>ᴋᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>"""
    HELP_TXT = """<b>Bruh {}
Here Is The Help For My Commands</b>."""
    ABOUT_TXT = """<b>
🤖 My Name : <a href='https://telegram.dog/KOT_MOVIES_FILTER_BOT'>Kᴏᴛ Tʜᴀʟᴀᴘᴀᴛʜʏ Vɪᴊᴀʏ</a>
 
👨‍💻 Developer : <a href='https://telegram.dog/KOT_FREE_DE_LA_HOYA_OFF'>Kᴏᴛ Dᴇᴠᴇʟᴏᴘᴇʀ</a>
  
📌 Credits : <a href='https://telegram.dog/KOT_REPORS'>@KOT REPORTS</a>
  
📡 Server : <a href='https://Heroku.com'>Heroku</a>
  
📕 Library : <a href='https://Pyrogram.com'>Pyrogram</a>
  
📦 Source Code : <a href='https://telegram.dog/KOT_Source_Code'>𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘</a>
  
📢 Updates Channel : <a href='https://telegram.dog/KristyBots'>@𝗞𝗢𝗧 𝗕𝗢𝗧𝗦</a>
  
📮 Powerded By : <a href='https://telegram.dog/KING_OF_THE_CARTOONS_CHANNEL'>@𝗞𝗢𝗧 𝗖𝗔𝗥𝗧𝗢𝗢𝗡𝗦</a>
"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝗞𝗢𝗧 𝗧𝗛𝗔𝗟𝗔𝗣𝗔𝗧𝗛𝗬 𝗩𝗜𝗝𝗔𝗬 is a open source project. 
- Source - https://t.me/KOT_SOURCE_CODE

<b>DEVS:</b>
- <a href=https://t.me/KOT_DEVELOPERS>𝗧𝗘𝗔𝗠 𝗞𝗢𝗧</a>"""
    MANUELFILTER_TXT = """<b>Help : Manual Filters
    
    - Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Tessa Will Respond Whenever A Keyword Is Found The Message

NOTE :
---> @KOT_MOVIES_FILTER_BOT Should Have Admin Privillage / Rights !!! 
---> Only Admins Can Add Filters In A Chat...
---> Alert Buttons Have A Limit Of 64 Characters...

Commands And Usage :
• /filter - <code>Add A Filter In Chat</code>
• /filters - <code>List All The Filters Of A Chat</code>
• /del - <code>Delete A Specific Filter In Chat</code>
• /delall - <code>Delete The Whole Filters In A Chat ( Chat Owner Only )</code></b>"""
    BUTTON_TXT = """<b>Help : Buttons

- @KOT_MOVIES_FILTER_BOT Supports Both Url And Alert Inline Buttons.

NOTE :
---> Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
---> @KOT_MOVIES_FILTER_BOT Supports Buttons With Any Telegram Media Type.
---> Buttons Should Be Properly Parsed As Markdown Format

URL Buttons :
<code>[Button Text](buttonurl:https://telegram.dog/KOT_BOTS)</code>

Alert buttons :
<code>[Button Text](buttonalert:This Is An Alert Message)</code></b>"""
    CONNECTION_TXT = """<b>Help : Connections

- Used To Connect Bot To PM For Managing Filters 
- It Helps To Avoid Spamming In Groups.

NOTE :
---> Only Admins Can Add A Connection.
---> Send <code>/connect</code> For Connecting Me To Ur PM

Commands And Usage :
• /connect  - <code>Connect A Particular Chat To Your PM</code>
• /disconnect  - <code>Disconnect From A Chat</code>
• /connections - <code>List All Your Connections</code></b>"""
    EXTRAMOD_TXT = """<b>Help : Extra Modules

Commands And Usage :
• /id - <code>Get Id Of A Specifed User.</code>
• /info  - <code>Get Information About A User.</code>
• /imdb  - <code>Get The Film Information From IMDB Source.</code>
• /search  - <code>Get The Film Information From Various Sources.</code></b>"""
    ADMIN_TXT = """<b>Help : Admin mods

NOTE :
This Module Only Works For My Admins

Commands and Usage :
• /logs - <code>To Get The Rescent Errors</code>
• /stats - <code>To Get Status Of Files In Db.</code>
• /users - <code>To Get List Of My Users And Ids.</code>
• /chats - <code>To Get List Of The My Chats and Ids </code>
• /leave  - <code>To Leave From A Chat.</code>
• /disable  -  <code>Do Disable A Chat.</code>
• /ban  - <code>To Ban a User.</code>
• /unban  - <code>To Unban a User.</code>
• /channel - <code>To Get List Of Total Connected Channels</code>
• /broadcast - <code>To Broadcast a Message To All Users</code></b>"""
    STATUS_TXT = """<b>--> Total Files</b> : <code>{}</code>
<b>--> Total Users</b> : <code>{}</code>
<b>--> Total Chats</b> : <code>{}</code>
<b>--> Used Storage</b> : <code>{}</code> MIB
<b>--> Free Storage</b> : <code>{}</code> MIB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
