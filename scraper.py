import requests
import re


def scrape(x, y):
    response = requests.get(x)
    # requests.get takes a URL and gets its response
    # .text (used below) gets the content of the response in unicode
    count = len(re.findall(y, response.text))
    # findall creates a list of every instance of y from response.text
    # because findall returns a list, we have to use len to get the number of instances

    print('There is/are ' + str(count) + ' instance(s) of the phrase "' + y +
          '" on ' + x)

