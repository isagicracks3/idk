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

#8061815204:AAE5tG35y-Ztsyq1aXHFByqTjs4OoXMHsUY
API_TOKEN = "7567332983:AAEdMfS5Lg_H0pSJ6-9qNf-dBwHO5ggbmA0"

bot = telebot.TeleBot(API_TOKEN)

command_usage = {}
BANK_NAME_FIXES = {}  

# Channel ID for forwarding reports
REPORT_CHANNEL_ID = -1001903160469
REQUIRED_CHANNEL = -1002311823274 




#============ Api Import ==≠=====≠==

from reg import reg
from gate import Tele   #===|
from gatet import Fele   #====|  Mutiple 
from gatat import Gele #===|
from stripe import au # au,mass,stxt 
from Shopify import vbv #sh,msh
from pay import pp # pp,mpp
from sq import sq # sq ,msq 
from mix import sk #sk ,msk
from cr import cr #cr ,mcr


# chk = Tele
# b3txt = multiple (not implement)
# cchk = 
# au = ppc
# mass = 
# ustxt = st (not implement)
# sh = vbv
# msh = vbv


# start
# help
# cmds
# ping
# id
# fl
# gen
# bin
# mbin
# chk
# au
# b3txt
# stxt
# nikal
# user vip
# redeem
# code
# sh
# msh

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
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- START CALLBACKS ---
@bot.message_handler(commands=["start"])
def start(message):
    def handle_start():
        user_id = str(message.from_user.id)
        name = message.from_user.first_name

        data = load_data()
        if user_id not in data:
            data[user_id] = {"plan": "FREE", "timer": "none"}
            save_data(data)

        # Inline menu
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("Gate", callback_data="gate"),
            InlineKeyboardButton("Tools", callback_data="tools"),
            InlineKeyboardButton("Update", url="https://t.me/hrefcm/111"),
            InlineKeyboardButton("Premium", callback_data="premium")
        )

        bot.reply_to(message, """✦━━━[ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʀᴀᴠᴀɴ ᴄʜᴇᴄᴋᴇʀ  ]━━━✦

⟡ ʙᴏᴛ sᴛᴀᴛᴜs 𝟸𝟶𝟶 ᴏᴋ ʟɪᴠᴇ  
⟡ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴍᴇᴍʙᴇʀꜱ ᴏɴʟʏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ  
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  

⟡ ғᴏʀ ʜᴇʟᴘ ᴠɪsɪᴛ /help
⟡ ᴛᴏ ʙᴜʏ /buy  
⟡ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ ᴜsᴅᴛ  
⟡ ʟᴀsᴛ : ᴀsɪᴀ 𝟸𝟶/𝟶𝟿/𝟸𝟶𝟸𝟻  𝟺:𝟸𝟶 ᴘᴍ
⟡ ᴇxᴘʟᴏʀᴇ - ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴅɪsᴄᴏᴠᴇʀ
ᴀʟʟ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇs ᴡᴇ ᴏғғᴇʀ!
""", parse_mode="HTML", reply_markup=markup)

    threading.Thread(target=handle_start).start()


# --- CALLBACK HANDLERS ---
@bot.callback_query_handler(func=lambda call: call.data in ["gate", "auth", "charge", "tools", "premium", "close"])

def callback_handler(call):
    if call.data == "gate":
        text = """Check Our Features
Main : @hrefcm
Chat Group : @worstgenerationofgenzz

Note : Report Bugs To @Live_ShopX1Bot
Proxy : Live 💎

Choose Your Gate Type :
"""
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("Auth", callback_data="auth"),
            InlineKeyboardButton("Charge", callback_data="charge"),
            InlineKeyboardButton("Tools", callback_data="tools"),
            InlineKeyboardButton("Premium", callback_data="premium")
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "auth":
        text = """AUTH GATES
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: Braintree Auth - 1
⟐ Command: /chk cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
═══════════════════
⟐ Name: Braintree Auth - 1
⟐ Mass Cmd: /mchk cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: Braintree Auth - 1
⟐ Txt Mass Cmd: /ctxt cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: Stripe Auth - 1
⟐ Command: /au cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Plan : FREE
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: Stripe Auth - 1
⟐ Mass Cmd: /mass cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Plan : FREE
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: Stripe Auth - 1
⟐ Txt Mass Cmd: /stxt cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: square Auth - 1
⟐ Command: /sq cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Plan : FREE
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: square Auth - 1
⟐ Mass Cmd: /msq cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: square Auth - 1
⟐ Txt Mass Cmd: /qt cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Note: Only For Premium Users

"""
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("⬅️ Back", callback_data="gate"),
            InlineKeyboardButton("✖ Close", callback_data="close")
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "charge":
        text = """ 〔Charge〕
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: Stripe 1$
⟐ Command: /cr cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Plan : FREE
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Mass Cmd: /mcr cc|mes|ano|cvv
⟐ Limit: 10
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: paypal 1$
⟐ Command: /pp cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Plan : FREE
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Mass Cmd: /mpp cc|mes|ano|cvv
⟐ Limit: 10
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: shopify 1$
⟐ Command: /sh cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Plan : FREE
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Mass Cmd: /msh cc|mes|ano|cvv
⟐ Limit: 10
⟐ Status: Active ✅
⟐ Note: Only For Premium Users
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Name: shopify x stripe 1$
⟐ Command: /sk cc|mes|ano|cvv
⟐ Status: Active ✅
⟐ Plan : FREE
━ ━ ━ ━ ━━━ ━ ━ ━ ━
⟐ Mass Cmd: /msk cc|mes|ano|cvv
⟐ Limit: 10
⟐ Status: Active ✅
⟐ Note: Only For Premium Users


"""
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("⬅️ Back", callback_data="gate"),
            InlineKeyboardButton("✖ Close", callback_data="close")
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
       
    elif call.data == "tools":
        text = """📋 Available Commands:

🔍 Check Tools:

⚙️ Generators:
•  ɢᴇɴᴇʀᴀᴛᴏʀ – /gen 

💳 BIN Tools:
• ғɪʟᴛᴇʀ ᴄᴄ – /fl 
• ʟᴏᴏᴋʜᴜʙ ʙɪɴ – /bin 
•  ᴍᴏʀᴇ ʙɪɴ ᴛᴏᴏʟs – /mbin

🆔 User Tools:
• sʜᴏᴡ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ – /id 
"""
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("⬅️ Back", callback_data="gate"),
            InlineKeyboardButton("✖ Close", callback_data="close")
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "premium":
        text = """❯  Buy Ravan premium BOT

- Plan: TrialX - 1  
- Credits: 40
- Price: $1 
- Validity: 1 Days

- Plan: TrialX - 2  
- Credits: 400
- Price: $10
- Validity: 15 Days

- Plan: ForeverPro 🎖️  
- Credits: 999  
- Price: $15  
- Validity: 20 Days

- To purchase, contact the provider only.
-  service providers @MKNXW
"""
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")


    elif call.data == "close":
        bot.delete_message(call.message.chat.id, call.message.message_id)


