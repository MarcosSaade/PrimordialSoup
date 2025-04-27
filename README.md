<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="images/header.png" alt="Header">

  <h3 align="center">PrimordialSoup</h3>

  <p align="center">
    A simplified natural selection simulator built with Python and Pygame.
    <br />
    <a href="https://github.com/MarcosSaade/PrimordialSoup/issues">Report Bug</a>
    ·
    <a href="https://github.com/MarcosSaade/PrimordialSoup">Request Feature</a>
  </p>
</div>

---

## About The Project

<img src='images/screenshot.png'>

**PrimordialSoup** is a lightweight simulation of natural selection, designed to model the basic principles of evolution through simple organisms.  
Organisms move, eat, reproduce, mutate, and occasionally evolve into new species depending on their survival success.

I built this project during high school as a learning exercise to explore Python programming, object-oriented design, and evolutionary algorithms.  
It was a ton of fun and gave me a solid foundation in simulation design and visual programming with Pygame.

---

## Features

- Organism classes with different behaviors and mutation paths
- Simple food dynamics and movement simulation
- Procedural gene pool evolution and spontaneous generation
- Configurable settings (mutation rates, food spawn rates, etc.)
- Basic visualization of organisms and mutation trees
- Built entirely in **Python** with **Pygame**

---

## Installation

This project is a prototype, but you can run it locally:

### Prerequisites

- Python 3.x
- Pygame library

Install Pygame with:

```bash
pip install pygame
```

### Running the Simulation

Clone the repository and run:

```bash
git clone https://github.com/MarcosSaade/PrimordialSoup.git
cd PrimordialSoup
python main.py
```

You'll be prompted to choose between default or custom simulation settings.

---

## Gene Pool and Mutation Tree

The image below shows the gene pool and the possible mutation paths between organisms:

<img src='images/tree.png'>

---

## Organisms

Each organism has distinct traits like speed, food needs, and mutation probabilities:

### Single Cell
<img src='images/single_cell.png'>

- Simplest organism; can spawn spontaneously.
- Mutates into Big or Long (50/50 chance).
- Reproduction requires 12 food units.
- Speed: 1.

---

### Long
<img src='images/long.png'>

- Evolves from Single Cell.
- Can mutate into Carnivore.
- Reproduction requires 16 food units.
- Speed: 2.

---

### Carnivore
<img src='images/carnivore.png'>

- Evolves from Long.
- Eats other organisms instead of food.
- Needs to digest before eating again.
- Can starve to death if no prey is available.
- Speed: 2.

---

### Big
<img src='images/big.png'>

- Evolves from Single Cell.
- Can mutate into Sponge.
- Reproduction requires 21 food units.
- Speed: 0.5.

---

### Sponge
<img src='images/sponge.png'>

- Evolves from Big.
- Cannot move.
- Cannot be eaten by Carnivores.
- Reproduction requires 36 food units.

---

## Future Improvements

Some planned or possible enhancements:

- Real-time graphs of population dynamics
- Additional species and mutation chains
- Environmental hazards and adaptive behaviors
- Smarter carnivore behavior and digestion mechanics

---

## Contact

If you have any questions or feedback, feel free to reach out:  
📧 marcossr2626@gmail.com

---
