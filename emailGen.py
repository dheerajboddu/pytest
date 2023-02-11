# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:40:13 2023

@author: Dheeraj Boddu
"""

import smtplib

e_s = 'dheeraj7121997@gmail.com'
e_p = "zrsgymshilruheic"
e_r = "boddudheerajkumar@gmail.com"

sub = "hello Docker"
bod = "Hi this message is automated from docker"

#em = EmailMessage()

#em['From'] = e_s
#em['To'] = e_r
#em['Subject'] = sub
#em.set_content(bod)


#context = ssl.create_default_context()

f = open("email.txt")
emails = f.readlines()

for each in emails:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
        smpt.login(e_s,e_p)
        smpt.sendmail(e_s,e_r,bod)
