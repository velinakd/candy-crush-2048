Judy
====

Judy is an interactive game that could be played through a GUI or a CLI. The GUI uses both keyboard and mouse. The game's main purpose is to destroy the blocks in the 2D field by clicking on them. If the clicked block is a part of a group of at least three neighbouring blocks of the same kind, the whole group will disappear.

When you destroy blocks, the remaining blocks won't move. But when you tilt the board using the arrow keys, they will move in the desired direction.

As you proceed through the game and go up through the levels, the number of different kinds of blocks increases. You can go up a level if you have destroyed a sufficient amount of the blocks on the screen. You get points for every destroyed group of blocks. The bigger the group is, the more points you acquire.

There are also bombs that, when clicked, destroy themselves and all neighbouring blocks. (Bonus feature)

Another advantage is that upon entering the game, you can choose among a few tile themes and board sizes.


Plan for Milestone 2
--------------------
To have an initial object model implementation (the `Board` and `Block` classes).

To decide on the parameters of the game: points rewarding, requirements for passing a level, etc.

Game Parameters
---------------
1) First level starts with 2 kinds of blocks and every subsequent level adds one kind.
2) In order to proceed to the next level, you must have no more than 5 blocks left undestroyed. 
3) For a destroyed group of 3 blocks you get 5 points, for every additional block in the group the points are doubled (e.g. 4 blocks - 10 points, 5 blocks - 20 points, etc.).
4) Board sizes: Small (6x5), Medium (15x10), Big (20x15)
