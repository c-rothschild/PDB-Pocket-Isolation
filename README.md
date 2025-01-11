Project submitted Jul 24, 2024

Purpose: Given a PDB file of a Protein-Protein Interaction (PPI) with two chains, return the surface of the pocket in the PPI

Author: Charlie Rothschild
Email: c_rothschild@coloradocollege.edu

Instructions to Build:
Required application: ChimeraX
Download Link: https://www.cgl.ucsf.edu/chimerax/download.html
Required Packages:
1. Biopython
2. numpy
3. meshplot
4. Sklearn
(three modules below should be installed by default)
5. itertools
6. os
7. sys
Strings to change:
AtomLocations.py:
1. structure_id = ‘2b0z’
   1. Change ‘2b0z’ to the ID of the PPI you want to input
2. filename = r'PPI dataset/2b0z.pdb'
   1. Change r'PPI dataset/2b0z.pdb' to the path of the PDB you want to input
3. os.system('chimerax-daily --nogui --exit ChimeraTest.py')
   1. Change ‘chimerax-daily’ to the name of your ChimeraX application
RunChimera.py:
1. run(session, "open \"/home/charl/Desktop/Summer Research Code/PPI dataset/2b0z.pdb\"")
   1. Change "open \"/home/charl/Desktop/Summer Research Code/PPI dataset/2b0z.pdb\"" to “open /path/to/file.pdb”
2. run(session, "save \"/home/charl/Desktop/Summer Research Code/testSession.cxs\"")
   1. Change “save \"/home/charl/Desktop/Summer Research Code/testSession.cxs\"" to “save /path/to/newfile.cxs”


Instructions to Run:
(In project folder)$ python AtomLocations.py
To Change Selection Distance From PPI:
On line:
1. commands+= get_minDist_cmd(chainA, chainAMins, 6)
   1. Change 6 adjust threshold for atoms on chain A to be included in the selection
2. commands+= get_minDist_cmd(chainB, chainBMins, 6)
   1. Change 6 adjust threshold for atoms on chain B to be included in the selection
