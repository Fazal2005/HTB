import smtplib

hostname = "127.0.0.1"
sender_email = "kyle@writer.htb"
port = 25
reciever_email = "john@writer.htb"
message = "Nedd shell"

try:
    server = smtplib.SMTP(hostname, port)
    server.ehlo()
    server.sendmail(sender_email, reciever_email, message)
except exception as e:
    print(e)
finally:
    server.quit()
~                                                                                                                     
~                                                                                                                     
~                         
