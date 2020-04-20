# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                Sulfuras(item).update()
            else:
                MalleableItem(item).update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class MalleableItem:
    def __init__(self, item):
        self.item = item

    def decrease_sell_in(self):
        item = self.item

        item.sell_in = item.sell_in - 1

    def decrease_quality(self):
        item = self.item

        if item.quality > 0:
            item.quality = item.quality - 1

    def increase_quality(self):
        item = self.item

        if item.quality < 50:
            item.quality = item.quality + 1

    def increase_backstage_quality_further(self):
        item = self.item

        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                self.increase_quality()
            if item.sell_in < 6:
                self.increase_quality()

    def update(self):
        item = self.item

        if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.increase_quality()
            self.increase_backstage_quality_further()
        else:
            self.decrease_quality()

        self.decrease_sell_in()

        if item.sell_in < 0:
            if item.name == "Aged Brie":
                self.increase_quality()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = 0
            else:
                self.decrease_quality()


class Sulfuras(MalleableItem):
    def decrease_quality(self):
        pass

    def decrease_sell_in(self):
        pass
