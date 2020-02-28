# -*- coding: utf-8 -*-
import json
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

# TODO: Put all AI into Lifecycle package and add a licence to it
from lifecycle import Sherlock

# Starting testcases
class Helper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def intreractiveRPA(self):
        driver = self.driver
        Sherlock = Sherlock()



        # TODO: Realize logging

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def executeStep(self, selector_type, selector, action_type, wait = True):
        driver = self.driver
        # Run a step with selenium driver
        try:
            if selector_type == "css":
                if action_type == "click":
                    driver.find_element_by_css_selector(selector).click()
            if selector_type == "url":
                if action_type == "get":
                    driver.get(selector)
            print("Executing action " + action_type + " on " + selector_type + ":" + selector + " -- Success")
        except:
            # TODO: add ability to game model to track actual game behaviour (by default assumes exec was successful)
            print("Executing action " + action_type + " on " + selector_type + ":" + selector + " -- Failure")
        # waiting, so that user can see what's going on
        if wait:
            time.sleep(2)

    def executeSteps(self, steps_json_url):
        # Read the json file
        # print("Loading next steps from json file")
        with open(steps_json_url) as json_file:
            next_steps_json = json.loads(json_file.read())

        # Get the list of steps and execute them
        for step in next_steps_json["steps"]:
            # TODO: add exception handling in case json has variable structure OR make the fields in json obligatory
            selector_type = step["selectorType"]
            selector = step["selector"]
            action_type = step["action"]
            self.executeStep(selector_type, selector, action_type)

if __name__ == "__main__":
    unittest.main()
