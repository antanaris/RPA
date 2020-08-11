## Web automation API

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class Web():
    """Writes and executed next steps with Selenium"""

    def __init__(self):
        # next steps parameters
        self.next_steps_file_url = "next_steps.json"


## Get next_steps

# no next steps --> check if next_steps.json is empty
def empty(self):
    steps_file = open("next_steps.json", 'w')

## execute next_steps

