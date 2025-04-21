class PumpController:
    def __init__(self):
        self.target_pressure = 4.0  # Целевое давление
    
    def adjust_pressure(self, current_pressure):
        if current_pressure < self.target_pressure:
            print("Увеличение мощности насоса")  # Эмуляция работы электромотора
        else:
            print("Снижение мощности насоса")  # [[10]]

# Тестирование
controller = PumpController()
controller.adjust_pressure(3.5)  # Выведет: Увеличение мощности