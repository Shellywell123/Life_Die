import random

class die():
    """
    class for rolling dice to give various instructions
    """

    def __init__(self):
        """
        empty
        """
        pass

    def roll_n_die(self,dice_outcomes):
        """
        returns random element of a list
        """

        choice_index = random.randint(0,len(dice_outcomes)-1)
        choice = dice_outcomes[choice_index]
        return choice

    #######################################
    # preset die
    #######################################

    def roll_double_6_sided_preset(self):
        """
        returns inpedent 6 sided pair of dice outcome
        """
        sides = [1,2,3,4,5,6]

        dice1 = self.roll_n_die(sides)
        dice2 = self.roll_n_die(sides)

        output = '{} + {} = {}'.format(dice1,dice2,dice1+dice2)

        print(output)
        return(output)

    def roll_skate_preset(self):
        """
        returns random skateboard trick
        """
        stances     = ['Regular','Switch','Fakie','Nollie']
        rotations   = ['FS 180','BS 180','FS 360','BS 360']
        basic_flips = ['Kickflip','Heelflip']

        stance     = self.roll_n_die(stances)
        rotation   = self.roll_n_die(rotations)
        basic_flip = self.roll_n_die(basic_flips)

        output = '{} {} {}'.format(stance,rotation,basic_flip)

        print(output)
        return output

    def roll_cocktail_preset(self):
        """
        returns a random cocktail recipe
        """

        spirits        = ['vodka','gin','rum','whisky']
        garnishes      = ['lemon slice','lime slice','cucumber','water melon']
        methods        = ['shaken','stirred']
        spirit_volumes = ['25 ml','50 ml']

        spirit         = self.roll_n_die(spirits)
        mixers         = ['orange juice','apple juice','lemonade','cocacola','more '+spirit,'water']
        mixer_volumes  = ['100 ml','200 ml']
        glasses        = ['flute glass','mug','pint glass','yard glass','beer bong','coconut']

        
        spirit_volume  = self.roll_n_die(spirit_volumes) 
        mixer          = self.roll_n_die(mixers)
        mixer_volume   = self.roll_n_die(mixer_volumes)
        method         = self.roll_n_die(methods)
        glass          = self.roll_n_die(glasses)
        garnish        = self.roll_n_die(garnishes) 

        output = 'your drink is ...\n{} {} with {} {}, {} and served in a {} with {}'.format(spirit_volume,spirit,mixer_volume,mixer,method,glass,garnish)

        print(output)
        return output

    def flip_coin_preset(self):
        """
        returns heads of tails
        """
        sides   = ['heads','tails']
        outcome = self.roll_n_die(sides)

        print(outcome)
        return outcome

    def roll_roll_a_dice(self):
        """
        decide wether to go and find a real dice
        """
        options = ['stop being a lazy piece of shit and go get a real dice','carry on being a lazy piece of shit and using virual dice']
        choice  = self.roll_n_die(options)

        print(choice)
        return choice

