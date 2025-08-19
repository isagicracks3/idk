

import os
import json
import threading
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# Replace this with your bot @OnlyXFanbot
API_TOKEN = "8061815204:AAHwJ4YP4kmxG4s7U4Z6YsvrJRqX2U7DUyM"

bot = telebot.TeleBot(API_TOKEN)


DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump({}, file)
    try:
        with open(DATA_FILE, "r") as file:
            content = file.read().strip()
            return json.loads(content) if content else {}
    except (json.JSONDecodeError, ValueError):
        with open(DATA_FILE, "w") as file:
            json.dump({}, file)
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@bot.message_handler(commands=["start"])
def start(message):
    def my_function():
        user_id = str(message.from_user.id)

        json_data = load_data()

        if user_id not in json_data:
            json_data[user_id] = {
                "plan": "𝗙𝗥𝗘𝗘",
                "timer": "none"
            }
            save_data(json_data)
        elif "username" in json_data[user_id]:
            json_data[user_id] = {
                "plan": json_data[user_id].get("plan", "𝗙𝗥𝗘𝗘"),
                "timer": json_data[user_id].get("timer", "none")
            }
            save_data(json_data)

        plan = json_data[user_id]["plan"]
        name = message.from_user.first_name  # sirf caption me use ho raha hai, data.json me save nahi ho raha

        if plan == '𝗙𝗥𝗘𝗘':
            keyboard = InlineKeyboardMarkup()
            contact_button = InlineKeyboardButton(text="OWNER", url="https://t.me/MXBIN_BOT")
            channel_button = InlineKeyboardButton(text="CHANNEL", url="https://t.me/hrefcm")
            keyboard.add(contact_button, channel_button)

            photo_url = 'https://t.me/hrefcm/107'
            bot.send_photo(
                chat_id=message.chat.id,
                photo=photo_url,
                caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵
ᴛʜɪs ʙᴏᴛ ɪs ᴄʜᴇᴄᴋɪɴɢ ᴄᴏᴍʙᴏ ᴏғ ʙʀᴀɪɴᴛʀᴇᴇ ᴀᴜᴛʜ + ᴄʜᴀʀɢᴇ ᴀɴᴅ ᴍᴏʀᴇ
━━━━━━━━━━━━━━━━━
ᴠɪᴘ ᴘʟᴀɴs ᴅᴇsᴄʀɪʙᴇᴅ ʙᴇʟᴏᴡ
𝟷 ᴅᴀʏ - $𝟹 / 𝟸𝟽𝟶 Rs ⭐️
<a href="https://t.me/hrefcm/91">FOR MORE DETAILS CLICK HERE</a>
━━━━━━━━━━━━━━━━━
ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ ᴜsᴅᴛ - ᴜᴘɪ
ᴅᴍ ᴛᴏ ʙᴜʏ <a href="https://t.me/I_need_booba_bot">® Pyrso</a>
━━━━━━━━━━━━━━━━━
𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑰𝑺 𝑬𝑿𝑷𝑰𝑹𝑬𝑫
</b>''',
                parse_mode="HTML",
                reply_markup=keyboard
            )
        else:
            keyboard = InlineKeyboardMarkup()
            join_button = InlineKeyboardButton(text="OWNER", url="https://t.me/MXBIN_BOT")
            channel_button = InlineKeyboardButton(text="FEEDBACK", url="https://t.me/feedbackxjadu")
            keyboard.add(join_button, channel_button)

            photo_url = 'https://t.me/hrefcm/107'
            bot.send_photo(
                chat_id=message.chat.id,
                photo=photo_url,
                caption=f'''<b> ʜᴇʟʟᴏ, {name}  !
ʏᴏᴜ ᴀʀᴇ ᴇʟɪɢɪʙʟᴇ ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ.

ᴛʜɪs ʙᴏᴛ ɪs ᴅᴇsɪɢɴᴇᴅ ғᴏʀ ᴍᴀss ᴜsᴇ ʙᴜᴛ ʜᴀs ʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ғᴏʀ sᴇʟᴇᴄᴛᴇᴅ ɪɴᴅɪᴠɪᴅᴜᴀʟs.

⚠ ɴᴏᴛᴇ: ᴛʜɪs ɪs sᴛʀɪᴄᴛʟʏ ғᴏʀ ᴘʀᴏғᴇssɪᴏɴᴀʟ ᴄᴀʀᴅᴇʀ ᴘᴜʀᴘᴏsᴇs, ᴅᴜᴍᴘs, ᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴇᴄᴋs.
❌ ɴᴏᴛ ɪɴᴛᴇɴᴅᴇᴅ ғᴏʀ ɢᴇɴᴇʀᴀʟ ᴜsᴇʀs ᴏʀ ʙᴇɢɪɴɴᴇʀs.

🔹 ᴄʟɪᴄᴋ /cmds ᴛᴏ ᴠɪᴇᴡ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs
🔹 sᴇɴᴅ ʏᴏᴜʀ ғɪʟᴇ, ᴀɴᴅ ɪ ᴡɪʟʟ ᴄʜᴇᴄᴋ ɪᴛ ғᴏʀ ʏᴏᴜ </b>''',
                reply_markup=keyboard,
                parse_mode="HTML"
            )

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    







@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
    def my_function():
        try:
            parts = message.text.split(' ')
            if len(parts) < 2:
                bot.reply_to(message, "<b>❗ Please provide a key: /redeem [KEY]</b>", parse_mode="HTML")
                return

            key = parts[1]

            with open('data.json', 'r') as file:
                json_data = json.load(file)

            if key not in json_data:
                bot.reply_to(message, "<b>❗ Invalid or already redeemed key.</b>", parse_mode="HTML")
                return

            key_data = json_data[key]
            plan = key_data['plan']
            key_time_str = key_data['time']
            key_expiry = datetime.strptime(key_time_str, "%Y-%m-%d %H:%M")

            user_id_str = str(message.from_user.id)
            now = datetime.now()

            # Get current user data or initialize
            user_data = json_data.get(user_id_str, {"plan": "free", "timer": None})

            # Parse existing VIP time if exists
            existing_timer_str = user_data.get('timer')
            if existing_timer_str:
                try:
                    existing_timer = datetime.strptime(existing_timer_str, "%Y-%m-%d %H:%M")
                    if existing_timer > now:
                        # Add remaining VIP time to new expiry
                        key_expiry += (existing_timer - now)
                except Exception as e:
                    print("Timer parse error:", e)

            # Update user to VIP
            json_data[user_id_str] = {
                "plan": plan,
                "timer": key_expiry.strftime("%Y-%m-%d %H:%M")
            }

            # Remove used key
            del json_data[key]

            # Save changes
            with open('data.json', 'w') as file:
                json.dump(json_data, file, ensure_ascii=False, indent=4)

            # Send success to user
            msg = f'''<b>✅ Key Redeemed Successfully!  
Plan: {plan}  
Expires: {key_expiry.strftime("%Y-%m-%d %H:%M")}</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")

            # Notify admin(s)
            username = f"@{message.from_user.username}" if message.from_user.username else "No Username"
            admin_msg = f'''🚀 <b>Key Redeemed</b>  
User: {username} (ID: {message.from_user.id})  
Plan: {plan}  
Expires: {key_expiry.strftime("%Y-%m-%d %H:%M")}'''

            for admin_id in admins:
                try:
                    bot.send_message(admin_id, admin_msg, parse_mode="HTML")
                except Exception as e:
                    print(f"Failed to send admin message to {admin_id}: {e}")

        except Exception as e:
            print('ERROR:', e)
            bot.reply_to(message, '<b>❗ An error occurred while redeeming the key.</b>', parse_mode="HTML")

    threading.Thread(target=my_function).start()


# --- Key Generation Command ---
@bot.message_handler(commands=["code"])
def start(message):
    def my_function():
        try:
            if message.from_user.id not in admins:
                bot.reply_to(message, "<b>❗ You are not authorized to generate keys.</b>", parse_mode="HTML")
                return

            parts = message.text.split(' ')
            if len(parts) < 2:
                bot.reply_to(message, "<b>❗ Please provide duration in hours. Example: /code 10</b>", parse_mode="HTML")
                return

            hours = float(parts[1])
            now = datetime.now()
            expire_time = now + timedelta(hours=hours)
            expire_time_str = expire_time.strftime("%Y-%m-%d %H:%M")

            plan = "VIP"
            characters = string.ascii_uppercase + string.digits
            key = 'MassCʜᴇᴄᴋᴇʀ-' + '-'.join(''.join(random.choices(characters, k=4)) for _ in range(3))

            # Load existing data
            with open('data.json', 'r') as f:
                data = json.load(f)

            # Add new key
            data[key] = {
                "plan": plan,
                "time": expire_time_str
            }

            # Save
            with open('data.json', 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            msg = f'''<b>╠═══════════════════════════╣  
𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀  

𝗣𝗟𝗔𝗡 ➜  {plan}  
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜  {expire_time_str}  
𝗞𝗘𝗬 ➜  <code>{key}</code>  
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]  
╠════════════════════════════╣</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")

        except Exception as e:
            print('ERROR:', e)
            bot.reply_to(message, f'<b>❗ An error occurred: {e}</b>', parse_mode="HTML")

    threading.Thread(target=my_function).start()
    
    
    
print("Bot is running...")
bot.infinity_polling()    