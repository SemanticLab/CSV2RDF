import csv, re, json
from rdflib.graph import Graph, URIRef, Literal
import rdflib

name_id_dict_list = []
link_finder = re.compile('[^,]+')

date_of_birth_is = URIRef("http://schema.org/birthDate")
date_of_death_is = URIRef("http://schema.org/deathDate")
instrument_is = URIRef("http://purl.org/ontology/mo/primary_instrument")

parent_of = URIRef("http://purl.org/vocab/relationship/parentOf")
mother_of = URIRef("http://dbpedia.org/ontology/mother")
father_of = URIRef("http://dbpedia.org/ontology/father")
child_of = URIRef("http://purl.org/vocab/relationship/childOf")
adopted_son_of = URIRef("http://cedric.cnam.fr/isid/ontologies/PersonLink.owl#3.1.2.1")
daughter_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.1.1")
son_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.1.2")
sibling_of = URIRef("http://purl.org/vocab/relationship/siblingOf")
sister_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#5.1")
brother_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#5.2")
spouse_of = URIRef("http://purl.org/vocab/relationship/spouseOf")
wife_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#13.1.2")
husband_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#13.2.2")
aunt_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#8")
uncle_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#9")
neice_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#10")
nephew_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#11")
grandparent_of = URIRef("http://purl.org/vocab/relationship/grandparentOf")
grandmother_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#1.2.1")
grandfather_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#1.2.2")
grandchild_of = URIRef("http://purl.org/vocab/relationship/grandchildOf")
granddaughter_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.2.1")
grandson_of = URIRef("http://cedric.cnam.fr/isid/ontologies/files/PersonLink.html#3.2.2")

performer_is = URIRef("http://purl.org/ontology/mo/performer")
composer_is = URIRef("http://purl.org/ontology/mo/composer")





