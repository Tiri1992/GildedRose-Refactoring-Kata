from items import Item, ISellInUpdate, IQualityUpdate, ItemUpdate

class GildedRose(object):

    def __init__(self, items: tuple[Item, ISellInUpdate, IQualityUpdate]) -> None:
        self.items = items

    def update_quality(self):
        
        for item, sell_in_cls, quality_cls in self.items:
            item_update = ItemUpdate(
                sell_in_handler=sell_in_cls(item),
                quality_handler=quality_cls(item),
            )

            item_update.update_quality()
            item_update.update_sell_in()

