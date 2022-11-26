# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.normal_items = [ 
            Item("Apple", 10, 10),
            Item("Bread", 5, 12),
        ]

        self.quality_increasing_items = [ 
            Item("Aged Brie", 10, 15),
            Item("Backstage passes to a TAFKAL80ETC concert", 8, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 3, 15),
            Item("Aged Brie", 7, 11),
        ]

        self.quality_stagnent_items = [ 
            Item("Sulfuras, Hand of Ragnaros", 10, 80)

        ]

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_quality_decreases(self):
        gilded_rose = GildedRose(
            items=self.normal_items,
        )    
        gilded_rose.update_quality()
        
        self.assertEqual(self.normal_items[0].quality, 9)
        self.assertEqual(self.normal_items[1].quality, 11)

    def test_sellin_decreases(self):
        gilded_rose = GildedRose(
            items=self.normal_items,
        )    
        gilded_rose.update_quality()
        
        self.assertEqual(self.normal_items[0].sell_in, 9)
        self.assertEqual(self.normal_items[1].sell_in, 4)

    def test_quality_increase(self):
        gilded_rose = GildedRose(
            items=self.quality_increasing_items,
        )

        gilded_rose.update_quality()

        self.assertEqual(self.quality_increasing_items[0].quality, 16)
        self.assertEqual(self.quality_increasing_items[1].quality, 22)
        self.assertEqual(self.quality_increasing_items[2].quality, 18)
        self.assertEqual(self.quality_increasing_items[3].quality, 12) # Brie increases linearly irrespective of sellin

    def test_quality_stagnent(self):
        gilded_rose = GildedRose(
            items=self.quality_stagnent_items,
        )

        gilded_rose.update_quality()

        self.assertEqual(self.quality_stagnent_items[0].quality, 80)

    def test_sellin_stagnent(self):
        gilded_rose = GildedRose(
            items=self.quality_stagnent_items,
        )

        gilded_rose.update_quality()

        self.assertEqual(self.quality_stagnent_items[0].sell_in, 10)


    def test_quality_lower_bound(self):
        items = [Item("Banana", 10, 0)] 
        gilded_rose = GildedRose(
            items=items,
        )

        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 0)
        

    def test_quality_upper_bound(self):
        items = [
                Item("Sulfuras, Hand of Ragnaros", 10, 80), 
                Item("Backstage passes to a TAFKAL80ETC concert", 8, 50), 
                Item("Aged Brie", 8, 50), 
        ] # Items that only increase it quality each day 

        gilded_rose = GildedRose(
            items=items,
        )

        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[1].quality, 50)
        self.assertEqual(items[2].quality, 50)

    @unittest.skip(reason="Not implemented yet")
    def test_conjured_items(self):
        items = [ 
            Item("Conjured", 12, 10),
        ]

        gilded_rose = GildedRose(items=items)

        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 8)


        
if __name__ == '__main__':
    unittest.main()
