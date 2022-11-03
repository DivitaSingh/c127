from bs4 import BeautifulSoup 
import requests
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
time.sleep(10)

start_url = requests.get(START_URL)
soup = BeautifulSoup(start_url.content, "html.parser")

headers = ["name", "distance", "mass", "radius"]
star_data = []

for th_tag in soup.find_all("th", attrs={"class", "headerSort"}):
            tr_tags = th_tag.find_all("li")
            temp_list = []
            for index, tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
with open("scrapper_2.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)



