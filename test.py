import os
#import pyConText.pyConTextGraph.pyConTextGraph as pyConText
import pyConText.helpers as helpers
from critfindingItemData import *
import pyConTextGraph_update as pyConText
from itemData_update import *
import string
#import csv
import re

def classifyDocumentTargets(context, allow_uncertainty=False):
        """
        negation_status (negated, affirmed, possible)
        temporality (historical, recent, hypothetical)
        experiencer (patient, other)
        """
        rslts = {}
        alerts = {}
        cntxt = context
        cntxt.computeDocumentGraph()
        g = cntxt.getDocumentGraph()
        targets = [n[0] for n in g.nodes(data = True) if n[1].get("category","") == 'target']
        
        if( not targets ):
            return alerts,rslts
        if(allow_uncertainty):
            pos_filters = ["definite_existence","probable_existence"]#["PROBABLE_NEGATED_EXISTENCE","DEFINITE_NEGATED_EXISTENCE"]#
        else:
            pos_filters = ["definite_existence"]
        for t in targets:
            mods = g.predecessors(t)
            tL = t.getLiteral()
            rslts[tL] = {}
            if( not mods ): # an unmodified target is disease positive,certain, and acute               
                rslts[tL]['disease'] = 'Pos'
                rslts[tL]['uncertainty'] = 'No'
                rslts[tL]['temporality'] = 'New'
                rslts[tL]['experiencer'] = 'Patient'
            else:
                if ((modifies(g,t,pos_filters) and not modifies(g,t,["future","indication","pseudoneg"]))):
                    rslts[tL]['disease'] = 'Pos'
                elif(modifies(g,t,["probables",
                                  "probableNegations"]) ):
                    rslts[tL]['disease'] = 'Probable'
                else:
                    rslts[tL]['disease'] = 'Neg'
                if( modifies(g,t,["probable_existence",
                                  "probable_negated_existence"]) ):
                    rslts[tL]['uncertainty'] = 'Yes'
                else:
                    rslts[tL]['uncertainty'] = 'No'
                if (modifies(g,t,["historical"]) ):
                    rslts[tL]['temporality'] = 'Old'
                elif(modifies(g,t,["hypothetical"])):
                    if rslts[tL]['disease']=='Neg':
                        rslts[tL]['temporality'] = 'Hypothetical'
                    else: ## disease == pos or probable
                        rslts[tL]['temporality'] = 'New' ## not sure if this is correct
                else:
                    if (rslts[tL]['disease'] == 'Neg'):
                        rslts[tL]['temporality'] = 'NA'
                    else:
                        rslts[tL]['temporality'] = 'New'
                        
                if ((modifies(g,t,["experiencers"])) and not (modifies(g,t,["pseudoexperiencers"]))):
                    rslts[tL]['experiencer'] = 'Other'
                else:
                    rslts[tL]['experiencer'] = 'Patient'
            rsum = alerts.get(t.getCategory(),0)
            if( rslts[tL]["disease"] == 'Pos' and rslts[tL]["temporality"] == 'New'):
                alert = 1
            else:
                alert = 0
            rsum = max(rsum,alert)
            alerts[t.getCategory()] = rsum
            

        return rslts#alerts, 

def modifies(g,n,modifiers):
        pred = g.predecessors(n)
        if( not pred ):
                return False
        pcats = [n.getCategory().lower() for n in pred]
        #print "pcats",set(pcats).intersection([m.lower() for m in modifiers])
        return bool(set(pcats).intersection([m.lower() for m in modifiers]))

def main():
        path = os.getcwd()
        fileName = "".join([path,r"\rsAnnotations-1-120-random.txt"])
        f=open(fileName,'r') 
        t=f.readlines()
        f.close()

        sentences = []
        targets = []
        negationStatus = []
        temporalityStatus = []
        experiencerStatus = []
        for line in xrange(1,len(t)):
            contents = t[line].split("\t")
            target = contents[1]
            sentence = contents[2]
            negation = contents[3]
            temporality = contents[4]
            experiencer = contents[5]
            targets.append(target)
            sentences.append(sentence)
            negationStatus.append(negation)
            temporalityStatus.append(temporality)
            experiencerStatus.append(experiencer)

