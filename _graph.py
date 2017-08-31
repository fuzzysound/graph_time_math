from graphviz import Digraph

def Node():
    g= Digraph('g', filename='c:/users/user/desktop/project2/project6.gv',engine='dot')
    g.attr('node',size='7.5' , style='filled', color='goldenrod2')


    g.edge('7th Edition','32V')
    g.edge('7th Edition','V7M')
    g.edge('7th Edition','Xenix')
    g.edge('7th Edition','UniPlus+')
    g.edge('8th Edition','9th Edition')
    g.edge('1 BSD','2 BSD')
    g.edge('2 BSD','2.8 BSD')
    g.edge('2.8 BSD','Ultrix-11')
    g.edge('2.8 BSD','2.9 BSD')
    g.edge('32V','3 BSD')
    g.edge('3 BSD','4 BSD')
    g.edge('4 BSD','4.1 BSD')
    g.edge('4.1 BSD','4.2 BSD')
    g.edge('4.1 BSD','2.8 BSD')
    g.edge('4.1 BSD','8th Edition')
    g.edge('4.2 BSD','4.3 BSD')
    g.edge('4.2 BSD','Ultrix-32')

    g.view()

Node()