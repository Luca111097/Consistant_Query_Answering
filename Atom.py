class Atom:

    def __init__(self, relation_name, key, non_key):
        self.relation_name = relation_name
        self.key = key
        self.non_key = non_key
        self.closure = []

    # Calculate closure for an atom
    def calculate_closure(self, functional_dependency_to_check, all_constant_in_query):
     
        i = 0

        # If the only element of the array is empty string then pass
        if '' in self.key and len(self.key) == 1:
            pass
        else:
            for attribute in self.key:
                # Check if the element is a variable not empty
                if attribute not in all_constant_in_query and attribute != '': 
                    if attribute not in self.closure:
                        self.closure.append(attribute)

            print("Dépendances fonctionelles de " + self.relation_name)

            for df in functional_dependency_to_check:
                print(f"{' '*4}-{df}")

            # Runs through the whole array
            while i <= len(functional_dependency_to_check):
                for index, df in enumerate(functional_dependency_to_check):
                    check = any(item in df.left_member for item in self.closure)
                    # Check if item is in left member of functional dependency 
                    # or the second check is for the case that the left member 
                    # contains only one empty element
                    if check or ('' in df.left_member and len(df.left_member) == 1):
                        del functional_dependency_to_check[index]
                        for attribute in df.right_member:
                            # Check if the element is a variable not empty
                            if attribute not in all_constant_in_query and attribute != '':
                                if attribute not in self.closure:
                                    self.closure.append(attribute)
                        i = 0
                i += 1

    def __repr__(self):
        return f"Atom(relation name: {self.relation_name}, key: {self.key}, non key {self.non_key})"

    def __str__(self):
        return str(self.relation_name) +"(" + str(self.key) +"," +str(self.non_key) +")"