####### build modifier list        
        modifiers = itemData()
        modifiers.prepend(pseudoNegations)
        modifiers.prepend(definiteNegations)
        modifiers.prepend(probableNegations)
        modifiers.prepend(probables)
        modifiers.prepend(definites)
        modifiers.prepend(indications)
        modifiers.prepend(conjugates)
        modifiers.prepend(historicals)
        modifiers.prepend(hypothetical)
        modifiers.prepend(pseudoexperiencers)
        modifiers.prepend(experiencers)
        
####### END modifier list

####### Condition List
        conditions = []
        for target in targets:#[:20]:
            tar = target.split(" ")
            tar = filter(None,tar)
            sLiteral = (" ".join(tar)).lower().translate(string.maketrans("",""), string.punctuation)###### END condition list
            conditions.append(sLiteral)
####### END condition list

####### build target list        
        targetItems= itemData()
        targetDict = {}
        for target in targets:#[:20]:
            tar = target.split(" ")
            tar = filter(None,tar)
            sLiteral = (" ".join(tar)).lower().translate(string.maketrans("",""), string.punctuation)
            sCategory = re.sub(" ","_",sLiteral.upper())
            sRe = sLiteral
            sRule = ""
            s = contextItem([sLiteral,sCategory,sRe,sRule])
            condLen = len(tar)
            if not targetDict.has_key(condLen):
                targetDict[condLen]=itemData()
            targetDict[condLen].append(s)
        for key in targetDict.keys(): #xrange(1,2):#
            targetItems.prepend(targetDict[key])
        print len(targetItems)

####### END targets

        negCount = 0
        tempCount = 0
        ptCount = 0
        #negs = []
        #temps = []
        #exps = []   
        sentenceCount=0
        for s in sentences:
            print sentenceCount,":",s       
            context = pyConText.pyConText(s)
            context.setTxt(s) 
            context.markItems(modifiers, mode="modifier")
            context.markItems(targetItems, mode="target")
            context.pruneMarks()
            context.dropMarks('Exclusion')
            context.applyModifiers()
            context.dropInactiveModifiers()
            context.commit()

            rec = classifyDocumentTargets(context,False)
            #print rec
            #print conditions[sentenceCount]
            if type(rec) == dict and rec.has_key(conditions[sentenceCount]):
                #print rec[conditions[sentenceCount]]
                neg = rec[conditions[sentenceCount]]['disease']
                #print neg
                temp = rec[conditions[sentenceCount]]['temporality']
                #print temp
                experiencer = rec[conditions[sentenceCount]]['experiencer']
                #negs.append(neg)
                #temps.append(temp)
                #exps.append(experiencer)
                if (neg == "Pos" and  negationStatus[sentenceCount]=="Affirmed") or (neg == "Neg" and  negationStatus[sentenceCount]=="Negated") or (neg == "Probable" and  negationStatus[sentenceCount]=="Possible"):
                    negCount+=1
                else: print "other negation status"
                if (temp == "Old" and temporalityStatus[sentenceCount] == "Historical") or (temp == "New" and temporalityStatus[sentenceCount] == "Recent") or (temp == "Hypothetical" and temporalityStatus[sentenceCount] == "Hypothetical"):
                    tempCount+=1
                if (experiencer =='Patient' and experiencerStatus == "Patient") or (experiencer =='Other' and experiencerStatus == "Other"):
                    ptCount+=1
            sentenceCount+=1

        print "neg accuracy:",negCount*1.0/sentenceCount
        print "temp accuracy:",tempCount*1.0/sentenceCount
        print "pt accuracy:", ptCount*1.0/sentenceCount
        
main()
