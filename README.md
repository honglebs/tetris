# Tetris Game

This is a Tetris game implemented in Python using the Pygame library and object-oriented programming principles. It allows you to play the classic Tetris game, where you manipulate falling blocks to complete lines and earn points.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the Pygame library by running the following command:
3. Download the source code for the Tetris game from the repository.

## How to Play

1. Run the `main.py` file to start the game.
2. The goal of the game is to complete as many lines as possible by arranging the falling blocks in a way that fills entire rows.
3. Use the following keyboard controls to play the game:
- **Left Arrow**: Move the current block to the left.
- **Right Arrow**: Move the current block to the right.
- **Down Arrow**: Move the current block down faster.
- **Up Arrow**: Rotate the current block.
4. The game ends when the stack of blocks reaches the top of the grid, and you can start a new game by pressing any key after the game over screen appears.

## Code Structure

The game code consists of the following files:

- `game.py`: Defines the `Game` class, which manages the game logic, including block movement, rotation, scoring, and grid management.
- `grid.py`: Contains the `Grid` class, responsible for managing the Tetris grid and handling operations such as clearing rows.
- `blocks.py`: Defines the various block shapes and their behavior.
- `colors.py`: Contains color constants used for drawing the game elements.
- `main.py`: Implements the game loop, event handling, and rendering using the Pygame library.

The `Game` class in `game.py` contains the core functionality of the game, such as initializing the grid, managing blocks, scoring, and game over conditions. It uses object-oriented programming principles to create and manipulate block objects.

The `Block` class in `blocks.py` represents a single Tetris block. It contains methods for moving, rotating, and drawing the block on the screen. The class also stores information about the block's position, rotation state, and color.

## Acknowledgements

This game is based on the classic Tetris game and was developed using the Pygame library. The implementation follows object-oriented programming principles to provide a modular and extensible code structure.

## License

The Tetris game is provided under the [MIT License](LICENSE). Feel free to modify and distribute the game according to the terms of the license.
