#Copyright 2010 Brian E. Chapman
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
"""
This module contains three class definitions that are used in the pyConText
algorithm. The pyConText algorithm relies on regular expressions to identify
sub-texts of interest

1) termObject: a class that describes terms of interest within the text 
2) tagObject: a class inherited from termObject that describes modifiers
3) pyConText: a class that implements the context algorithm 

"""
import re
import copy
import networkx as nx
        
class tagObject(object):
    """
    A class that describes terms of interest in the text.
    tagObject is characterized by the following attributes
    1) The contextItem defining the tag
    3) The location of the tag within the text being parsed

    """
    def __init__(self, item, ConTextCategory,scope=None, **kwargs):
        """
        item: contextItem used to generate term
        ConTextCategory: category this term is being used for in pyConText
        
        variants
        """
        self.__item = item
        self.__spanStart = 0
        self.__spanEnd = 0
        self.__ConTextCategory = ConTextCategory
        if( scope == None ):
            self.__scope = []
        else:
            self.__scope = list(scope)
        self.__SCOPEUPDATED = False
    def setScope(self):
        """
        applies the objects own rule and span to modify the object's scope
        Currently only "forward" and "backward" rules are implemented
        """
        
        if( 'forward' in self.__item.getRule().lower() ):
            self.__scope[0] = self.getSpan()[1]
        elif( 'backward' in self.__item.getRule().lower() ):
            self.__scope[1] = self.getSpan()[0]
            
    def parseRule(self):
        """parse the rule for the associated"""
        pass
    def getScope(self):
        return self.__scope
    def getRule(self):
        return self.__item.getRule()
 
    def limitScope(self,obj):
        """If self and obj are of the same category or if obj has a rule of
        'terminate', use the span of obj to
        update the scope of self"""
        if( not self.getRule() or self.getRule()== 'terminate' or 
             (self.getCategory() != obj.getCategory() and obj.getRule() != 'terminate')):
            return
        if( 'forward' in self.getRule().lower() ):
            if( obj > self ):
                self.__scope[1] = min(self.__scope[1],obj.getSpan()[0])
        elif( 'backward' in self.getRule().lower() ):
            if( obj < self ):
                self.__scope[0] = max(self.__scope[0],obj.getSpan()[1])

    def applyRule(self,term):
        """applies self's rule to term. If the start of term lines within
        the span of self, then term may be modified by self"""
        if( not self.getRule() or self.getRule() == 'terminate'):
            return False
        if(self.__scope[0] <= term.getSpan()[0] <= self.__scope[1]):
            return True #term.updateModifiedBy(self)
    def getConTextCategory(self):
        return self.__ConTextCategory
    def getBriefDescription(self):
        return """(%d,%d): %s (%s) <<%s>>"""%(self.getSpan()[0],self.getSpan()[1],
                                              self.getLiteral(),self.getPhrase(),
                                              self.getCategory())
    def getLiteral(self):
        """returns the term defining this object"""
        return self.__item.getLiteral()
    def getCategory(self):
        """returns the category (e.g. CONJUNCTION) for this object"""
        return self.__item.getCategory()

    def setSpan(self,span):
        """set the span within the associated text for this object"""
        self.__spanStart = span[0]
        self.__spanEnd = span[1]
    def getSpan(self):
        """return the span within the associated text for this object"""
        return self.__spanStart,self.__spanEnd
    def setPhrase(self,phrase):
        """set the actual matched phrase used to generate this object"""
        self.__foundPhrase = phrase
    def getPhrase(self):
        """return the actual matched phrase used to generate this object"""
        return self.__foundPhrase
        
    def dist(self,obj):
        """returns the minimum distance from the current object and obj.
        Distance is measured as current start to object end or current end to object start"""
        return min(abs(self.__spanEnd-obj.__spanStart),abs(self.__spanStart-obj.__spanEnd))
                    
    def __lt__(self,other): return self.__spanStart < other.__spanStart
    def __le__(self,other): return self.__spanStart <= other.__spanStart
    def __eq__(self,other): 
        return (self.__spanStart == other.__spanStart and 
                self.__spanEnd == other.__spanEnd)
    def __ne__(self,other): return self.__spanStart != other.__spanStart
    def __gt__(self,other): return self.__spanStart > other.__spanStart
    def __ge__(self,other): return self.__spanStart >= other.__spanStart
    def encompasses(self,other):
        """tests whether other is completely encompassed with the current object"""
        if( self.__spanStart <= other.__spanStart and 
            self.__spanEnd >= other.__spanEnd ):
            return True
        else:
             return False
    def __str__(self):
        txt = self.getBriefDescription()
        return txt
    def __rpr__(self):
        return self.getBriefDescription()
