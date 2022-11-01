import camelot
import pandas as pd

from patternFactory import addrpatternfactory
from patternStore import addrStore


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

df['city'] = city
df['state'] = state
df['zipcode'] = zipcode

print(df)
df.to_csv('upto_addr5.csv', index=False)

# non_city_df = df[(df['city'] == 'IL') & (df['city'] == '')]
# non_city_df.to_csv('non_city_df_v2.csv', index=False)
# rejected_df = df[df['city'].isnull()]

# rejected_df.to_csv('rejected_df.csv', index=False)
# cleaned_df = df[df[rejected_df]]
# cleaned_df.to_csv('cleaned_df.csv', index=False)


# chunk_first_set = df[df['state'] != 'IL']
# first_set = first_set[first_set['city'] != 'IL']
# first_set.to_csv('clean_first_set_v3.csv', index=False)
#
# second_set = df[df['state'] != 'IL']
# second_set.to_csv('second_set_v2.csv', index=False)
# df.to_csv('new_city_3110.csv', index=False)
