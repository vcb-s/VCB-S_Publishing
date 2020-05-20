# -*- coding: utf-8 -*-
import requests
import getopt
import sys
import re

noSock= False
try:
    import socket
    import socks
except:
    noSock = True

def help():
    print("\nUsage:\n  bbcode.py -i <url> [-o <path>] [-p <proxy>] [-c <count>]\n")
    print("General Options:")
    print("  -h, --help          Show help.")
    print("  -i, --input <url>   Url contains comparison code.")
    print("                      NO SUPPORT for 'bangumi.moe'.")
    print("                      You need to wrap NYAA's url with '\"'.")
    print("  -o, --output <path> Path to save bbcode.")
    print("  -c, --count <count> Amount of imgs in a row, 2 as default value.")
    print("  -p, --proxy <proxy> Specify a socks proxy in the form")
    print("                      proxy.server:port")
    if(noSock):
        print("    No 'PySocks' installed, '--proxy' option has been disabled.")
        print("    You can run 'pip install PySocks' to enable this option")
    exit()

def setSock(url, port):
    if(noSock):
        print("You need run 'pip install PySocks' to enable this option")
        return
    socks.set_default_proxy(socks.SOCKS5, url, port)
    socket.socket = socks.socksocket

def getBBCode(url, outputFile, imgCount):
    context = requests.get(url).text
    pattern = re.compile(r'<a href="([^"]*\.png)"[^>]*><img src="([^"]*\.png)"[^>]*></a>')
    mResult = re.findall(pattern, context)

    bbcode = ''
    count = 0

    if(imgCount == None): imgCount = 2
    for item in mResult:
        bbcode += "[URL={0}][IMG]{1}[/IMG][/URL]".format(item[0], item[1])
        count += 1
        if(count % imgCount == 0): bbcode += '\n'
        else: bbcode += ' '

    if(outputFile != None):
        f = open(outputFile, "w+")
        f.write(bbcode)
        f.close()
        print("{0} saved".format(outputFile))
    else:
        print(bbcode)

def main(argv):
    if(len(argv) < 1):
        help()
    url        = None
    outputFile = None
    imgCount   = None
    sockUrl    = None
    port       = None
    try:
      opts, args = getopt.getopt(argv,"hi:o:c:p:",["help", "input", "output", "--count", "proxy"])
    except getopt.GetoptError:
        help()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
        elif opt in ("-i", "--input"):
            url = arg
        elif opt in ("-o", "--output"):
            outputFile = arg
        elif opt in ("-c", "--count"):
            imgCount = int(arg)
        elif opt in ("-p", "--proxy"):
            sockUrl = arg
            colon = sockUrl.find(':')
            if(colon > 0):
                port = (int)(sockUrl[colon+1:])
                sockUrl = sockUrl[:colon]
    if(sockUrl != None and port != None):
        setSock(sockUrl, port)
    if(url != None):
        getBBCode(url, outputFile, imgCount)
    else:
        help()

if __name__ == "__main__":
   main(sys.argv[1:])
