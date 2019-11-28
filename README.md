# python-selenium-screenshot

 This program visits specific URL to take screenshot and save it.  
     Parameters include:
     
          - { URL } : Website Link (Necessary)
          - { SCROLL POSITION } : Website scroll position in ratio (default: 0) (Optional)
          - { Wait Time } : Wait time for Website fully render (default: 1) (Optional)
          - { File Name } : Screenshot Save Name (default: current timestamp) (Optional)
## Changelog
          - [0.0.1] support chrome browser download (Env: Win10, Chrome 77 above)

## Requirement
1. Download Chrome Browser (https://cloud.google.com/chrome-enterprise/browser/download/)
2. Install Python (https://www.python.org/downloads/)
3. Install PIP (https://pip.pypa.io/en/stable/installing/)
4. Install Selenium for Python (Intro: https://selenium.dev/)
 ```bash
 $ pip install selenium
 ```

 
## Run
 ```bash
 $ python -m image_downloader https://www.bbc.com/
 ```
