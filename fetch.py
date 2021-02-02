###Super sloppy code - don't laugh!

import requests
import json

import settings




links = []

r = requests.get(f'{settings.BASE_URL}/groups/{settings.GROUP_GUID}/bitlinks', headers=settings.HEADERS)
data = r.json()

links += data['links']

for i in range(7):
    if data['pagination']['next'] == '':
        break
    r = requests.get(data['pagination']['next'], headers=settings.HEADERS)
    data = r.json()
    links += data['links']
    


# print(links)
# print(len(links))
def key_maker(value):
    result = value.rsplit('/', 1)[-1]
    # print('result:', result)
    return result

final = {}
redirects = []

for link in links:
    long_url = link['long_url']
    final[key_maker(link['link'])] = long_url
    for bitlink in link['custom_bitlinks']:
        final[key_maker(bitlink)] = long_url
        redirects.append(f'{key_maker(bitlink)}    {long_url}')


data['ppp'] = 'https://www.feldroy.com/products/practical-python-projects'


with open('data.json', 'w') as f:

    data = json.dumps(final, indent=2)
    f.write(data)

redirects.append('ppp    https://www.feldroy.com/products/practical-python-projects')

with open('public/_redirects', 'w') as f:
    for redirect in redirects:
        f.write(f'/{redirect}\n')

