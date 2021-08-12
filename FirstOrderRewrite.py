import re

STR_EXISTS = u"\u2203"
STR_FORALL = u"\u2200"
STR_AND = u" \u2227 "
STR_ARROW = u" \u2192 "


class FirstOrderRewrite:

    def __init__(self, all_constant_in_query, all_variable_in_query):

        global STR_EXISTS
        global STR_FORALL
        global STR_AND
        global STR_ARROW

        self.idx_constant = 1
        self.all_variable_in_query = all_variable_in_query
        self.all_constant_in_query = all_constant_in_query

    def is_empty_string(self, string_to_check):
        return re.search("^\s*$", string_to_check)

    def formatting_all_elements(self, VAR, NEWVAR, CONST):

        if len(VAR) != 0:
            existVar = ""
            for existingVar in VAR:
                existVar += STR_EXISTS + existingVar
        else:
            existVar = ""

        if len(NEWVAR) != 0:
            existNewVar = ""
            for existingNewVar in NEWVAR:
                existNewVar += STR_FORALL + existingNewVar
        else:
            existNewVar = ""

        if not all([self.is_empty_string(constant) for constant in CONST]):
            existConst = STR_ARROW
            is_first_iteration = True
            for i in range(0,len(CONST)):
                if CONST[i] != '':
                    if is_first_iteration:
                        existConst += NEWVAR[i] + " = " + str(CONST[i])
                        is_first_iteration = False
                    else:
                        existConst += STR_AND + NEWVAR[i] + " = " + str(CONST[i])
        else:
            existConst = ""

        return existVar, existNewVar, existConst

    def perform_first_order_rewrite(self, atom_list, not_free):

        if len(atom_list) == 0:
            return "true"
        else:
            VAR = []
            NEWVAR = []
            F = atom_list[0]
            CONST = [''] * len(F.non_key)

            for key in F.key:
                if key in self.all_variable_in_query and key not in not_free:
                    VAR.append(key)
                    not_free.append(key)

            for nonKey in F.non_key:
                if nonKey in self.all_variable_in_query and nonKey not in not_free:
                    VAR.append(nonKey)
                    NEWVAR.append(nonKey)
                    not_free.append(nonKey)

                elif nonKey in self.all_constant_in_query:
                    NEWVAR.append("c" + str(self.idx_constant))
                    i = F.non_key.index(nonKey)
                    CONST[i] = nonKey
                    self.idx_constant += 1

        existVar, existNewVar, existConst = self.formatting_all_elements(VAR, NEWVAR, CONST)

        del atom_list[0]

        toContinue = self.perform_first_order_rewrite(atom_list, not_free)

        if toContinue != "true" and existConst:
            toContinue = STR_AND + toContinue
        elif toContinue != "true" and existConst != "":
            toContinue = STR_ARROW + toContinue
        elif toContinue == "true" and existConst != "":
            toContinue = STR_AND + toContinue
        else :
            toContinue = STR_ARROW + toContinue

        return existVar + " (" + F.relation_name + "(" + ",".join(F.key) + "," + ",".join(
            F.non_key) + ") " + STR_AND + " (" + existNewVar + " (" + F.relation_name + "(" + ",".join(
            F.key) + "," + ",".join(
            NEWVAR) + ") " + existConst + toContinue + ")))"

