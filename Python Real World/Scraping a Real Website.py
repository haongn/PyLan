# how to grab some job posts with some of the filters 


from bs4 import BeautifulSoup
import requests       # request some information from a website 

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)      # 200: status code, the request is done successfully 
                      # add .text: store the html text of that specific page

# create a BeautifulSoup instance of that html_text 
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs: 
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date: 
        company_name = job.find('h3', class_ = 'joblist-comp-name').text
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')

        # pretty print (not so pretty actually)
        print(f""" 
        Company Name: {company_name}
        Required Skills: {skills}
        """)




 






















