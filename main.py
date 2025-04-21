from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

db_link = "sqlite:///test.db"


mesin = create_engine(db_link)

base = declarative_base()

class sintesa(base):
	__tablename__ = "sintesa"

	id = Column(Integer ,primary_key=True)
	Nama = Column(String(25))
	Alamat = Column(String(255))
	Umur = Column(Integer)
	Password = Column(String(255))

base.metadata.create_all(mesin)
