import streamlit as st
from google.cloud import firestore
from info import *
from trade import *
from nav import *
from ship import *
from system_info import *
import pandas as pd
from google.cloud import firestore
from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

st.title('Rods Space Trader App')


db = firestore.Client.from_service_account_json("firestore-key.json")




def add_market_table(table_name, system_symbol, waypoint_symbol):
    data = get_market_info(system_symbol, waypoint_symbol)['data']['tradeGoods']
    waypoint_ref = db.collection(table_name)

    for item in data:
        waypoint_ref.document(item['symbol']).set(item)

#add_market_table('X1-DF55-17335A')

#users_ref = db.collection(u'X1-DF55-17335A')
#waypoint_ref = db.collection("X1-DF55-17335A")
#docs = waypoint_ref.stream()

#data = []
#for doc in docs:
#    data.append(doc.to_dict())

#df = pd.DataFrame(data)
#df["Profit Margin"] = ((df["purchasePrice"] - df["sellPrice"]) / df["purchasePrice"])*100

#st.dataframe(df)    

with st.sidebar:
    my_info = get_my_info()
    st.write("account id:", my_info['accountId'])
    credits = st.write("credits:", my_info['credits'])   
    st.write("headquarters:", my_info['headquarters'])
    st.write("symbol:", my_info['symbol'])
    st.write("SHIP INFO")
    ship_info = get_ship_location_info(0)
    #status, system_symbol, waypoint_symbol, fuel_current, fuel_capacity, ship_symbol
    st.write("status:", ship_info[0])
    sys_current = st.write("system_symbol:", ship_info[1])
    waypoint_current = st.write("waypoint_symbol:", ship_info[2])
    st.write("fuel_current:", ship_info[3])
    st.write("fuel_capacity:", ship_info[4])
    ship_symbol = st.write("ship_symbol:", ship_info[5])
    x_coord = st.write("x_coord:", ship_info[6])
    y_coord = st.write("y_coord:", ship_info[7])
    if st.button("Dock Ship"):
        dock_ship(ship_symbol=ship_symbol)
    if st.button("Go to Orbit"):
        orbit_ship(ship_symbol=ship_symbol)


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Trade", "Nav", "Ship", "Contracts", "System Explore", "Mine for Resources"])

with tab1:
    waypnt = st.text_input("Enter Waypoint Symbol:")
    myship = st.text_input("Enter Ship symbol")
    systm_current = st.text_input("system_symbol:")
    if st.button("Nearest Market Data:"):
        dock_ship(ship_symbol=myship)
        data = get_market_info(systm_current, waypnt)['data']['tradeGoods']
        df1 = pd.DataFrame(data)
        df1["Profit Margin"] = ((df1["purchasePrice"] - df1["sellPrice"]) / df1["purchasePrice"])*100
        ship_inventory = get_ship_inventory(myship)
        df2 = pd.DataFrame(ship_inventory)
        df2.drop(['description'], axis=1, inplace=True)
        df = pd.merge(df1, df2, on='symbol', how='left')
        df.drop(['name'], axis=1, inplace=True)
        st.dataframe(df)
    if st.button("save to DB"):
        add_market_table(waypnt, systm_current, waypnt)


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Get Waypoints"):
            waypoints = list_waypoints(system_symbol='X1-DF55')
            st.write(waypoints)
    with col2:
        waypnt = st.text_input("Enter Waypoint Symbol")
        myship = st.text_input("Enter Ship Symbol")
        if st.button("go to Waypoint"):
            #refuel_ship(0)
            route = navigate_ship(myship, waypnt)['data']['nav']
            departure_time = route['departureTime']
            arrival_time = route['arrival']
            dt1 = datetime.strptime(departure_time, "%Y-%m-%dT%H:%M:%SZ")
            dt2 = datetime.strptime(arrival_time, "%Y-%m-%dT%H:%M:%SZ")
            time_difference = dt2 - dt1
            st.write("time to arrival:", time_difference.total_seconds())

#print(time_difference.total_seconds())
with tab3:
    myship = st.text_input("Enter the Ship Symbol:")
    if st.button("get ship inventory:"):
        ship_inventory = get_ship_inventory(myship)
        st.write(ship_inventory)

with tab5:
    ship_info = get_ship_location_info(0)
    x_coord = st.write("x_coord:", ship_info[6])
    y_coord = st.write("y_coord:", ship_info[7])
    x = x_coord
    y = y_coord
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
    df = pd.DataFrame.from_dict(waypoint_symbols, orient='index')
    df.columns = ['waypoint & type']
    st.dataframe(df)
    coord_dict = defaultdict(list)

    for key, value in waypoints_coords.items():
        coord_dict[tuple(value)].append(key + ' (' + waypoint_symbols[key] + ')')

    fig = plt.figure(figsize=(10, 8))

    for value, keys in coord_dict.items():
        plt.plot(value[0], value[1], 'o')
        plt.text(value[0], value[1], '\n'.join(keys), fontsize=8)

    plt.title('CURRENT SYSTEM MAP')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    center = [int(x), int(y)]
    plt.plot(center[0], center[1], marker='x', markersize=10, color='red')
    plt.text(center[0], center[1], 'YOU ARE HERE', fontsize=12, ha='right')
    x_range = max(abs(v[0] - center[0]) for v in waypoints_coords.values())
    y_range = max(abs(v[1] - center[1]) for v in waypoints_coords.values())

    plt.xlim(center[0] - x_range, center[0] + x_range)
    plt.ylim(center[1] - y_range, center[1] + y_range)
    st.pyplot(fig)
with tab6:
    myship = st.text_input("Enter Ship Symbol:", placeholder='ROD56-1')
    if st.button("Mine"):
        cooldown, cargo_capacity, cargo_units_current = extract_resources(myship)
        st.write("cooldown:", cooldown)
        st.write("cargo_capacity:", cargo_capacity)
        st.write("cargo_units_current:", cargo_units_current)
        progress_text = "Mining Cooldown in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            sleep(cooldown['totalSeconds']/100)
            my_bar.progress(percent_complete + 1, text=progress_text)