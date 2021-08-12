class FunctionalDependency:

    def __init__(self, left_member, right_member):
        self.left_member = left_member
        self.right_member = right_member
        self.left_member_to_print = None
        self.right_member_to_print = None

    # Display functional dependency in the form X -> Y
    def print_functional_dependency(self):
        print(str(self.left_member) + u"\u2192" + str(self.right_member))

    def __repr__(self):
        return f"FunctionalDependency(left_member: {self.left_member}, right_member: {self.right_member})"

    def __str__(self):
        # Have to create a copy of each functional dependency member to make pretty print
        # The pretty print consist of removing the empty string of each part of the functional dependency
        self.left_member_to_print = [variable for variable in self.left_member if variable != ""]
        self.right_member_to_print = [variable for variable in self.right_member if variable != ""]
        return str(self.left_member_to_print) + u"\u2192" + str(self.right_member_to_print)