# --- /help command ---
@bot.message_handler(commands=['help'])
def help_command(message):
    help_msg = '''<b>⚙️ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs</b>
🆘 @MKNXW
🆔  ᴠɪᴇᴡ ᴀᴄᴄᴏᴜɴᴛ ɪɴғᴏ /id 
🏓  ᴄʜᴇᴄᴋ ʙᴏᴛ ʟᴀᴛᴇɴᴄʏ /ping '''
    bot.reply_to(message, help_msg, parse_mode='HTML')
    

@bot.message_handler(commands=['cmds'])
def send_command_list(message):
    msg = '''<b>📋 Available Commands:</b>

🔍 <b>Check Tools:</b>
• <code>/chk</code> – B3 ᴀᴜᴛʜ ᴄʜᴇᴄᴋᴇʀ
• <code>/cchk</code> – ᴍᴀss ᴀᴜᴛʜ ᴄʜᴇᴄᴋᴇʀ
• <code>/b3txt</code> – [sᴏᴏɴ]
• <code>/au</code> – sᴛʀɪᴘᴇ ᴀᴜᴛʜ
• <code>/mass</code> – ᴍᴀss sᴛʀɪᴘᴇ
• <code>/ustxt</code> – [sᴏᴏɴ]
• <code>/sh</code> – sʜᴏᴘɪғʏ ᴄʜᴀʀɢᴇ $0.98  
• <code>/msh</code> – ᴍᴀss ᴄʜᴀʀɢᴇ ᴄʜᴇᴄᴋᴇʀ 

⚙️ <b>Generators:</b>
• <code>/gen</code> – ɢᴇɴᴇʀᴀᴛᴏʀ  

💳 <b>BIN Tools:</b>
• <code>/fl</code> – ғɪʟᴛᴇʀ ᴄᴄ
• <code>/bin</code> – ʟᴏᴏᴋʜᴜʙ ʙɪɴ
• <code>/mbin</code> – ᴍᴏʀᴇ ʙɪɴ ᴛᴏᴏʟs

🆔 <b>User Tools:</b>
• <code>/id</code> – sʜᴏᴡ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ
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
Credits: 0"""
    
    bot.reply_to(message, id_info, parse_mode='HTML')

import telebot
import re
import os


# Handler for both /fl and .fl commands
@bot.message_handler(commands=['fl'])  # Handles /fl
@bot.message_handler(regexp=r'^\.fl')  # Handles .fl
def filter_cards(message):
    try:
        # Get the message text or replied message text
        if message.reply_to_message and message.reply_to_message.text:
            input_text = message.reply_to_message.text
        else:
            # Remove command prefix (/fl or .fl) from the text
            input_text = message.text[3:] if message.text.startswith('/fl') else message.text[3:]

        # Handle file attachments if present
        if message.reply_to_message and message.reply_to_message.document:
            file_info = bot.get_file(message.reply_to_message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            input_text = downloaded_file.decode('utf-8')

        # Process the input text
        if input_text:
            all_cards = input_text.split('\n')
        else:
            all_cards = []

        cards = ""
        for cc in all_cards:
            try:
                # Extract numbers using regex
                x = re.findall(r'\d+', cc)
                if len(x) >= 4:  # Ensure we have all required fields
                    ccn = x[0]    # Card number
                    mm = x[1]     # Month
                    yy = x[2]     # Year
                    cvv = x[3]    # CVV

                    # Fix common format issues
                    if mm.startswith('2'):  # If month starts with 2, swap with year
                        mm, yy = yy, mm
                    if len(mm) >= 3:       # If month is too long, rearrange
                        mm, yy, cvv = yy, cvv, mm

                    # Validate card number length
                    if 15 <= len(ccn) <= 16:
                        cards += f"{ccn}|{mm}|{yy}|{cvv}\n"
            except:
                continue

        # Send response based on results
        if cards:
            card_count = len(cards.split('\n')) - 1  # Subtract 1 for empty last line
            if card_count >= 32:
                # Save to file and send as document
                filename = 'Filtered_Cards.txt'
                with open(filename, 'w') as file:
                    file.write(cards)
                with open(filename, 'rb') as file:
                    bot.reply_to(message, f"Filtered {card_count} cards", parse_mode='HTML')
                    bot.send_document(message.chat.id, file, reply_to_message_id=message.message_id)
                os.remove(filename)
            else:
                # Send as text message
                bot.reply_to(
                    message,
                    f"<code>{cards}</code>",
                    parse_mode='HTML'
                )
        else:
            bot.reply_to(
                message,
                "<b>Filter Failed ⚠️\n\nNo Valid Cards Found in the Input.</b>",
                parse_mode='HTML'
            )

    except Exception as e:
        bot.reply_to(
            message,
            f"Error occurred: {str(e)}"
        )



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


owners = ['5995041264', '8009385011','']  # Add your admin user IDs as strings

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



admins = [5995041264,8009385011]
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
            key = 'MassCʜᴇᴄᴋᴇʀ-' + '-'.join(''.join(random.choices(characters, k=4)) for _ in range(3))

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
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🤖 Bot Status: Active ✅

🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot and stay updated — make sure to join our channel!
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴀᴜᴛʜᴏʀɪᴢᴇᴅ &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  

🆘 Need help?
Use /help anytime for support.</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
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
    gate = 'Shopify charge $0.98'
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
            "ᴜsᴀɢᴇ: /msh ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
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

    result = ["↯ Shopify charge $0.98 ♻️\n"]
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
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🤖 Bot Status: Active ✅

🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot and stay updated — make sure to join our channel!
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴀᴜᴛʜᴏʀɪᴢᴇᴅ &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  

🆘 Need help?
Use /help anytime for support.</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
        return  

    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  Shopify charge $0.98 ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_cmds_command, args=(message, msg)).start()

import telebot
import re
import time
import threading
import json
import os
from datetime import datetime, timedelta
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import csv
import pycountry

REQUIRED_CHANNEL = -1002311823274
CSV_FILE = 'bins_all.csv'
BANK_NAME_FIXES = {}  # Assuming this is defined elsewhere
GATE_FUNCTIONS = [Tele, Fele, Gele]  # Assuming these are defined
CHECKERS_STXT = [au]  # Assuming st is defined
CHECKERS_ct = [cr]  # Assuming st is defined for /qtxt (was /ct in your code)

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

    BIN_LOGS[bin_number]["declines"] = [t for t in BIN_LOGS[bin_number]["declines"] if now - t <= timedelta(minutes=20)]
    BIN_LOGS[bin_number]["risks"] = [t for t in BIN_LOGS[bin_number]["risks"] if now - t <= timedelta(minutes=20)]

    if len(BIN_LOGS[bin_number]["declines"]) >= 14 or len(BIN_LOGS[bin_number]["risks"]) >= 4:
        add_to_blacklist(bin_number)

# --- Load BIN Info from CSV ---
def expand_bank_name(bank_name):
    words = bank_name.split()
    expanded_words = [BANK_NAME_FIXES.get(word, word) for word in words]
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

def get_country_name(code, fallback_country_name):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else fallback_country_name
    except Exception as e:
        print(f"Error getting country name: {e}")
        return fallback_country_name

def is_valid_cc_format(line):
    pattern = r'^\d{15,16}\|\d{2}\|\d{2,4}\|\d{3}$'
    return bool(re.match(pattern, line.strip()))

def get_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    return json_data.get(str(user_id), {}).get("plan", "FREE")

# --- /b3txt Command ---
active_checks = {}
stopuser = {}

@bot.message_handler(commands=['ctxt'])
@bot.message_handler(regexp=r'^\.ctxt')
def ustxt_cmd(message):
    user_id = str(message.from_user.id)  # Ensure str
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Txt Braintree ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    if not (message.reply_to_message and message.reply_to_message.document):
        bot.reply_to(message,
            "ɢᴀᴛᴇ ɴᴀᴍᴇ: sᴛʀɪᴘᴇ ᴀᴜᴛʜ ♻️\n\n"
            "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
            "ᴜsᴀɢᴇ: /ctxt [ reply to fileLimited 1K ]"
        )
        return

    handle_ustxt_command(message)

def handle_ustxt_command(message):
    user_id = str(message.from_user.id)  # Ensure str
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Braintree ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
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
                "ᴜsᴀɢᴇ: /ctxt [ reply to file Limited 10K ]"
            )
            return

        active_checks[user_id] = active_checks.get(user_id, 0) + 1
        msg = bot.reply_to(message, f"𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 {len(cards)}  𝘾𝙖𝙧𝙙𝙨...⌛", parse_mode="HTML")

        stopuser[user_id] = {'status': 'start'}

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
    if str(call.from_user.id) == user_id:  # Ensure str comparison
        stopuser[user_id] = {'status': 'stop'}
        bot.answer_callback_query(call.id, "Stopping your check...")
    else:
        bot.answer_callback_query(call.id, "❌ You can't stop someone else's check.")

# --- /stxt Command ---
active_checks_stxt = {}
stopuser_stxt = {}

@bot.message_handler(commands=['stxt'])
@bot.message_handler(regexp=r'^\.stxt')
def stxt_cmd(message):
    user_id = str(message.from_user.id)  # Ensure str
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: TxT stripe ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
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
    user_id = str(message.from_user.id)  # Ensure str
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Txt stripe ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
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

        stopuser_stxt[user_id] = {'status': 'start'}

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
𝐂𝐨𝐮𝐧𝐭𝐣: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} seconds
</b>'''
                bot.send_message(message.chat.id, msg, parse_mode="HTML")

            elif any(x in result.lower() for x in ["3d_required", "otp", "action_required", "3d", "risk"]):
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
    if str(call.from_user.id) == user_id:  # Ensure str comparison
        stopuser_stxt[user_id] = {'status': 'stop'}
        bot.answer_callback_query(call.id, "Stopping your check...")
    else:
        bot.answer_callback_query(call.id, "❌ You can't stop someone else's check.")

