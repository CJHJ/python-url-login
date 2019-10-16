from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import argparse


# Facebook URL
URL = "https://facebook.com"
output = "test.png"


def main(args):
    # Set headless
    options = Options()
    options.headless = True

    # Open browser and go to url
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(640, 480)
    driver.get(URL)

    # Get login elements
    user_element = driver.find_element_by_name('email')
    pass_element = driver.find_element_by_name('pass')

    # Input login elements
    user_element.send_keys(args.uname)
    pass_element.send_keys(args.pwd)

    # Submit
    try:
        driver.find_element_by_name('login').click()
    except:
        driver.find_element_by_id(
            'loginbutton').find_elements_by_tag_name('input')[0].click()

    # Take a screenshot
    driver.save_screenshot(args.output_path)
    driver.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Take screenshot of homepage after login. Currently only supports Facebook.")
    parser.add_argument('-u', '--uname', action='store', type=str, dest='uname',
                        help="your username")
    parser.add_argument('-p', '--pass', action='store', type=str, dest='pwd',
                        help="your password")
    parser.add_argument('-o', '--screenshot-path', type=str, dest='output_path',
                        default='output.png', help="screenshot path")
    args = parser.parse_args()

    main(args)
