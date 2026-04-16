"""V032 Browser History Design Practice
TODO: implement class BrowserHistory
"""


class BrowserHistory:
    def __init__(self, homepage):
        raise NotImplementedError("TODO: implement v032 browser history __init__")

    def visit(self, url):
        raise NotImplementedError("TODO: implement v032 browser history visit")

    def back(self, steps):
        raise NotImplementedError("TODO: implement v032 browser history back")

    def forward(self, steps):
        raise NotImplementedError("TODO: implement v032 browser history forward")


if __name__ == '__main__':
    browser = BrowserHistory('leetcode.com')
    browser.visit('google.com')
    browser.visit('facebook.com')
    print(browser.back(1))  # expected: google.com
    print(browser.forward(1))  # expected: facebook.com
