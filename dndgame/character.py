from dndgame.dice import roll


class Character:
    """Represent a character with a name, race, ability scores, and hit points.

    Attributes:
        name: The character's name.
        race: The character's race, such as Human, Elf, or Dwarf.
        hp: The character's current hit points.
        max_hp: The character's maximum hit points.
        stats: Ability names mapped to their integer scores.
        base_hp: Base hit points before adding the Constitution modifier.
        level: The character's level.
        armor_class: The minimum attack roll required to hit the character.
    """
    def __init__(self, name: str, race: str, base_hp: int) -> None:
        """Initialize a character before rolling ability scores.

        Args:
            name: The character's name.
            race: The character's race.
            base_hp: Base hit points before adding the Constitution modifier.
        """
        self.name = name
        self.race = race
        self.stats: dict[str, int] = {}
        self.base_hp = base_hp
        self.hp = 0
        self.max_hp = 0
        self.level = 1
        self.armor_class = 10

    def get_modifier(self, stat: str) -> int:
        """
        Calculate the modifier for an ability score.

        Args:
            stat: An ability name, such as "STR", "DEX", or "CON".

        Returns:
            The ability modifier, calculated as (score - 10) // 2.

        Raises:
            KeyError: If the ability name is not present in stats.
        """
        return (self.stats[stat] - 10) // 2

    def roll_stats(self) -> None:
        """Roll ability scores and initialize hit points.

        Set each ability score to the sum of three six-sided dice.
        Set maximum hit points to base_hp plus the Constitution modifier,
        then set current hit points to that maximum.
        Print the dice rolls and return no value.
        """
        print("Rolling stats...\n")
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self) -> None:
        """Apply racial bonuses to existing ability scores.

        Add 2 to CON for Dwarves, 2 to DEX for Elves,
        or 1 to every ability score for Humans.
        Leave other races unchanged.
        Return no value and do not recalculate hit points.
        """
        if self.race == "Dwarf":
            self.stats["CON"] += 2
        elif self.race == "Elf":
            self.stats["DEX"] += 2
        elif self.race == "Human":
            for stat in self.stats:
                self.stats[stat] += 1
