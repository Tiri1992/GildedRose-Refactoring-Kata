import unittest
from items import Item, AgedBrieSellIn, AgedBrieQuality, ItemUpdate

# Break up test cases by implementation interfaces
class TestSellInUpdate(unittest.TestCase):
    
    def test_aged_brie(self):
        item = Item(name="Aged Brie", sell_in=10, quality=20)
        aged_brie = AgedBrieSellIn(item=item)
        response: Item = aged_brie.apply()

        self.assertEqual(response.sell_in, 9)

    def test_aged_brie_sellin_lower_bound(self):
        item = Item(name="Aged Brie", sell_in=0, quality=20)
        aged_brie = AgedBrieSellIn(item=item)
        response: Item = aged_brie.apply()

        self.assertEqual(response.sell_in, 0)
        self.assertEqual(aged_brie.has_expired(), True)


class TestQualityUpdate(unittest.TestCase):

    def test_aged_brie_increase_quality(self):
        item = Item(name="Aged Brie", sell_in=10, quality=20)
        aged_brie = AgedBrieQuality(item=item)
        response: Item = aged_brie.apply()
        self.assertEqual(response.quality, 21) 

    def test_aged_brie_quality_upper_bound(self):
        item = Item(name="Aged Brie", sell_in=10, quality=50)
        aged_brie = AgedBrieQuality(item=item)
        response: Item = aged_brie.apply()
        self.assertEqual(response.quality, 50) 
    
    
class TestItemUpdate(unittest.TestCase):

    def test_aged_brie(self):
        item = Item(name="Aged Brie", sell_in=10, quality=20)
        sell_in_handler = AgedBrieSellIn(item=item)
        quality_handler = AgedBrieQuality(item=item)
        aged_brie_profile = ItemUpdate(
            sell_in_handler=sell_in_handler,
            quality_handler=quality_handler,
        )

        aged_brie_profile.update_quality()
        aged_brie_profile.update_sell_in()

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 21)