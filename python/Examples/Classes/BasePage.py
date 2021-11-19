class Page:    
    count = 0

    # Constructor
    def __init__(self, **kwargs):
        self._title = kwargs['title'] if 'title' in kwargs else 'Untitled'
        self._url = kwargs['url'] if 'url' in kwargs else '0.0.0.0'

    # Getters/Accessors
    # The 'self' makes this method and not just a fcn
    def title(self, t=None):
        if t:
            self._title = t
        return self._title

    def url(self, u=None):
        if u:
            self._url = u
        return self._url
    def __str__(self):
        return f'The {self.title()} url is {self.url()}'

def main():
    page = Page(title="Login page",url="https://localhost/login")
    print(page)
    page2 = Page()
    print(page2)
    print("The count is " + str(Page.count))
    print("The count is " + str(page.count))

if __name__ == '__main__' : main()