with open("Batiste Information Resources - Genealogy Data.csv") as f:
    g = Graph()
    file = csv.DictReader(f)

    for row in file:
        identifier = ""
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
        instrument = ""
        birthdate = ""
        deathdate = ""

        identifier = row['Personal Identifier 1']
        label = row['Family Member First Name'] + " " + row['Family Member Last Name']
        father_lbl = row['Father']
        father_id = row['Father ID']
        mother_lbl = row['Mother']
        mother_id = row['Mother ID']
        sibling_lbl = row['Sibling']
        sibling_id = row['Sibling ID']
        child_lbl = row['Child']
        child_id = row['Child ID']
        adopted_child_lbl = row['Adopted Child']
        adopted_child_id = row['Adopted Child ID']
        spouse_lbl = row['Spouse']
        spouse_id = row['Spouse ID']
        instrument = row['Instrument']
        birthdate = row['Date of Birth']
        deathdate = row['Date of Death']

        # if identifier != "":
        #     print(label)
        #     print(id)
        #     print("\n")
        # print(father_id)
        # print(father_lbl)

        if identifier != "":
            identifier = URIRef(row['Personal Identifier 1'])

            if father_id != "":
                father_id = URIRef(father_id)
                g.add((identifier, child_of, father_id))

            elif father_id == "":
                if father_lbl != "":
                    g.add((identifier, child_of, Literal(father_lbl)))

            if mother_id != "":
                mother_id = URIRef(mother_id)
                g.add((identifier, child_of, mother_id))

            elif mother_id == "":
                if mother_lbl != "":
                    g.add((identifier, child_of, Literal(mother_lbl)))

            if sibling_id != "":
                sibling_id = URIRef(sibling_id)
                g.add((identifier, sibling_of, sibling_id))

            elif sibling_id == "":
                if sibling_lbl != "":
                    g.add((identifier, sibling_of, Literal(sibling_lbl)))

            if child_id != "":
                child_id = URIRef(child_id)
                g.add((identifier, parent_of, child_id))

            elif child_id == "":
                if child_lbl != "":
                    g.add((identifier, parent_of, Literal(child_lbl)))

            if adopted_child_id != "":
                adopted_child_id = URIRef(adopted_child_id)
                g.add((identifier, parent_of, adopted_child_id))
                g.add((adopted_child_id, adopted_son_of, identifier))

            elif adopted_child_id == "":
                if adopted_child_lbl != "":
                    g.add((identifier, parent_of, Literal(adopted_child_lbl)))
                    g.add((Literal(adopted_child_id), adopted_son_of, identifier))

            if spouse_id != "":
                spouse_id = URIRef(spouse_id)
                g.add((identifier, spouse_of, spouse_id))

            elif spouse_id == "":
                if spouse_lbl != "":
                    g.add((identifier, spouse_of, Literal(spouse_lbl)))

            if instrument != "":
                instrument = Literal(instrument)
                g.add((identifier, instrument_is, instrument))

            if birthdate != "":
                birthdate = Literal(birthdate)
                g.add((identifier, date_of_birth_is, birthdate))

            if deathdate != "":
                deathdate = Literal(deathdate)
                g.add((identifier, date_of_death_is, deathdate))


        elif identifier == "":
            label = Literal(label)

            if father_id != "":
                father_id = URIRef(father_id)
                g.add((label, child_of, father_id))

            elif father_id == "":
                if father_lbl != "":
                    g.add((label, child_of, Literal(father_lbl)))

            if mother_id != "":
                mother_id = URIRef(mother_id)
                g.add((label, child_of, mother_id))

            elif mother_id == "":
                if mother_lbl != "":
                    g.add((label, child_of, Literal(mother_lbl)))

            if sibling_id != "":
                sibling_id = URIRef(sibling_id)
                g.add((label, sibling_of, sibling_id))

            elif sibling_id == "":
                if sibling_lbl != "":
                    g.add((label, sibling_of, Literal(sibling_lbl)))

            if child_id != "":
                child_id = URIRef(child_id)
                g.add((label, parent_of, child_id))

            elif child_id == "":
                if child_lbl != "":
                    g.add((label, parent_of, Literal(child_lbl)))

            if adopted_child_id != "":
                adopted_child_id = URIRef(adopted_child_id)
                g.add((label, parent_of, adopted_child_id))
                g.add((adopted_child_id, adopted_son_of, label))

            elif adopted_child_id == "":
                if adopted_child_lbl != "":
                    g.add((label, parent_of, Literal(adopted_child_lbl)))
                    g.add((Literal(adopted_child_id), adopted_son_of, label))

            if spouse_id != "":
                spouse_id = URIRef(spouse_id)
                g.add((label, spouse_of, spouse_id))

            elif spouse_id == "":
                if spouse_lbl != "":
                    g.add((label, spouse_of, Literal(spouse_lbl)))

            if instrument != "":
                instrument = Literal(instrument)
                g.add((label, instrument_is, instrument))

            if birthdate != "":
                birthdate = Literal(birthdate)
                g.add((label, date_of_birth_is, birthdate))

            if deathdate != "":
                deathdate = Literal(deathdate)
                g.add((label, date_of_death_is, deathdate))




            # if mother_id != "":
            #     g.add((identifier, son_of, mother_id))
            # elif mother_id == "":
            #     g.add((identifier, son_of, mother_lbl))
            #
            # if sibling_id != "":
            #     g.add((identifier, sibling_of, sibling_id))
            # elif sibling_id == "":
            #     g.add((identifier, sibling_of, sibling_lbl))
            #
            # if child_id != "":
            #     g.add((identifier, parent_of, child_id))
            # elif child_id == "":
            #     g.add((identifier, parent_of, child_lbl))
            #
            # if adopted_child_id != "":
            #     g.add((identifier, parent_of, adopted_child_id))
            # elif adopted_child_id == "":
            #     g.add((identifier, parent_of, adopted_child_lbl))
            #
            # if spouse_id != "":
            #     g.add((identifier, spouse_of, spouse_id))
            # elif spouse_id == "":
            #     g.add((identifier, spouse_of, spouse_lbl))
            #
            #
            #
            #
            #


g.serialize("test.rdf", format="turtle")
















        #     identifier = re.findall(link_finder, ids)
        #     identifier = id[0]
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
