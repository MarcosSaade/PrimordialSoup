# Natural selection simulator
# Marcos Saade, 2022

# pygame and random imported in other files
from organisms import *
from settings import *
from stats import *


class Main:
    def __init__(self):
        self.food = Food()
        self.organisms = []
        self.organisms.append(
            Organism('single_cell', random.randint(0, WIDTH), random.randint(0, HEIGHT), origin='spawned'))

    def start(self):
        self.food.init_food()

    def update(self):
        self.food.generate_food()
        self.food.draw()
        self.food.move()
        for index, organism in enumerate(self.organisms):
            organism.draw()
            organism.move()
            organism.eat()
            organism.reproduce()
            organism.die(index)

            if organism.id not in ids:
                ids.append(organism.id)
                gene_pool.append(organism.species)
                origins.append(organism.origin)

        if spontaneous_frequency != 0:
            if random.randint(0, (10000 - (spontaneous_frequency * 100))) == 0:  # Self forming
                self.organisms.append(
                    Organism('single_cell', random.randint(0, WIDTH), random.randint(0, HEIGHT), origin='spawned'))

        stats(food=len(main.food.food), show=False)


class Food:
    def __init__(self):
        self.food = []
        self.xs = []
        self.ys = []
        self.quantity = food_quantity
        self.size = food_size
        self.speed = random.randint(0, 4)
        self.negative_speed = random.randint(-4, 0)

    def init_food(self):
        if len(self.food) == 0:
            for i in range(self.quantity):
                self.xs.append(random.randint(0, WIDTH))
                self.ys.append(random.randint(0, HEIGHT))
                self.food.append(pygame.rect.Rect(self.xs[i], self.ys[i], self.size, self.size))

    def generate_food(self):
        if random.randint(0, (100 - food_freq)) == 0:
            for i in range(food_generation_quantity):
                self.xs.append(random.randint(0, WIDTH))
                self.ys.append(random.randint(0, HEIGHT))
                self.food.append(pygame.rect.Rect(self.xs[i], self.ys[i], self.size, self.size))

    def draw(self):
        for i in range(len(self.food)):
            pygame.draw.rect(screen, (255, 255, 255), self.food[i])

    def move(self):
        while self.speed == 0 and self.negative_speed == 0:
            self.speed = random.randint(0, 4)
            self.negative_speed = random.randint(-4, 0)
        if random.randint(0, 100) == 0:
            self.speed = random.randint(0, 4)
            self.negative_speed = random.randint(-4, 0)

        for index, i in enumerate(self.food):
            self.xs[index] += random.randint(self.negative_speed, self.speed)
            self.ys[index] += random.randint(self.negative_speed, self.speed)
            self.food[index] = pygame.rect.Rect(self.xs[index], self.ys[index], self.size, self.size)

        for index, i in enumerate(self.xs):
            if i < 0:
                self.xs[index] = WIDTH
                self.ys[index] = random.randint(0, HEIGHT)
            if i > WIDTH:
                self.xs[index] = 0
                self.ys[index] = random.randint(0, HEIGHT)

        for index, i in enumerate(self.ys):
            if i < 0:
                self.ys[index] = HEIGHT
                self.xs[index] = random.randint(0, WIDTH)
            if i > HEIGHT:
                self.ys[index] = 0
                self.xs[index] = random.randint(0, WIDTH)


