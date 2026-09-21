from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Victory Rule
def victory_rule(world: World):
    """Calculates Victory"""
    comp = world.options.goal_characters.value

    logic = f"|@Character:{comp}|"

    return logic

def sourcesanity_always_true():
    return True
