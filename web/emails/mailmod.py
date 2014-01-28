import imaplib
import socket

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login('opensource.mer@gmail.com', '')
mail.list()

mail.select("inbox")

result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")

raw_email = data[0][1]