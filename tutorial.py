from __future__ import print_function
import numpy as np

import gambit
from fractions import Fraction

# Build extensive game

g = gambit.Game.new_tree()

g.title = "A Simple poker example"

p1 = g.players.add("Alice")

print(p1.label)

print(g.players)

# Build strategic form

g2 = gambit.Game.new_table([2,2])

g2.title = "A prison's dilemma game"

g2.players[0].label = "Alphonse"

g2.players[1].label = "Gaston"

print(g2.players[0].strategies)

g2.players[0].strategies[0].label = "Cooperative"
g2.players[0].strategies[1].label = "Defect"
g2.players[1].strategies[0].label = "Cooperative"
g2.players[1].strategies[1].label = "Defect"

g2[0,0][0]=8
g2[0,0][1]=8
g2[0,1][0]=2
g2[0,1][1]=10
g2[1,0][0]=10
g2[1,0][1]=2
g2[1,1][0]=5
g2[1,1][1]=5

# Build strategic form in a simpler way

m = np.array([[8,2],[10,5]], dtype = gambit.Rational)

g3 = gambit.Game.from_arrays(m, np.transpose(m))

# read from file

gamepath = "/media/markxueyuan/Data/data/games/"

g4 = gambit.Game.read_game(gamepath + "e02.nfg")
list(g4.contingencies)

# iterate pure strategy profiles
for profile in g4.contingencies:
    print(profile, g4[profile][0], g4[profile][1])

# Mixed strategy

p4 = g4.mixed_strategy_profile()

list(p4)

print(p4[g4.players[0]])

print(p4[g4.players[1].strategies[0]])

p4.payoff(g4.players[0])

# expected payoff assuming other

p4.strategy_value(g4.players[0].strategies[0])


# Behavior strategies

g5 = gambit.Game.read_game(gamepath + "e02.efg")

p5 =g5.mixed_behavior_profile()

list(p5)

print(p5[g5.players[0]])

print(p5[g5.players[1]])

    # check infosets
print(p5[g5.players[0].infosets[0]])

print(p5[g5.players[0].infosets[0].actions[0]])


# mix <--> behavior conversion

p55 = p5.as_strategy()

p50 = p55.as_behavior()


p5 == p50
p5 is p50

# Mash equilibrium

    # Pure

PureSolver = gambit.nash.ExternalEnumPureSolver()
PrisonerDelimma = PureSolver.solve(g2)

