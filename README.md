# scraping-fun
A nonsense little experiment scraping the results of a library catalogue search. 


# A Scraper for the library records of HAB Wobü
This little program will extract the metadata from the library catalog in structured form. This metadata is supposed to be reused, yet copy and paste is tedious.
This script is supposed to automate the process.

## Description of the site
* The links looks as follows: http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=31
* with the =31 at the end being the results with which it starts, there are 71 results linked to Michael Maier.
* possibly not all are needed
* annoyingly, the URL is not really straightforward: http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=37/MAT=/NOMAT=T/REL?PPN=080093043
* Maier, Michael has a fixed person id apparently: `Maier, Michael, 1568 - 1622 (Zeit, Lebensdaten)  = PPN=080093043`



```python
from lxml import html
import requests
```


```python
starting_url = 'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=01'
url_front = 'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST='

pages_list = ['01','11','21','31','41','51', '61']

for item in pages_list:
    print(url_front + item)
    
page_store = []

the_pages = [(url_front + item) for item in pages_list]
the_pages
```

    ['http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=01',
     'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=11',
     'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=21',
     'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=31',
     'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=41',
     'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=51',
     'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=21/NXT?FRST=61']




```python
def print_elem(elem):
    print("<%s>\nTags: %s;\n%s...\n\n" % (elem.tag, elem.attrib, elem.text_content()[:200].replace('\n', ' ')))
```


```python
for one_page in the_pages:
    page = requests.get(one_page)
    page_store.append(page)
```


