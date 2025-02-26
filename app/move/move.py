import dataclasses
import enum

from app.db.damage_chart import Type


class MoveCategory(enum.Enum):
    PHYSICAL = "Physical"
    SPECIAL = "Special"
    OTHER = "Other"


class MoveRange(enum.Enum):
    ADJACENT_POKEMON = "Adjacent Pokemon"
    ALL_ENEMIES_IN_THE_ROOM = "All enemies in the room"
    ALL_ENEMIES_ON_THE_FLOOR = "All enemies on the floor"
    ALL_IN_THE_ROOM_EXCEPT_USER = "All in the room except user"
    ALL_POKEMON_IN_THE_ROOM = "All Pokemon in the room"
    ALL_POKEMON_ON_THE_FLOOR = "All Pokemon on the floor"
    ALL_TEAM_MEMBERS_IN_THE_ROOM = "All team members in the room"
    ENEMIES_WITHIN_1_TILE_RANGE = "Enemies within 1-tile range"
    ENEMY_IN_FRONT = "Enemy in front"
    ENEMY_IN_FRONT_CUTS_CORNERS = "Enemy in front, cuts corners"
    ENEMY_UP_TO_2_TILES_AWAY = "Enemy up to 2 tiles away"
    FACING_POKEMON = "Facing Pokemon"
    FACING_POKEMON_CUTS_CORNERS = "Facing Pokemon, cuts corners"
    FACING_TILE_AND_2_FLANKING_TILES = "Facing tile and 2 flanking tiles"
    FLOOR = "Floor"
    ITEM = "Item"
    LINE_OF_SIGHT = "Line of sight"
    ONLY_THE_ALLIES_IN_THE_ROOM = "Only the allies in the room"
    POKEMON_WITHIN_1_TILE_RANGE = "Pokemon within 1-tile range"
    POKEMON_WITHIN_2_TILE_RANGE = "Pokemon within 2-tile range"
    SPECIAL = "Special"
    TEAM_MEMBERS_ON_THE_FLOOR = "Team members on the floor"
    USER = "User"
    WALL = "Wall"


@dataclasses.dataclass(frozen=True)
class Move:
    move_id: int
    name: str
    description: str
    type: Type
    category: MoveCategory
    pp: int
    accuracy: int
    critical: int
    power: int
    animation: int
    chained_hits: int
    move_range: MoveRange
    weight: int
    activation_condition: str
    ginseng: bool
    magic_coat: bool
    snatch: bool
    muzzled: bool
    taunt: bool
    frozen: bool
