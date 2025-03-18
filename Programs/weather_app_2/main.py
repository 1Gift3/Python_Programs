import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.Qtcore import Qt
#Im also still getting error on pyqt5 saying no module names 'pyqt5.qt...

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter your city")
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel (self)
        #I learned how to do degrees which you make sure numlock is on then Alt with 0176
        self.emoji_label = QLabel(self)
        # I have EMoji Problems
        self.description_label =QLabel("Sunny", self)
        self.initUI()


    def iniUI(self):
        self.setWindowTitle("Wether App")


        vbox = QVBoxLayout()


        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)


        self.city_label.setAlignment(Qt.ALignCenter)
        self.city_input.setAlignment(Qt.ALignCenter)
        self.temperature_label.setAlignment(Qt.ALignCenter)
        self.emoji_label.setAlignment(Qt.ALignCenter)
        self.description_label.setAlignment(Qt.ALignCenter)

        self.city_label.setObjectName("city_label")
        self.city_label.setObjectName("city_input")
        self.city_label.setObjectName("get_weather_button")
        self.city_label.setObjectName("temperature_label")
        self.city_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-famaily: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;               
            }               
            QLineEdit#city_input{
                fornt-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }  
            QLabel#temperature_label{
                fornt-size: 75px;
            }
            QLabel#emoji_label{
            font-size: 100px
            font-family: segoe UI emoji;
            }
            QLabel#description_label{
            font-size: 50px;
            }               
        """) 

        self.get_weather_button.clicked.connect(self.get_weather)                            


    def get_weather(self):

        api_key = "f343ca3a5ec4f731a75ec2583844b49b"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:

            response = requests.get(url)
            response.rasie_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad request/nPlease check your input")
                case 401:
                    self.display_error("Unathorized/nInvalid API key")
                    #found how i can unauthorised whaat what mode edit mode i believe
                case 403:
                    self.display_error("Forbiden/nAccess is denied")
                case 404:
                    self.display_error(" Not founds/nCity not found")
                case 500:
                    self.display_error("Internal Server Error/nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway/nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable/nServer is down")
                case 504:
                    self.display_errorint("Gateway Timeout/nNo response from the serve")
                case _:
                    self.display_error("HTTP error happened/n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: /nCheck your internet connction")  
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error: /nThe request timed out")  
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects: /nCheck your url")  
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: /n{req_error}") 


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]


        self.temperature_label.setText(f"{temperature_c:.0f}°")
        self.emoji_label.setText(self.get_weather_emjoi())
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        
        if  200 <= weather_id <= 232:
            return ""
        elif 300 <= weather_id <= 321:
            return ""
        elif 500 <= weather_id <= 531:
            return ""
        elif 600 <= weather_id <= 622:
            return ""
        elif 701 <= weather_id <= 741:
            return ""
        elif weather_id == 762:
            return ""
        elif weather_id == 771:
            return ""
        elif weather_id == 781:
            return ""
        elif weather_id == 800:
            return ""
        elif 801 <= weather_id <= 804:
            return ""
        else:
            return ""
        #emoji column cant make - hold windows key then semi collon





if __name__ == "__main__":
    app = QApplication(sys.argv) 
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())      

