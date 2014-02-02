from web import db
from web.database.entities import User

db.create_all()
admin = User()
admin.email = 'opensource.mer@gmail.com'
admin.openid = 'https://www.google.com/accounts/o8/id?id=AItOawkURSdc4bgUdnirxse_VYXAvfk9KioBMPg'
db.session.add(admin)
db.session.commit()