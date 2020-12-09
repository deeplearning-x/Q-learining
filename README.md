# Q-learining
运用Python和简单的强化学习算法实现智能体绕行障碍

Q-Learning是强化学习算法中value-based的算法，Q即为Q（s,a）就是在某一时刻的 s 状态下(s∈S)，
采取 动作a (a∈A)动作能够获得收益的期望，环境会根据agent的动作反馈相应的回报reward r，所以
算法的主要思想就是将State与Action构建成一张Q-table来存储Q值，然后根据Q值来选取能够获得最大
的收益的动作。
