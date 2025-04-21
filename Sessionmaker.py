from sqlalchemy.orm import sessionmaker
from main import sintesa, mesin

session = sessionmaker(bind=mesin)

session = session()

new_data = sintesa(Nama="", Alamat="", Umur=, Password="")

session.add(new_data)

session.commit()

print("Data inserted successfully")
