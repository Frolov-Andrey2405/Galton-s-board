# Galton-s-board

A "Galton Board", also known as a "Quincunx" or a "Bean Machine", is a vertically mounted device used to demonstrate the normal distribution and the central limit theorem in statistics. It consists of a vertical board with a series of evenly spaced nails or pegs arranged in a zigzag pattern.

![Galton_board](https://tinyurl.com/r6et8v9f)

When a ball is dropped from the top of the board, it will encounter the pegs and randomly bounce either to the left or right with equal probability at each peg. As the ball continues to bounce down the board, its final position at the bottom of the board will be determined by the cumulative result of these random left or right deflections.

The distribution of the balls at the bottom of the board follows a "binomial distribution", which approximates a normal distribution as the number of pegs increases. The probability mass function (PMF) of the binomial distribution is given by:

$$P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$$

Where:
- $n$ is the number of pegs
- $k$ is the number of times the ball moves to the right
- $p$ is the probability of moving to the right (which is 0.5 for a fair Galton Board)

As $n$ increases, the binomial distribution approaches the normal distribution, with the mean $\mu = np$ and the standard deviation $\sigma = \sqrt{np(1-p)}$.

## Normal distribution curve

The "Normal Distribution Curve", also known as the "Gaussian Distribution" or the "Bell Curve", is a continuous probability distribution that is widely used in statistics, probability theory, and various other fields. It is a symmetric, bell-shaped curve that is defined by two parameters: the mean ($\mu$) and the standard deviation ($\sigma$).

![Normal_distribution_curve](https://tinyurl.com/2ypvj6dp)

The normal distribution curve is described by the probability density function (PDF):

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

Where:
- $x$ is the variable (e.g., height, weight, test scores)
- $\mu$ is the mean or the expected value of the distribution
- $\sigma$ is the standard deviation, which measures the spread or dispersion of the distribution
- $e$ is the base of the natural logarithm (approximately 2.71828)
- $\pi$ is the mathematical constant pi (approximately 3.14159)

## Code implementation

The `main.py` file contains the implementation of a simulation for a Galton Board using the Pygame library and the Pymunk physics engine.

### Libraries Used

- `pygame`: Used for creating the graphical interface and handling events such as quitting the application.
- `pymunk`: A physics engine library used for creating the physics simulation of the Galton Board.

### Constants

- `RES`, `WIDTH`, and `HEIGHT`: Define the resolution and dimensions of the simulation window.
- `FPS`: Sets the frames per second for the simulation.
- `ball_mass`, `ball_radius`: Parameters defining the mass and size of the balls dropped in the simulation.
- `segment_thickness`: Thickness of the segments representing the pegs and platforms.
- Constants `a`, `b`, `c`, `d`: Define specific coordinates for creating segments and pegs.

### Functions

1. `create_ball(space)`: Creates a ball object with random initial position within specified boundaries.
2. `create_segment(from_, to_, thickness, space, color)`: Creates a segment shape (e.g., pegs, platforms) with given parameters.
3. `create_peg(x, y, space, color)`: Creates a peg at specified coordinates with given color.

### Pegs and Platforms

The script dynamically creates pegs and platforms on the Galton Board based on predefined coordinates and patterns. Pegs are represented by circles, and platforms are represented by segments.

### Balls

- Generates a specified number of balls with random colors and initial positions.
- Simulates the movement of balls through the Galton Board by bouncing off pegs and platforms.
- Utilizes physics properties such as elasticity and friction for realistic ball behavior.

### Simulation Loop

- Continuously updates the simulation by processing events, updating the physics simulation, and rendering the scene.
- Ensures a smooth animation with the specified frames per second (`FPS`).

### Preview
![Result](/img/result.gif)