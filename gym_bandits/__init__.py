from gym.envs.registration import register

from .bandit import BanditTenArmedRandomFixed
from .bandit import BanditTenArmedRandomRandom
from .bandit import BanditTenArmedGaussian
from .bandit import BanditTenArmedUniformDistributedReward
from .bandit import BanditTwoArmedDeterministicFixed
from .bandit import BanditTwoArmedHighHighFixed
from .bandit import BanditTwoArmedHighLowFixed
from .bandit import BanditTwoArmedLowLowFixed
from .bandit import BanditTwoArmedIndependentUniform
from .bandit import BanditTwoArmedDependentUniform
from .bandit import BanditTwoArmedDependentEasy
from .bandit import BanditTwoArmedDependentMedium
from .bandit import BanditTwoArmedDependentHard
from .bandit import BanditElevenArmedWithIndex

environments = [['BanditTenArmedRandomFixed', 'v0'],
                ['BanditTenArmedRandomRandom', 'v0'],
                ['BanditTenArmedGaussian', 'v0'],
                ['BanditTenArmedUniformDistributedReward', 'v0'],
                ['BanditTwoArmedDeterministicFixed', 'v0'],
                ['BanditTwoArmedHighHighFixed', 'v0'],
                ['BanditTwoArmedHighLowFixed', 'v0'],
                ['BanditTwoArmedLowLowFixed', 'v0'],
                ['BanditTwoArmedIndependentUniform', 'v0'],
                ['BanditTwoArmedDependentUniform','v0'],
                ['BanditTwoArmedDependentEasy','v0'],
                ['BanditTwoArmedDependentMedium','v0'],
                ['BanditTwoArmedDependentHard','v0'],
                ['BanditElevenArmedWithIndex','v0']]

for environment in environments:
    register(
        id='{}-{}'.format(environment[0], environment[1]),
        entry_point='gym_bandits:{}'.format(environment[0]),
        nondeterministic=True,
        ### https://github.com/carpedm20/deep-rl-tensorflow/issues/47
        # timestep_limit=1,
    )
