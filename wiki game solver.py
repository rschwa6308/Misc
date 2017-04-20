import urllib2
#from pprint import pprint




def get_links(title):
    links = []
    
    page = urllib2.urlopen("https://en.wikipedia.org/wiki/" + title).read()

    page = page[page.index('<div id="bodyContent"'):]


    sane = 0
    needlestack = []
    while sane == 0:
      curpos = page.find("href")
      if curpos >= 0:
        pagelen = len(page)
        page = page[curpos:pagelen]
        curpos = page.find('"')
        pagelen = len(page)
        page = page[curpos+1:pagelen]
        curpos = page.find('"')
        needle = page[0:curpos]
        needlestack.append(needle)
      else:
        sane = 1
    for item in needlestack:
      #print item
      links.append(item)

    links = [x[6:] for x in links if x.startswith("/wiki/")]
    
    return links







def find_path(start, end, path):
    path.append(start)

    links = get_links(start)

    if end in links:
        path.append(end)
        return path
    else:
        for link in links:
            #print link
            if end in get_links(link):
                path.append(link)
                path.append(end)
                return path

            
        





print (" " + "" + " ").join(find_path("Table", "Data", []))



#print get_links("Table")


##page = urllib2.urlopen("http://xkcd.com")
##
##print(page.read())
