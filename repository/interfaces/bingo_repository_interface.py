from abc import ABC, abstractmethod

class BingoRepositoryInterface(ABC):
    @abstractmethod
    def insert_card(self, card):
        raise NotImplementedError

    @abstractmethod
    def get_all_cards(self):
        raise NotImplementedError

    @abstractmethod
    def insert_drawn_number(self, number):
        raise NotImplementedError

    @abstractmethod
    def get_drawn_numbers(self):
        raise NotImplementedError