class Organism:
    def __init__(self, species, x, y, origin):
        self.species = species
        self.id = random.random()
        self.x = x
        self.y = y
        self.molecule_size = 10
        self.origin = origin

        # Initialization
        self.molecules = 0
        self.size_x = 0
        self.size_y = 0
        self.weight = 0
        self.color = (0, 0, 0)
        self.mutation_prob = 0
        self.mutant_offspring = 'single_cell'
        self.eaten = 0
        self.hunger = 0
        self.movements = ()
        self.has_eaten = []

        self.body = self.get_body()

    def get_body(self):
        if self.species == 'single_cell':
            self.molecules = 12
            self.size_x = 4
            self.size_y = 4
            self.weight = 1
            if self.color == (0, 0, 0):
                self.color = generate_color(self.species)
            self.mutation_prob = single_cell_mutation_prob
            self.mutant_offspring = random.choice(('big', 'long'))
            self.movements = single_cell_movement
        elif self.species == 'long':
            self.molecules = 16
            self.size_x = 6
            self.size_y = 4
            self.weight = 0.5
            if self.color == (0, 0, 0):
                self.color = generate_color(self.species)
            self.mutation_prob = long_mutation_prob
            self.mutant_offspring = 'carnivore'
            self.movements = long_movements
        elif self.species == 'carnivore':
            self.molecules = 20
            self.size_x = 7
            self.size_y = 4
            self.weight = 0.7
            if self.color == (0, 0, 0):
                self.color = generate_color(self.species)
            self.mutation_prob = carnivore_mutation_prob
            self.mutant_offspring = 'lethal'
            self.movements = carnivore_movements
        elif self.species == 'big':
            self.molecules = 21
            self.size_x = 5
            self.size_y = 5
            self.weight = 1.5
            if self.color == (0, 0, 0):
                self.color = generate_color(self.species)
            self.mutation_prob = big_mutation_prob
            self.mutant_offspring = 'sponge'
            self.movements = big_movements
        elif self.species == 'sponge':
            self.molecules = 36
            self.size_x = 6
            self.size_y = 6
            self.weight = 2
            if self.color == (0, 0, 0):
                self.color = generate_color(self.species)
            if random.randint(1, 5) == 1:
                self.color = generate_color(self.species)
            self.mutation_prob = 0
            self.mutant_offspring = 'lethal'
            self.movements = sponge_movements

        shape = generate_organism(self.x, self.y, self.molecule_size, self.species)
        return shape

    def draw(self):
        for i in range(self.molecules):
            pygame.draw.rect(screen, self.color, self.body[i])

    def move(self):
        if self.x <= 0:
            self.x = 30
        if self.x >= (WIDTH - self.size_x):
            self.x = WIDTH - (25 * self.size_x)
        if self.y <= 0:
            self.y = 30
        if self.y >= (HEIGHT - self.size_y):
            self.y = HEIGHT - (25 * self.size_y)

        if random.randint(0, 7) == 0:
            water_direction = random.choice(('x', 'y'))
            water_strength = random.choice(self.movements)
            if water_direction == 'x':
                for i in range(4):
                    if i < 4:
                        self.x += water_strength / self.weight  # F/m = a
                        self.draw()  # animation smoothness
                        i += 1
            elif water_direction == 'y':
                for i in range(4):
                    if i < 4:
                        self.y += water_strength / self.weight
                        self.draw()
                        i += 1

        self.body = self.get_body()

    def eat(self):
        if self.species == 'carnivore':
            others = []

            for index, organism in enumerate(main.organisms):  # For every existing organism
                if organism.species not in ['carnivore', 'sponge']:  # They can't eat sponges because bigger and harder
                    others.append((index, organism.body))  # others <= (index of other, body of other)

            for i in self.body:
                for other in others:  # For every non member of the species
                    eaten = i.collidelist(other[1])  # If a carnivore molecule collides with body of other
                    if eaten != -1:
                        if self.hunger <= 500:  # If hungry (not digesting previous food)
                            # They use the food on energy for moving, digestion, etc
                            self.eaten += (main.organisms[other[0]].molecules / 6)
                            main.organisms.pop(other[0])  # Destroy organism
                            self.hunger = 0
                            return

        else:
            for molecule in self.body:  # For the entire body, check if touched a food, and which food
                eaten = molecule.collidelist(main.food.food)

                if eaten != -1 and eaten not in self.has_eaten:
                    main.food.food.pop(eaten)  # Remove eaten food from environment
                    main.food.xs.pop(eaten)  # Remove eaten food from environment
                    main.food.ys.pop(eaten)  # Remove eaten food from environment
                    self.has_eaten.append(eaten)
                    self.eaten += 1

    def reproduce(self):
        if self.eaten >= self.molecules:  # If organism has enough food for reproducing
            if self.mutation_prob != 0 and random.randint(1, int(
                    100 / self.mutation_prob)) == 1:  # Mutation in reproduction?
                mutation = True
            else:
                mutation = False

            x = self.x + random.randint(-100, 100)
            y = self.y + random.randint(-100, 100)

            if mutation:
                if self.mutant_offspring == 'lethal':
                    self.eaten = 0
                    return
                main.organisms.append(Organism(self.mutant_offspring, x, y, origin='mutation'))
            else:
                main.organisms.append(Organism(self.species, x, y, origin='reproduction'))
            self.eaten = 0

    def die(self, index):
        if self.species == 'carnivore':
            self.hunger += 1
            if self.hunger >= 1500:
                main.organisms.pop(index)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.KEYUP:
            pass


screen = pygame.display.set_mode((WIDTH, HEIGHT))
main = Main()
clock = pygame.time.Clock()
main.start()

while True:
    events()
    screen.fill((0, 0, 100))
    main.update()
    clock.tick(60)
    pygame.display.update()
