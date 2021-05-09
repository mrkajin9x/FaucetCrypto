# Solve captcha by using https://2captcha.com?from=11528745.

import requests
import time


class Captcha:
    def __init__(self, APIKey):
        self.APIKey = APIKey

    def HCaptcha(self, sitekey, pageurl):
        link = 'http://2captcha.com/in.php?key=%s&method=hcaptcha&sitekey=%s&pageurl=%s'
        req = requests.get(link % (self.APIKey, sitekey, pageurl), timeout=30)
        id = ''
        if 'OK|' in req.text:
            id = req.text.split('|')[1]
        result = ''
        if id != '':
            while True:
                time.sleep(5)
                link = 'http://2captcha.com/res.php?key=%s&action=get&id=%s'
                req = requests.get(link % (self.APIKey, id), timeout=30)
                if 'OK|' in req.text:
                    result = req.text.split('|')[1]
                    break
        return result
