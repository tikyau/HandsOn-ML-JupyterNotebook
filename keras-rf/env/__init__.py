from gym.envs.registration import register

register(
    id='mycartpole-v0',
    entry_point='env.cartpole_env:myCartPoleEnv'
)
