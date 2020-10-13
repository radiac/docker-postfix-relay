#!/usr/bin/env python
import datetime
import os
import smtplib

mail_host = os.environ["MAIL_HOST"]
mail_from = os.environ["MAIL_FROM"]
mail_to = os.environ["MAIL_TO"]

message = f"""From: {mail_from}
To: {mail_to}
Subject: Sample email {datetime.datetime.now()}

This is an email sent by the sample container
"""

try:
    smtpObj = smtplib.SMTP(mail_host)
    smtpObj.sendmail(mail_from, mail_to, message)
    print("Email sent")
except Exception as e:
    print(f"Email failed: {e}")
