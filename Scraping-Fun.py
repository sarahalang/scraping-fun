#!/usr/bin/env python
# coding: utf-8

# # A Scraper for the library records of HAB Wobü
# This little program will extract the metadata from the library catalog in structured form. This metadata is supposed to be reused, yet copy and paste is tedious.
# This script is supposed to automate the process.
# 
# ## Description of the site
# * The links looks as follows: http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=31
# * with the =31 at the end being the results with which it starts, there are 71 results linked to Michael Maier.
# * possibly not all are needed
# * annoyingly, the URL is not really straightforward: http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=37/MAT=/NOMAT=T/REL?PPN=080093043
# * Maier, Michael has a fixed person id apparently: `Maier, Michael, 1568 - 1622 (Zeit, Lebensdaten)  = PPN=080093043`
# 

# In[1]:


from lxml import html
import requests


# In[2]:


starting_url = 'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=01'
url_front = 'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST='

pages_list = ['01','11','21','31','41','51', '61']

for item in pages_list:
    print(url_front + item)
    
page_store = []

the_pages = [(url_front + item) for item in pages_list]
the_pages


# In[3]:


def print_elem(elem):
    print("<%s>\nTags: %s;\n%s...\n\n" % (elem.tag, elem.attrib, elem.text_content()[:200].replace('\n', ' ')))


# In[4]:


for one_page in the_pages:
    page = requests.get(one_page)
    page_store.append(page)


# In[5]:


page_store
for page in page_store:
    tree = html.fromstring(page.text)
    print_elem(tree)


# # Overview page of the search results

# In[6]:


mainpage = 'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=37/MAT=/NOMAT=T/REL?PPN=080093043'
page = requests.get(mainpage)
tree = html.fromstring(page.text)
print_elem(tree)
tree.text_content()


# ## The data is structured as follows
# There is a table with `@summary` whose value is `hitlist`
# ```html
# table @summary="hitlist"
# tbody
# tr 1=picture
# tr valign=top
# 
# td class=hit algin=left 
# ```
# --> text contains a link (the title) and the author name, first name - pub place: publisher, year. 
# 
# ```html
# a #InitialFocusPoint
# href SHW?FRST=1
# ```
# the results are then numbered from 1-69
# 
# 

# ## Having fun

# When we run the next cell, we realize that - oh my- my master's thesis shows up as the first search result. Well isn't this fun....

# In[7]:


hits = tree.xpath("//table[@summary='hitlist']/tr[@valign='top']/td[@class='hit' and @align='left']")
for hit in hits:
    print_elem(hit)


# # Getting the data in structured form
# Now that we have localized the data we wanted (yet didn't actually need..), we save it in structured from.
# * linklist has all the links (i.e. titles)
# * href attribute is the link to the catalog entry for the title, we want to save that just in case. 

# In[8]:


titles = {}
linklist = tree.xpath("//table[@summary='hitlist']/tr[@valign='top']/td[@class='hit' and @align='left']/a")
tds = tree.xpath("//table[@summary='hitlist']/tr[@valign='top']/td[@class='hit' and @align='left']")

for link in linklist:
    print(link.text_content())
    print(link.attrib['href'])


# ## We can also get the whole citation like this:

# In[9]:



for td in tds:
    print(td.text_content())


# * `http://opac.lbs-braunschweig.gbv.de/DB=2/SET=4/TTL=11/NXT?FRST=21` 
# is the current page. 
# * The follow-up hrefs are SHW?FRST=num
# * `http://opac.lbs-braunschweig.gbv.de/DB=2/SET=4/` + `TTL=21/SHW?FRST=21`
# 
# 

# Using the link list generated earlier, we could do this for all the result pages so we'd get all the 69 results. 
# And we could follow the follow-up links to the catalogue but the catalogue entries are not as easy to scrape, so we'll stop here.



