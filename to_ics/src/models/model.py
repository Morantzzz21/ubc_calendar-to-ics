from dataclasses import dataclass
import datetime
from typing import Optional

@dataclass
class event:
    title: str                          # Course name
    start: datetime
    end: datetime
    location: Optional[str] = None      
    description: Optional[str] = None   # Could include instructor/specific name
