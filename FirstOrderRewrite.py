class FirstOrderRewrite:

    all_constant_in_query = None
    all_variable_in_query = None
    j = 1

    def __init__(self, all_constant_in_query, all_variable_in_query):

        self.all_variable_in_query = all_variable_in_query
        self.all_constant_in_query = all_constant_in_query

    def formatting_all_elements(self, VAR, NEWVAR, CONST):

        if len(VAR) != 0:
            existVar = ""
            for existingVar in VAR:
                existVar = existVar + u" \u2203" + existingVar
        else:
            existVar = ""

        if len(NEWVAR) != 0:
            existNewVar = ""
            for existingNewVar in NEWVAR:
                existNewVar = existNewVar + u"\u2200" + existingNewVar
        else:
            existNewVar = ""

        if len(CONST) != 0:
            existConst = u"\u2192 "
            for index, everyConst in enumerate(CONST):
                if index == 0:
                    existConst = existConst + NEWVAR[index] + " = " + str(everyConst)
                else:
                    existConst = existConst + u"\u2227 " + NEWVAR[index] + " = " + str(everyConst)
        else:
            existConst = ""

        return existVar, existNewVar, existConst

    def perform_first_order_rewrite(self, Atoms, Free):

        if len(Atoms) == 0:
            return "true"
        else:
            VAR = []
            CONST = []
            NEWVAR = []
            F = Atoms[0]


            for key in F.key:
                if key in self.all_variable_in_query and key not in Free:
                    VAR.append(key)
                    Free.append(key)

            for nonKey in F.non_key:
                if nonKey in self.all_variable_in_query and nonKey not in Free:
                    VAR.append(nonKey)
                    NEWVAR.append(nonKey)
                    Free.append(nonKey)

                elif nonKey in self.all_constant_in_query:
                    NEWVAR.append("c" + str(self.j))
                    i = F.non_key.index(nonKey)
                    CONST.insert(i, nonKey)
                    self.j += 1

        existVar, existNewVar, existConst = self.formatting_all_elements(VAR, NEWVAR, CONST)

        del Atoms[0]

        toContinue = self.perform_first_order_rewrite(Atoms, Free)

        if toContinue != "":
            toContinue = u"\u2192" + toContinue

        return existVar + " (" + F.relation_name + " (" + ",".join(F.key) + "," + ",".join(
            F.non_key) + ") " + u"\u2227 (" + existNewVar + " " + F.relation_name + "(" + ",".join(
            F.key) + "," + ",".join(
            NEWVAR) + ") " + existConst + toContinue + "))"

