from re import M
from xmlrpc import client

url = 'http://localhost:8069'
db = 'library'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
#print(common.version())

uid = common.authenticate(db, username, password, {})
#print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'library.rental','check_access_rights',
                                ['write'],{'raise_exception':False})
#print(model_access)


rental = models.execute_kw(db, uid, password,
                                'library.rental','search',
                                [[['duration','>',60]]])

print(rental)

updating_rental = models.execute_kw(db, uid, password,
                                'library.rental','write',
                                [rental,{'name':"UpdatedBook"}])

print(updating_rental)