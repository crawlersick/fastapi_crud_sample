from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from ..dataconfig import Base, engine


class sampledbobj(Base):
    __tablename__ = "sampledbobj"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(bind=engine)

