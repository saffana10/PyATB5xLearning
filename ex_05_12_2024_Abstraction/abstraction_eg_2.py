from abc import ABC , abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def read_from_excel(self):
        pass


class Browser(ExcelReader):

    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def stop_browser(self):
        pass

class TC1():

    def start_browser(self):
        print("Browser is starting")


    def stop_browser(self):
        print("Browser is stopping")

    def read_from_excel(self):
        print("Read from excel")

tc = TC1()
tc.start_browser()
tc.read_from_excel()
tc.stop_browser()

