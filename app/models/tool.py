
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base


class Tool(Base):
    """
    Modelo Tool:
    Representa cada herramienta disponible en el coworking.
    """
    __tablename__ = "tools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="available") # available | maintenance | broken
    requires_training = Column(Boolean, default=False)

    reservations = relationship("Reservation", back_populates="tool")


    def __repr__(self):
        return f"<Tool id={self.id} name={self.name} status={self.status}>"
