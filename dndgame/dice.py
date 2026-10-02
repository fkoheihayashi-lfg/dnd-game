import random


def roll(dice_type: int, number_of_dice: int) -> int:
    """Roll dice, print the individual results, and return their sum.

    Args:
        dice_type: Number of sides on each die; must be positive.
        number_of_dice: Number of dice to roll.

    Returns:
        The sum of the rolled values, or zero if no dice are rolled.

    Raises:
        ValueError: If dice_type is not positive and a roll is attempted.
    """
    rolls = []
    total = 0
    for _ in range(number_of_dice):
        roll_result = random.randint(1, dice_type)
        rolls.append(roll_result)
        total += roll_result
    print(f"Rolling {number_of_dice}d{dice_type}: {rolls} = {total}")
    return total


def roll_with_advantage(dice_type: int) -> int:
    """Roll twice and return the higher result.

    Args:
        dice_type: Number of sides on the die; must be positive.

    Returns:
        The higher of the two rolls.

    Raises:
        ValueError: If dice_type is not positive.
    """
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return max(roll1, roll2)


def roll_with_disadvantage(dice_type: int) -> int:
    """Roll twice and return the lower result.

    Args:
        dice_type: Number of sides on the die; must be positive.

    Returns:
        The lower of the two rolls.

    Raises:
        ValueError: If dice_type is not positive.
    """
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return min(roll1, roll2)
