import http.client
from pprint import pprint

#temp
n = 0

def get_my_ships(n=0):
    conn = http.client.HTTPSConnection("api.spacetraders.io")

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    conn.request("GET", "/v2/my/ships", headers=headers)

    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict['data']

def get_ship_location_info(n=0):
    status = get_my_ships()['nav']['status']
    system_symbol = get_my_ships()['nav']['systemSymbol']
    waypoint_symbol = get_my_ships()['nav']['waypointSymbol']
    x = get_my_ships()['nav']['route']['destination']['x']
    y = get_my_ships()['nav']['route']['destination']['y']
    fuel_current = get_my_ships()['fuel']['current']
    fuel_capacity = get_my_ships()['fuel']['capacity']
    ship_symbol = get_my_ships()['symbol']
    return status, system_symbol, waypoint_symbol, fuel_current, fuel_capacity, ship_symbol, x, y


def get_ship_cargo_numbers(n):
    conn = http.client.HTTPSConnection("api.spacetraders.io")
    ship_symbol = get_ship_location_info(n)[5]
    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    url = f"/v2/my/ships/{ship_symbol}/cargo"
    conn.request("GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    capacity = mydict['data']['capacity']
    current_units = mydict['data']['units']
    return capacity, current_units

def get_ship_inventory(ship_symbol):
    conn = http.client.HTTPSConnection("api.spacetraders.io")
    ship_symbol = ship_symbol
    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    url = f"/v2/my/ships/{ship_symbol}/cargo"
    conn.request("GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict['data']['inventory']

def dock_ship(ship_symbol):
    conn = http.client.HTTPSConnection("api.spacetraders.io")
    ship_symbol = ship_symbol
    payload = ""

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    url = f"/v2/my/ships/{ship_symbol}/dock"
    conn.request("POST", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict

def refuel_ship(n):
    conn = http.client.HTTPSConnection("api.spacetraders.io")
    ship_symbol = get_ship_location_info(n)[5]
    payload = ""

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    url = f"/v2/my/ships/{ship_symbol}/refuel"
    conn.request("POST", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict

def orbit_ship(ship_symbol):
    conn = http.client.HTTPSConnection("api.spacetraders.io")
    ship_symbol = get_ship_location_info(n)[5]
    payload = ""

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    url = f"/v2/my/ships/{ship_symbol}/orbit"
    conn.request("POST", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    return mydict

def extract_resources(ship_symbol):
    conn = http.client.HTTPSConnection("api.spacetraders.io")
    ship_symbol = ship_symbol
    payload = ""

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUk9ENTYiLCJpYXQiOjE2ODM1NjIzMjEsInN1YiI6ImFnZW50LXRva2VuIn0.HKURfm315SXdXqMo7l7ddofTXjydk-K0FspHjmE-syXnXhGKh7MNU4kJACzoagRYRTn7iWxuh5V6I3o1cPTzskdHo7l9DXWk3G34I1px7xgswdLw2xsYNM6ZRnOkib7huA4gsmAT4N5m0xySLpwgGd2DoHfvYk6nfllV0SF-Dv7bQuLlbO_QR8U0ZquEuxqtk7ka0hhgQ3N3FTogZpHdkZ3sMP8lJDZIfiiX-Wm6BNvgMjIoyp4QdMW3j0hN-MpzKycx4lDOtDdVu1hepFtUKU9q6TXMPV_Mf0taZ6k2UxPvTaj0-GIlSBMpnhSjJ1oFMaVB8vLqeMMxJElxZZX4jq5r9_sNomDG1Bx7u2EUn6IwD_B3i5sVWzHIX-6NMnMRZFkg_5TtACOm6oo33-9ccUFF8dh3GD1jOIymjiKIGk_OaO93OX_UnVU69QpDff8HnOCzAe4c9x_6GhzFB09HalU4fgX7-H3z2jxqMyxfpYCTZJmDSqprB38paLcChtuX"
    }

    url = f"/v2/my/ships/{ship_symbol}/extract"
    conn.request("POST", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    mystr = data.decode("utf-8")
    mydict = eval(mystr)
    cooldown_time = mydict['data']['cooldown']
    cargo_capacity = mydict['data']['cargo']['capacity']
    cargo_units = mydict['data']['cargo']['units']
    return cooldown_time, cargo_capacity, cargo_units

