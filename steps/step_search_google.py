import os
import time

from behave import *
from selenium import webdriver
from pages.home import HomePage
from helpers.common import *
from selenium.webdriver.common.action_chains import ActionChains

script_dir = os.path.dirname(os.path.realpath(__file__))
chromepath = os.path.join(script_dir, "drivers/chromedriver")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@given(u"user access to Google website")
def user_access_to_google_website(context):
    logging.info('Start user access to Google website')
    options = webdriver.ChromeOptions()
    options.add_argument('--accept-cookies')
    context.driver = webdriver.Chrome(executable_path=chromepath, options=options)
    context.actions = ActionChains(context.driver)
    context.driver.get(HomePage.get_base_url())
    context.home_page = HomePage(context.driver)
    context.driver.maximize_window()
    save_results("user_access_to_google_website", "Success", 'None')


@step(u"cookies accept")
def cookies_accept(context):
    logging.info('Start cookies accept')
    if context.home_page.find_button_accept_cookies():
        logging.info('Exist cookies accept button')
        button_accept = context.home_page.find_button_accept_cookies()
        button_accept.click()

        create_screenshots(context, "cookies_accept.png")
    else:
        logging.warning('Not exist cookies accept')
    save_results("cookies_accept", "Success", 'None')


time.sleep(4)


@step(u"searching {text_search}")
def searching_text_search(context, text_search):
    search_box = context.home_page.find_search_tool()
    search_box.send_keys(text_search)
    search_box.submit()
    save_results("searching_text_search", "Success", 'None')


@when(u"selecting wikipedia result")
def selecting_wikipedia_result(context):
    try:
        context.home_page.get_key_search().click()
        create_screenshots(context, "selecting_wikipedia_result.png")
        save_results("selecting_wikipedia_result", "Success", 'None')
    except Exception as e:
        save_results("selecting_wikipedia_result", "Error", e)


@then(u"valid the year of the first automatic process")
def valid_the_year_of_the_first_automatic_process(context):
    find_phrase_in_text = extract_paragraph_with_text("https://es.wikipedia.org/wiki/Automatizaci%C3%B3n",
                                                      "primer proceso")
    year = find_year_in_text(find_phrase_in_text)
    year_find = str(year[0])
    logging.info('Year of the first automatic process is  ' + year_find)
    context.driver.execute_script("window.scrollTo(0, 3500)")
    create_screenshots(context, "valid_the_year_of_the_first_automatic_process.png")
    save_csv('valid_the_year_of_the_first_automatic_process.csv')
    save_results("valid_the_year_of_the_first_automatic_process", "Success", 'None')
    context.driver.close()
