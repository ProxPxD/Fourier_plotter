import pygame
from Fourier import Fourier
from math import pi

class Window:
    GRID_COLOR = [40, 40, 40]
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]


    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.reset()
        self.fourier += [1, 0]

        pygame.init()
        pygame.display.set_caption("Fourier")
        self.screen = pygame.display.set_mode((self.width, self.height))


    def reset(self):
        self.ended = False
        self.fourier = Fourier()
        self.t = 0
        self.periods = 3
        self.time_step = 10 ** -3
        self.points_0 = {
            'x': (self.width // 2, self.height // 4),
            'y': (self.width // 2, 3 * self.height // 4),
            '2D': (self.width // 4, 2 * self.height // 4)
        }
        self.x_step = 1
        self.scale = self.width // (4 * pi)
        self.points_x = []
        self.points_y = []
        self.values = []
        self.times = []
        self.max_points = 10 ** 4

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.ended = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    self.reset()
                    self.fourier.set_step_function(1)
                elif event.key == pygame.K_2:
                    self.reset()
                    self.fourier.set_step_function(2)
                elif event.key == pygame.K_3:
                    self.reset()
                    self.fourier.set_step_function(3)
                elif event.key == pygame.K_4:
                    self.reset()
                    self.fourier.set_step_function(4)
                elif event.key == pygame.K_5:
                    self.reset()
                    self.fourier.set_step_function(5)
                elif event.key == pygame.K_6:
                    self.reset()
                    self.fourier.set_step_function(6)
                elif event.key == pygame.K_7:
                    self.reset()
                    self.fourier.set_step_function(20)
                elif event.key == pygame.K_8:
                    self.reset()
                    self.fourier.set_step_function(50)
                elif event.key == pygame.K_9:
                    self.reset()
                    self.fourier.set_step_function(100)
                elif event.key == pygame.K_0:
                    self.reset()
                    self.fourier += [1, 0]
                print(self.fourier)
    def run(self):

        while not self.ended:
            self.handle_events()
            self.draw()
            self.update()

            pygame.display.flip()
            #time.sleep(self.tick_value)

    def update(self):
        if self.t < 1:
            self.t += self.time_step
            value = self.fourier.calc(self.t)
            self.values.append(value)
            self.times.append(self.t)
        elif self.t < self.periods:
            self.t += self.time_step
            self.times.append(self.t)
        else:
            self.values = self.values[1:] + self.values[:1]

    def draw(self):
        self.screen.fill(self.BLACK)
        k = 0
        for i in range(len(self.times)):
            if i % len(self.values) == 0:
                k += 1
            for type in self.points_0.keys():
                if i < len(self.values):
                    value = self.values[i]
                else:
                    value = self.values[i - k * len(self.values)]
                point = (self.times[i], value)
                scaled = self.scale_point(point)
                mapped = self.map_point(scaled, type)
                repositioned = self.move_point(mapped, self.points_0[type])
                self.screen.set_at(repositioned, self.WHITE)

    def scale_point(self, point, scale=None):
        if scale is None:
            scale = self.scale
        new_point = [point[0] * scale *2, point[1] * scale]
        return new_point

    def move_point(self, point, position):
        new_point = [position[0] + point[0], position[1] - point[1]]
        return new_point

    def map_point(self, point, type):
        if type == 'x':
            return self.get_time_real(point)
        if type == 'y':
            return self.get_time_imaginary(point)
        if type == '2D':
            return self.get_real_imaginary(point)

    def get_time_real(self, num):
        return (int(num[0].real), int(num[1].real))

    def get_time_imaginary(self, num):
        return (int(num[0].real), int(num[1].imag))

    def get_real_imaginary(self, num):
        return (int(num[1].real), int(num[1].imag))