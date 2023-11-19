from PyQt5.QtWidgets import QMenuBar, QAction


class MainMenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        # Пункты в баре
        vessels_menu = self.addMenu("Узконаправленные")  #
        metal_product_menu = self.addMenu("Металлопрокат")  #

        # Пункты меню Сосуды
        gost_34347_drop_menu = vessels_menu.addMenu("ГОСТ 34347-2017")  # Дроп меню
        geometry_drop_menu = vessels_menu.addMenu("Геометрические")
        weight_drop_menu = vessels_menu.addMenu("Массы")

        # Пункты "ГОСТ 34347-2017"
        self.thermal_treatment = QAction("Термообработка", self)
        self.pipe_thinning_item = QAction("Утонение патрубка", self)

        # Пункты "Геометрические"
        self.shell_reamers_item = QAction("Развертка обечайки", self)
        self.arc_length_item = QAction("Длина дуги", self)
        self.circumference_item = QAction("Длина окружности", self)
        self.arc_size_item = QAction("Размер по дуге", self)

        # Пункты "Массы"
        self.ring_weight = QAction("Кольцо укрепляющее", self)
        self.flooring_weight = QAction("Масса настила ТУ 36.26.11-5-89", self)


        # Добавляем в дроп меню пункты ("Сосуды")
        gost_34347_drop_menu.addAction(self.thermal_treatment)
        gost_34347_drop_menu.addAction(self.pipe_thinning_item)

        geometry_drop_menu.addAction(self.shell_reamers_item)
        geometry_drop_menu.addAction(self.arc_length_item)
        geometry_drop_menu.addAction(self.circumference_item)
        geometry_drop_menu.addAction(self.arc_size_item)

        weight_drop_menu.addAction(self.ring_weight)
        weight_drop_menu.addAction(self.flooring_weight)


        corner_drop_menu = metal_product_menu.addMenu("Уголки")  # Дроп меню "Уголки"
        # Пункты "Уголки"
        self.corner_equal_shelves_item = QAction("Уголки равнополочные", self)
        self.corner_different_shelves_item = QAction("Уголки неравнополочные", self)

        # Добавляем в дроп меню пункты ("Уголки")
        corner_drop_menu.addAction(self.corner_equal_shelves_item)
        corner_drop_menu.addAction(self.corner_different_shelves_item)

        self.circle_item = QAction("Кругляк", self)
        self.square_item = QAction("Квадрат", self)
        self.sheet_item = QAction("Лист", self)
        self.tube_item = QAction("Труба", self)
        self.profile_pipe_item = QAction("Профильная труба", self)
        self.beam_y_item = QAction("Двутавр ГОСТ 8239-89", self)

        # Добавляем пункты меню в "Металлопрокат"
        metal_product_menu.addAction(self.circle_item)
        metal_product_menu.addAction(self.square_item)
        metal_product_menu.addAction(self.sheet_item)
        metal_product_menu.addAction(self.tube_item)
        metal_product_menu.addAction(self.profile_pipe_item)
        metal_product_menu.addAction(self.beam_y_item)

        self.channel_drop_menu = metal_product_menu.addMenu("Швеллер ГОСТ 8240-97")  # Дроп меню "Швеллер ГОСТ 8240-97"
        # Пункты "Швеллер ГОСТ 8240-97"
        self.series_y_channel = QAction("Серия У", self)
        self.series_p_channel = QAction("Серия П", self)
        self.series_eh_channel = QAction("Серия Э", self)
        self.series_l_channel = QAction("Серия Л", self)
        # Добавляем пункты в дроп меню "Швеллер ГОСТ 8240-97"
        self.channel_drop_menu.addAction(self.series_y_channel)
        self.channel_drop_menu.addAction(self.series_p_channel)
        self.channel_drop_menu.addAction(self.series_eh_channel)
        self.channel_drop_menu.addAction(self.series_l_channel)

        self.beam_p_drop_menu = metal_product_menu.addMenu("Двутавр ГОСТ 26020-83")  # Дроп меню "Двутавр ГОСТ 26020-83"
        # Пункты "Двутавр ГОСТ 26020-83"
        self.beam_b_item = QAction("Номер Б", self)
        self.beam_ch_item = QAction("Номер Ш", self)
        self.beam_k_item = QAction("Номер К", self)
        self.beam_d_item = QAction("Номер Д", self)
        # Добавляем пункты в дроп меню "Двутавр ГОСТ 26020-83"
        self.beam_p_drop_menu.addAction(self.beam_b_item)
        self.beam_p_drop_menu.addAction(self.beam_ch_item)
        self.beam_p_drop_menu.addAction(self.beam_k_item)
        self.beam_p_drop_menu.addAction(self.beam_d_item)

        # Неактивные пункты
        self.flooring_weight.setEnabled(False)
        self.beam_p_drop_menu.setEnabled(False)
        self.channel_drop_menu.setEnabled(False)
        self.beam_y_item.setEnabled(False)
