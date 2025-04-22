class BaseTest:

    def open_browser(self):
        print("starting the browser")

    def closing_browser(self):
        print("closing the browser")

class TestCase1(BaseTest):

    def test_1(self):
        self.open_browser()
        print("Testcase 1 executed")
        self.closing_browser()

class TestCase2(BaseTest):

    def test_2(self):
        self.open_browser()
        print("TestCase P1 executed")
        self.closing_browser()

    def test_3(self):
        self.open_browser()
        print("TestCase N1 executed")

class TestCase3(BaseTest):

    def test_3(self):
        self.open_browser()
        print("Tescase P2 executed")
        self.closing_browser()

    def test_4(self):
        self.open_browser()
        print("Testcase N2 executed")
        self.closing_browser()

testcase1 = TestCase1()
#testcase1.open_browser()
testcase1.test_1()
print("-----")
testcase2 = TestCase2()
testcase2.test_2()
print("-----")
testcase3 = TestCase3()
testcase3.test_3()
print("-----")
testcase3.test_4()

