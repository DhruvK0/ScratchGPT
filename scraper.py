import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import numpy as np

URL = "https://practice.dsc10.com/wi22-midterm/index.html"
page = requests.get(URL)
encoded_text = page.text.encode("utf-8")
test = encoded_text.decode("utf-8")

soup = BeautifulSoup(encoded_text, "html.parser")

info_picture = soup.find_all("center")[0]
paragraphs = soup.find_all("p")

info_pars = paragraphs[4:7]

titles = soup.find_all(["h3"])
title_split = [] 
for tag in titles:
    title_split.append(tag.text.split(".")[0])

h2_headers = soup.find_all("h2")

# test_filtered = []

for tag in h2_headers:
    if tag.get('class') != ['accordion-header']:
        if tag.text not in title_split:
            if "Problem" in tag.text:
                number = tag.text.split(" ")[1]
                #find the first tag with a number 1 greater than the current number
                for i in range(len(titles)):
                    if int(titles[i].text.split(" ")[1].split(".")[0]) == int(number) + 1:
                        titles.insert(i, tag)
                        break                





first_prob = titles[0]
first_desc = first_prob.next_sibling.next_sibling.next_sibling.next_sibling
first_answers = first_desc.find_next_sibling("ul")
first_answer = first_answers.find_next_sibling("div")

problem_list = []

for tag in titles:
    next_tag = tag.next_sibling
    current_content = tag.text
    while next_tag: 
        #check if the next tag is a div and has the class "accordion-body"
        # if isinstance(next_tag, bs4.element.Tag) and len(next_tag.attrs) > 0:
        #     attributes = next_tag.attrs
        #     if next_tag.get('id') == 'accordionExample':
        #         print(next_tag)
        if isinstance(next_tag, bs4.element.Tag) and len(next_tag.attrs) > 0:
            if next_tag.get('id') == 'accordionExample':
                break
            #print(next_tag.attrs)
            # if next_tag["id"] == "accordionExample":
            #     break


        # if isinstance(next_tag, bs4.element.Tag):
        #     if next_tag["id"] == 'accordionExample':
        #             break   
        current_content += next_tag.text
        next_tag = next_tag.next_sibling
    problem_list.append(current_content)


answer_list = soup.find_all("div", {"class": "accordion-body"})

#convert answers and titles to text
for i in range(len(answer_list)):
    answer_list[i] = answer_list[i].text
for i in range(len(titles)):
    #print(titles[i].get('class'))
    # if titles[i].get('class') == ['accordion-header'] :
    #     current_id = titles[i].get('id')
    #     print(current_id)
    #     titles[i] = ""
    titles[i] = titles[i].text


df = pd.DataFrame(list(zip(problem_list, answer_list)), columns = ["Problem", "Answer"])
df.to_csv("midterm.csv", index = False)
