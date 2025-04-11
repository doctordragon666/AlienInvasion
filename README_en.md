# Spaceship Game
[English](README_en.md)

## Game Introduction

This is a simple spaceship game where players need to control the spaceship to shoot down obstacles and score points. This project is based on the book "Python Beginner Practical Battle".

## How to Play

- Use the arrow keys on the keyboard to control the movement of the spaceship.
- Avoid collisions with obstacles, otherwise the game will end.
- Each time an obstacle is shot down, the score increases and the speed also increases.

## Project File Description
```shell
.
│   .gitignore
│   alien.py
│   alien_invasion.py # Program entry point, start from here
│   bullet.py # Bullet
│   button.py # Game start button
│   game_functions.py
│   game_stats.py # Game status
│   LICENSE
│   README.md
│   scoreboard.py # Scoreboard
│   settings.py # Game settings
│   ship.py
│
└───images
        alien.bmp # Alien image
        luoxuanwan.bmp # Bullet
        naruto.bmp # Spaceship 1
        ship.bmp # Spaceship 2
```

## Game Flowchart

```mermaid
flowchart TB
    Main[alien_invasion.py] -->|Initialize Game| Init[settings.py, alien.py, ship.py, bullet.py]
    Main -->|Event Handling| Events[game_functions.py]
    Main -->|Update Game State| Update[game_functions.py]
    Main -->|Draw Screen| Draw[game_functions.py]
    Events -->|Mouse Click| MouseClick[button.py]
    Events -->|Key Press| KeyPress[game_functions.py]
    Update -->|Update Bullets| BulletUpdate[bullet.py]
    Update -->|Update Aliens| AlienUpdate[alien.py]
    Update -->|Update Ship| ShipUpdate[ship.py]
    Draw -->|Draw Bullets| DrawBullet[bullet.py]
    Draw -->|Draw Aliens| DrawAlien[alien.py]
    Draw -->|Draw Ship| DrawShip[ship.py]
    Draw -->|Draw Scoreboard| DrawScore[Scoreboard.py]
    AlienUpdate -->|Check Edges| CheckEdges[alien.py]
    AlienUpdate -->|Check Collision| CheckCollision[game_functions.py]
    CheckCollision -->|Bullet-Alien Collision| BulletAlienCollision[game_functions.py]
    CheckCollision -->|Ship-Alien Collision| ShipAlienCollision[game_functions.py]
    ShipAlienCollision -->|Reset Game State| ResetGame[game_stats.py]
    BulletAlienCollision -->|Update Score| UpdateScore[Scoreboard.py]
    UpdateScore -->|Check High Score| CheckHighScore[game_stats.py]
    CheckEdges -->|Change Direction| ChangeDirection[alien.py]
    ChangeDirection -->|Move Down Aliens| MoveDown[alien.py]
    KeyPress -->|Move Ship| MoveShip[ship.py]
    KeyPress -->|Fire Bullet| FireBullet[bullet.py]
    FireBullet -->|Update Bullets| BulletUpdate[bullet.py]
    MoveShip -->|Update Ship| ShipUpdate[ship.py]
```


## Game Play Example
![Game Play Image](gamedemo.gif)

## License Description
This project is released under the MIT License.