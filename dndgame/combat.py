from dndgame.dice import roll
from dndgame.character import Character

class Combat:
    """Handle initiative and attacks between a player and an enemy.

    Attributes:
        player: The player's character.
        enemy: The opposing character.
        round: Round counter initialized to zero; currently not updated.
        initiative_order: Characters arranged in their acting order.
    """
    def __init__(self, player: Character, enemy: Character) -> None:
        """Initialize combat with a player and an enemy.

        Args:
            player: The player's character.
            enemy: The opposing character.
        """
        self.player = player
        self.enemy = enemy
        self.round = 0
        self.initiative_order: list[Character] = []

    def roll_initiative(self) -> list[Character]:
        """Determine and store the acting order.

        Roll a twenty-sided die for each character and add its DEX modifier.
        The higher total acts first; the player acts first on a tie.

        Returns:
            The player and enemy arranged in their acting order.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker: Character, defender: Character) -> int:
        """Attack a character and reduce its hit points on a hit.

        Args:
            attacker: The character making the attack.
            defender: The character receiving the attack.

        Returns:
            Damage from one six-sided die on a hit, or zero on a miss.

        The attack hits when a twenty-sided die plus the attacker's STR
        modifier is at least the defender's armor_class.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")
        weapon_max_damage = 6
        if attack_roll >= defender.armor_class:
            damage = roll(weapon_max_damage, 1)
            defender.hp -= damage
            return damage
        return 0
