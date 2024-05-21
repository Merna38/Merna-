#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


website ="https://www.yallakora.com/Match-Center/?date=18/21/2023"


# In[3]:


requests.get(website)


# In[4]:


website =requests.get(website).text


# In[5]:


print(website)


# In[6]:


print(type(website))


# In[7]:


website =BeautifulSoup(website ,"lxml")


# In[8]:


type(website)


# In[9]:


website.title.text


# In[10]:


website


# In[11]:


championships = website.find_all('div',class_='matchCard')


# In[12]:


len(championships)


# In[119]:


for i in range(len(championships)):
    print(championships[i].contents[1].find('h2').text.strip())
    matches = championships[i].contents[3].find_all('div', class_='teamCntnr')
    
    # Extracting live channel information for the current championship
    try:
        lives = championships[i].contents[3].find_all('div', class_='channel icon-channel')
    except:
        print("Error occurred while extracting live data.")
        lives = []

    for j in range(len(matches)):
        match_info = matches[j]
       
        # Extracting live channel information for the current match
        try:
            live_info = lives[j].text.strip()
        except IndexError:
            live_info = "Not available"

        teamA = match_info.find('div', {'class': 'teamA'}).text.strip()
        teamB = match_info.find('div', {'class': 'teamB'}).text.strip()
        results = match_info.find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
        score = f'{results[0].text.strip()}-{results[1].text.strip()}'
        time = match_info.find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
        
        # Printing the live channel information along with match details
        print(f" {teamA} {score} {teamB}\n\t{time}\n\tLive: {live_info}") 
    
    print('=' * 20)

