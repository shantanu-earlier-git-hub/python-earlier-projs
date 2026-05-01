from sqlalchemy.orm import Mapped, mapped_column

from app.entities import Base


class DbProduct(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(index=True, unique=False)
    price: Mapped[float] = mapped_column(index=True, unique=False)
    isavailable: Mapped[bool] = mapped_column(index=True, unique=False)