```python
page_store
for page in page_store:
    tree = html.fromstring(page.text)
    print_elem(tree)
```

    <html>
    Tags: {};
           window.addEventListener("load", function(){ window.cookieconsent.initialise({   "palette": {     "popup": {       "background": "#dbdbdb"     },     "button": {       "background": "#9e9e9e"   ...
    <html>
    Tags: {};
           window.addEventListener("load", function(){ window.cookieconsent.initialise({   "palette": {     "popup": {       

# Overview page of the search results


```python
mainpage = 'http://opac.lbs-braunschweig.gbv.de/DB=2/SET=2/TTL=37/MAT=/NOMAT=T/REL?PPN=080093043'
page = requests.get(mainpage)
tree = html.fromstring(page.text)
print_elem(tree)
tree.text_content()
```
...
    Tags: {};
           window.addEventListener("load", function(){ window.cookieconsent.initialise({   "palette": {     "popup": {       "background": "#dbdbdb"     },     "button": {       "background": "#9e9e9e"   ...
...
Suchen\n\n\n\xa0\n\xa0|\xa0\n\xa0Suchergebnis\xa0\n\xa0|\xa0\n\xa0\nvar ah=screen.availHeight-100;\nvar aw=screen.availWidth-.....
    \n\t\teingrenzen\n\t\terweitern\n\t\tausgenommen\n\t\tneu ordnen\n\t    \n\t    Index blättern\n\t    \n\t\n\t\n\t    \n\t\t\n\t\t[ALL] Alle Wörter\n\t    \n\t\t\n\t\t[PER] Person\n\t    \n\t\t\n\t\t[TIT] Titel (Stichwort)\n\t    \n\t\t\n\t\t[WTP] Werktitel (Phrase)\n\t    \n\t\t\n\t\t[SER] Serie, Zeitschrift (Stichwort)\n\t    \n\t\t\n\t\t[KOR] Körperschaft, Konferenz, Geografikum (Stichwort)\n\t    \n\t\t\n\t\t[NUM] Nummern (allgemein)\n\t    \n\t\t\n\t\t[SLW] Schlagwörter\n\t    \n\t\t\n\t\t[BKL] Basisklassifikation\n\t    \n\t\t\n\t\t[SGN] Signatur ohne Blanks und ohne Sonderzeichen\n\t    \n\t\t\n\t\t[VER] Veröffentlichungsangaben\n\t    \n\t\t\n\t\t[BBG] Bibliogr. Gattung und Status\n\t    \n\t\t\n\t\t[FPR] Fingerprint (Phrase)\n\t    \n\t\t\n\t\t[PRN] Provenienz (Ex-Ebene)\n\t    \n\t\t\n\t\tSystematik Altbestand [LSY]\n\t    \n            \n\n\npu="";\npopup="";\nfunction PU(URL,w,h,NAME) {\n    var v=parseInt(navigator.appVersion);\n    if (v>="3") {\n        if (typeof NAME == \'undefined\' || NAME == "") {\n          NAME="_blank";\n        }\n        .
    .....
    </TR>\');\n\n\n\nAbmelden\n\nTrefferanalyse\n\n\xa0\n\xa0\n\xa0\n\xa0\n\xa0\n\xa0\n\xa0\n\xa0\n\n  \n\n    \n    \n\n\n    \n    \n\n    \n\n1\xa0-\xa010\xa0von\xa069\xa0\xa0\xa0\xa0\xa0\xa0\n    \n\n    Ihre Aktion\n    \xa0bezogen auf\xa0Maier, Michael, 1568 - 1622 (Zeit, Lebensdaten)\n\n\n\n\n        \n    \n        \n\n\n\n    \n    \n    \n\n\n\n    \n    1.\xa0\n    \n\nEin religionswissenschaftlicher Kommentar zu den Arcana Arcanissima und der Mythoalchemie des alchemo-hermetischen latrochemikers Michael Maier (1568-1622)/ Lang, Sarah. - Graz : Grazer Universitätsverlag - Leykam - Karl-Franzens-Universität Graz, 2018\n    \n    \n  \n\n  \n\n    \n    2.\xa0\n    \n\nMichael Maier : nine newly discovered letters/ Lenke, Nils. - In: Ambix, Bd. 61 (2014), 1, S.1-47\n    \n    \n  \n\n  \n\n    \n    3.\xa0\n    \n\nDie Tradierung alchemischen Wissens bei Michael Maier, Andreas Libavius und Oswald Croll/ Wels, Volkhard. - In: Natur - Religion - Medien (2013), S.63-85\n    \n    \n  \n\n  \n\n    \n    4.\xa0\n    \n\nDoppelt verkettete Tricinien : Zarlino, Calvisius und 

## The data is structured as follows
There is a table with `@summary` whose value is `hitlist`
```html
table @summary="hitlist"
tbody
tr 1=picture
tr valign=top

td class=hit algin=left 
```
--> text contains a link (the title) and the author name, first name - pub place: publisher, year. 

```html
a #InitialFocusPoint
href SHW?FRST=1
```
the results are then numbered from 1-69



## Having fun

When we run the next cell, we realize that - oh my- my master's thesis shows up as the first search result. Well isn't this fun....


```python
hits = tree.xpath("//table[@summary='hitlist']/tr[@valign='top']/td[@class='hit' and @align='left']")
for hit in hits:
    print_elem(hit)
```

    <td>
    Tags: {'class': 'hit', 'align': 'left', 'valign': 'top'};
      Ein religionswissenschaftlicher Kommentar zu den Arcana Arcanissima und der Mythoalchemie des alchemo-hermetischen latrochemikers Michael Maier (1568-1622)/ Lang, Sarah. - Graz : Grazer Universitäts...
    
    
    <td>
    Tags: {'class': 'hit', 'align': 'left', 'valign': 'top'};
      Michael Maier : nine newly discovered letters/ Lenke, Nils. - In: Ambix, Bd. 61 (2014), 1, S.1-47     ...
    


# Getting the data in structured form
Now that we have localized the data we wanted (yet didn't actually need..), we save it in structured from.
* linklist has all the links (i.e. titles)
* href attribute is the link to the catalog entry for the title, we want to save that just in case. 


```python
titles = {}
linklist = tree.xpath("//table[@summary='hitlist']/tr[@valign='top']/td[@class='hit' and @align='left']/a")
tds = tree.xpath("//table[@summary='hitlist']/tr[@valign='top']/td[@class='hit' and @align='left']")

for link in linklist:
    print(link.text_content())
    print(link.attrib['href'])
```

    Ein religionswissenschaftlicher Kommentar zu den Arcana Arcanissima und der Mythoalchemie des alchemo-hermetischen latrochemikers Michael Maier (1568-1622)
    SHW?FRST=1
    Michael Maier : nine newly discovered letters
    SHW?FRST=2
    Die Tradierung alchemischen Wissens bei Michael Maier, Andreas Libavius und Oswald Croll
    SHW?FRST=3


## We can also get the whole citation like this:


```python

for td in tds:
    print(td.text_content())
```

   
Using the link list generated earlier, we could do this for all the result pages so we'd get all the 69 results. 
And we could follow the follow-up links to the catalogue but the catalogue entries are not as easy to scrape, so we'll stop here.



