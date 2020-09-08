from Die_class import *

#class instance
d = die()

#contructed die
print('\nCONSTRUCTED DIE')
die_sides  = ['list','of','die','face','values']
rolled_val = d.roll_n_die(die_sides)
print(rolled_val)

#preset die
print('\nPRESET DIE')
d.roll_skate_preset()
d.roll_double_6_sided_preset()
d.roll_cocktail_preset()
d.flip_coin_preset()
d.roll_roll_a_dice()