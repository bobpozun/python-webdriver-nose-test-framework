#!/usr/local/bin/python

def wait_and_find_element(driver, element, tries=10, selector='css'):
    import time
    elem = None
    timeout = tries
    for x in range(0, timeout):
        time.sleep(1)
        try:
            if selector == 'css':
                elem = driver.find_element_by_css_selector(element)
            if selector == 'text':
                elem = driver.find_element_by_link_text(element)
            if selector == 'xpath':
                elem = driver.find_element_by_xpath(element)
            if elem.is_displayed():
                break
        except:
            print ('Element %s not found. Trying again.' % element)
    if not elem:
        raise ValueError('Element %s not found.' % element)
    return elem


def wait_for_element_text(driver, element):
    import time
    e = ''
    for x in range(0, 10):
        time.sleep(1)
        e = wait_and_find_element(driver, element).text
        if e != '':
            break
    return e


def get_multiple_elements(driver, element, selector_format='css'):
    wait_and_find_element(driver, element)
    if selector_format == 'css':
        return driver.find_elements_by_css_selector(element)
    if selector_format == 'text':
        return driver.find_elements_by_link_text(element)
    if selector_format == 'xpath':
        return driver.find_elements_by_xpath(element)


def verify_not_exists(driver, element):
    exists = None
    try:
        wait_and_find_element(driver, element, tries=3)
        exists = True
    except:
        print "This is expected. Continuing."
    if exists:
        raise ValueError('Element %s exists and should not' % element)


def verify_not_visible(driver, element):
    exists = None
    try:
        wait_and_find_element(driver, element, tries=3).is_displayed()
        exists = True
    except:
        print "This is expected. Continuing."
    if exists:
        raise ValueError('Element %s is displayed and should not be' % element)


def move_to_element(driver, element):
    from selenium.webdriver import ActionChains
    action = ActionChains(driver)
    action.move_to_element(element).perform()

def close_tab(driver, main_tab):
    tabs = driver.window_handles
    for tab in tabs:
        if tab != main_tab:
            driver.switch_to.window(tabs[1])
            driver.close()
    driver.switch_to.window(main_tab)


def validate_checkbox(driver, checkbox, expected="False"):
    checked = wait_and_find_element(driver, checkbox).is_selected()
    if checked:
        if expected == "True":
            return driver
        else:
            raise ValueError('%s is checked. Failing test.' % checkbox)
    if not checked:
        if expected == "False":
            return driver
        else:
            raise ValueError('%s is not checked. Failing test.' % checkbox)

def clear_element(element):
    from selenium.webdriver.common.keys import Keys
    for x in range(0, 100):
        element.send_keys(Keys.BACKSPACE)
    return element