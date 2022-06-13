# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 10:06:07 2022

@author: shipk
"""
# the following note is the content of model.lp
"""
\ Model mip1 exercise
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  2 x + 5 y
Subject To
 cons1: - x + 2 y <= 2
 cons2: x + y <= 4
 cons3: x - y <= 2
Bounds
End
"""

"""
some useful tips:
    1. we can access help info by command 'help(Model.addVar)'
"""
import gurobipy as gb
from gurobipy import GRB

# create a model named mip1 exercise
m = gb.Model("mip1 exercise")

# Create variables
x = m.addVar(vtype = GRB.CONTINUOUS, name = "x")
y = m.addVar(vtype = GRB.CONTINUOUS, name = "y")

# constraint
cons1 = m.addConstr(-1 * x + 2 * y  <= 2,name = "cons1")
cons2 = m.addConstr(x + y <= 4,name = "cons2")
cons3 = m.addConstr(x - y <= 2,name = "cons3")

# Set objective
obj = m.setObjective(2*x + 5*y , GRB.MAXIMIZE)

m.optimize()
m.write("model.lp")

for v in m.getVars():
    print('%s %g' % (v.VarName, v.x))