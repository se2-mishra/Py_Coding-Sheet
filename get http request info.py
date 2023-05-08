import urllib
import webbrowser
choice=input("Want to get http request information(Yes/No):")
while choice.upper()=="YES" or choice.upper()=="Y":
    urlop=input("Enter the url \n In the format prescribed(http://www.abc.com/) :\n  ->")
    weburl=urllib.request.urlopen(urlop)
    html=weburl.read()
    data=weburl.getcode()
    url=weburl.geturl()
    hd=weburl.headers
    inf=weburl.info()
    print("The url is",url)
    print("HTTP status code is",data)
    print("headers returned \n",hd)
    print("the info() returned :\n",inf)
    print("Now opening the url",url)
    webbrowser.open_new(url)
    choice=input("Want some more:")
else:
    print("Now you can go through the data arrived")