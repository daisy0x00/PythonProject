#coding:utf-8

#
import curses
from random import randrange, choice
from collections import defaultdict


# 用户行为
# 所有的有效输入都可以转换为“上， 下， 左， 右， 游戏重置， 退出”这六种行为，用actions表示
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

# 有效输入键是最常见的W（上)， A（左）， S（下）， D（右）， R（重置）， Q（退出）
# 这里要考虑到大写键开启的情况，获得有效键值列表
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

# 将输入与行为进行关联：
actions_dict = dict(zip(letter_codes, actions * 2))


# 状态机主逻辑代码
def main():
    def init():
        # 重置游戏棋盘
        return 'Game'

    def not_game(state):
        # 画出GameOver或者Win的界面
        # 读取用户输入得到action， 判断是重启游戏还是结束游戏

        # 默认是当前状态，没有行为就会一直在当前界面循环
        responses = defaultdict(lambda: state)
        # 对应不同的行为转换到不同的状态
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'

        # if成功移动了一步：
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'GameOver'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'GameOver': lambda: not_game('GameOver'),
        'Game': game
    }

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()