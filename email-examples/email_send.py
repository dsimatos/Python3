#!/usr/bin/env python3

"""Send a simple email."""

import smtplib
fromaddr = 'dsimatos@gmail.com'
toaddrs  = 'dsimatos@gmail.com'
msg = "\r\n".join([
  "From: dsimatos@gmail.com",
  "To: dsimatos@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = 'dsimatos@gmail.com'
password = '!dio@nat#1974'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