class pyConText(object):
    """
    base class for context.
    build around markedTargets a list of termObjects representing desired terms
    found in text and markedModifiers, tagObjects found in the text
    """
    # regular expressions for cleaning text
    r1 = re.compile(r"""\W""")
    r2 = re.compile(r"""\s+""")
    r3 = re.compile(r"""\d""")
    # regular expression for identifying word boundaries (used for more
    # complex rule specifications
    rb = re.compile(r"""\b""")
    def __init__(self,txt=''):
        """txt is the string to parse"""
        # __archive is for multisentence text processing. A markup is done
        # for each sentence and then put in the archives when the next sentence
        # is processed
        self.__archive = {}
        self.__currentSentence = 0
        self.__rawTxt = txt
        self.__txt = None
        self.__graph = nx.DiGraph()
        self.__scope = None
        self.__SCOPEUPDATED = False
        self.__documentGraph = nx.DiGraph()

        # regular expressions for finding text
        self.res = {}


    def reset(self):
        """deletes all archived values and sets all class attributes to empty or
        zero values
        """
        self.__archive = {}
        self.__graph = nx.DiGraph()
        self.__scope = None
        self.__SCOPEUPDATED 
        self.__currentSentence = 0
        self.__documentGraph = nx.DiGraph()
    def commit(self):
        """
        takes the values stored in current attributes and copies them to the
        object archive
        """
        # I'm not sure if I want to be using copy here
        self.__archive[self.__currentSentence] = {"rawTxt":self.__rawTxt,
                                                  "txt":self.__txt,
                                                  "graph":self.__graph.copy(),
                                                  "scope":copy.copy(self.__scope),
                                                  "scopeUpdated":self.__SCOPEUPDATED}
        self.__currentSentence += 1
        self.setTxt()
    def setSentence(self,num):
        """
        set the current context to sentence num in the archive
        """
        self.__rawTxt = self.__archive[num]["rawTxt"]
        self.__txt = self.__archive[num]["txt"]
        self.__graph = self.__archive[num]["graph"]
        self.__scope = self.__archive[num]["scope"]
        self.__SCOPEUPDATED = self.__archive[num]["scopeUpdated"]

                                        
    def setTxt(self,txt=''):
        """
        sets the current txt to txt and resets the current attributes to empty
        values, but does not modify the object archive
        """
        self.__rawTxt = txt
        self.__txt = None
        self.__graph = nx.DiGraph(sentence=txt)
        self.__scope = None
        self.__SCOPEUPDATED = False
        
    def getText(self):
        return self.__txt
    def getNumberSentences(self):
        return len(self.__archive)
    def getCurrentSentenceNumber(self):
        return self.__currentSentence

    def getCurrentGraph(self):
        return self.__graph
    def getDocumentGraph(self):
        return self.__documentGraph
    def getCleanTxt(self,stripNumbers=False):
        """Need to rename. applies the regular expression scrubbers to rawTxt"""
        self.__txt = self.r1.sub(" ",self.__rawTxt)
        self.__txt = self.r2.sub(" ",self.__txt)
        if( stripNumbers ):
            self.__txt = self.r3.sub("",self.__txt)
            
        self.__scope= (0,len(self.__txt))
    #def __str__(self):
    #    txt = ''
    #    txt += self.renderMarkedTargets()
    #    for term in self.__markedModifiers:
    #        txt += term.__str__()+"\n"
    #    txt += "-"*60
    #    return txt
    def getConTextModeNodes(self,mode, currentGraph = True ):
        if( currentGraph ):
            nodes = [n[0] for n in self.__graph.nodes(data=True) if n[1]['category'] == mode]
        else:
            nodes = [n[0] for n in self.__documentGraph.nodes(data=True) if n[1]['category'] == mode]
        return nodes
    def updateScopes(self):
        """
        update the scopes of all the marked modifiers in the txt. The scope
        of a modifier is limited by its own span and the and the span of
        modifiers in the same category marked in the text.
        """
        self.__SCOPEUPDATED = True
        # make sure each tag has its own self-limited scope
        modifiers = self.getConTextModeNodes("modifier")
        for modifier in modifiers:
            modifier.setScope()

        # Now limit scope based on the domains of the spans of the other
        # modifier
        for i in range(len(modifiers)-1):
            modifier = modifiers[i]
            for j in range(i+1,len(modifiers)):
                modifier2 = modifiers[j]
                modifier.limitScope(modifier2)
                modifier2.limitScope(modifier)

    def markItems(self,items, mode="target"):
        """tags the sentence for a list of items
        items: a list of contextItems"""
        if( not items ):
            #print "not items"
            return
        for item in items:
            self.__graph.add_nodes_from(self.markItem(item, ConTextMode=mode), category=mode)
            #print "just printed nodes"
        #print "items"
        #print len(items)
        #print mode
        #print "self.__graph.node"
        #print self.__graph.node
                                
    def markItem(self,item, ConTextMode="target", ignoreCase=True ):
        """
        markup the current text with the current item.
        If ignoreCase is True (default), the regular expression is compiled with
        IGNORECASE."""
            
        if( not self.__txt ):
            self.getCleanTxt()

        # See if we have already created a regular expression

        if(not self.res.has_key(item.getLiteral()) ):
            if(not item.getRE()):
                regExp = item.getLiteral()
            else:
                regExp = item.getRE()
            if( ignoreCase ):
                r = re.compile(regExp, re.IGNORECASE)
            else:
                r = re.compile(regExp)
            self.res[item.getLiteral()] = r
        else:
            r = self.res[item.getLiteral()]
        iter = r.finditer(self.__txt)
        terms=[]
        for i in iter:
            tO = tagObject(item,ConTextMode, scope = self.__scope)
            tO.setSpan(i.span())
            tO.setPhrase(i.group())
            terms.append(tO)
        return terms

    def pruneMarks(self):    
        """
        prune Marked objects by deleting any objects that lie within the span of
        another object. Currently modifiers and targets are treated separately
        """
        self.__prune_marks(self.__graph.nodes())
    def dropInactiveModifiers(self):
        mnodes = [ n for n in self.getConTextModeNodes("modifier") if self.__graph.degree(n) == 0]
        self.__graph.remove_nodes_from(mnodes)
    def pruneModifierRelationships(self):
        """Initially modifiers may be applied to multiple targets. This function
        computes the text difference between the modifier and each modified
        target and keeps only the minimum distance relationship"""
        modifiers = self.getConTextModeNodes("modifier")
        for m in modifiers:
            modifiedBy = self.__graph.successors(m)
            if( modifiedBy and len(modifiedBy) > 1 ):
                minm = min([ (m.dist(mb),mb) for mb in modifiedBy ])
                edgs = self.__graph.edges(m)
                edgs.remove((m,minm[1]))
                self.__graph.remove_edges_from(edgs)
        
    def __prune_marks(self, marks):
        if( len(marks) < 2 ):
            return
        # this can surely be done faster
        marks.sort()
        nodesToRemove = []
        for i in range(len(marks)-1):
            t1 = marks[i]
            if( t1 not in nodesToRemove ):
                for j in range(i+1,len(marks)):
                    t2 = marks[j]
                    if( t1.encompasses(t2) ):
                        nodesToRemove.append(t2)
                    elif( t2.encompasses(t1) ):
                        nodesToRemove.append(t1)
                        break
        self.__graph.remove_nodes_from(nodesToRemove)
        
    def dropMarks(self,category="exclusion"):
        """Drop any targets that have the category equal to category"""
        dnodes = [n for n in self.__graph.nodes() if n.getCategory().lower() == category.lower()]
        self.__graph.remove_nodes_from(dnodes)           

    def applyModifiers(self):
        """
        If the scope has not yet been updated, do this first.
        
        Loop through the marked targets and for each target apply the modifiers
        """
        if( not self.__SCOPEUPDATED ):
            self.updateScopes()
        targets = self.getConTextModeNodes("target")
        modifiers = self.getConTextModeNodes("modifier")
        for target in targets:
            for modifier in modifiers:
                if( modifier.applyRule(target) ):
                    self.__graph.add_edge(modifier, target)
    def getMarkedTargets(self):
        """
        Return the list of marked targets in the current sentence
        """
        return self.getConTextModeNodes("target")
    def getNumMarkedTargets(self):
        """
        Return the number of marked targets in the current sentence
        """
        return len(self.getConTextModeNodes("target"))
           
    def getModifiers(self, node, currentGraph = True):
        if( currentGraph ):
            return self.__graph.predecessors(node)
        else:
            return self.__documentGraph.predecessors(node)
    def isModifiedBy(self,node, modFilter, currentGraph = True):
        """tests whether self is modified by term. Return modifier if true"""
        pred = self.getModifiers(node, currentGraph)
        for p in pred:
            if( modFilter.lower() == p.getCategory().lower() ):
                return p
                 
        return None

    def computeDocumentGraph(self):
        self.__documentGraph = nx.DiGraph()
        ic = 0
        for key in self.__archive.keys():
            g = self.__archive[key]["graph"]
            self.__documentGraph = nx.union(g,self.__documentGraph)
            # this should work but doesn't preseve the node data attributes
            #nds = g.nodes(data=True) # for python < 2.6 need to use code below
            #for n in nds:
            #    self.__documentGraph.add_node(n[0],category=n[1]['category'])
            #
            #self.__documentGraph.add_edges_from(g.edges())

    
