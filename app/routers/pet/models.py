from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, DateTime, Integer, String

from app.utilities.mdb import Base


class PetUsers(Base):
    __tablename__ = "pet_users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(30))
    wechat: Mapped[str] = mapped_column(String(30))
    pic: Mapped[str] = mapped_column(String(30))
    sex: Mapped[int] = mapped_column(Integer)
    reg_time: Mapped[DateTime] = mapped_column(DateTime)
    actived: Mapped[bool] = mapped_column(Boolean)
    