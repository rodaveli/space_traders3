import http.client
from pprint import pprint
from trade import *
from time import sleep

def get_systems():
    conn = http.client.HTTPSConnection("api.spacetraders.io")

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    conn.request("GET", "/v2/systems", headers=headers)

    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict['data']
    
    
def get_waypoints(system_symbol):
    conn = http.client.HTTPSConnection("api.spacetraders.io")

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }
		#url = f"/v2/{system_symbol}/waypoints"
    conn.request("GET", f"/v2/systems/{system_symbol}/waypoints", headers=headers)

    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict['data']
    
#systm_current = 'X1-DF55'

#pprint(get_systems())
all_systems = get_systems()
all_systems_all = []
for n in all_systems:
	#print(n['symbol'])
	all_systems_all.append(n['symbol'])
	#print(n['type'])
	#print(n['waypoints'])

#print(all_systems_all)
#pprint(get_waypoints(all_systems_all[0]))
all_waypoints = get_waypoints(all_systems_all[0])
#print("---------")
#pprint(all_waypoints)
#print("---------")

#for n in range 
# waypoint_symbols append list from all_waypoint[n]['symb']

waypoint_symbols = {}
waypoints_coords = {}
for i, n in enumerate(all_waypoints):
    waypoint_symbols[n['symbol']] = n['type']
    waypoints_coords[n['symbol']] = [n['x'], n['y']]  

#pprint(waypoint_symbols)
#print("---------")
#pprint(waypoints_coords)
#data = get_market_info(systm_current, 'X1-DF55-20250Z')['data']['tradeGoods']
all_data = {}

#for k,v in waypoint_symbols.items():
#    try:
#        all_data[k] = get_market_info(systm_current, k)['data']['tradeGoods']
#    except Exception:
#        pass

#for k in waypoint_symbols.keys():
#    try:
#        all_data[k] = get_market_info(systm_current, k)['data']['tradeGoods']
#        sleep(2)
#    except KeyError:
#        continue
#    else:
#        all_data[k] = get_market_info(systm_current, k)['data']['tradeGoods']
#        sleep(2)
pprint(waypoint_symbols)