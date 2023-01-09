import requests
import re


def scrape(x, y, z):
    response = requests.get(x)
    # requests.get takes a URL and gets its response
    # .text (used below) gets the content of the response in unicode

    if z:
        count = len(re.findall(y, response.text))
        # findall creates a list of every instance of y from response.text
        # because findall returns a list, we have to use len() to get the number of instances
    else:
        count = len(re.findall(y.casefold(), response.text.casefold()))
        # casefold allows us to compare both strings in every possible case

    print('There is/are ' + str(count) + ' instance(s) of the phrase "' + y +
          '" in ' + x)
