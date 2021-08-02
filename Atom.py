class Atom:

    relation_name = None
    key = []
    non_key = []
    closure = []

    def __init__(self, relation_name, key, non_key):
        self.relation_name = relation_name
        self.key = key
        self.non_key = non_key
        self.closure = []

    # Calculate closure for an atom
    def calculate_closure(self, functionalDependencyToCheck, all_constant_in_query):

        i = 0

        if '' in self.key and len(self.key) == 1:
            self.closure = []
        else:
            for attribute in self.key:
                if attribute not in all_constant_in_query:
                    self.closure.append(attribute)

            print("Dépendances fonctionelles de " + self.relation_name)

            for df in functionalDependencyToCheck:
                df.print_functional_dependency()

            while i <= len(functionalDependencyToCheck):
                for index, df in enumerate(functionalDependencyToCheck):
                    check = any(item in df.left_member for item in self.closure)
                    if (df in functionalDependencyToCheck and check) or ('' in df.left_member and len(df.left_member) == 1):
                        del functionalDependencyToCheck[index]
                        for attribute in df.right_member:
                            if attribute not in all_constant_in_query:
                                self.closure.append(attribute)
                        i = 0
                i += 1

    # Display an atom in the form R(x,y)
    def print_atom(self):
        print(str(self.relation_name) + "(" + str(self.key) + "," + str(self.non_key) + ")")