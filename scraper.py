import requests
from bs4 import BeautifulSoup
import bs4

URL = "https://practice.dsc10.com/wi22-midterm/index.html"
page = requests.get(URL)
encoded_text = page.text.encode("utf-8")
test = encoded_text.decode("utf-8")

soup = BeautifulSoup(encoded_text, "html.parser")

info_picture = soup.find_all("center")[0]
paragraphs = soup.find_all("p")

info_pars = paragraphs[4:7]

titles = soup.find_all("h3")

first_prob = titles[0]
first_desc = first_prob.next_sibling.next_sibling.next_sibling.next_sibling
first_answers = first_desc.find_next_sibling("ul")
first_answer = first_answers.find_next_sibling("div")

# for paragraph in paragraphs:
#     if "Welcome to the Midterm Exam for DSC 10 Winter 2022" in paragraph or " For each skyscraper, we have: - its name, which is stored in the index of" in paragraph:
#         info_par.append(paragraph)
# print(first_prob)
# print(first_desc)
# print(first_answers)
#print(first_answer)

problem_list = []

for tag in titles:
    next_tag = tag.next_sibling
    current_content = tag.text
    while next_tag: 
        #check if the next tag is a div and has the class "accordion-body"
        if isinstance(next_tag, bs4.element.Tag):
            print(next_tag.attrs)
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
    titles[i] = titles[i].text

#print(problem_list[0])