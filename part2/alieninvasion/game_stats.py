"""
======================
@title: game_stats
@description: 用于跟踪游戏统计信息的类
@author: elijah
@date: 2022/9/22 12:18
=====================
"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ships_left = None
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏启动处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化信息统计"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
