package com.gildedrose

class GildedRose(var items: List<Item>) {

    fun updateQuality() {
        for (i in items.indices) {
            updateQualityForItem(items[i])
        }
    }

    private fun updateQualityForItem(item: Item) {
        if (item.name != "Aged Brie" && item.name != "Backstage passes to a TAFKAL80ETC concert") {
            if (itemQualityNotTooLow(item)) {
                if (item.name != "Sulfuras, Hand of Ragnaros") {
                    if (item.name == "Conjured Mana Cake") {
                        item.quality = incrementQualityForItem(item, -2)
                    } else {
                        item.quality = incrementQualityForItem(item, -1)
                    }
                }
            }
        } else {
            if (itemQualityNotTooHigh(item)) {
                item.quality = incrementQualityForItem(item, 1)

                if (item.name == "Backstage passes to a TAFKAL80ETC concert") {
                    if (item.sellIn < 11) {
                        if (itemQualityNotTooHigh(item)) {
                            item.quality = incrementQualityForItem(item, 1)
                        }
                    }

                    if (item.sellIn < 6) {
                        if (itemQualityNotTooHigh(item)) {
                            item.quality = incrementQualityForItem(item, 1)
                        }
                    }
                }
            }
        }

        if (item.name != "Sulfuras, Hand of Ragnaros") {
            item.sellIn = item.sellIn - 1
        }

        if (item.sellIn < 0) {
            if (item.name != "Aged Brie") {
                if (item.name != "Backstage passes to a TAFKAL80ETC concert") {
                    if (itemQualityNotTooLow(item)) {
                        if (item.name != "Sulfuras, Hand of Ragnaros") {
                            if (item.name == "Conjured Mana Cake") {
                                item.quality = incrementQualityForItem(item, -2)
                            } else {
                                item.quality = incrementQualityForItem(item, -1)
                            }
                        }
                    }
                } else {
                    item.quality = 0
                }
            } else {
                if (itemQualityNotTooHigh(item)) {
                    item.quality = incrementQualityForItem(item, 1)
                }
            }
        }
    }

    private fun itemQualityNotTooLow(item: Item) = item.quality > 0

    private fun itemQualityNotTooHigh(item: Item) = item.quality < 50

    private fun incrementQualityForItem(item: Item, i: Int): Int = item.quality + i

}