# --- /qtxt Command ---
active_checks_ct = {}
stopuser_ct = {}

@bot.message_handler(commands=['qtxt'])
@bot.message_handler(regexp=r'^\.qtxt')
def ct_cmd(message):
    user_id = str(message.from_user.id)  # Ensure str
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Txt square ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    if not (message.reply_to_message and message.reply_to_message.document):
        bot.reply_to(message,
            "ɢᴀᴛᴇ ɴᴀᴍᴇ: square ᴀᴜᴛʜ ♻️\n\n"
            "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
            "ᴜsᴀɢᴇ: /qtxt [ reply to fileLimited 1K ]"
        )
        return

    handle_ct_command(message)

def handle_ct_command(message):
    user_id = str(message.from_user.id)  # Ensure str
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Txt square ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    if active_checks_ct.get(user_id, 0) >= 2:
        bot.reply_to(message, "⚠️ You already have 2 active /qtxt checks running.")
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

        active_checks_ct[user_id] = active_checks_ct.get(user_id, 0) + 1

        msg = bot.reply_to(message, f"𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 {len(cards)}  𝘾𝙖𝙧𝙙𝙨...⌛", parse_mode="HTML")

        stopuser_ct[user_id] = {'status': 'start'}

        threading.Thread(target=process_cards_ct, args=(message, msg.message_id, cards, user_id)).start()

    except Exception:
        bot.reply_to(message, "⚠️ Unable to read the file.")

