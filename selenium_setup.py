#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
#from urllib.request import urlopen

if __name__ == '__main__':

    # https://www.vpngate.net/en/
    url = "https://www.vpngate.net/en/"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    speed = soup.findAll('span', attrs={'style': 'font-size: 10pt;'})
    links = soup.findAll('a', href=True)    

    vpn_speed = [str(s.text).strip(" Mbps") for s in speed if "Mbps" in s.text]
    download_pages = [l['href'] for l in links if "do_openvpn" in l['href']]

    speeds_and_links = dict(zip(download_pages, vpn_speed))

    max_speed = 0.0
    max_speed_link = ""

    for l, s in speeds_and_links.items():
        connection_speed = float(s)
        if connection_speed > max_speed:
            max_speed = connection_speed
            max_speed_link = l
        else:
            continue

    selected_link = driver.find_element_by_xpath('//a[@href="'+max_speed_link+'"]')
    selected_link.click()

    sleep(5)

    #driver.get_screenshot_as_file('proof.png')
    selected_link_html = driver.page_source
    download_soup = BeautifulSoup(selected_link_html, 'html.parser')
    download_links = download_soup.findAll('a', href=True)
    
    driver.quit()

    dl_links = list()

    print(f"Speed\tLink\n-----\t-----\n{max_speed}\t{max_speed_link}\n\n")
    for dl in download_links:
        if "common" in dl['href']:
            dl_links.append(dl)
    
    for x in dl_links:
        print(x)
    



    # [print(d) for d in download_pages]


    # speed = soup.findAll('span')
    #speed, links = list(), list()

    # for item in soup.find('table', {"id":"vg_hosts_table_id"}).tr.td.children:
    #     print(item)



    # [print(i) for i in speed_list]


    # for child in soup.find("tr").children:
    #     print(child)
