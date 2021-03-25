#pip install requests
#pip install bs4
#pip install pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

#this extract function is for getting argument as page and put that argument on url dynamically
#for getting header just type my user agent on google chrome and the copy that user id
#Beautifulsoup is here to just prettify the Html content and show it in html format with the help of html.parser
def extract(page):
    header ={'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    url = f'https://in.indeed.com/jobs?q=python+developer&l=Delhi&start={page}'
    r = requests.get(url,header)
    soup =BeautifulSoup(r.content,'html.parser')
    return soup

#this function is taking soup as argument and use the find_all function to scrap data from indeed with the help of tag name and class name
#here i started with the div tag in which all the information is stored and use its class name...
def transform(soup):
    divs =soup.find_all('div', class_ ='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='company').text.strip()
        #using of try and except in salary because salary has null value also so it will genrate an error...

        try:
            salary = item.find('span',class_='salaryText').text.strip()
        except:
            salary =''
        summary = item.find('div',class_= 'summary').text.strip()

        job ={
            'title' : title,
            'salary' : salary,
            'company' : company,
            'summary' : summary
        }
        joblist.append(job)
    return

print("data is scrapping please wait......")

#empty list for storing that data which is in job dictionary....
joblist=[]


# 0 page of indeed has only 15 entity/content..and next page number is 10,so for getting content from other page i use this for loop
#this loop is just to scrap data from diffrent page with a jump of 10..range(0,40,10)..0 means starting page number..
# 40 means end page number and 10 means that jump from 0 to 10,then 10 to 20, then 20 to 30...and so on


for i in range(0,90,10):
    c=extract(i)
    transform(c)

# print(len(joblist))  before printing the data which is scrapped, print the length of list,just to get result fast that data scrapping is going good or not

df =pd.DataFrame(joblist)
print(df.head())

#to save Dataframe into CSV we use to_csv method and then give the name of file whatever you want to give

df.to_csv('newcsv.csv')


print("file is created")




