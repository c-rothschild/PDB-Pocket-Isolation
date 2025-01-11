
import Bio
from Bio.PDB.PDBParser import PDBParser
import numpy as np
from sklearn.neighbors import KDTree
import os
from itertools import compress

def parse_to_struc(structure_id, filename):
    """
    gets a structure (biopy datatype) from a PDB file+structure ID
    """
    p = PDBParser(PERMISSIVE=1)
    return p.get_structure(structure_id, filename)


def get_atom_ID(structure, atom):
    """
    given a structure and an atom,
    this function returns the chimerax atom ID
    """
    atom_data = atom.get_full_id() #gets properties associated with atom

    #the 3 lines below seperates the full id into a chain ID, residue ID, and the name of the atom
    chain_id = atom_data[2]
    residue_id = str(atom_data[3][1])
    atom_name = atom_data[4][0]

    ID = "/"+chain_id+":"+residue_id+"@"+atom_name #creating a string that will be used for the chimerax command
    return ID


def get_coord_array(structure): #given a structure object, this function returns a numpy array of that structure's atomic locations
    atoms = list(structure.get_atoms())
    return np.array(list(map(lambda atom: atom.get_coord(), atoms)))


def get_min_dists(coordsX, coordsY): #go through all atoms in chain X and find closest chain Y atom
    coordsYTree = KDTree(coordsY, leaf_size = 2)
    dist, ind = coordsYTree.query(coordsX, k = 1)
    r = dist
    return r



def get_minDist_cmd(chain, minDists, thresh): # select add each atom that has a minimum distance below the thresh
    r = []
    atomList = list(chain.get_atoms())

    select = list(map(lambda dist: True if dist < thresh else False, minDists ))
    atomsToSelect = list(compress(atomList, select))

    r = list(map(lambda atom: "select add " + get_atom_ID(chain, atom), atomsToSelect))

    return r


commands = [] #empty list of commands

structure_id = '2b0z'

filename = r'PPI dataset/2b0z.pdb'

s = parse_to_struc(structure_id, filename) #getting structure from 2b0z.pdb

chainList = list(s.get_chains()) #get list of chains from structure

#seperate chain A and B
chainA = chainList[0]
chainB = chainList[1]
#get list of coords for each chain
chainACoords = get_coord_array(chainA)
chainBCoords = get_coord_array(chainB)

#list of distances to closet atom in other chain
chainAMins = get_min_dists(chainACoords, chainBCoords)
chainBMins = get_min_dists(chainBCoords, chainACoords)

commands+= get_minDist_cmd(chainA, chainAMins, 6)
commands+= get_minDist_cmd(chainB, chainBMins, 6)

# write command(s) onto a text file
with open("Output.txt", "w") as text_file:
    text_file.write('\n'.join(commands))

os.system('chimerax-daily --nogui --exit RunChimera.py')#runs command to execute a python script in chimerax
#
# for dist in chainBMins:print(dist)
