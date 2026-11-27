"""Esta clase modela los datos de un usuario"""
from dataclasses import dataclass, field
from uuid import UUID, uuid4

# Decorador -> Extiende la funcionalidad de mi class o funciones
@dataclass
class task:
    fname: str
    lname: str
    age: int
    email: str
    uuid: UUID = field(default_factory=uuid4)
