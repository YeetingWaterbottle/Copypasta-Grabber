"""
This Code Is Really Bad, Don't Expect It to Perform Well
"""


import os
import requests
import pyperclip
import re
from bs4 import BeautifulSoup

# you don't have to touch this, but you can edit it, just don't leave it blank, it will break
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"


def clear_screen():  # Clear Screen
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        return


# clear_screen()


def character_2k(text):  # See If CopyPasta Have Over 2,000 Characters
    if len(text) <= 2000:
        print("This Copypasta Has Under 2,000 Characters, {} Characters in Total".format(len(text)))

    elif len(text) > 2000:
        print("This Copypasta Has Over 2,000 Characters, {} Characters in Total".format(len(text)))


def copypasta(text):
    choice_copy = input(
        "\nDo You Want The Text To Be Copied? [y/n]: ").lower()

    if choice_copy == "y" or choice_copy == "yes":
        pyperclip.copy(text)
    elif choice_copy == "n" or choice_copy == "no":
        return
    else:
        print("Enter 'Yes' or 'No'")
        return


def CopyPastaText_Com(search_input):  # Search CopyPasta On Site "https://copypastatext.com/"
    page_number = 1  # Set Default Page Number To 1
    while True:
        search_url = "https://copypastatext.com/page/{}/?s={}".format(page_number, search_input)
        page = requests.get(search_url, headers={"User-Agent": user_agent})
        soup = BeautifulSoup(page.content, "html.parser")

        site_title = soup.find_all("h2", class_="blog-entry-title entry-title")  # Find CopyPasta Title
        # site_content = soup.find_all("code")  # Find CopyPasta Content
        site_content = soup.find_all("div", class_="excerpt-wrap entry-summary")  # Find CopyPasta Content
        site_page_number = soup.find("ul", class_="page-numbers")  # Find Page Number

        clear_screen()
        if len(site_title) <= 0 or len(site_content) <= 0:  # If Cannot Find Result, Search With New Input
            print("Could Not Find Copypasta With That Search")
            search_input = input("What Copypasta Do You Want To Search: ")
        else:  # If Search Input Found, Continue
            try:
                site_max_page = max(list(map(int, re.findall(r'\d+', site_page_number.text))))
                site_min_page = min(list(map(int, re.findall(r'\d+', site_page_number.text))))
                print("Page {} / {}".format(page_number, site_max_page))
            # AttributeError: 'NoneType' object has no attribute 'text' ; If Only 1 Page Exist, print("Page 1 / 1")
            except AttributeError:
                print("Page 1 / 1")
                site_max_page = 1
                site_min_page = 1

            except:
                print("Something Went Wrong During Getting Page Number")
                os.system("pause")
                return

            for index in range(1, len(site_title)+1):  # Prints The Title With Number ex. "1 Example CopyPasta"
                print(index, site_title[index-1].text)
            print("\n'N' Goto The Next Page For Copypasta\n'P' Goto The Previous Page For Copypasta")

            choice_select = input("Which One Do You Want: ")
            try:
                choice_select = int(choice_select)

                if choice_select == 0:
                    clear_screen()
                    print("0 Is Not An Option\n")
                    os.system("pause")
                    return
                else:  # Check if "choice_select" = to 0, If It Does = to 0 Do Not - 1, Else - 1
                    choice_select -= 1
                    print(type(choice_select), choice_select)

                    copypasta_text = site_content[choice_select].text

                    clear_screen()
                    print(copypasta_text)
                    character_2k(copypasta_text)
                    copypasta(copypasta_text)
                    return

            except ValueError:
                str(choice_select).lower()
                if choice_select == "n" or choice_select == "next":
                    if page_number >= site_max_page:
                        clear_screen()
                        print("Cannot Go To The Next Page When You Are On The Last Page")
                        os.system("pause")
                    else:
                        page_number += 1
                        clear_screen()

                elif choice_select == "p" or choice_select == "previous":
                    if page_number <= site_min_page:
                        clear_screen()
                        print("Cannot Go To The Previous Page When You Are On The First Page")
                        os.system("pause")
                    else:
                        page_number -= 1
                        clear_screen()

                else:
                    print("Please Enter Only Enter Options From The Prompt")
                    os.system("pause")
                    return
            except:
                print("Something Went Wrong During 'choice_select'")
                os.system("pause")
                return


CopyPastaText_Com(input("What Copypasta Do You Want To Search: "))
