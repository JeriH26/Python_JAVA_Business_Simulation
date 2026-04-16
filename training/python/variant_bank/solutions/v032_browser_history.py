"""V032 Browser History Design
Time: O(1) amortized per operation, Space: O(n)
"""


class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.index = 0

    def visit(self, url):
        self.history = self.history[:self.index + 1]
        self.history.append(url)
        self.index += 1

    def back(self, steps):
        self.index = max(0, self.index - steps)
        return self.history[self.index]

    def forward(self, steps):
        self.index = min(len(self.history) - 1, self.index + steps)
        return self.history[self.index]


if __name__ == '__main__':
    browser = BrowserHistory('leetcode.com')
    browser.visit('google.com')
    browser.visit('facebook.com')
    print(browser.back(1))
    print(browser.forward(1))
