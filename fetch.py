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
    return result.lower()

final = {}
redirects = []

for link in links:
    long_url = link['long_url']
    key = key_maker(link['link'])
    final[key] = long_url
    redirects.append((key, long_url))
    for bitlink in link['custom_bitlinks']:
        final[key_maker(bitlink)] = long_url
        redirects.append((key_maker(bitlink),long_url))


data['ppp'] = 'https://www.feldroy.com/products/practical-python-projects'


with open('data.json', 'w') as f:

    data = json.dumps(final, indent=2)
    f.write(data)

redirects.append(('ppp','https://www.feldroy.com/products/practical-python-projects'))

with open('public/_redirects', 'w') as f:
    for link in redirects:
        print(link)
        f.write(f'/{link[0]}    {link[1]}\n')

with open("public/index.html", "w") as f:
    f.write("<h1>Feldroy Links</h1>")
    f.write('<ol>')
    for link in redirects:
        f.write(f'<li><a href="{link[1]}">/{link[0]}</a></li>')
    f.write('</ol>')
