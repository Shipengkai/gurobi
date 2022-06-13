# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 10:06:07 2022

@author: shipk
"""
# This is a easy exercise.
# date: Jun 12 2022 
# This example formulates and solves the following simple MIP model:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary
"""
some useful tips:
    1. we can access help by command 'help(Model.addVar)'
"""
import gurobipy as gb
from gurobipy import GRB

# create a model named mip1 exercise
m = gb.Model("mip1 exercise")

# Create variables
x = m.addVar(vtype = GRB.BINARY, name = "x")
y = m.addVar(vtype = GRB.BINARY, name = "y")
z = m.addVar(vtype = GRB.BINARY, name = "z")

# constraint
cons1 = m.addConstr(x + 2*y + 3*z <=4,name = "cons1")
cons2 = m.addConstr(x + y >= 1,name = "cons2")

# Set objective
obj = m.setObjective(x + y + 2 * z, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.VarName, v.xn))