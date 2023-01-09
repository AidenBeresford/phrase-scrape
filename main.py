import sys
import scraper

url = "https://github.com"
phrase = "Did you forget to enter a phrase?"
sensitive = True

while True:
    print("\nChoose an option:\n1. Enter URL\n2. Enter Phrase\n3. Search Website\n4. Toggle"
          " Case Sensitivity (" + str(sensitive) + ")\n5. Quit\n")
    choice = input("Enter number: ")

    match choice:
        case '1':
            url = input("URL: ")

        case '2':
            if sensitive:
                phrase = input("Phrase (Case Sensitive): ")
            else:
                phrase = input("Phrase (Case Insensitive): ")

        case '3':
            scraper.scrape(url, phrase, sensitive)
            # function used in scraper.py

        case '4':
            if sensitive:
                sensitive = False
            else:
                sensitive = True

        case '5':
            sys.exit()
            # exits the program

        case _:
            print("Invalid!")
