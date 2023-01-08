import sys

import scraper

url = "https://github.com"
phrase = "Did you forget to enter a phrase?"

while True:
    print("\nChoose an option:\n1. Enter URL\n2. Enter Phrase\n3. Search Website\n4. Quit\n")
    choice = input("Enter number: ")

    match choice:
        case '1':
            url = input("URL: ")

        case '2':
            phrase = input("Phrase (Case Sensitive): ")

        case '3':
            scraper.scrape(url, phrase)
            # function used in scraper.py

        case '4':
            sys.exit()
            # exits the program

        case _:
            print("Invalid!")
