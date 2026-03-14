# Population Dynamics: Fibonacci Recurrence Relations

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview
This repository contains a computational implementation of population growth models based on classical recurrence relations. Specifically, it explores the **Fibonacci Rabbit Model**, a discrete-time model used to predict population size over $n$ generations given specific maturation and fertility constraints.

## Mathematical Formulation
The growth of the rabbit population is governed by a second-order linear homogeneous recurrence relation with constant coefficients. 

Under the idealized conditions (immortal rabbits, one-month maturation, one-pair litter size), the population at month $n$ is defined by:

$$F_n = F_{n-1} + F_{n-2}$$

### Model Constraints:
* **Initial State:** $F_1 = 1, F_2 = 1$
* **Growth Factor:** Each mature pair produces exactly $k=1$ pair per generation.
* **Maturation:** Newborn pairs require one time step before becoming reproductive.

## Implementation
The repository includes multiple approaches to solving the recurrence:
1. **Recursive:** Direct implementation of the mathematical definition (Caution: $O(2^n)$ complexity).
2. **Iterative:** Optimized linear-time solution ($O(n)$) using state variables.
3. **Dynamic Programming:** Memoization-based approach to minimize redundant calculations.

## Usage
To execute the solver, ensure you have Python installed and run:
```bash
python solution.py