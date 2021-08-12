class AttackGraph:

    def __init__(self, all_constant_in_query):

        self.not_used_functional_dependency = []
        self.attacked_vars = []
        self.is_first_order_expressible = True
        self.are_there_any_attack = False
        self.attack = []
        self.occur_in_atom = {}
        self.all_variable_in_atom = []
        self.all_constant_in_query = all_constant_in_query

    # Perfom the union of two lists
    @staticmethod
    def union(list1, list2):
        final_list = list1 + list2
        return final_list

    def initialize(self, atom_list):

        for index_atom_f, atom_F in enumerate(atom_list):

            self.all_variable_in_atom = AttackGraph.union(atom_F.key, atom_F.non_key)

            # Identify in which atom occur each var
            for var in self.all_variable_in_atom:
                if var in self.occur_in_atom:
                    self.occur_in_atom[var].append(atom_list[index_atom_f])
                else:
                    self.occur_in_atom[var] = [atom_list[index_atom_f]]

            # Build the attack matrix
            col_of_attack_graph = []
            for i in range(0, len(atom_list)):
                col_of_attack_graph.append(0)
            self.attack.append(col_of_attack_graph)

    def realize_attack_graph(self, atomList, functionalDependencyList):

        self.is_first_order_expressible = True

        for index_atom_f, atom_f in enumerate(atomList):

            not_used_functional_dependency = functionalDependencyList.copy()
            del not_used_functional_dependency[index_atom_f]
            atomList[index_atom_f].calculate_closure(not_used_functional_dependency, self.all_constant_in_query)

            print("Fermeture pour l'atome " + atom_f.relation_name + " " + str(atom_f.closure))

            # Put all variables which are not in the closure of the F atom in attacked_var
            attacked_vars = [x for x in atom_f.non_key if x not in atom_f.closure
                             and x not in self.all_constant_in_query]

            while len(attacked_vars) != 0:

                x = attacked_vars[0]
                del attacked_vars[0]

                for atom_g in self.occur_in_atom[x]:
                    if atom_g != atom_f and self.attack[index_atom_f][atomList.index(atom_g)] == 0:
                        self.attack[index_atom_f][atomList.index(atom_g)] = 1
                        self.are_there_any_attack = True
                        if self.attack[atomList.index(atom_g)][index_atom_f] == 1:
                            self.is_first_order_expressible = False

                        for y in self.union(atom_g.key, atom_g.non_key):
                            if y != x and y not in atom_f.closure and y not in self.all_constant_in_query:
                                attacked_vars += y
