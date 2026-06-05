from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)

    competition_id: Mapped[int] = mapped_column(
        ForeignKey("competitions.id")
    )

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id")
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id")
    )

    provider_match_id: Mapped[int]

    match_date: Mapped[datetime]