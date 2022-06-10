# PyGame-(Multi-Task)-Learning-Environment

### Hello from the forker
Just a brief explanation of this fork. It's designed to make the environments in this original repo a lot more configurable, in order to test agents' multi task abilities in RL environments. I am currently focused on pong.

Here's the rundown of what has changed:

- Many more parameters changeable in Pong, including but not limited to acceleration behaviour of agent, colours of things on screen, side of screen that agent controls
- Integrated [gym-ple](https://github.com/lusob/gym-ple) directly to the repo (that upstream didn't include pong; and making a pull request would mean it wouldn't work with original PLE, only my fork)
- Renamed pong to pgpong, so gym would work with the pong game. Basically it won't work if it's also called pong because there's already a gym environment called pong. That's probably why gym-ple didn't implement it.

![Games](ple_games.jpg?raw=True "Games!")

**PyGame Learning Environment (PLE)** is a learning environment, mimicking the [Arcade Learning Environment](https://github.com/mgbellemare/Arcade-Learning-Environment) interface, allowing a quick start to Reinforcement Learning in Python. The goal of PLE is allow practitioners to focus design of models and experiments instead of environment design.

PLE hopes to eventually build an expansive library of games.

**Accepting PRs for games.**

## Documentation

Docs for the project can be [found here](http://pygame-learning-environment.readthedocs.org/). They are currently WIP.

## Games

Available games can be found in the [docs](http://pygame-learning-environment.readthedocs.org/en/latest/user/games.html).

## Getting started

A `PLE` instance requires a game exposing a set of control methods. To see the required methods look at `ple/games/base.py`. 

Here's an example of importing PgPong from the games library within PLE:

```python
from ple.games.pgpong import PgPong

game = PgPong()
```

Next we configure and initialize PLE:

```python
from ple import PLE

p = PLE(game, fps=30, display_screen=True, force_fps=False)
p.init()
```

The options above instruct PLE to display the game screen, with `display_screen`, while allowing PyGame to select the appropriate delay timing between frames to ensure 30fps with `force_fps`.

You are free to use any agent with the PLE. Below we create a fictional agent and grab the valid actions:

```python
myAgent = MyAgent(p.getActionSet())
```

We can now have our agent, with the help of PLE, interact with the game over a certain number of frames:

```python

nb_frames = 1000
reward = 0.0

for f in range(nb_frames):
	if p.game_over(): #check if the game is over
		p.reset_game()

	obs = p.getScreenRGB()
	action = myAgent.pickAction(reward, obs)
	reward = p.act(action)

```

Just like that we have our agent interacting with our game environment.

## Installation

PLE requires the following dependencies:
* numpy
* pygame
* pillow

Clone the repo and install with pip.

```bash
git clone https://github.com/ntasfi/PyGame-Learning-Environment.git
cd PyGame-Learning-Environment/
pip install -e .
``` 

## Headless Usage

Set the following in your code before usage:
```python
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.environ["SDL_VIDEODRIVER"] = "dummy"
```

Thanks to [@wooridle](https://github.com/ntasfi/PyGame-Learning-Environment/issues/26#issuecomment-289517054).

## Updating

`cd` into the `PyGame-Learning-Environment` directory and run the following:

```bash
git pull
```

## Todos
 * Documentation is currently in progress.
 * Tests
 * Parallel Learning (One agent, many game copies)
 * Add games
 * Generalize the library (eg. add Pyglet support)


## Citing PLE

If PLE has helped your research please cite it in your publications. Example BibTeX entry:

```
@misc{tasfi2016PLE,
  author = {Tasfi, Norman},
  title = {PyGame Learning Environment},
  year = {2016},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ntasfi/PyGame-Learning-Environment}}
}
```
