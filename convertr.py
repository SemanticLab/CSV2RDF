import csv, re
from rdflib.graph import Graph, URIRef, Literal
import rdflib

name_id_dict_list = []
link_finder = re.compile('[^,]+')

date_of_birth = URIRef("http://dbpedia.org/ontology/birthDate")
instrument = URIRef("http://dbpedia.org/ontology/instrument")

parent_of = URIRef("http://vocab.org/relationship/#parentOf")
mother_of = URIRef("http://dbpedia.org/ontology/mother")
father_of = URIRef("http://dbpedia.org/ontology/father")
child_of = URIRef("http://vocab.org/relationship/childOf")
daughter_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.1.1")
son_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.1.2")
sibling_of = URIRef("http://vocab.org/relationship/siblingOf")
sister_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#5.1")
brother_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#5.2")
spouse_of = URIRef("http://vocab.org/relationship/spouseOf")
wife_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#13.1.2")
husband_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#13.2.2")
aunt_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#8")
uncle_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#9")
neice_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#10")
nephew_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#11")
grandparent_of = URIRef("http://vocab.org/relationship/grandparentOf")
grandmother_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#1.2.1")
grandfather_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#1.2.2")
grandchild_of = URIRef("http://vocab.org/relationship/grandchildOf")
granddaughter_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.2.1")
grandson_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.2.2")






with open("Batiste Information Resources - Genealogy Data.csv") as f:
    g = Graph()
    file = csv.DictReader(f)

    for row in file:
        id = ""
        label = ""
        father_lbl = ""
        father_id = ""
        mother_lbl = ""
        mother_id = ""
        sibling_lbl = ""
        sibling_id = ""
        child_lbl = ""
        child_id  = ""
        adopted_child_lbl = ""
        adopted_child_id = ""
        spouse_lbl = ""
        spouse_id = ""

        id = URIRef(row['Personal Identifier 1'])
        label = Literal(row['Family Member First Name'] + " " + row['Family Member Last Name'])
        father_lbl = Literal(row['Father'])
        father_id = URIRef(row['Father ID'])
        mother_lbl = Literal(row['Mother'])
        mother_id = URIRef(row['Mother ID'])
        sibling_lbl = Literal(row['Sibling'])
        sibling_id = URIRef(row['Sibling ID'])
        child_lbl = Literal(row['Child'])
        child_id = URIRef(row['Child ID'])
        adopted_child_lbl = Literal(row['Adopted Child'])
        adopted_child_id = URIRef(row['Adopted Child ID'])
        spouse_lbl = Literal(row['Spouse'])
        spouse_id = URIRef(row['Spouse ID'])
        # if id != "":
        #     print(label)
        #     print(id)
        #     print("\n")
        if id != "":
            if father_id != "":
                g.add((id, son_of, father_id))
            elif father_id == "":
                g.add((id, son_of, father_lbl))
    print(g.serialize(format='turtle'))















        #     id = re.findall(link_finder, ids)
        #     id = id[0]
        #     print(name)
        #     print(id)
        #     name_id_dict = {
        #     'name': name,
        #     'id': id}
        #     name_id_dict_list.append(name_id_dict)
        #     # print(name_id_dict)
    # print(name_id_dict_list)
    # # print(len(name_id_dict_list))

    # for row in file:
    #     name = row['Family Member First Name'] + " " + row['Family Member Last Name']
    #
