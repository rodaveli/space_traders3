import http.client
from pprint import pprint
from google.cloud import firestore

#temp
db = firestore.Client.from_service_account_json("firestore-key.json")
#system_symbol = 'X1-DF55'
#waypoint_symbol = 'X1-DF55-17335A'

def get_market_info(system_symbol, waypoint_symbol):
    conn = http.client.HTTPSConnection("api.spacetraders.io")

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    url = f"/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/market"

    conn.request("GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict

def add_market_table(table_name, system_symbol, waypoint_symbol):
    waypoint_ref = db.collection(table_name)
    data = get_market_info(system_symbol, waypoint_symbol)['tradeGoods']
    for item in data:
        waypoint_ref.document(item['symbol']).set(item)