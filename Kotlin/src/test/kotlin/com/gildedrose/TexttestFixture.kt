package com.gildedrose

fun main(args: Array<String>) {

    val items = listOf(Item("+5 Dexterity Vest", 10, 20), //
            Item("Aged Brie", 2, 0), //
            Item("Elixir of the Mongoose", 5, 7), //
            Item("Sulfuras, Hand of Ragnaros", 0, 80), //
            Item("Sulfuras, Hand of Ragnaros", -1, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            // this conjured item does not work properly yet
            Item("Conjured Mana Cake", 3, 6))

    val app = GildedRose(items)

    var days = 500
    if (args.size > 0) {
        days = Integer.parseInt(args[0]) + 1
    }

    for (i in 0..days - 1) {
        println("-------- day $i --------")
        println("name, sellIn, quality")
        for (item in items) {
            println(item)
        }
        println()
        app.updateQuality()
    }

    /*
    business rules not to mess up:
    normal items go down 1 in sellIn and quality
    quality might be not be allowed to increase (for all items?) beyond 50
    Brie gets one better with age, then 2 better after sellIn
    what happens to quality for normal items after sellIn? go to 0, decrease twice as fast, ???
    backstage passes increase quality by 1 more than 10 days out; less, increase by 2. less than 5, maybe more?
    backstage passes quality goes to 0 after the date

    new rule to add:
    whatever happens to normal quality, happens twice as fast for "Conjured"
     */
}
