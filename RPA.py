# -*- coding: utf-8 -*-
import json
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

from automation import web

# TODO: export dmm creation/modification into dmm engine
# from lifecycle import dmm

# Starting testcases
class Helper(unittest.TestCase):
    """
    Selenium helper
    ----------
    It is a core class to run tests using Selenium library
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_interactiveRPA(self):
        """
        The main logic of interactive testing.

        ---
        `test_` added to run under unittest
        """
        driver = self.driver

        # TODO: ask what task we're doing
        # login.py -- Passing all untested test cases in the TestRail run

        # Testrun variables
        testrun_url = 'https://lifecycletest2.testrail.io/index.php?/runs/view/1'
        testrun_id = 'R1'
        version = '0.1'
        elapsed = '1m'

        username = 'anastasia@lifecycle.today'
        password = "Pass1234!"

        # Load the testrun page
        driver.get(testrun_url)

        # TODO: login

        # if login screen
            # url contains /auth/login
            # page has "Log into Your Account" text
        # execute login steps from login.py until next_steps.json is empty



        # TODO: load and execute dmm of the task

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

    #TODO: Extend actions for next_steps.json
    def executeStep(self, selector_type, selector, action_type, wait=True):
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
