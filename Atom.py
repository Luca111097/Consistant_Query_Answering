class Atom:

    relation_name = None
    key = []
    non_key = []
    closure = []
    AllConst = ["a", "b"]

    def __init__(self, relation_name, key, non_key):
        self.relation_name = relation_name
        self.key = key
        self.non_key = non_key
        self.closure = []

    # Calculate closure for an atom
    def calculateclosure(self, functionalDependencyToCheck):

        i = 0

        if len(self.key) == 0:
            self.closure = []
        else:
            for attribute in self.key:
                if attribute not in self.AllConst:
                    self.closure.append(attribute)

            print("Dépendances fonctionelles de " + self.relation_name)

            for df in functionalDependencyToCheck:
                df.printDF()

            while i <= len(functionalDependencyToCheck):
                for index, df in enumerate(functionalDependencyToCheck):
                    check = any(item in df.left_member for item in self.closure)
                    if df in functionalDependencyToCheck and check or len(df.left_member) == 0:
                        del functionalDependencyToCheck[index]
                        for attribute in df.right_member:
                            if attribute not in self.AllConst:
                                self.closure.append(attribute)
                        i = 0
                i += 1

    # Display an atom in the form R(x,y)
    def printatom(self):
        print(str(self.relation_name) + "(" + str(self.key) + "," + str(self.non_key) + ")")