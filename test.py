import sys
sys.path.append("Ducoments/CS631/proj/gui")
import database

db = database.Sign()



db.login('100000003', '123')

user = database.User(db)

user.viewbystatus(1)



