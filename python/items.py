from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Implementations
class ISellInUpdate(ABC):

    @abstractmethod
    def apply(self):
        pass


class IQualityUpdate(ABC):

    @abstractmethod
    def apply(self):
        pass 


class AgedBrieSellIn(ISellInUpdate):

    def __init__(self, item: Item) -> None:
        self._item = item 

    def has_expired(self) -> bool:
        return self._item.sell_in <= 0

    def apply(self) -> Item:
        if not self.has_expired():
            self._item.sell_in -= 1
        return self._item
    
class AgedBrieQuality(IQualityUpdate):

    def __init__(self, item: Item) -> None:
        self._item = item 

    def has_max_quality(self) -> bool:
        return self._item.quality >= 50

    def apply(self):
        if not self.has_max_quality():
            self._item.quality += 1
        return self._item

# Abstractions
class AbstractItemProfile(ABC):

    @abstractmethod
    def update_sell_in(self):
        pass 

    @abstractmethod
    def update_quality(self):
        pass


class ItemProfile(AbstractItemProfile):

    def __init__(self, sell_in_handler: ISellInUpdate, quality_handler: IQualityUpdate) -> None:
        self._sell_in_handler = sell_in_handler
        self._quality_handler = quality_handler

    def update_sell_in(self) -> Item:
        return self._sell_in_handler.apply()
    
    def update_quality(self) -> Item:
        return self._quality_handler.apply()