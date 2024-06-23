# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
class VictoryCondition(Choice):
    """
    The goal that must be achieved in order to mark your world as completed.
    Pantheon 5 requires all 4 Pantheon Fragments and clearing the Pantheon of Hallownest.
    Boss Rush requires defeating a specified amount of bosses in the Hall of Gods.
    """
    display_name = "Goal"
    option_pantheon_5 = 0
    option_boss_rush = 1
    default = 0


class NumOfBosses(Range):
    """
    The number of bosses to be defeated for the 'Boss Rush' Goal.
    Ignored if goal is set to anything other than 'Boss Rush.'
    """
    display_name = "Number of Bosses"
    range_start = 11
    range_end = 44
    default = 33


class includeP5(Toggle):
    """
    Whether to exclude locations related to the Pantheon of Hallownest.
    Ignored if goal is Pantheon 5.
    """
    display_name = "exclude_p5"


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["victory_condition"] = VictoryCondition
    options["number_of_bosses"] = NumOfBosses
    options["exclude_p5"] = includeP5
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options