#!/usr/bin/env python

import time
import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def lambda_handler(event, context):
#  print "hello, world"
#  print os.getcwd()

  # set user agent
  user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36")

  dcap = dict(DesiredCapabilities.PHANTOMJS)
  dcap["phantomjs.page.settings.userAgent"] = user_agent
  dcap["phantomjs.page.settings.javascriptEnabled"] = True

  browser = webdriver.PhantomJS(service_log_path=os.path.devnull, executable_path="/var/task/phantomjs", service_args=['--ignore-ssl-errors=true'], desired_capabilities=dcap)

  browser.get('http://google.com')
  html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
  print html
