
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm  import relationship
from app.core.database import Base


class User(Base):
    """
    Modelo User:
    Representa a los usuarios registrados en la plataforma del coworking.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    # Relación con Reservation
    reservations = relationship("Reservation", back_populates="user")


    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"
