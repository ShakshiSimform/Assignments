from bs4 import BeautifulSoup
from lxml import etree
import requests
import json

url = "https://www.javatpoint.com/python-mcq"
r = requests.get(url)

contents = BeautifulSoup(r.text, 'lxml')
dom = etree.HTML(str(contents))

data=[]

for i in range(1, 56):
  web_data={}

  #questions
  questions = dom.xpath(f'//p[@class="pq"][{i}]/text()')
  print(questions)

  web_data['question'] = questions if questions else None
  
  #code snippet
  code = dom.xpath(f'//p[@class="pq"][{i}]/following-sibling::div[1]//textarea[@name="code"]/text()')
  print(code)

  web_data['code_snippet'] = code if code else []

  #sub question
  sub = dom.xpath(f'//p[@class="pq"][{i}]/following-sibling::div[1]/following-sibling::*[1]/text()')
  print(sub)

  web_data['sub_question'] = sub if sub else []
  
  #options
  options = dom.xpath(f'//ol[@class="pointsa"][{i}]/li/text()')
  print(options)

  #correct_option
  answer = dom.xpath(f'//div[@class="testanswer"][{i}]/p[1]/text()')
  print(answer)

  web_data['correct_option'] = answer[0] if answer else None

  #explanation
  explanation = dom.xpath(f'//div[@class="testanswer"][{i}]/p[2]/text()')
  print(explanation)

  web_data['explanation'] = explanation[0] if explanation else None

  print()

  data.append(web_data)

# Convert the data to JSON and save it to a file
with open('web.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been successfully saved to web.json")

