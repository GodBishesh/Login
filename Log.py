import requests

class FacebookLogin:

    def __init__(self):
        self.email = None
        self.password = None
        self.session = requests.Session()

    def get_credentials(self):
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")

    def login(self):
        try:
            self._load_login_page()
            self._prepare_login_data()
            self._perform_login()
        except Exception as e:
            print(f"Login failed. Error: {e}")

    def _load_login_page(self):
        self.session.get("https://www.facebook.com/login.php")

    def _prepare_login_data(self):
        self.login_data = {
            'email': self.email,
            'pass': self.password
        }

    def _perform_login(self):
        login_response = self.session.post("https://www.facebook.com/login.php", data=self.login_data)

        if 'Welcome to Facebook' in login_response.text:
            access_token = self.session.cookies.get('c_user')
            print("Login successful!")
            print(f"Access Token: {access_token}")
        else:
            print("Login failed. Check your email and password.")

if __name__ == "__main__":
    fb_login = FacebookLogin()
    fb_login.get_credentials()
    fb_login.login()
      