def process_cards_ct(message, message_id, cards, user_id):
    approved, declined, otp_cards = 0, 0, 0
    total = len(cards)
    checked_cards = set()
    start_all = time.time()

    try:
        for cc in cards:
            if stopuser_ct.get(user_id, {}).get('status') == 'stop':
                elapsed = time.time() - start_all
                elapsed_formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=message_id,
                    text=f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - square auth play ♻️\n\n"
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
                checker = random.choice(CHECKERS_ct)
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
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: /qtxt Gateway
𝐑𝐞𝐬𝗽𝗼𝗻𝐬𝗲: {result}

𝗜𝗻𝗳𝗼: <code>{cc[:6]} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} seconds
</b>'''
                bot.send_message(message.chat.id, msg, parse_mode="HTML")

            elif any(x in result.lower() for x in ["3d_required", "otp", "action_required", "3d", "risk"]):
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
                InlineKeyboardButton("Stop", callback_data=f"stopct_{user_id}")
            )

            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=message_id,
                text=f"Checking Card <code>{cc}</code>\nGate ➜ <b>square auth play </b>",
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
            text=f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - square auth play ♻️\n\n"
                 f"- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 -  {total}\n"
                 f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜   {approved}\n"
                 f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜  {declined}\n"
                 f"• 3D Card 🏴‍☠️ ➜  {otp_cards}\n"
                 f"Time: {elapsed_formatted}\n"
                 f"𝐒𝐭𝐚𝐭𝐮𝐬 - Checked All ✅\n",
            parse_mode="HTML"
        )        

    finally:
        active_checks_ct[user_id] = max(0, active_checks_ct.get(user_id, 1) - 1)
        stopuser_ct.pop(user_id, None)

@bot.callback_query_handler(func=lambda call: call.data.startswith('stopct_'))
def stop_ct(call):
    user_id = call.data.split('_')[1]
    if str(call.from_user.id) == user_id:  # Ensure str comparison
        stopuser_ct[user_id] = {'status': 'stop'}
        bot.answer_callback_query(call.id, "Stopping your check...")
    else:
        bot.answer_callback_query(call.id, "❌ You can't stop someone else's check.")
 
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


# ======== BLACKLIST SYSTEM ==========

BLACKLIST_FILE = "blacklist.txt"
blacklisted_bins = {}
decline_tracker = defaultdict(lambda: deque())
risk_tracker = defaultdict(int)


def load_blacklist():
    global blacklisted_bins
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    bin_num, timestamp = parts
                    blacklisted_bins[bin_num] = float(timestamp)


def save_blacklist():
    with open(BLACKLIST_FILE, "w") as f:
        for bin_num, timestamp in blacklisted_bins.items():
            f.write(f"{bin_num}|{timestamp}\n")


def add_to_blacklist(bin_num):
    expire_time = time.time() + 48 * 3600  # 48 hrs
    blacklisted_bins[bin_num] = expire_time
    save_blacklist()


def is_blacklisted(bin_num):
    if bin_num in blacklisted_bins:
        if time.time() < blacklisted_bins[bin_num]:
            return True
        else:
            # expired, remove
            del blacklisted_bins[bin_num]
            save_blacklist()
            return False
    return False


def track_decline(bin_num):
    now = dt.datetime.now()
    dq = decline_tracker[bin_num]
    dq.append(now)
    while dq and (now - dq[0]).seconds > 1200:  # last 20 mins
        dq.popleft()
    if len(dq) >= 14:
        add_to_blacklist(bin_num)


def track_risk(bin_num):
    risk_tracker[bin_num] += 1
    if risk_tracker[bin_num] >= 4:
        add_to_blacklist(bin_num)
        risk_tracker[bin_num] = 0

# Load saved blacklist at startup
load_blacklist()

# =========== BIN INFO ==============

def expand_bank_name(bank_name):
    words = bank_name.split()
    expanded_words = [BANK_NAME_FIXES.get(word, word) for word in words]
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

def get_country_name(code, fallback_country_name):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else fallback_country_name
    except Exception as e:
        print(f"Error getting country name: {e}")
        return fallback_country_name


# ===================== HANDLER =====================

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
    user_id = str(message.from_user.id)  # Ensure str
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Braintree ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    # --- Extract CC ---
    try:
        cc = message.reply_to_message.text if message.reply_to_message else message.text
        cc = str(reg(cc))  # 🔁 Assumes reg() is defined
    except:
        cc = 'None'

    if cc == 'None':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Braintree ᴀᴜᴛʜ ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ɪɴ ʏᴏᴜʀ ɪɴᴘᴜᴛ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /chk ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ</b>''', parse_mode="HTML")
        return

    # --- Rate Limit Check ---
    current_time = datetime.now()
    last_usage = command_usage.get(user_id, None)

    if last_usage and (current_time - last_usage).seconds < 40:
        remaining_time = 40 - (current_time - last_usage).seconds
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    command_usage[user_id] = current_time
    processing_msg = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id
    threading.Thread(target=process_chk_command, args=(message, processing_msg, cc)).start()


# ===================== WORKER =====================

