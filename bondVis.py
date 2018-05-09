import numpy as np
import sys
import re
from PIL import Image
import math
import colorsys
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os

# The radius beyond which I will no longer consider atoms close to each other.
CUTOFF_RADIUS = 10

# Get File Name
root = tk.Tk()
root.withdraw()
# filename = sys.argv[1]
filename = askopenfilename()
# messagebox.showinfo("File Path", os.path.dirname(os.path.realpath(filename)))

# Read Lattice Parameters
inFile = open(filename, 'r')
# Name
nextLine = inFile.readline()
# Scale
nextLine = inFile.readline()
scale = float(nextLine)
# Lattice parameter A
nextLine = inFile.readline()
lineSplit = re.split("\s+",nextLine)
latA = (scale*float(lineSplit[1]), scale*float(lineSplit[2]), scale*float(lineSplit[3]))
# Lattice parameter B
nextLine = inFile.readline()
lineSplit = re.split("\s+",nextLine)
latB = (scale*float(lineSplit[1]), scale*float(lineSplit[2]), scale*float(lineSplit[3]))
# Lattice parameter C
nextLine = inFile.readline()
lineSplit = re.split("\s+",nextLine)
latC = (scale*float(lineSplit[1]), scale*float(lineSplit[2]), scale*float(lineSplit[3]))

# Read Atom Positions
# throw out all of the starting info
while nextLine != "Direct\n":
    nextLine = inFile.readline()
nextLine = inFile.readline()
# Read each atom position
atomList = []
while nextLine != " \n":
    xyz = re.split("\s+",nextLine)
    xyz = (latA[0]*float(xyz[1]) + latB[0]*float(xyz[2]) + latC[0]*float(xyz[3]),
           latA[1]*float(xyz[1]) + latB[1]*float(xyz[2]) + latC[1]*float(xyz[3]),
           latA[2]*float(xyz[1]) + latB[2]*float(xyz[2]) + latC[2]*float(xyz[3]))
    atomList += [xyz]
    nextLine = inFile.readline()
messagebox.showinfo("Atom List", atomList)

# Read density matrix
# read the next line to get the actual division information
divInfo = inFile.readline()
# Calculate the size of the array and line number
arraySizes = [int(x) for x in re.split("\s+", divInfo)[1:4]]
entryNum = arraySizes[0]*arraySizes[1]*arraySizes[2]
lineNum = int(entryNum/10) + bool(entryNum%10)
# Read in the density array
densityArray = np.empty(arraySizes)
zMax = 0
xMax = 0
yMax = 0
for lineCount in range(lineNum):
        nextLine = inFile.readline()
        lineData = re.split("\s+",nextLine)
        dataCount = 10*lineCount
        for datapoint in lineData[1:-1]:
                zVar = int(dataCount / (arraySizes[0] * arraySizes[1]))
                remainder = dataCount % (arraySizes[0] * arraySizes[1])
                yVar = int(remainder / (arraySizes[0]))
                yVar = arraySizes[1] - yVar - 1
                remainder = remainder % (arraySizes[0])
                xVar = int(remainder)
                if (datapoint[0] == "*"):
                        densityArray[xVar, yVar, zVar] = 0
                else:
                        densityArray[xVar, yVar, zVar] = float(datapoint)
inFile.close()

# NOTE TO SELF: this loop doesn't properly handle hexagonal lattices!
# Generate all allowable lattice shifts, subject to the cutoff distance
shiftList = []
# Generate the full range of a lattice spacings
for ai in range(-math.ceil(CUTOFF_RANGE/math.sqrt(latA[0]**2+latA[1]**2+latA[2]**2)),
                math.ceil(CUTOFF_RANGE/math.sqrt(latA[0]**2+latA[1]**2+latA[2]**2))+1):
    # Generate the full range of b lattice spacings
    for bi in range(-math.ceil(CUTOFF_RANGE/math.sqrt(latB[0]**2+latB[1]**2+latB[2]**2)),
                math.ceil(CUTOFF_RANGE/math.sqrt(latB[0]**2+latB[1]**2+latB[2]**2))+1):
        # Generate the full range of c lattice spacings
        for ci in range(-math.ceil(CUTOFF_RANGE/math.sqrt(latC[0]**2+latC[1]**2+latC[2]**2)),
                math.ceil(CUTOFF_RANGE/math.sqrt(latC[0]**2+latC[1]**2+latC[2]**2))+1):
            clA = 1 if ai > 0 else 0
            clB = 1 if bi > 0 else 0
            clC = 1 if ci > 0 else 0
            minDist = math.sqrt(((ai-clA)*latA[0]+(bi-clB)*latB[0]+(ci-clC)*latC[0])**2 +
                                ((ai-clA)*latA[1]+(bi-clB)*latB[1]+(ci-clC)*latC[1])**2 +
                                ((ai-clA)*latA[2]+(bi-clB)*latB[2]+(ci-clC)*latC[2])**2)
            if minDist < CUTOFF_RANGE:
                shiftList += [(ai,bi,ci)]


# For each atom
for atom in atomList:
    # For each point in space
    it = np.nditer(densityArray, flags=['f_index'])
    while not it.finished:
        # Loop over all lattice offsets
        for latOff in shiftList:
            xyz = 
            # Calculate distance to atom (include lattice shifts)
            
            # (optionally exclude point if longer than a particular distance)
            # Add to distance-sorted list of points
            # Include (distance, value, x, y, z) in tuple
    # Loop over all points in sorted list
        # Iterate backwards through indices until you reach the end or extend past a sample spacing
        # Do the same forwards
        # Fit the selected range with a cubic function
        # Take the value of the cubic at the point of interest
        # Subtract this value from the actual local density, put that in a new array
    # Write out the lattice parameters, atoms, and new array values.




# read the next line to get the actual division information
divInfo = inFile.readline()
# Calculate the size of the array and line number
arraySizes = [int(x) for x in re.split("\s+", divInfo)[1:4]]
entryNum = arraySizes[0]*arraySizes[1]*arraySizes[2]
lineNum = int(entryNum/10) + bool(entryNum%10)


