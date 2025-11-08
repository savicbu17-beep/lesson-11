# class Marker:
#     def __init__(self, color, size):
#         self.marker_color = color
#         self.marker_size = size
#
#     def draw(self):
#         print(f"Малюю кольором: {self.marker_color}, товщина лінії: {self.marker_size}")
#
#     def info(self):
#         print(f"Маркер {self.marker_color}, товщина {self.marker_size}")
#
# # Створення об’єктів
# m_red = Marker("червоний", 2)
# m_blue = Marker("синій", 4)
#
# # Виклик методів
# m_red.draw()
# m_blue.draw()
#
# m_red.info()
# m_blue.info()


class Student:
    def __init__(self, name, height, IT, hwork=0):
        self.name = name
        self.height = height
        self.IT = IT
        self.hwork = hwork

    def study(self):
        self.hwork += 10
        print(f"{self.name} вчится на {self.hwork}")

    def work(self):
        print(f"{self.name} працює щоб отримати досвід")

    def rest(self):
        print(f"{self.name} відпочиває після навчання")

vova = Student(name="Вова", height=170)
vova.study()

vova.study()
vova.work()
vova.rest()