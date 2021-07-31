class AttackGraph:

    notUsedFunctionalDependency = []
    attackedVars = []
    isFirstOrderExpressible = False
    areThereAnyAttack = False
    attack = []
    occurInAtom = {}
    AllConst = ["a", "b"]

    def __init__(self):
        pass

    # Perfom the union of two lists
    def union(self, list1, list2):
        final_list = list1 + list2
        return final_list

    def initialize(self, atomList, allVariableInQuery):

        for indexAtomF in range(len(atomList)):

            atomF = atomList[indexAtomF]
            allVariableInQuery = self.union(atomF.key, atomF.non_key)

            for var in allVariableInQuery:  # prendra successivement "x", "y", "z" avec l'exemple
                if var in self.occurInAtom:
                    self.occurInAtom[var].append(atomList[indexAtomF])  # ajout l'élement si
                    # la liste était déjà partiellement remplie
                else:
                    self.occurInAtom[var] = [atomList[indexAtomF]]  # créé la liste si elle était vide

            colOfAttackGraph = []
            for i in range(0, len(atomList)):
                colOfAttackGraph.append(0)
            self.attack.append(colOfAttackGraph)

    def realizeattackgraph(self, atomList, functionalDependencyList):

        self.isFirstOrderExpressible = True

        for indexAtomF, atomF in enumerate(atomList):

            notUsedFunctionalDependency = functionalDependencyList.copy()
            del notUsedFunctionalDependency[indexAtomF]
            atomList[indexAtomF].calculateclosure(notUsedFunctionalDependency)

            print("Fermeture pour l'atome " + atomF.relation_name + " " + str(atomF.closure))
            attackedVars = [x for x in atomF.non_key if x not in atomF.closure and x not in self.AllConst]

            while len(attackedVars) != 0:

                x = attackedVars[0]
                del attackedVars[0]

                for atomG in self.occurInAtom[x]:
                    if atomG != atomF and self.attack[indexAtomF][atomList.index(atomG)] == 0:
                        self.attack[indexAtomF][atomList.index(atomG)] = 1
                        self.areThereAnyAttack = True
                        if self.attack[atomList.index(atomG)][indexAtomF] == 1:
                            self.isFirstOrderExpressible = False

                        for y in self.union(atomG.key, atomG.non_key):
                            if y != x and y not in atomF.closure and y not in self.AllConst:
                                attackedVars += y
