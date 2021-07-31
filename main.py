from FunctionalDependency import *
from Atom import *
from AttackGraph import *
from FirstOrderRewrite import *

'''
query = input("Entrer votre requête :")
atomList = query.split(';')

for atom in atomList:
    for element in range(0, len(atom)):
        print(atom[element])
'''

#######################################################
#                     Parameters                      #
#######################################################

listOfRelation = ["R", "S"]
key = [["x"], ["y"]]
nonKey = [["y"], ["a"]]
vars = ["u", "v", "w", "x", "y", "z"]
Atoms = []
AllConst = ["a", "b"]
functionalDependencyList = []
Free = []
atom = None

#######################################################
#                     Functions                       #
#######################################################

# Build atoms and put them in a list
def buildatomlist():
    for index, relation in enumerate(listOfRelation):
        Atoms.append(Atom(relation, key[index], nonKey[index]))


# Build functional dependency and put them in a list
def buildfunctionaldependencylist():
    for atom in Atoms:
        functionalDependencyList.append(FunctionalDependency(atom.key, atom.non_key))


#######################################################
#                  Initialization                     #
#######################################################
buildatomlist()
buildfunctionaldependencylist()
attackGraph = AttackGraph()
forewritter = FirstOrderRewrite(AllConst, vars)

#######################################################
#                  Attack Graph                       #
#######################################################
attackGraph.initialize(Atoms, vars)
attackGraph.realizeattackgraph(Atoms, functionalDependencyList)

#######################################################
#                 First Order Rewrite                 #
#######################################################
if attackGraph.areThereAnyAttack and attackGraph.isFirstOrderExpressible:
    print("Tableau des attaques : " + str(attackGraph.attack))
    rewrite = forewritter.performfirstorderrewrite(Atoms, Free)
    print("Réécriture : " + rewrite)



