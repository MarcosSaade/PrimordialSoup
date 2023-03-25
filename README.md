<!-- PROJECT LOGO -->
<br />
<div align="center">
<img src="images/header.png" alt="Header">

  <h3 align="center">PrimordialSoup</h3>

  <p align="center">
   A  simplified natural selection simulator using python
    <br />
    <a href="https://github.com/MarcosSaade/PrimordialSoup/issues">Report Bug</a>
    ·
    <a href="https://github.com/MarcosSaade/PrimordialSoup">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#gene-pool">Gene Pool</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src='images/screenshot.png'>

Simulates the non random survival of simple organisms over time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

This is not yet production ready. However, you can test it by executing the code of main.py on an environment with pygame installed.

## Gene Pool

The image below shows the gene pool and posible mutations
<br/>
<img src='images/tree.png'>

## Organisms

<hr/>

### Single Cell
<img src='images/single_cell.png'>

* The simplest organism.
* Can form on its own.
* Mutates into: Big or Long (50/50)
* Food for reproduction: 12
* Speed: 1

<hr/>

### Long
<img src='images/long.png'>

* Comes from Single Cell
* Mutates into: Carnivore
* Food for reproduction: 16
* Speed: 2

<hr/>

### Carnivore
<img src='images/carnivore.png'>

* Comes from Long
* Food for reproduction: 20
* Doesn't eat normal food, eats other organisms
* Can only eat after digesting previous food
* Can die of hunger
* Some chance of having lethal mutation
* Speed: 2

<hr/>

### Big
<img src='images/big.png'>

* Comes from Single Cell
* Mutates into: Sponge
* Food for reproduction: 21
* Speed: 0.5

<hr/>

### Sponge
<img src='images/sponge.png'>

* Comes from Big
* Food for reproduction: 36
* Can't move, remains static
* Can't be eaten by carnivores
* Some chance of having lethal mutation

<hr/>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
