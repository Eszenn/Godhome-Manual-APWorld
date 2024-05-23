# Godhome-Manual-APWorld
A manual APWorld for implementing the Godhome portion of Hollow Knight into the Archipelago randomizer. 

## Prerequisites
Proper usage of this APWorld requires a save file that has unlocked the Pantheon of Hallownest, all boss
statues in the hall of gods, and all 40 charms.

## Locations
The following are all locations that must be checked:
- Defeating bosses on each of the 3 difficulties in the Hall of Gods
- Completing Pantheons
- Completing Pantheons with each of the 4 bindings
  
## Items to be Received
The following are all items that may be received:
- All 39 charms (Void Heart not included)
- 41 Individual Boss Statues (Gruz Mother, Brooding Mawlek, and False Knight are in starting inventory)
- All 5 Pantheons (4 if goal is set to Pantheon 5)
- 4 Pantheon of Hallownest Fragments (if goal is set to Pantheon 5)
- All 4 bindings

## Goals
### Ascend the Pantheon of Hallownest
Requires obtaining all 4 Pantheon of Hallownest Fragments and 8 "good" charms to ensure that challenging the
Pantheon of Hallownest isn't incredibly difficult.
  - This replaces the Pantheon of Hallownest item with 4 Pantheon of Hallownest Fragments
  - This removes locations tied to clearing the Pantheon of Hallownest with bindings regardless of whether
    the option is turned on or not
### Boss Rush
Requires obtaining a YAML option specified amount of Boss Statues and defeating them within the Hall of Gods

## Custom YAML Options
### Goal
Sets the goal for your world to one of the two mentioned above
### Number of Bosses
Sets the number of bosses you are required to defeat for the Boss Rush goal
### Include Bindings
Adds Bindings to the item pool and clearing each Pantheon with each Binding to the location pool
### Include Radiant Difficulty
Adds defeating each Boss on Radiant to the location pool
