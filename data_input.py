import pandas as pd


input_dat = pd.read_csv("price_paid_records.csv")

counties_keep = ["SOMERSET","WILTSHIRE","GLOUCESTERSHIRE","DORSET","DEVON","CORNWALL","AVON","BATH AND NORTH EAST SOMERSET","CITY OF BRISTOL","NORTH SOMERSET","SOUTH GLOUCESTERSHIRE"]

print(set(input_dat["County"]))

input_dat = input_dat[input_dat["County"].isin(counties_keep)]

print(set(input_dat["County"]))

input_dat.to_csv("Input_Reduced.csv")

