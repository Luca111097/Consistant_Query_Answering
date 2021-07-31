from FunctionalDependency import *
from Atom import *
from AttackGraph import *
from FirstOrderRewrite import *

#######################################################
#                     Parameters                      #
#######################################################
all_variable_in_query = []
all_constant_in_query = []
all_atom_in_query = []
atom_list = []
functional_dependency_list = []
free = []
atom = None


#######################################################
#                     Functions                       #
#######################################################

# Build functional dependency and put them in a list
def build_functional_dependency_list():
    for atom in atom_list:
        functional_dependency_list.append(FunctionalDependency(atom.key, atom.non_key))


def find_information_and_name(chain):
    idx_open_paranthesis = 0
    idx_close_paranthesis = -1
    for i in range(len(chain)):
        if chain[i] == '(':
            idx_open_paranthesis = i
        elif chain[i] == ')':
            idx_close_paranthesis = i
            break

    return chain[:idx_open_paranthesis].strip(' '), chain[
                                                    idx_open_paranthesis + 1:idx_close_paranthesis].strip(' ')


def extract_brackets(chain):
    for i in range(len(chain)):
        idx_open_bracket = 0
        idx_close_bracket = -1
        for i in range(len(chain)):
            if chain[i] == '[':
                idx_open_bracket = i
            elif chain[i] == ']':
                idx_close_bracket = i
                break

        return chain[idx_open_bracket + 1:idx_close_bracket].strip(' '), chain[idx_close_bracket + 2:].strip(
            ' ')


def find_keys_and_constants(chain, key):
    elements = chain.split(',')
    elements = [element.strip(' ') for element in elements]
    for element in elements:
        if '\'' in element:
            constant = element.strip('\'')
            key.append(constant)
            if constant not in all_constant_in_query:
                all_constant_in_query.append(constant)
        else:
            key.append(element)
            if element not in all_variable_in_query:
                all_variable_in_query.append(element)


#######################################################
#                  Input treatment                    #
#######################################################
query = input("Enter your query : ")
all_atom_in_query = query.split(";")

for atom_chain in all_atom_in_query:
    keys = []
    non_keys = []

    relation_name, info = find_information_and_name(atom_chain)
    key_chain, non_key_chain = extract_brackets(info)
    find_keys_and_constants(key_chain, keys)
    find_keys_and_constants(non_key_chain, non_keys)

    atom_list.append(Atom(relation_name, keys, non_keys))

#######################################################
#                  Initialization                     #
#######################################################
build_functional_dependency_list()
attackGraph = AttackGraph(all_constant_in_query)
forewritter = FirstOrderRewrite(all_constant_in_query, all_variable_in_query)

#######################################################
#                  Attack Graph                       #
#######################################################
attackGraph.initialize(atom_list, all_variable_in_query)
attackGraph.realize_attack_graph(atom_list, functional_dependency_list)

#######################################################
#                 First Order Rewrite                 #
#######################################################
if attackGraph.are_there_any_attack and attackGraph.is_first_order_expressible:
    print("Tableau des attaques : " + str(attackGraph.attack))
    rewrite = forewritter.perform_first_order_rewrite(atom_list, free)
    print("Réécriture : " + rewrite)

