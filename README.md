# CSE3910-FINAL_PROJECT

## FRY THE EGG

## Instructions
Fry the Egg is a game where the player's goal is to defeat the boss; an egg. The player has to attack the boss with oil darts or make contact with the boss in order to deal melee damage. However, the boss has methods to resist and repel the players advances. There are 5 small oildart bullets bouncing around the playing area, and making contact with them as the player will deal significant damage. Making contact with the boss will deal damage to the boss, however, it will also eject the player to a random point on the map; leaving them at the mercy of the boss's oildarts.

The player will move around the screen using WASD keys.

There are obstacles on the map which will deflect the path of the bullets, as well as allow the player protection to some extent. The frying pan is a stationary obstacle in the middle of the map which in a way helps conduct the bullets around. There's also a chicken which moves side to side, also moving the bullets and providing protection to the player.

If the boss HP hits 0 before the player, the player wins. If the player HP hits 0 first the player loses.

Before the fight there is a small minigame. The player must beat this minigame in order to proceed to the fight. There will be 5 eggs distributed across the screen, and the player has 5 seconds to make contact with all of them. The frying pan in the middle takes on the boss's ability of ejecting the player to a random point on the map, this makes collecting coins close to the frying pan challenging. Sometimes the teleportation can be helpful, sometimes it will lose the player the game.

## Reflection
Our idea for the program involved not only the boss fight, but it also involved a shop and minigame which would help the player customize their attack/speed/resistance in preparation for the boss fight. However, through the actual development process we decided that focusing more of our time on the actual main game would be more beneficial for the final product considering our time constraints. We still opt'd to implement a minigame, even if it is more so a win to proceed affair, rather than collect to customize. This adds additional depth to our project, and gives the player a chance to familiarize themselves with the controls, collisions, and even some boss fight mechanics with the teleportation on contact with the frying man. 

In terms of challenges we had a few with our collisions, image sprites, and with the implementation of the minigame.

The main issue with collisions was the fact that the player would constantly stay in contact with the boss as it moves, making the damage done by the player game breaking. To fix this we made it so that the player is teleported to a random spot on the map, making it so that player/boss contact is a risk vs reward situation.

There were some bugs with changing the regular sprites into image sprites, as it messed up the sizes we had set up. To fix this we went into the properties of the image, and changed the sizes manually. We opt'd to do this instead of setting the scale as we could customize the sizes in more detail, rather than using a scale factor. 

With regard to the minigame, we programmed it after we had created the main game. There were some challenges simply getting the indentation and blitting of the mini game sprites. It wasn't the most complex or deep problem but it was certianly time consuming as we had to go through the program with a fine tooth comb in order to make sure all the indentation was correct, that the sprites were blitting and transitioning properly between the minigame and the main game.

We are extremely proud of our decision to hand draw our sprites, we feel that it adds an authentic feeling to the game and from a developmental point of view it was certianly an enjoyable process. It allowed us to truly customize the feel we want the game to give off, rather than let images available online dictate that feel.

We are also satisfied with the difficulty of the game, the player has to think about startegy with regard to moving in close to deal a lot of damage vs staying back and dealing less. All this while avoiding the deadly oildarts. The obstacles add another level of play which the player can use. Hiding in the obstacles makes you unable to fire the bullets so they serve as an interesting form of protection. The obstacles conducting the bullets around also make them a "blessing or a curse" depending on the situation.

Overall we love the look and feel of the game. It is quick paced, it has depth and strategy from the player's point of view, as well as authentic graphics. We feel like we could have made collisions more defined, as well as maybe implement a full screen. However, considering the time we had it is a great product.

