# Keras-RL のカスタマイズ

強化学習のライブラリーであるKeras-RL のカスタマイズ手順です。一番簡単なサンプルである、CartPole を使います。

## 動作環境
Windowsは公式サポートはありませんが、一応動いています。

## 事前作業
幾つかのKeras-RL実行に必要なモジュールをインストールします。
- Make for Windows
http://gnuwin32.sourceforge.net/packages/make.htm

   純粋にダウンロードしてインストールします。

- OpenAI Gym

    強化学習全体のフレームワークです。

    https://github.com/openai/gym

```cmd
pip install gym
```

- Keras-RL

    Keras で、強化学習を行うためのライブラリーです。

    https://github.com/keras-rl/keras-rl

``` cmd
pip install keras-rl
```

## 独自 Env クラスの作成の準備
1.  ひな型として cartpole.py ファイルを取得
- [cartpole.py](https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py "cartpole.py")
- Open AI Gym
- ローカルパス: /env/cartpole_env.py

```python
import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np

class myCartPoleEnv(gym.Env):
  ...
```

2. Gymへの登録
- [__ini__.py](https://github.com/openai/gym/blob/master/gym/envs/__init__.py "__init__.py")
- Open AI Gym
- ローカルパス: /env/__init__.py

```python
from gym.envs.registration import register

register(
    id='mycartpole-v0',
    entry_point='env.cartpole_env:myCartPoleEnv'
)
```

3. Agent側 (呼び出し側) での参照設定
- [dqn_cartpole.py](https://github.com/keras-rl/keras-rl/blob/master/examples/dqn_cartpole.py "dqn_cartpole.py")
- Keras-RL
- ローカルパス: /

```python
import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

import env #Reference to custom Env

# ENV_NAME = 'CartPole-v0'
ENV_NAME = 'mycartpole-v0' #custom Env


# Get the environment and extract the number of actions.
env = gym.make(ENV_NAME)
```


4. カスタムEnvの登録

    pip コマンドで行います。

```python
pip install -e .
```

5. Agent 実行

```cmd
python dqn_cartpole.py
```

参考: https://qiita.com/ohtaman/items/edcb3b0a2ff9d48a7def/


2. Env のカスタマイズ

## Todo
- キー入力を受け付けるようにします。
- Rewardの変更
- モデルの保存と実行の分離