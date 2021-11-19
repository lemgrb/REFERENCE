class BasePage:
    def __init__(self, **kwargs):
        if 'title' in kwargs: self._title = kwargs['title']
        if 'url' in kwargs: self._url = kwargs['url']

    def title(self, t=None):
        if t: self._title = t
        try: return self._title
        except AttributeError: return None

    def url(self, u=None):
        if u: self._url = u
        try: return self._url
        except AttributeError: return None

    def __str__(self):
        return f'{self.title()} : {self.url()}'

class LoginPage(BasePage):
    def __init__(self, **kwargs):
        self._title='LOGINPAGE'
        if 'title' in kwargs: del kwargs['title']
        super().__init__(**kwargs)

    def log_in(self, username, password):
        print(f'Logging {username} in ....')

class Dashboard(BasePage):
    def __init__(self, **kwargs):
        self._title='DASHBOARD'
        if 'title' in kwargs: del kwargs['title']
        super().__init__(**kwargs)

def main():
    login = LoginPage()
    login.log_in('lemuel','P@ssw0rd')
    # Title provided is ignored (deleted in child constructor)
    dashboard = Dashboard(url="/dashboard", title='SOME_DASHBOARD_TITLE')

    print(login)
    print(dashboard)

if __name__ == '__main__': main()
