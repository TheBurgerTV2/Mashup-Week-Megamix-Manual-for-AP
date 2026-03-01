# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


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
#
class Starting_Characters(Range):
    """Number of characters to randomly add to the starting inventory.
    Note that these also contribute to the goal character count."""
    range_start = 1
    range_end = 6
    default = 3

class Goal_Characters(Range):
    """Number of characters required to goal.
    You will still need 75 of the 100 goal macguffins"""
    range_start = 0
    range_end = 30
    default = 24

class EnableRickHentai(Toggle):
    """Enables the sex guy, Rick Hentai.
    Disable if your group has issues with sexual themes."""
    default = False

class EnableLilDarkie(Toggle):
    """Enables the cowboy, Lil' Darkie.
    Disable if your group has issues with slurs."""
    default = False

class LocalFill(Range):
    """Sets an amount of filler to be local.
    Use if your friends hate sending loads of especially useless filler.
    Approximately 69 filler items are exempt from this setting."""
    range_start = 0
    range_end = 100
    default = 25

class Sourcesanity(Toggle):
    """Adds characters sources into the pool, adding about 180 progression items
    do note that this can result in very restrictive seeds."""
    default = False

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["starting_characters"] = Starting_Characters
    options["goal_characters"] = Goal_Characters
    options["enable_rick_hentai"] = EnableRickHentai
    options["enable_lil_darkie"] = EnableLilDarkie
    options["local_fill"] = LocalFill
    options["Sourcesanity"] = Sourcesanity
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
