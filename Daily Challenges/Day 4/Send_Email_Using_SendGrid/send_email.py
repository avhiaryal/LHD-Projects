import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

message = Mail(
    from_email='jitade4056@vu38.com',
    to_emails='utsavpanday2056@gmail.com',
    subject='Testing SendGid API',
    html_content='<strong>This is a MLH Local Hack Day 4 Challenge of Using SendGrid API</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
except Exception as e:
    print(e.message)
    