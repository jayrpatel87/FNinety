from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import JSON
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)

    match_id: Mapped[int] = mapped_column(
        ForeignKey("matches.id")
    )

    provider: Mapped[str] = mapped_column(
        String(50)
    )

    provider_event_id: Mapped[str] = mapped_column(
        String(100)
    )

    minute: Mapped[int]

    second: Mapped[int]

    event_type: Mapped[str] = mapped_column(
        String(50)
    )

    outcome: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    team_id: Mapped[int | None]

    player_id: Mapped[int | None]

    x: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    y: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    end_x: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    end_y: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    under_pressure: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    raw_event_json: Mapped[dict] = mapped_column(
        JSON
    )