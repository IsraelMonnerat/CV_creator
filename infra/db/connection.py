import os
from abc import ABC, abstractmethod


class DbConnectionHandler(ABC):
    def __init__(self) -> None:
        self.connection = "str de conexão os.environ.get('VAR1')"
    
    @abstractmethod
    async def get_connection(self) -> str:
        raise NotImplementedError("Should implement get_connection()")
    
    @abstractmethod
    async def close_connection(self):
        raise NotImplementedError("Should implement close_connection()")
