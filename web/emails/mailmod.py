import imaplib
import datetime
import email


def fetch_emails(valid_from=None, valid_to=None, host='imap.gmail.com', port=993, login='opensource.mer@gmail.com',
                 password='asdasd1234', folder='mer'): #TODO: Keep it in the config file
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

    condition += ')'
    result, data = client.search(None, condition)
    ids = data[0]
    id_list = ids.split()
    emails = []
    for id in id_list:
        result, data = client.fetch(id, "(RFC822)")
        emails.append(data)
    return emails


def parse_emails(emails):
    for mail in emails:
        raw_email = email.message_from_string(mail[0][1])
        reply_to = raw_email['In-Reply-To']
        if reply_to is None:
            pass # main thread
        else:
            pass # answers

a = datetime.date(2013,12,31)
mails = fetch_emails(a)
parse_emails(mails)


