# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *
from items import Item, AgedBrieQuality,AgedBrieSellIn,SulfurasQuality,SulfurasSellIn,BackstageQuality,BackstageSellIn,NormalQuality,NormalSellIn, ConjuredQuality, ConjuredSellIn

if __name__ == "__main__":
    print ("OMGHAI!")
    # (Item, ISellInUpdate, IQualityUpdate)
    items = [
             (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), NormalSellIn, NormalQuality),
             (Item(name="Aged Brie", sell_in=2, quality=0), AgedBrieSellIn, AgedBrieQuality),
             (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), NormalSellIn, NormalQuality,),
             (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), SulfurasSellIn, SulfurasQuality),
             (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), SulfurasSellIn, SulfurasQuality),
             (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), BackstageSellIn, BackstageQuality),
             (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), BackstageSellIn, BackstageQuality),
             (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), BackstageSellIn, BackstageQuality),
             (Item(name="Conjured Mana Cake", sell_in=3, quality=6), ConjuredSellIn, ConjuredQuality),  # <-- :O
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item, _, _ in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
