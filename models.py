from sqlalchemy import TIMESTAMP, Integer,String,Column
from sqlalchemy.sql.expression import null,text
from database import Base


class MustBeActive(Base):
    __tablename__ = "MustBeActiveUsers"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False , server_default=text("now()"))


class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False , server_default=text("now()"))