def process_chk_command(message, processing_msg_id, cc):
    gate = 'Braintree ᴀᴜᴛʜ'
    start_time = time.time()
    bin_num = cc[:6]

    # --- Blacklist check ---
    if is_blacklisted(bin_num):
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=processing_msg_id,
            text=f"❌ Message Sorry But This Bin({bin_num}) is on my blacklist!",
            parse_mode="HTML"
        )
        return

    try:
        last = str(Tele(cc))  # 🔁 Assumes Tele() is defined
    except Exception as e:
        last = 'Error'

    # --- BIN Info ---
    bin_info = get_bin_info_from_csv(bin_num)
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
    msg = f'''<b>𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}

𝗜𝗻𝗳𝗼: <code>{bin_num} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
</b>'''

    msgd = f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}

𝗜𝗻𝗳𝗼: <code>{bin_num} - {card_type} - {brand} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝗧𝗶𝗺𝗲: {execution_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
</b>'''

    # --- Track decline & risk ---
    if "risk_threshold" in last.lower():
        track_risk(bin_num)

    if any(x in last.lower() for x in ['funds', 'invalid postal', 'avs', 'added', 'duplicate', 'approved', 'allowed', 'purchase']):
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msg, parse_mode="HTML")
    else:
        track_decline(bin_num)
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msgd, parse_mode="HTML")


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
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot You Have To Join The Channels
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  
</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
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
        last = str(au(cc)) 
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


sq_command_usage = {}  # To track rate limits

# --- Rate limit function ---
def check_sq_rate_limit(user_id, cooldown):
    last_usage = sq_command_usage.get(user_id)
    if last_usage:
        elapsed_time = (datetime.now() - last_usage).seconds
        if elapsed_time < cooldown:
            return cooldown - elapsed_time
    sq_command_usage[user_id] = datetime.now()
    return 0

# --- .sq / /sq command handler ---
@bot.message_handler(func=lambda message: message.text.lower().startswith(('.sq', '/sq')))
def respond_to_sq(message):
    user_id = message.from_user.id
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot You Have To Join The Channels
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  
</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
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
            text='''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: square ᴀᴜᴛʜ ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /sq ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ</b>''',
            parse_mode="HTML"
        )
        return

    # --- Cooldown check ---
    cooldown = 35
    remaining_time = check_sq_rate_limit(user_id, cooldown)
    if remaining_time > 0:
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    processing_msg = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id

    threading.Thread(target=process_sq_command, args=(message, processing_msg, cc)).start()

# --- Main logic thread ---
def process_sq_command(message, processing_msg_id, cc):
    gate = 'square ᴀᴜᴛʜ'
    start_time = time.time()

    try:
        last = str(sq(cc)) 
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


cr_command_usage = {}  # To track rate limits

# --- Rate limit function ---
def check_cr_rate_limit(user_id, cooldown):
    last_usage = cr_command_usage.get(user_id)
    if last_usage:
        elapsed_time = (datetime.now() - last_usage).seconds
        if elapsed_time < cooldown:
            return cooldown - elapsed_time
    cr_command_usage[user_id] = datetime.now()
    return 0

# --- .cr / /cr command handler ---
@bot.message_handler(func=lambda message: message.text.lower().startswith(('.cr', '/cr')))
def respond_to_cr(message):
    user_id = message.from_user.id
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot You Have To Join The Channels
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  
</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
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
            text='''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: stripe charge ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /cr ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ</b>''',
            parse_mode="HTML"
        )
        return

    # --- Cooldown check ---
    cooldown = 35
    remaining_time = check_cr_rate_limit(user_id, cooldown)
    if remaining_time > 0:
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    processing_msg = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id

    threading.Thread(target=process_cr_command, args=(message, processing_msg, cc)).start()

# --- Main logic thread ---
def process_cr_command(message, processing_msg_id, cc):
    gate = 'stripe charge'
    start_time = time.time()

    try:
        last = str(cr(cc)) 
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


pp_command_usage = {}  # To track rate limits

# --- Rate limit function ---
def check_pp_rate_limit(user_id, cooldown):
    last_usage = pp_command_usage.get(user_id)
    if last_usage:
        elapsed_time = (datetime.now() - last_usage).seconds
        if elapsed_time < cooldown:
            return cooldown - elapsed_time
    pp_command_usage[user_id] = datetime.now()
    return 0

# --- .pp / /pp command handler ---
@bot.message_handler(func=lambda message: message.text.lower().startswith(('.pp', '/pp')))
def respond_to_pp(message):
    user_id = message.from_user.id
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "ppeator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot You Have To Join The Channels
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  
</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
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
            text='''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: PayPal charge ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /pp ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ</b>''',
            parse_mode="HTML"
        )
        return

    # --- Cooldown check ---
    cooldown = 35
    remaining_time = check_pp_rate_limit(user_id, cooldown)
    if remaining_time > 0:
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    processing_msg = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id

    threading.Thread(target=process_pp_command, args=(message, processing_msg, cc)).start()

# --- Main logic thread ---
def process_pp_command(message, processing_msg_id, cc):
    gate = 'PayPal charge'
    start_time = time.time()

    try:
        last = str(pp(cc)) 
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


sh_command_usage = {}  # To track rate limits

# --- Rate limit function ---
def check_sh_rate_limit(user_id, cooldown):
    last_usage = sh_command_usage.get(user_id)
    if last_usage:
        elapsed_time = (datetime.now() - last_usage).seconds
        if elapsed_time < cooldown:
            return cooldown - elapsed_time
    sh_command_usage[user_id] = datetime.now()
    return 0

# --- .sh / /sh command handler ---
@bot.message_handler(func=lambda message: message.text.lower().startswith(('.sh', '/sh')))
def respond_to_sh(message):
    user_id = message.from_user.id
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "sheator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot You Have To Join The Channels
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  
</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
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
            text='''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Shopify charge ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /sh ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ</b>''',
            parse_mode="HTML"
        )
        return

    # --- Cooldown check ---
    cooldown = 35
    remaining_time = check_sh_rate_limit(user_id, cooldown)
    if remaining_time > 0:
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    processing_msg = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id

    threading.Thread(target=process_sh_command, args=(message, processing_msg, cc)).start()

# --- Main logic thread ---
def process_sh_command(message, processing_msg_id, cc):
    gate = 'Shopify charge'
    start_time = time.time()

    try:
        last = str(sh(cc)) 
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

    if any(keyword in last.lower() for keyword in ["funds", "invalid postal", "avs", "added", "duplicate", "ashroved", "allowed", "purchase"]):
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msg, parse_mode="HTML")
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msgd, parse_mode="HTML")


sk_command_usage = {}  # To track rate limits

# --- Rate limit function ---
def check_sk_rate_limit(user_id, cooldown):
    last_usage = sk_command_usage.get(user_id)
    if last_usage:
        elapsed_time = (datetime.now() - last_usage).seconds
        if elapsed_time < cooldown:
            return cooldown - elapsed_time
    sk_command_usage[user_id] = datetime.now()
    return 0

# --- .sk / /sk command handler ---
@bot.message_handler(func=lambda message: message.text.lower().startswith(('.sk', '/sk')))
def respond_to_sk(message):
    user_id = message.from_user.id
    # --- Check user memberskip ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "skeator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot You Have To Join The Channels
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  
</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
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
            text='''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: skopify charge ♻️

ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌

ᴜsᴀɢᴇ: /sk ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ</b>''',
            parse_mode="HTML"
        )
        return

    # --- Cooldown check ---
    cooldown = 35
    remaining_time = check_sk_rate_limit(user_id, cooldown)
    if remaining_time > 0:
        bot.reply_to(message, f"<b>Try again after {remaining_time} seconds.</b>", parse_mode="HTML")
        return

    processing_msg = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id

    threading.Thread(target=process_sk_command, args=(message, processing_msg, cc)).start()

# --- Main logic thread ---
def process_sk_command(message, processing_msg_id, cc):
    gate = 'skopify charge'
    start_time = time.time()

    try:
        last = str(sk(cc)) 
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

    if any(keyword in last.lower() for keyword in ["funds", "invalid postal", "avs", "added", "duplicate", "askroved", "allowed", "purchase"]):
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msg, parse_mode="HTML")
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=processing_msg_id, text=msgd, parse_mode="HTML")









        

from datetime import datetime  
import threading  
import time  
import requests  
import json  
import os  
from collections import defaultdict, deque  
import datetime as dt  

# ============ GATE FUNCTIONS ============  
GATE_FUNCTIONS = [Tele, Fele, Gele]  
gate_index = 0  # ← added here  

# ============ Rate Limit Tracking ============  
cchk_last_used = {}  
mass_last_used = {}  

# ============ BLACKLIST SYSTEM ============  
BLACKLIST_FILE = "blacklist.txt"  
blacklisted_bins = {}  
decline_tracker = defaultdict(lambda: deque())  
risk_tracker = defaultdict(int)  

def load_blacklist():  
    global blacklisted_bins  
    if os.path.exists(BLACKLIST_FILE):  
        with open(BLACKLIST_FILE, "r") as f:  
            for line in f:  
                parts = line.strip().split("|")  
                if len(parts) == 2:  
                    bin_num, timestamp = parts  
                    blacklisted_bins[bin_num] = float(timestamp)  

def save_blacklist():  
    with open(BLACKLIST_FILE, "w") as f:  
        for bin_num, timestamp in blacklisted_bins.items():  
            f.write(f"{bin_num}|{timestamp}\n")  

def add_to_blacklist(bin_num):  
    expire_time = time.time() + 48 * 3600  # 48 hrs  
    blacklisted_bins[bin_num] = expire_time  
    save_blacklist()  

def is_blacklisted(bin_num):  
    if bin_num in blacklisted_bins:  
        if time.time() < blacklisted_bins[bin_num]:  
            return True  
        else:  
            del blacklisted_bins[bin_num]  # expired  
            save_blacklist()  
            return False  
    return False  

def track_decline(bin_num):  
    now = dt.datetime.now()  
    dq = decline_tracker[bin_num]  
    dq.append(now)  
    while dq and (now - dq[0]).seconds > 1200:  # last 20 mins  
        dq.popleft()  
    if len(dq) >= 14:  
        add_to_blacklist(bin_num)  

def track_risk(bin_num):  
    risk_tracker[bin_num] += 1  
    if risk_tracker[bin_num] >= 4:  
        add_to_blacklist(bin_num)  
        risk_tracker[bin_num] = 0  

# Load blacklist on startup  
load_blacklist()  

# ============ Validate CC ============  
def validate_cc(cc_line):  
    try:  
        cc_valid = reg(cc_line)  
        return cc_valid if cc_valid != "None" else None  
    except:  
        return None  

# ============ BIN Info ============  
def get_card_info(cc):  
    try:  
        data = requests.get(f"https://bins.antipublic.cc/bins/{cc[:6]}").json()  
        brand = data.get("brand", "Unknown")  
        card_type = data.get("type", "Unknown")  
        country = data.get("country_name", "Unknown")  
        country_flag = data.get("country_flag", "🏳️")  
        bank = data.get("bank", "Unknown")  
    except:  
        brand = card_type = country = country_flag = bank = "Unknown"  
    return brand, card_type, country, country_flag, bank  

# ============ CCHK Command Handler ============  
def process_card_cchk(cc):  
    global gate_index  # ← added  
    brand, card_type, country, flag, bank = get_card_info(cc)  

    bin_num = cc[:6]  
    if is_blacklisted(bin_num):  
        return f"❌ Message Sorry But This Bin({bin_num}) is on my blacklist!\n"  

    try:  
        current_gate = GATE_FUNCTIONS[gate_index % len(GATE_FUNCTIONS)]  
        gate_index += 1  # ← added  
        result = str(current_gate(cc))  
    except:  
        result = "Error"  

    # Track risk  
    if "risk_threshold" in result.lower():  
        track_risk(bin_num)  

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"  

    # Track decline if failed  
    if status == "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌":  
        track_decline(bin_num)  

    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"  

def process_cchk_command(message, processing_msg):  
    user_id = message.from_user.id  
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]  
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]  
    cards = [c for c in cards if c][:5]  

    if not cards:  
        bot.edit_message_text(  
            "ɢᴀᴛᴇ ɴᴀᴍᴇ: Mass Braintree ᴀᴜᴛʜ ♻️\n\n"  
            "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"  
            "ᴜsᴀɢᴇ: /mchk ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",  
            chat_id=message.chat.id,  
            message_id=processing_msg.message_id  
        )  
        return  

    current_time = time.time()  
    if user_id in cchk_last_used and (current_time - cchk_last_used[user_id]) < 100:  
        wait = int(100 - (current_time - cchk_last_used[user_id]))  
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .mchk again.", chat_id=message.chat.id, message_id=processing_msg.message_id)  
        return  

    cchk_last_used[user_id] = current_time  

    result = ["↯ Braintree ᴀᴜᴛʜ ♻️\n"]  
    start = time.time()  
    for cc in cards:  
        result.append(process_card_cchk(cc))  
    elapsed = time.time() - start  
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")  

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")  

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.mchk', '/mchk')))  
def respond_to_cchk(message):  
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: Txt Braintree ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return

    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  Braintree ᴀᴜᴛʜ ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")  
    threading.Thread(target=process_cchk_command, args=(message, msg)).start()
# ===============================
#    . M A S S    C O M M A N D
# ===============================
def process_card_mass(cc):
    brand, card_type, country, flag, bank = get_card_info(cc)
    try:
        result = str(pp(cc)) 
    except:
        result = "Error"

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"

def process_mass_command(message, processing_msg):
    user_id = message.from_user.id
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]
    cards = [c for c in cards if c][:12]

    if not cards:
        bot.edit_message_text(
    "ɢᴀᴛᴇ ɴᴀᴍᴇ: Mass stripe ᴀᴜᴛʜ ♻️\n\n"
    "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
    "ᴜsᴀɢᴇ: /mass ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
    chat_id=message.chat.id,
    message_id=processing_msg.message_id
)
        return  # no rate limit applied here

    current_time = time.time()
    if user_id in mass_last_used and (current_time - mass_last_used[user_id]) < 80:
        wait = int(80 - (current_time - mass_last_used[user_id]))
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .mass again.", chat_id=message.chat.id, message_id=processing_msg.message_id)
        return

    mass_last_used[user_id] = current_time

    result = ["↯ Stripe ᴀᴜᴛʜ ♻️\n"]
    start = time.time()
    for cc in cards:
        result.append(process_card_mass(cc))
    elapsed = time.time() - start
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.mass', '/mass')))
def respond_to_mass(message):
    user_id = message.from_user.id
    # --- Check user membership ---
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not a member")
    except:
        msg = '''<b>🔴 ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ :

🚨 To use this bot You Have To Join The Channels
<a href="https://t.me/hrefcm/111">&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; ᴜᴘᴅᴀᴛᴇs &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</a>  
</b>'''
        bot.reply_to(message, msg, parse_mode='HTML')
        return    
    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  Stripe ᴀᴜᴛʜ ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_mass_command, args=(message, msg)).start()
    
# ===============================
#    . M A S S    S Q U A R E
# ===============================

msq_last_used = {}  



def process_card_msq(cc):
    brand, card_type, country, flag, bank = get_card_info(cc)
    try:
        result = str(sq(cc)) 
    except:
        result = "Error"

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"

def process_msq_command(message, processing_msg):
    user_id = message.from_user.id
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]
    cards = [c for c in cards if c][:12]

    if not cards:
        bot.edit_message_text(
    "ɢᴀᴛᴇ ɴᴀᴍᴇ: msq square ᴀᴜᴛʜ ♻️\n\n"
    "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
    "ᴜsᴀɢᴇ: /msq ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
    chat_id=message.chat.id,
    message_id=processing_msg.message_id
)
        return  # no rate limit applied here

    current_time = time.time()
    if user_id in msq_last_used and (current_time - msq_last_used[user_id]) < 80:
        wait = int(80 - (current_time - msq_last_used[user_id]))
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .msq again.", chat_id=message.chat.id, message_id=processing_msg.message_id)
        return

    msq_last_used[user_id] = current_time

    result = ["↯ square ᴀᴜᴛʜ ♻️\n"]
    start = time.time()
    for cc in cards:
        result.append(process_card_msq(cc))
    elapsed = time.time() - start
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.msq', '/msq')))
def respond_to_msq(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: square ᴀᴜᴛʜ ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return
    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  square ᴀᴜᴛʜ ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_msq_command, args=(message, msg)).start()
    
# ===============================
#    . M A S S    S Q U A R E
# ===============================

mcr_last_used = {}  



def process_card_mcr(cc):
    brand, card_type, country, flag, bank = get_card_info(cc)
    try:
        result = str(cr(cc)) 
    except:
        result = "Error"

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"

def process_mcr_command(message, processing_msg):
    user_id = message.from_user.id
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]
    cards = [c for c in cards if c][:12]

    if not cards:
        bot.edit_message_text(
    "ɢᴀᴛᴇ ɴᴀᴍᴇ: mcr mass stripe charge ♻️\n\n"
    "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
    "ᴜsᴀɢᴇ: /mcr ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
    chat_id=message.chat.id,
    message_id=processing_msg.message_id
)
        return  # no rate limit applied here

    current_time = time.time()
    if user_id in mcr_last_used and (current_time - mcr_last_used[user_id]) < 80:
        wait = int(80 - (current_time - mcr_last_used[user_id]))
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .mcr again.", chat_id=message.chat.id, message_id=processing_msg.message_id)
        return

    mcr_last_used[user_id] = current_time

    result = ["↯ mass stripe charge ♻️\n"]
    start = time.time()
    for cc in cards:
        result.append(process_card_mcr(cc))
    elapsed = time.time() - start
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.mcr', '/mcr')))
def respond_to_mcr(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: mass stripe charge ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return
    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  mass stripe charge ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_mcr_command, args=(message, msg)).start()
    
# ===============================
#    . M A S S    S Q U A R E
# ===============================

mpp_last_used = {}  



def process_card_mpp(cc):
    brand, card_type, country, flag, bank = get_card_info(cc)
    try:
        result = str(pp(cc)) 
    except:
        result = "Error"

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"

def process_mpp_command(message, processing_msg):
    user_id = message.from_user.id
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]
    cards = [c for c in cards if c][:12]

    if not cards:
        bot.edit_message_text(
    "ɢᴀᴛᴇ ɴᴀᴍᴇ: mpp mass PayPal charge ♻️\n\n"
    "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
    "ᴜsᴀɢᴇ: /mpp ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
    chat_id=message.chat.id,
    message_id=processing_msg.message_id
)
        return  # no rate limit applied here

    current_time = time.time()
    if user_id in mpp_last_used and (current_time - mpp_last_used[user_id]) < 80:
        wait = int(80 - (current_time - mpp_last_used[user_id]))
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .mpp again.", chat_id=message.chat.id, message_id=processing_msg.message_id)
        return

    mpp_last_used[user_id] = current_time

    result = ["↯ mass PayPal charge ♻️\n"]
    start = time.time()
    for cc in cards:
        result.append(process_card_mpp(cc))
    elapsed = time.time() - start
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.mpp', '/mpp')))
def respond_to_mpp(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: mass PayPal charge ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return
    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  mass PayPal charge ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_mpp_command, args=(message, msg)).start()
    
# ===============================
#    . M A S S    S Q U A R E
# ===============================

msh_last_used = {}  



def process_card_msh(cc):
    brand, card_type, country, flag, bank = get_card_info(cc)
    try:
        result = str(sh(cc)) 
    except:
        result = "Error"

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"

def process_msh_command(message, processing_msg):
    user_id = message.from_user.id
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]
    cards = [c for c in cards if c][:12]

    if not cards:
        bot.edit_message_text(
    "ɢᴀᴛᴇ ɴᴀᴍᴇ: msh mass Shopify charge ♻️\n\n"
    "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
    "ᴜsᴀɢᴇ: /msh ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
    chat_id=message.chat.id,
    message_id=processing_msg.message_id
)
        return  # no rate limit applied here

    current_time = time.time()
    if user_id in msh_last_used and (current_time - msh_last_used[user_id]) < 80:
        wait = int(80 - (current_time - msh_last_used[user_id]))
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .msh again.", chat_id=message.chat.id, message_id=processing_msg.message_id)
        return

    msh_last_used[user_id] = current_time

    result = ["↯ mass Shopify charge ♻️\n"]
    start = time.time()
    for cc in cards:
        result.append(process_card_msh(cc))
    elapsed = time.time() - start
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.msh', '/msh')))
def respond_to_msh(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: mass Shopify charge ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return
    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  mass Shopify charge ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_msh_command, args=(message, msg)).start()
            
            
    
# ===============================
#    . M A S S    S Q U A R E
# ===============================

msk_last_used = {}  



def process_card_msk(cc):
    brand, card_type, country, flag, bank = get_card_info(cc)
    try:
        result = str(sk(cc)) 
    except:
        result = "Error"

    status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅" if any(i in result.lower() for i in ["approved", "funds", "added", "purchase", "duplicate", " avs"]) else "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    return f"Card↯ <code>{cc}</code>\nStatus - {status}\nResult -⤿ {result} ⤾\n"

def process_msk_command(message, processing_msg):
    user_id = message.from_user.id
    text = message.reply_to_message.text if message.reply_to_message else message.text[5:]
    cards = [validate_cc(i.strip()) for i in text.strip().split('\n') if i.strip()]
    cards = [c for c in cards if c][:12]

    if not cards:
        bot.edit_message_text(
    "ɢᴀᴛᴇ ɴᴀᴍᴇ: msk mass mix charge ♻️\n\n"
    "ᴍᴇssᴀɢᴇ: ɴᴏ ᴄᴄ ғᴏᴜɴᴅ ᴏʀ ɪɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ❌\n\n"
    "ᴜsᴀɢᴇ: /msk ᴄᴄ|ᴍᴇs|ᴀɴᴏ|ᴄᴠᴠ",
    chat_id=message.chat.id,
    message_id=processing_msg.message_id
)
        return  # no rate limit applied here

    current_time = time.time()
    if user_id in msk_last_used and (current_time - msk_last_used[user_id]) < 80:
        wait = int(80 - (current_time - msk_last_used[user_id]))
        bot.edit_message_text(f"⏳ Please wait {wait}s before using .msk again.", chat_id=message.chat.id, message_id=processing_msg.message_id)
        return

    msk_last_used[user_id] = current_time

    result = ["↯ mass mix charge ♻️\n"]
    start = time.time()
    for cc in cards:
        result.append(process_card_msk(cc))
    elapsed = time.time() - start
    result.append(f"- 𝗧𝗶𝗺𝗲 - {elapsed:.2f}s")

    bot.edit_message_text("\n".join(result), chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text.lower().startswith(('.msk', '/msk')))
def respond_to_msk(message):
    user_id = message.from_user.id
    plan = get_user_plan(user_id)

    if plan == 'FREE':
        bot.reply_to(message, '''<b>ɢᴀᴛᴇ ɴᴀᴍᴇ: mass mix charge ♻️

✧ ᴍᴇssᴀɢᴇ: You do not have sufficient credit 

✧ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ: ꜰᴏʀ credit top up
✧ ᴀᴅᴍɪɴ: @MKNXW</b>''', parse_mode="HTML")
        return
    msg = bot.reply_to(message, "- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  mass mix charge ♻️\n- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️", parse_mode="HTML")
    threading.Thread(target=process_msk_command, args=(message, msg)).start()
            


print("Bot is running...")
bot.infinity_polling()
