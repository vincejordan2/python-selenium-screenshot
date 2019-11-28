import time
import os
import sys
from datetime import datetime

from selenium import webdriver

DRIVER_PATH = '\\chromedriver_win32\\chromedriver.exe'

def download_image():
    height_ratio = 0
    wait_time = 1
    file_name = '{}.png'.format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    def_paras = [height_ratio, wait_time, file_name]
    
    path = '{0}{1}'.format(os.path.dirname(__file__), DRIVER_PATH)
    print(path)
    
    args = sys.argv[1:]    
    if len(args) < 1:
        err_msg = '''
        This program visits specific URL to take screenshot and save it.  
        Parameters include:  
        { URL } : Website Link (Necessary)  
        { SCROLL POSITION } : Website scroll position in ratio (default: 0) (Optional)
        { Wait Time } : Wait time for Website fully render (default: 1) (Optional)
        { File Name } : Screenshot Save Name (default: current timestamp) (Optional)
        '''
        return err_msg
    elif len(args) == 1:
        args.extend(def_paras)
    elif len(args) == 2:
        args.extend(def_paras[1:])
    elif len(args) == 3:
        args.extend(def_paras[2:])
    print(args)
    
    chrome_options = webdriver.ChromeOptions().add_argument('–headless')
    brower=webdriver.Chrome(executable_path=path,
                            chrome_options=chrome_options)
    brower.get(args[0])
    brower.maximize_window()
    page_height = brower.execute_script("return document.body.scrollHeight")
    scroll_pos = page_height * float(args[1])
    brower.execute_script("window.scrollBy(0, {0})".format(scroll_pos))
    time.sleep(float(args[2]))
    brower.save_screenshot(args[3])
    brower.close()


if __name__ == "__main__":
    # grapWebSite('http://pi.garmin.com.tw:999/SmartFactory/#/analytics/prod-dashboard')
    # download_image('http://pi.garmin.com.tw:999/SmartFactory/#/analytics/job?jobNumber=14641228')
    sys.exit(download_image())