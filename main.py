import requests
from bs4 import BeautifulSoup

info_dict = {}
page = 1

while page < 4:
    main_url = 'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev' + f'?page={page}'
    response = requests.get(main_url)
    src = response.text
    soup = BeautifulSoup(src, 'html.parser')
    all_ads = soup.find_all('a', class_='css-rc5s2u', href=True)
    for i in all_ads:
        url = "https://www.olx.ua" + i.get('href')
        response2 = requests.get(url)
        src2 = response2.text
        soup = BeautifulSoup(src2, 'html.parser')
        try:
            title = soup.find('h1', class_='css-1dhh6hr er34gjf0').text
            price = soup.find('h3', class_='css-1twl9tf er34gjf0').text
            description = soup.find('div', class_='css-1t507yq er34gjf0').text
            info_dict[title] = [price, description, f'{url}\n\n']
        except:
            continue

    page += 1

count = 1
with open('info.txt', 'w') as file:
    for key, value in info_dict.items():
        file.write(f'{count}. {key}:\n')
        count += 1
        for values in value:
            file.write(f'- {values}\n')
