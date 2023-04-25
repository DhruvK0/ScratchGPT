import requests
from bs4 import BeautifulSoup

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

# problem_list = []

# for tag in titles:
#     next_tag = tag.next_sibling
#     current_content = tag
#     while next_tag:
#         if next_tag.name == "h3":
#             break
#         # if next_tag.get("id") == 'accordionExample':
#         current_content += next_tag.text
#         next_tag = next_tag.next_sibling
#     problem_list.append(current_content)

#print(problem_list[2])

print(titles[0].text)