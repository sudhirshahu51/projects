import sys

sys.path.append('/usr/local/lib/python3.4/dist-packages')

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


# insert at the end of file
# all the classes that is tables will be formed in between here

engine = create_engine('sqlite:///<name of database>')
Base.metadata.create_all(engine)
