# type: ignore
class Spell:
    """Store a spell's properties; casting is not yet implemented.

    Attributes:
        name: The spell's name.
        level: The spell's level.
        school: The spell's school of magic.
        spell_power: The spell's power value.
    """
    def __init__(self, name: str, level: int, school: str, spell_power: int):
        """Initialize a spell with its properties.

        Args:
            name: The spell's name.
            level: The spell's level.
            school: The spell's school of magic.
            spell_power: The spell's power value.
        """
        self.name = name
        self.level = level
        self.school = school
        self.spell_power = spell_power

    def cast(self, caster, target):
        """Provide a placeholder for casting; currently has no effect.

        Args:
            caster: The intended spell caster.
            target: The intended spell target.

        Returns:
            None.
        """
        pass


class SpellBook:
    """Manage a collection of spells.

    Attributes:
        spells: The spells stored in this spell book.
    """
    def __init__(self) -> None:
        """Initialize an empty spell book."""
        self.spells: list[Spell] = []

    def add_spell(self, spell: Spell) -> None:
        """Append a spell to this spell book.

        Args:
            spell: The spell to add.

        Returns:
            None.
        """
        self.spells.append(spell)

    def get_available_spells(self, spell_level: int) -> list[Spell]:
        """Return spells at or below the specified level.

        Args:
            spell_level: The maximum spell level to include.

        Returns:
            Matching spells in their original order.
            An empty list if no spells match.

        Examples:
            A spell_level of 2 includes spells of levels 0, 1, and 2.
        """
        available = []
        for spell in self.spells:
            if spell.level <= spell_level:
                available.append(spell)
        return available
