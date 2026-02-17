from abc import ABC, abstractmethod

class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        return {"message": f"Channeling {amount} mana."}

    def get_magic_stats(self) -> dict:
        return {"type": self.__class__.__name__}
