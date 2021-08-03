class FunctionalDependency:

    def __init__(self, left_member, right_member):
        self.left_member = left_member
        self.right_member = right_member

    # Display functional dependency in the form X -> Y
    def print_functional_dependency(self):
        print(str(self.left_member) + u"\u2192" + str(self.right_member))

    def __repr__(self):
        return f"FunctionalDependency(left_member: {self.left_member}, right_member: {self.right_member})"

    def __str__(self):
        return str(self.left_member) + u"\u2192" + str(self.right_member)