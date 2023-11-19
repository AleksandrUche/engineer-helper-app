from math import pi, degrees, acos
from decimal import Decimal

from services.services_widget.services import round_the_number


def heat_treatment(diameter: Decimal, thickness: Decimal) -> bool:
    """Термическая обработка обечайки"""
    action_1 = (diameter + thickness) / 2  # Rs формула
    action_2 = 50 * thickness / action_1
    return action_2 > 5


def refine_the_pipe(thin_pipe: Decimal, thick_pipe: Decimal) -> bool:
    """Утонение трубы по ГОСТ 34347-2017
    thin_pipe - труба меньшей толщины
    thick_pipe - более толстая труба"""
    action_1 = thin_pipe * Decimal(0.3)
    action_2 = thick_pipe - thin_pipe
    return action_1 < action_2


def expand_shell(diameter: Decimal, thickness: Decimal, rounding: str) -> Decimal:
    """Развертка обечайки"""
    result = (diameter + thickness) * Decimal(pi)
    return round_the_number(result, rounding)


def arc_length(radius: Decimal, angle: Decimal, rounding: str) -> Decimal:
    """Длина дуги"""
    result = radius * angle * Decimal(pi) / 180
    return round_the_number(result, rounding)


def circumference(diameter: Decimal, rounding: str) -> Decimal:
    """Длина окружности"""
    result = diameter * Decimal(pi)
    return round_the_number(result, rounding)


def calculate_angle_of_triangle(cathet: Decimal, hypotenuse: Decimal) -> Decimal:
    """Вычисление угла прямоугольного треугольника"""
    action_acos = Decimal(acos(cathet / hypotenuse))
    alpha = Decimal(degrees(action_acos))
    beta = 180 - 90 - alpha
    return beta


def calculation_arc_by_angle_and_radius(radius: Decimal, distance: Decimal, rounding: str) -> Decimal:
    """Вычисление дуги по углу (градусы) и радиусу (для емкостного оборудования)"""
    result = Decimal(pi) * radius * calculate_angle_of_triangle(distance, radius) / 180
    return round_the_number(result, rounding)


def ring_weight_diameter(diameter_inside: Decimal,
                         diameter_outside: Decimal,
                         thickness: Decimal,
                         rounding: str) -> Decimal:
    """Масса кольца укрепляющего по внутреннему и внешнему диаметру"""
    action_1 = Decimal(pi) * (diameter_outside / 2 / 1000) ** 2 * thickness / 1000 * 7850
    action_2 = Decimal(pi) * (diameter_inside / 2 / 1000) ** 2 * thickness / 1000 * 7850
    result = action_1 - action_2
    return round_the_number(result, rounding)
