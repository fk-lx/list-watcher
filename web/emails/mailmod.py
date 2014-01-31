import imaplib
import datetime
import email
from operator import attrgetter


def fetch_emails(valid_from=None, valid_to=None, host='imap.gmail.com', port=993, login='opensource.mer@gmail.com',
                 password='hehe', folder='mer'): #TODO: Keep it in the config file
    if valid_from is None and valid_to is None:
        return []
    client = imaplib.IMAP4_SSL(host, port)
    client.login(login, password)
    client.select(folder)

    condition = '('
    since_condition = ''
    before_condition = ''
    if valid_from is not None:
        valid_from_rfc822 = valid_from.strftime("%d-%b-%Y")
        since_condition = str('SINCE "%s"' % valid_from_rfc822)
        condition += since_condition
    if valid_to is not None: #TODO
        valid_to_rfc822 = valid_to.strftime("%d-%b-%Y")
        before_condition = str('BEFORE "%s"' % valid_to_rfc822)
        condition += before_condition

    condition += ')'
    result, data = client.search(None, condition)
    ids = data[0]
    id_list = ids.split()
    emails = []
    for id in id_list:
        result, data = client.fetch(id, "(RFC822)")
        emails.append(data)
    return emails

def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()



def xstr(s):
    return '' if s is None else str(s)


def parse_emails(emails):
    dt = []
    for mail in emails:
        raw_email = email.message_from_string(mail[0][1])
        data = {'InReplyTo': raw_email['In-Reply-To'],
                'Body': get_first_text_block(raw_email),
                'Subject': raw_email['Subject'],
                'MessageId': raw_email['Message-ID']}
        dt.append(data)
    dt.sort(key=lambda x: x['InReplyTo'])
    return dt
