import math
from decimal import Decimal

from services.services_widget.services import round_the_number


def calculate_mass_corner_equal(side: Decimal,
                                thickness: Decimal,
                                length: Decimal,
                                rounding: str) -> Decimal:
    """Расчет массы уголка равнополочного"""
    calculation_weight = \
        (side / 1000 * 2 - thickness / 1000) * thickness / 1000 * length * Decimal(7850)
    return round_the_number(calculation_weight, rounding)


def calculate_mass_corner_different(side: Decimal,
                                    side_b: Decimal,
                                    thickness: Decimal,
                                    length: Decimal,
                                    rounding: str) -> Decimal:
    """Расчет массы уголка с разными полками"""
    calculation_weight = \
        (side / 1000 + side_b / 1000 - thickness / 1000) * thickness / 1000 * length * Decimal(7850)
    return round_the_number(calculation_weight, rounding)


def calculate_mass_circle(diameter: Decimal, length: Decimal, rounding: str) -> Decimal:
    """Расчет массы круга"""
    calculation_weight = Decimal(math.pi) / 4 * Decimal(7850) * (diameter / 1000) ** 2 * length
    return round_the_number(calculation_weight, rounding)


def calculate_mass_square(size: Decimal,
                          length: Decimal,
                          rounding: str) -> Decimal:
    """Расчет массы квадрата"""
    calculation_weight = Decimal(7850) * (size / 1000) ** 2 * length
    return round_the_number(calculation_weight, rounding)


def calculate_mass_sheet(side_a: Decimal,
                         side_b: Decimal,
                         thickness: Decimal,
                         rounding: str) -> Decimal:
    """Расчет массы листа"""
    calculation_weight = side_a / 1000 * side_b / 1000 * thickness / 1000 * Decimal(7850)
    return round_the_number(calculation_weight, rounding)


def calculate_mass_tube(diameter: Decimal,
                        thickness: Decimal,
                        length: Decimal,
                        rounding: str) -> Decimal:
    """Расчет массы трубы"""
    # Внутренний диаметр
    inner_diameter = diameter / 1000 - 2 * thickness / 1000
    # Площадь
    square = Decimal(math.pi) / 4 * ((diameter / 1000) ** 2 - inner_diameter ** 2)
    # Расчет массы листа
    calculation_weight = square * length * Decimal(7850)
    return round_the_number(calculation_weight, rounding)


def calculate_mass_profile_pipe(side_a: Decimal,
                                side_b: Decimal,
                                thickness: Decimal,
                                length: Decimal,
                                rounding: str) -> Decimal:
    """Расчет массы профильной трубы"""
    calculation_weight = (Decimal(7850) / Decimal('7850') * Decimal('0.0157') * thickness * (
            side_a + side_b - Decimal('2.86') * thickness)) * length
    return round_the_number(calculation_weight, rounding)


def calculate_mass_channel():
    """Расчет массы швеллеры"""
    pass


def calculate_mass_beam():
    """Расчет массы двутавра"""
    pass
