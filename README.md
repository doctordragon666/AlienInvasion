# 飞船小游戏
[English](README_en.md)

## 游戏介绍

这是一个简单的飞船小游戏，玩家需要控制飞船击落障碍物，并获取得分。
本项目基于python入门实战一书。

## 游戏玩法

- 使用键盘上的方向键控制飞船的移动。
- 避免与障碍物碰撞，否则游戏结束。
- 每次击落障碍物，得分增加，速度也会加快。

## 项目文件说明
```shell
.
│   .gitignore
│   alien.py
│   alien_invasion.py # 程序入口，从这里启动
│   bullet.py # 子弹
│   button.py # 游戏开始按钮
│   game_functions.py
│   game_stats.py # 游戏状态
│   LICENSE
│   README.md
│   scoreboard.py # 计分板
│   settings.py # 游戏设置
│   ship.py
│
└───images
        alien.bmp # 外星人图片
        luoxuanwan.bmp # 子弹
        naruto.bmp # 飞船1
        ship.bmp # 飞船2
```

## 游戏流程图

```mermaid
flowchart TB
    Main[alien_invasion.py] -->|初始化游戏| Init[settings.py, alien.py, ship.py, bullet.py]
    Main -->|事件处理| Events[game_functions.py]
    Main -->|游戏状态更新| Update[game_functions.py]
    Main -->|绘制屏幕| Draw[game_functions.py]
    Events -->|鼠标点击| MouseClick[button.py]
    Events -->|键盘按键| KeyPress[game_functions.py]
    Update -->|更新子弹| BulletUpdate[bullet.py]
    Update -->|更新外星人| AlienUpdate[alien.py]
    Update -->|更新飞船| ShipUpdate[ship.py]
    Draw -->|绘制子弹| DrawBullet[bullet.py]
    Draw -->|绘制外星人| DrawAlien[alien.py]
    Draw -->|绘制飞船| DrawShip[ship.py]
    Draw -->|绘制得分板| DrawScore[Scoreboard.py]
    AlienUpdate -->|检测边缘| CheckEdges[alien.py]
    AlienUpdate -->|检测碰撞| CheckCollision[game_functions.py]
    CheckCollision -->|子弹与外星人碰撞| BulletAlienCollision[game_functions.py]
    CheckCollision -->|飞船与外星人碰撞| ShipAlienCollision[game_functions.py]
    ShipAlienCollision -->|重置游戏状态| ResetGame[game_stats.py]
    BulletAlienCollision -->|更新得分| UpdateScore[Scoreboard.py]
    UpdateScore -->|检查最高分| CheckHighScore[game_stats.py]
    CheckEdges -->|改变方向| ChangeDirection[alien.py]
    ChangeDirection -->|下移外星人| MoveDown[alien.py]
    KeyPress -->|移动飞船| MoveShip[ship.py]
    KeyPress -->|发射子弹| FireBullet[bullet.py]
    FireBullet -->|更新子弹| BulletUpdate[bullet.py]
    MoveShip -->|更新飞船| ShipUpdate[ship.py]
```

## 游戏运行示例
![游戏运行图片](gamedemo.gif)

## 许可证说明
本项目基于 MIT 许可证发布。