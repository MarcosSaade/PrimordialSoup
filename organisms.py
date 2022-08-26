import pygame


def generate_organism(x, y, size, organism):
    if organism == 'single_cell':
        return [
            # First row
            pygame.rect.Rect(x, y, size, size),
            pygame.rect.Rect((x + size), y, size, size),

            # Second
            pygame.rect.Rect((x - size), (y + size), size, size),
            pygame.rect.Rect(x, (y + size), size, size),
            pygame.rect.Rect((x + size), (y + size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + size), size, size),

            # Third
            pygame.rect.Rect((x - size), (y + 2 * size), size, size),
            pygame.rect.Rect(x, (y + 2 * size), size, size),
            pygame.rect.Rect((x + size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 2 * size), size, size),

            # Fourth
            pygame.rect.Rect(x, (y + 3 * size), size, size),
            pygame.rect.Rect((x + size), (y + 3 * size), size, size),
        ]

    elif organism == 'long':
        return [
            # First row
            pygame.rect.Rect(x, y, size, size),
            pygame.rect.Rect((x + size), y, size, size),

            # Second
            pygame.rect.Rect((x - 2 * size), (y + size), size, size),
            pygame.rect.Rect((x - size), (y + size), size, size),
            pygame.rect.Rect(x, (y + size), size, size),
            pygame.rect.Rect((x + size), (y + size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + size), size, size),

            # Third
            pygame.rect.Rect((x - 2 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x - size), (y + 2 * size), size, size),
            pygame.rect.Rect(x, (y + 2 * size), size, size),
            pygame.rect.Rect((x + size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 2 * size), size, size),

            # Fourth
            pygame.rect.Rect(x, (y + 3 * size), size, size),
            pygame.rect.Rect((x + size), (y + 3 * size), size, size),
        ]

    elif organism == 'carnivore':
        return [
            # First row
            pygame.rect.Rect(x, y, size, size),
            pygame.rect.Rect((x + size), y, size, size),

            # Second
            pygame.rect.Rect((x - 3 * size), (y + size), size, size),
            pygame.rect.Rect((x - 2 * size), (y + size), size, size),
            pygame.rect.Rect((x - size), (y + size), size, size),
            pygame.rect.Rect(x, (y + size), size, size),
            pygame.rect.Rect((x + size), (y + size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + size), size, size),
            pygame.rect.Rect((x + 4 * size), (y + size), size, size),

            # Third
            pygame.rect.Rect((x - 3 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x - 2 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x - size), (y + 2 * size), size, size),
            pygame.rect.Rect(x, (y + 2 * size), size, size),
            pygame.rect.Rect((x + size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 4 * size), (y + 2 * size), size, size),

            # Fourth
            pygame.rect.Rect(x, (y + 3 * size), size, size),
            pygame.rect.Rect((x + size), (y + 3 * size), size, size),
        ]

    elif organism == 'big':
        return [
            # First row
            pygame.rect.Rect(x, y, size, size),
            pygame.rect.Rect((x + size), y, size, size),
            pygame.rect.Rect((x + 2 * size), y, size, size),

            # Second
            pygame.rect.Rect((x - size), (y + size), size, size),
            pygame.rect.Rect(x, (y + size), size, size),
            pygame.rect.Rect((x + size), (y + size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + size), size, size),

            # Third
            pygame.rect.Rect((x - size), (y + 2 * size), size, size),
            pygame.rect.Rect(x, (y + 2 * size), size, size),
            pygame.rect.Rect((x + size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 2 * size), size, size),

            # Fourth
            pygame.rect.Rect((x - size), (y + 3 * size), size, size),
            pygame.rect.Rect(x, (y + 3 * size), size, size),
            pygame.rect.Rect((x + size), (y + 3 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 3 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 3 * size), size, size),

            # Fifth
            pygame.rect.Rect(x, (y + 4 * size), size, size),
            pygame.rect.Rect((x + size), (y + 4 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 4 * size), size, size),
        ]
    elif organism == 'sponge':
        return [
            # First row
            pygame.rect.Rect((x - size), y, size, size),
            pygame.rect.Rect(x, y, size, size),
            pygame.rect.Rect((x + size), y, size, size),
            pygame.rect.Rect((x + 2 * size), y, size, size),
            pygame.rect.Rect((x + 3 * size), y, size, size),
            pygame.rect.Rect((x + 4 * size), y, size, size),

            # Second
            pygame.rect.Rect((x - size), (y + size), size, size),
            pygame.rect.Rect(x, (y + size), size, size),
            pygame.rect.Rect((x + size), (y + size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + size), size, size),
            pygame.rect.Rect((x + 4 * size), (y + size), size, size),

            # Third
            pygame.rect.Rect((x - size), (y + 2 * size), size, size),
            pygame.rect.Rect(x, (y + 2 * size), size, size),
            pygame.rect.Rect((x + size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 2 * size), size, size),
            pygame.rect.Rect((x + 4 * size), (y + 2 * size), size, size),

            # Fourth
            pygame.rect.Rect((x - size), (y + 3 * size), size, size),
            pygame.rect.Rect(x, (y + 3 * size), size, size),
            pygame.rect.Rect((x + size), (y + 3 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 3 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 3 * size), size, size),
            pygame.rect.Rect((x + 4 * size), (y + 3 * size), size, size),

            # Fifth
            pygame.rect.Rect((x - size), (y + 4 * size), size, size),
            pygame.rect.Rect(x, (y + 4 * size), size, size),
            pygame.rect.Rect((x + size), (y + 4 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 4 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 4 * size), size, size),
            pygame.rect.Rect((x + 4 * size), (y + 4 * size), size, size),

            # Sixth
            pygame.rect.Rect((x - size), (y + 5 * size), size, size),
            pygame.rect.Rect(x, (y + 5 * size), size, size),
            pygame.rect.Rect((x + size), (y + 5 * size), size, size),
            pygame.rect.Rect((x + 2 * size), (y + 5 * size), size, size),
            pygame.rect.Rect((x + 3 * size), (y + 5 * size), size, size),
            pygame.rect.Rect((x + 4 * size), (y + 5 * size), size, size),
        ]