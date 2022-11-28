import unittest
from items import Item, AgedBrieSellIn, AgedBrieQuality, ItemUpdate, BackstageSellIn, BackstageQuality

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

    def test_backstage_sellin(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=20, quality=10)
        backstage = BackstageSellIn(item=item)
        response: Item = backstage.apply() 

        self.assertEqual(response.sell_in, 19)
        


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
    
    def test_backstage_increase_quality_le_10days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=12)
        backstage = BackstageQuality(item=item)
        response: Item = backstage.apply()

        self.assertEqual(response.quality, 14)
        
    def test_backstage_increase_quality_le_5days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=12)
        backstage = BackstageQuality(item=item)
        response: Item = backstage.apply()

        self.assertEqual(response.quality, 15)
        
    def test_backstage_increase_quality_gt_10days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=12)
        backstage = BackstageQuality(item=item)
        response: Item = backstage.apply()

        self.assertEqual(response.quality, 13)
        
    
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

        self.assertEqual(item.quality, 21)
        self.assertEqual(item.sell_in, 9)

    def test_backstage(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
        sell_in_handler = BackstageSellIn(item=item)
        quality_handler = BackstageQuality(item=item)
        aged_brie_profile = ItemUpdate(
            sell_in_handler=sell_in_handler,
            quality_handler=quality_handler,
        )

        # Quality updates before sell_in
        aged_brie_profile.update_quality()
        aged_brie_profile.update_sell_in()

        self.assertEqual(item.quality, 22)
        self.assertEqual(item.sell_in, 9)

    