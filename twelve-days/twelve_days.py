def recite(start_verse, end_verse):
    ordinals = ['',
                'first',
                'second',
                'third',
                'fourth',
                'fifth',
                'sixth',
                'seventh',
                'eighth',
                'ninth',
                'tenth',
                'eleventh',
                'twelfth'
                ]
    gifts = ['',
             'a Partridge in a Pear Tree',
             'two Turtle Doves',
             'three French Hens',
             'four Calling Birds',
             'five Gold Rings',
             'six Geese-a-Laying',
             'seven Swans-a-Swimming',
             'eight Maids-a-Milking',
             'nine Ladies Dancing',
             'ten Lords-a-Leaping',
             'eleven Pipers Piping',
             'twelve Drummers Drumming'
             ]

    result = []
    base = 'On the %s day of Christmas my true love gave to me: ' % ordinals[start_verse]
    gift_list = ''
    for i in range(end_verse, 0, -1):
        if i == 1 and end_verse > 1:
            gift_list += 'and ' + gifts[i]
        elif end_verse == 1:
            gift_list += gifts[i]
        else:
            gift_list += gifts[i] + ', '
    result.append(base + gift_list + '.')
    return result