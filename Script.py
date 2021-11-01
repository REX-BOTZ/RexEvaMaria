class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href='https://t.me/EvaMariaBot'>𝙴𝚅𝙰 𝙼𝙰𝚁𝙸𝙰</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """
    
🤖 My Name : <a href='https://telegram.dog/Filter_KristyBot'> Filter Admin Bot</a>
👨‍💻 Developer : <a href='https://telegram.dog/I_m_Kristy'>✯°• Iᴍ Kʀɪsᴛʏ கிறிஸ்டி Via @HiroshiBots •°✯ « Tᴇᴀᴍ Kʀɪsᴛʏ »</a>
📌 Credits : <a href='https://telegram.dog/TeamEvamaria'>EvaMaria</a> & <a href='https://github.com/EvamariaTG/EvaMaria
📡 Server : <a href='https://Heroku.com'>Heroku</a>
📕 Library : <a href='https://Pyrogram.com'>Pyrogram</a>
📦 Source Code : <a href='https://telegram.dog/WantSourceCode'>Click Here</a>
📢 Updates Channel : <a href='https://telegram.dog/KristyBots'>@KristyBots</a>
📮 Powerded By : <a href='https://telegram.dog/TamilMV_WEB'>@TamilMV_WEB</a>

"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """<b>Help : Manual Filters
    
    - Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Tessa Will Respond Whenever A Keyword Is Found The Message

NOTE :
---> @Filter_KristyBot Should Have Admin Privillage / Rights !!! 
---> Only Admins Can Add Filters In A Chat...
---> Alert Buttons Have A Limit Of 64 Characters...

Commands And Usage :
• /filter - <code>Add A Filter In Chat</code>
• /filters - <code>List All The Filters Of A Chat</code>
• /del - <code>Delete A Specific Filter In Chat</code>
• /delall - <code>Delete The Whole Filters In A Chat ( Chat Owner Only )</code></b>"""
    BUTTON_TXT = """<b>Help : Buttons

- @Filter_KristyBot Supports Both Url And Alert Inline Buttons.

NOTE :
---> Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
---> @Filter_KristyBot Supports Buttons With Any Telegram Media Type.
---> Buttons Should Be Properly Parsed As Markdown Format

URL Buttons :
<code>[Button Text](buttonurl:https://telegram.dog/KristyBots)</code>

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
