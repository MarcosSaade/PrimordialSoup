import random

single_cell_movement = (-7, -5, 5, 7)
long_movements = (-7, 0, 7)
carnivore_movements = (-6, 0, 6)
big_movements = (-10, 0, 10)
sponge_movements = (0, 0)


def generate_color(species):
    if species == 'single_cell':
        return random.randint(50, 150), random.randint(200, 255), random.randint(50, 150)
    elif species == 'long':
        return random.randint(200, 255), random.randint(75, 125), random.randint(0, 25)
    elif species == 'carnivore':
        return random.randint(75, 125), random.randint(0, 25), random.randint(0, 25)
    elif species == 'big':
        return random.randint(200, 255), random.randint(0, 50), random.randint(200, 255)
    elif species == 'sponge':
        return random.randint(96, 102), random.randint(0, 5), random.randint(147, 152)


def init_props():
    default = input('For default values press D. For manual press any key: ')

    if default in ['d', 'D']:
        w, h, sc_mp, l_mp, c_mp, b_mp, s_mp, food_q, food_s, food_f, food_gq, spontaneous_f = 1100, 700, 6, 2,\
                                                                                        10, 25, 0, 3000, 10, 1, 10, 60
        print(f'Screen Width: {w}')
        print(f'Screen Height: {h}')
        print(f'Single cell mutation probability: {sc_mp}')
        print(f'Long mutation probability: {l_mp}')
        print(f'Carnivore mutation probability: {c_mp}')
        print(f'Big mutation probability: {b_mp}')
        print(f'Sponge mutation probability: {s_mp}')
        print(f'Food quantity: {food_q}')
        print(f'Food size: {food_s}')
        print(f'Food generation frequency: {food_f}')
        print(f'Food generation quantity: {food_gq}')
        print('\n\n')
        print(f'Spontaneous replicator formation: {spontaneous_f} '
              f'(1 in {10000 - (spontaneous_f * 100)}) chance every frame')
    else:
        print('Single cell mutates into "Long" or "Big" at random \n')
        print('"Long" mutates into "Carnivore", and "Carnivore" has X probability of a lethal mutation\n')
        print('"Big" mutates into "Sponge" and "Sponge" has Y probability of a lethal mutation \n \n')
        w = int(input('Screen width: '))
        h = int(input('Screen height: '))
        sc_mp = int(input('Single cell mutation prob: '))
        l_mp = int(input('Long mutation prob: '))
        c_mp = int(input('Carnivore mutation prob: '))
        b_mp = int(input('Big mutation prob: '))
        s_mp = int(input('Sponge mutation prob: '))
        print('\n\n')
        food_q = int(input('Food quantity: '))
        food_s = int(input('Food size: '))
        food_f = int(input('Food generation frequency (1-100): '))
        food_gq = int(input('Food generation quantity: '))
        spontaneous_f = int(input('Frequency of spontaneous replicator formation (0-100): '))

    return [w, h, sc_mp, l_mp, c_mp, b_mp, s_mp, food_q, food_s, food_f, food_gq, spontaneous_f]


WIDTH, HEIGHT, single_cell_mutation_prob, long_mutation_prob, carnivore_mutation_prob, big_mutation_prob,\
    sponge_mutation_prob, food_quantity, food_size, food_freq, food_generation_quantity,\
    spontaneous_frequency = init_props()
