class OldBrowser:

    def start_browser(self):
        print("IE browser will start")

    def stop_browser(self):
        print("IE browser will stop")

class Chrome(OldBrowser):

    def start_browser(self):

       super().start_browser() #parent browser also
        #print("Chrome will start")

    def stop_browser(self):
        print("Chrome will stop")

chrome = Chrome()

chrome.start_browser()
chrome.stop_browser()