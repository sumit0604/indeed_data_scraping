# indeed_data_scraping

def extraction(page):
    information about that function---------
    this extract function is for getting argument as page and put that argument on url dynamically
    for getting header just type my user agent on google chrome and the copy that user id
    Beautifulsoup is here to just prettify the Html content and show it in html format with the help of html.parser


def transform(soup):
      information about this function......
      this function is taking soup as argument and use the find_all function to scrap data from indeed with the help of tag name and class name
      here i started with the div tag in which all the information is stored and use its class name...
      
  
  
url = f'https://in.indeed.com/jobs?q=python+developer&l=Delhi&start={page}'

important note about url paging----
0 page of indeed has only 15 entity/content..and next page number is 10,so for getting content from other page i use this for loop
this loop is just to scrap data from diffrent page with a jump of 10..range(0,40,10)..0 means starting page number..
40 means end page number and 10 means that jump from 0 to 10,then 10 to 20, then 20 to 30...and so on


at last storing all those data into CSV file----
to save Dataframe into CSV we use to_csv method and then give the name of file whatever you want to give
