#!/usr/bin/python3
#coding:utf8

import os, re, smtplib
from email.utils import COMMASPACE
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
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
        # support attachment
        msg = MIMEMultipart()
        if filespath is not None:
            for singlefile in filespath:
                singlefile = singlefile.replace('~', os.environ['HOME'])
                filename = os.path.basename(singlefile)
                att = MIMEBase('application', 'octet-stream')
                att.set_payload(open(singlefile, 'rb').read())
                encoders.encode_base64(att)
                att.add_header('Content-Disposition', 'attachment;filename="%s"' % filename)
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
        smtp.login(sender, password)
        smtp.sendmail(sender, tolist, msg.as_string())
        smtp.close()
        return True
    except Exception as err:
        print(err)
        return False

def main():
    content = 'Hi, Young!'
    subject = 'A multimedia file'
    filespath = ['~/Media/raspberrypi_200x200.jpg']
    if sendMail(content, subject, filespath):
        print("send mail successfully.")
    else:
        print("send mail failed.")

if __name__ == "__main__":
    main()
