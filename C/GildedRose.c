#include <stdbool.h>
#include <string.h>
#include "GildedRose.h"
#include <stdio.h>

#define MAX_QUALITY 50
#define MIN_QUALITY  0

Item*
init_item(Item* item, const char *name, int sellIn, int quality)
{
    item->sellIn = sellIn;
    item->quality = quality;
    item->name = strdup(name);
    
    return item;
}

extern char* 
print_item(char* buffer, Item* item) 
{
    sprintf(buffer, "%s, %d, %d", item->name, item->sellIn, item->quality);
}

bool is_brie(Item item)
{
    return (0 == strcmp(item.name, "Aged Brie"));
}

bool is_passes(Item item)
{
    return (0 == strcmp(item.name, "Backstage passes to a TAFKAL80ETC concert"));
}

bool is_sulfuras(Item item)
{
    return (0 == strcmp(item.name, "Sulfuras, Hand of Ragnaros"));
}

void increment_quality(Item *item)
{
    if (item->quality < MAX_QUALITY)
        ++item->quality;
}

void
update_quality(Item items[], int size) 
{
    int i;
    
    for (i = 0; i < size; i++)
    {
        if (!is_brie(items[i]) && !is_passes(items[i]))
        {
            if (items[i].quality > MIN_QUALITY && !is_sulfuras(items[i]))
            {
                --items[i].quality;
            }
        }
        else
        {
            increment_quality(&items[i]);

            if (is_passes(items[i]))
            {
                if (items[i].sellIn < 11)
                    increment_quality(&items[i]);

                if (items[i].sellIn < 6)
                    increment_quality(&items[i]);
            }
        }

        if (!is_sulfuras(items[i]))
        {
            --items[i].sellIn;
        }

        if (items[i].sellIn < 0)
        {
            if (!is_brie(items[i]))
            {
                if (!is_passes(items[i]))
                {
                    if (items[i].quality > MIN_QUALITY && !is_sulfuras(items[i]))
                    {
                        --items[i].quality;
                    }
                }
                else
                {
                    items[i].quality = 0;
                }
            }
            else
            {
                increment_quality(&items[i]);
            }
        }
    }
}
