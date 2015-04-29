#!/usr/bin/python
#coding:utf8

import os, re, smtplib
from email.utils import COMMASPACE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mailInfo import sender, password, def_subject, tolist, cclist, def_filespath

def sendMail(content, subject = def_subject, filespath = def_filespath):
    assert type(sender) == str
    assert type(tolist) == list
    assert type(cclist) == list
    assert type(subject) == str
    assert type(content) == str
    assert type(filespath) == list or filespath is None
    try:
        # get server name from email sender
        r_server = re.compile(r'.*@(.*)\.com')
        server_name = re.findall(r_server, sender)
        smtpserver = 'smtp.' + server_name[0] + '.com'
        smtpport = '25'
        username = sender
        # support attachment
        msg = MIMEMultipart()
        if filespath is not None:
            for singlefile in filespath:
                singlefile = singlefile.replace('~', os.environ['HOME'])
                filename = os.path.basename(singlefile)
                # convert bytes to str
                ctnt_bytes = open(singlefile, 'rb').read()
                ctnt_str = ctnt_bytes.decode('utf-8', 'strict')
                att = MIMEText(ctnt_str, 'base64')
                att['content-type'] = 'application/octet-stream'
                att['content-disposition'] = 'attachment;filename="%s"' % filename
                msg.attach(att)
        # mail body
        body = MIMEText(content)
        msg.attach(body)
        msg['from'] = sender
        msg['to'] = COMMASPACE.join(tolist)
        msg['cc'] = COMMASPACE.join(cclist)
        msg['subject'] = subject
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, smtpport)
        smtp.login(username, password)
        smtp.sendmail(sender, tolist, msg.as_string())
        smtp.close()
        return True
    except Exception as err:
        print(err)
        return False

def main():
    content = 'Hi, Young!'
    subject = 'A piece of Music'
    filespath = ['~/Media/raspberrypi_200x200.jpg']
    if sendMail(content, subject, filespath):
        print("send mail successfully.")
    else:
        print("send mail failed.")

if __name__ == "__main__":
    main()
