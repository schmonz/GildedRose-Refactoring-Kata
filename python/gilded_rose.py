# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            MalleableItem.factory(item).update()


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

    @staticmethod
    def factory(item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
        elif item.name == "Aged Brie":
            return AgedBrie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(item)
        elif item.name == "Conjured Mana Cake":
            return Conjured(item)
        else:
            return MalleableItem(item)

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1

    def update(self):
        self.before_updating_sell_in()

        self.decrease_sell_in()

        if self.item.sell_in < 0:
            self.when_sell_date_has_passed()

    def before_updating_sell_in(self):
        self.decrease_quality()

    def when_sell_date_has_passed(self):
        self.before_updating_sell_in()


class Sulfuras(MalleableItem):
    def decrease_quality(self):
        pass

    def decrease_sell_in(self):
        pass


class AgedBrie(MalleableItem):
    def before_updating_sell_in(self):
        self.increase_quality()


class BackstagePasses(MalleableItem):
    def before_updating_sell_in(self):
        self.increase_quality()
        if self.item.sell_in <= 10:
            self.increase_quality()
        if self.item.sell_in <= 5:
            self.increase_quality()

    def when_sell_date_has_passed(self):
        self.item.quality = 0


class Conjured(MalleableItem, object):
    def before_updating_sell_in(self):
        super(Conjured, self).decrease_quality()
        super(Conjured, self).decrease_quality()
