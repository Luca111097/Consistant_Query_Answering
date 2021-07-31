class FunctionalDependency:
    left_member = None
    right_member = None

    def __init__(self, left_member, right_member):
        self.left_member = left_member
        self.right_member = right_member

    # Display functional dependency in the form X -> Y
    def printDF(self):
        print(str(self.left_member) + u"\u2192" + str(self.right_member))

