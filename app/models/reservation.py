
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Reservation(Base):
    """
    Modelo Reservation:
    Representa una reserva realizada por un usuario osbre una herramienta.
    """
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tool_id = Column(Integer, ForeignKey("tools.id"), nullable=False)

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(String, default="pending") # pending | confirmed | cancelled

    # Relaciones bidireccionales
    user = relationship("User", back_populates="reservations")
    tool = relationship("Tool", back_populates="reservations")


    def __repr__(self):
        return f"<Reservation id={self.id} user={self.user_id} tool={self.tool_id}>"
