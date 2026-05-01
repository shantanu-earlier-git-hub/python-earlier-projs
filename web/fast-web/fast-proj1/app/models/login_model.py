from dataclasses import dataclass
from app.models import Audit


@dataclass
class Login(Audit):
    username: str
    password: str
