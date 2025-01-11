from chimerax.core.commands import run
import sys

f = open("Output.txt", "r") #read text file with list of commands
commands = f.read().splitlines() #split text file into list of lines (each line is a command)

run(session, "open \"/home/charl/Desktop/Summer Research Code/PPI dataset/2b0z.pdb\"")#open 2b0z.pdb in chimerax session (edit to specify the location)
run(session, "show atoms") #show all atom s
run(session, "hide cartoons") #hides 'cartoons' (protein folds?)
run(session, "style sphere") #represents atoms as balls of certain colors/sizes
run(session, "color bychain") #colors atom by the chain its associated with

#runs list of commands in output.txt
for cmd in commands:
    run(session, cmd)
run(session, "surface sel")
run(session, "hide atoms")
run(session, "save \"/home/charl/Desktop/Summer Research Code/testSession.cxs\"") #save chimeraX session as testSession.cxs (edit to specify the location)
