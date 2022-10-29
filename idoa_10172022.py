import camelot
import pandas as pd
from addrPatterns import addrpattern1, addrpattern2, addrpattern3, addrpattern4
from patternFactory import addrpatternfactory
from patternStore import addrStore
import requests

# Storing pdf contents to a Dataframe - Stream
def IDOALicenseeList_stream_pdf_to_Table(path_or_url):
    temp = pd.DataFrame()
    try:
        pdf_tables = camelot.read_pdf(path_or_url, pages='all', flavor='stream')
        for table in pdf_tables:
            frames = [temp, table.df]
            temp = pd.concat(frames, ignore_index=True)
    except:
        temp = pd.read_csv(path_or_url, skip_blank_lines=True)
    return temp


# Preprocess address data
def preprocess_addr(address):
    addr = addrpatternfactory(address)
    # print(addrFact.get_addr().show_addr())
    addr = addrStore(addr)
    # addr.show_addr()
    return addr.fix_addr()
#
df = IDOALicenseeList_stream_pdf_to_Table('IDOALicenseeList_20221014.pdf')
df.columns = ['name', 'address']
print(df)
# df.to_csv('raw_2510.csv', index=False)

# Wrangle raw.csv

# df = pd.read_csv('raw.csv', names=['name', 'address'])
# print(df.columns)
city = []
state= []
zipcode = []

for i in df['address']:
    try:
        # print(preprocess_addr(i))
        city.append(preprocess_addr(i)['city']),
        # print(city)
    except:
        city.append('')
    try:
        state.append(preprocess_addr(i)['state'])
        # print(state)
    except:
        state.append('')
    try:
        zipcode.append(preprocess_addr(i)['zipcode'])
    except:
        zipcode.append('')

# pre_processed_record = preprocess_addr(df[1][2])
# print(pre_processed_record)
# print(pre_processed_record['city'])
# print(pre_processed_record['zipcode'])
# print(pre_processed_record['street_address'])
df['city'] = city
df['state'] = state
df['zipcode'] = zipcode
# df['state'] = df['state'].astype(str).replace(r'', "IL", regex=True)
# df['zipcode'] = df['zipcode'].str.lstrip('IL ')
# df['zipcode'] = df['zipcode'].astype(str).replace(r'', "", regex=True)

# df = df[df['zipcode'] != df['zipcode'].str.isnumeric()]
# if df['zipcode'] != ''
print(df)
# df.to_csv('new_city_2610.csv', index=False)
