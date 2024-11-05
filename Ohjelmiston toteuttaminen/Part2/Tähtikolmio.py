"""   Tehtävänanto

Kirjoita ohjelma, joka tulostaa kolmion muotoisen kuvion tähdillä, jossa on viisi riviä.

*

**

***

****

*****  """

def draw_christmas_tree(height=5, trunk=0, number=1):
    print("\n")
    for iter in range(height):
        for lkm in range(number):
            # print line
            print(' ' * (height - iter), end='')
            dummy = 1 + (iter * 2)
            print('*' * dummy, end='')
            print(' ' * (height - iter), end='')
        print()

    for iter4 in range(trunk):
        for lkm in range(number):
            print(' ' * height, end='')
            print('*', end='')
            print(' ' * height, end='')
        print()

draw_christmas_tree()
