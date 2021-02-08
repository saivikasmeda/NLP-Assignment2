
import nltk
from nltk.parse.stanford import StanfordParser

def traverse_phrase(tree):
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            traverse_phrase(subtree)
        else:
            print( "constituent : " + subtree )


def traverse_tree(tree):
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            if subtree.label() == 'NP':
                print("\n[Noun Phrase]")
                traverse_phrase(subtree)
            else :
                traverse_tree(subtree)


stanford_parser_dir = '/Users/student/Desktop/UTD_Courses/2 Sem/NLP -CS6320/SXM190011_HW2/stanford-parser-full-2018-10-17/' # change it to your own path
path_to_models = stanford_parser_dir  + "stanford-parser-3.9.2-models.jar"
path_to_jar = stanford_parser_dir  + "stanford-parser.jar"

sentences = ["Sales of the company to return to normalcy.","The new products and services contributed to increase revenue.","Dow falls as recession indicator flashed red and economical worries continue through the month.","Figure skater lands historic quadruple jump in senior international competition at the 2019 World Figure Skating Championships on Day 3 but could only clinch a silver medal."]
for index in range(len(sentences)):
    sentence = sentences[index]
    parser=StanfordParser(path_to_models, path_to_jar)
    parsed_sentence = parser.raw_parse(sentence)
    tree = parsed_sentence.__next__()
    print( tree )
    tree.draw()
