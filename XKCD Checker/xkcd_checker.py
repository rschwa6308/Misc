import urllib
from win10toast import ToastNotifier






#fetch html source and parse to find comic title
def get_comic():
    source = urllib.urlopen("http://xkcd.com").read()

    title = source[source.index("<title>")+7:source.index("</title>")][6:]

    return title



def get_whatif():
    source = source = urllib.urlopen("https://what-if.xkcd.com/").read()

    header = source[source.index("<h1>")+4:source.index("</h1>")]

    return header





if __name__ == "__main__":

    #initialize toaster object
    toaster = ToastNotifier()
    icon_path = "xkcd icon 16.ico"         #toast icon path
    
    #open log files in read+write mode
    comic_log = open("comic_log.txt", "r+")
    whatif_log = open("whatif_log.txt", "r+")
    
    #read latest titles from file
    latest_comic = comic_log.read()
    latest_whatif = whatif_log.read()

    #get current titles
    current_comic = get_comic()
    current_whatif = get_whatif()

    #compare latest to current
    if latest_comic == current_comic:
        #print "No new Comic"
        pass
    else:
        #print "New Comic!\nTitle: '" + current_comic + "'"
        comic_log.seek(0)        #clear file
        comic_log.truncate()     #^^^^^^^^^^
        comic_log.write(current_comic) #write current title to file
        toaster.show_toast("XKCD", "New Comic!\nTitle: \"" + current_comic + "\"", icon_path, 10)

    print ""

    if latest_whatif == current_whatif:
        #print "No new WhatIf"
        pass
    else:
        #print "New WhatIf!\nTitle: '" + current_whatif + "'"
        whatif_log.seek(0)        #clear file
        whatif_log.truncate()     #^^^^^^^^^^
        whatif_log.write(current_whatif) #write current title to file
        toaster.show_toast("XKCD", "New What If!\nTitle: \"" + current_whatif + "\"", icon_path, 10)

    #close files
    comic_log.close()
    whatif_log.close()
        

    
