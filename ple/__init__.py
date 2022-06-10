from .ple import PLE
from gym.envs.registration import register
from .ple_env import PLEEnv
# Pygame
# ----------------------------------------
for game in ['PgPong', 'Catcher', 'MonsterKong', 'FlappyBird', 'PixelCopter', 'PuckWorld', 'RaycastMaze', 'Snake', 'WaterWorld']:
    nondeterministic = False
    register(
        id='{}-v0'.format(game),
        entry_point='ple:PLEEnv',
        max_episode_steps=10000,
        kwargs={'game_name': game, 'display_screen':False},
        nondeterministic=nondeterministic,
    )
