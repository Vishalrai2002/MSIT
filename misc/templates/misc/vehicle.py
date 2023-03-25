import requests

cookies = {
    'PHPSESSID': '10a21q57dubaqfdk3qp0mk25rl',
    '_ga': 'GA1.2.1005225365.1679663730',
    '_gid': 'GA1.2.2119590732.1679663731',
    '_gat_gtag_UA_68910922_13': '1',
    '__gads': 'ID=32f0dd6f3e9fa157-2278974eb3dc0015:T=1679663856:RT=1679663856:S=ALNI_MZ1Bi2FS9ly42zN_bfgNATsh5D_DA',
    '__gpi': 'UID=00000bdfae9455de:T=1679663856:RT=1679663856:S=ALNI_MbdpF3bSOIXzVJhNir6yhfXT30AxQ',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=10a21q57dubaqfdk3qp0mk25rl; _ga=GA1.2.1005225365.1679663730; _gid=GA1.2.2119590732.1679663731; _gat_gtag_UA_68910922_13=1; __gads=ID=32f0dd6f3e9fa157-2278974eb3dc0015:T=1679663856:RT=1679663856:S=ALNI_MZ1Bi2FS9ly42zN_bfgNATsh5D_DA; __gpi=UID=00000bdfae9455de:T=1679663856:RT=1679663856:S=ALNI_MbdpF3bSOIXzVJhNir6yhfXT30AxQ',
    'Origin': 'https://vahaninfos.com',
    'Referer': 'https://vahaninfos.com/vehicle-details-by-number-plate',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'num': 'MTE4NzUxOTU4MA==',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'number': 'DL4SAZ6522',
    'g-recaptcha-response': '03AFY_a8XwSW8UTi5j-kOChnaE4rNfLcHBlWHpF2u-MlMRKXP_yYSKBugoX_gsPXhz7bL7KksKrC1Wo3cBorf6Ty77kuMs9HqHdlbqV_0cUHBXUTS8bhJaCJGqSjMB5tUSXvozpJJFzCMMSQSAJWbbk3eufS4upOt1NzyOxZ_uIS1C-_F40EfZxmH33XKGdUfoC_VR334pbDjeTZnbI23VSMbSlOTBe--JePpNQQhBuAupPHYu5ejTHLwnRWA3MGztVuv_1ZRAY_Tt1ramMiEP1l1NCft3f6cM-h0xubfSgZRIgHRHTtlZxSX4SLgJEPb0ycdOqT3MDeIVTTbTmDU0mUA3tdFGaf43QtiiunuGggBnl4yUpxOVXBQNx4yWxdEHEYzdByR9A3QLpnRJ0hRkkaVi-CBKjy4Q3YonzWDnsnBIDVFZ6jYCwbaxdpvpP_OPR913o7-im8_p9OkWjNCgM82d75bw7Im4cozmtk9BFtQXh5n-zV1tNsznqhnH_Bohtdv8OGvJEqedrUiWVf9e7ynhFaZ-qfGvnoge6X7pQXH4IhwRiUayZqbDxR9_6NwtaFewPNgX0JYzFlYCA5Rmglxhj7I3O9ZdAAuBnzp5wZugqO9OpVnJHKI',
}

response = requests.post('https://vahaninfos.com/getdetails.php', cookies=cookies, headers=headers, data=data)


 curl --location 'https://api.emptra.com/vehicleRegistrationsV3' \
--header 'Content-Type: application/json' \
--header 'clientId: 24a770ad9acb652965599c658092c1f0:fdc448ec044da300d922055f6674aa80' \
--header 'secretKey: 8Cf4Cf5v1bq5LuIfXG1opYd0tk0WV9G6QnoH0EbGh83iCfglPmHIKKE6B8r2ijyI1' \
--data '{
"vehicleNumber": "DL4SAZ6522"
}'



# https://parivahan.gov.in/rcdlstatus/?pur_cd=101