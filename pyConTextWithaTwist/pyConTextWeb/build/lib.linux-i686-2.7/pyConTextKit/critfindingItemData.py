from pyConText.pyConTextGraph.itemData import *
probables.dropByLiteral("seen")
probableNegations.dropByLiteral("cannot be excluded")
probableNegations.dropByLiteral("no evidence of")
probableNegations.dropByLiteral("free")
critItems = itemData(
['pulmonary embolism','PULMONARY_EMBOLISM',r'''pulmonary\s(artery )?(embol[a-z]+)''',''], 
['pe','PULMONARY_EMBOLISM',r'''\bpe\b''',''],
['embolism','PULMONARY_EMBOLISM',r'''\b(emboli|embolism|embolus)\b''',''],
['pe examination','EXCLUSION',r'''(pulmonary )(artery )?(embol[a-z]+)(exam[a-z]*|study|protocol)''',''],
['aortic dissection','AORTIC_DISSECTION','',''],
['appendicitis','APPENDICITIS','',''],
['bowel obstruction','BOWEL_OBSTRUCTION','',''],
['retroperitoneal hemorrhage','RETROPERITONEAL_HEMORRHAGE','',''],
['ischemic bowel','ISCHEMIC_BOWEL','',''],
['portal venous air','PORTAL_VENOUS_AIR',r'''portal\bvenous\b(gas|air)''',''],
['ruptured aneurysm','RUPTURED_ANEURYSM',r'''(ruptured aneurysm|aortic rupture)''',''],
['tension pneumothorax','TENSION_PNEUMOTHORAX','',''],
['spinal cord compression','SPINAL_CORD_COMPRESSION','',''],
['cervical fracture','CERVICAL_FRACTURE',r'''(cervical spine fracture|c[1-7]\sfracture)''',''], #changed to cervical spine fracture
['mediastinal emphysema','MEDIASTINAL_EMPHYSEMA','',''],
#['tumor infiltration','MALIGNANCY','',''],
#['malignancy','MALIGNANCY',r'''\bmalignan[a-z]*|cancer[a-z]*|carcinoma|sarcoma''',''],
#['metastatic disease','MALIGNANCY',r'''(metastatic\sdisease|metastasis|metastases)''',''],
#['nonmalignant','EXCLUSION',r'''nonmalignant|non-malignant''',''],
['in the setting of','EXCLUSION','',''],
['embolization','EXCLUSION','',''],
['septic embolism','EXCLUSION',r'''septic\s(emboli|embolus|embolism)''',''],
# New conditions
['carotid dissection','CAROTID_DISSECTION',r'''carotid?\s*?\w*\s*dissection''',''],
['retroperitoneal hemorrhage','RETROPERITONEAL_HEMORRHAGE',r'''(retro|intra)?peritoneal\s(hemorrhage|hematoma)''',''],
['cerebral hemorrhage','CEREBRAL_HEMORRHAGE',r'''(cereblal|intracranial|brain)\s(hemorrhage|hematoma)''',''],
['depressed skull fracture','DEPRESSED_SKULL_FRACTURE','',''],
['DVT','DVT',r'''((non.?)?occlusive)?\s?(thromb[a-z]*|DVT)''',''],
['free air','FREE_AIR','''(pneumoperitoneum|((intraperitoneal|free)\s(gas|air)))''',''],
['cord compression','CORD_COMPRESSION','',''],
['torsion','TORSION','',''],
['volvulus','VOLVULUS','',''],
['infarct','INFARCT','',''],
['ectopic pregnancy','ECTOPIC_PREGNANCY','',''],
['fetal demise','FETAL_DEMISE','',''],
)

future = itemData(
["at risk for","FUTURE",r'''at\srisk\s(in\sthe\sfuture\s)?for''','forward'],
["if clinical concern for","FUTURE",r"""if\sclinical\s(concern|suspicion)\sfor""","forward"],
["if there is concern for","FUTURE","","forward"])

definiteNegations.prepend([["nor","DEFINITE_NEGATED_EXISTENCE","","forward"],])

indications.prepend([["is more sensitive","INDICATION",r"""is more sensitive""","forward"],
                     ["assessment for","INDICATION","","forward"],])
historicals.prepend([["history of","HISTORICAL","","forward"],
                   ["progression of","HISTORICAL",r"""progression\s(of|in)""","forward"],
                   ["old","HISTORICAL","","bidirectional"],
                   ["subacute","HISTORICAL","","bidirectional"],
                   ["redemonstration of","HISTORICAL","","forward"],
                   ["decrease in","HISTORICAL","","forward"],
                   ["persistent","HISTORICAL","","bidirectional"],
                   ["evolving","HISTORICAL","","bidirectional"],
                   ["again","HISTORICAL","","bidirectional"],
                   ["healing","HISTORICAL",r"\b(healing|healed)\b","bidirectional"],])

probableNegations.prepend([["is not excluded",
                          "PROBABLE_NEGATED_EXISTENCE",
                          r"""(is|was|are|were)\snot\s(entirely|totally|completely\s)?excluded""",
                          'backward'],
                         ["low probability","PROBABLE_NEGATED_EXISTENCE","","forward"],
                         ["unable to adequately assess","PROBABLE_NEGATED_EXISTENCE","","forward"],
                         ["unable to assess","PROBABLE_NEGATED_EXISTENCE","","forward"],
                         ["cannot exclude","PROBABLE_NEGATED_EXISTENCE",r"cannot\sexclude","forward"],
                         ["not excluded","PROBABLE_NEGATED_EXISTENCE",r"""not\s(excluded|ruled\sout)""",'backward'],
                         ["cannot be excluded",
                          "PROBABLE_NEGATED_EXISTENCE",
                          r"""cannot\sbe\s((entirely|completely)\s)?(excluded|ruled out)""", #added ? aftercompletely?\s)
                          "backward"],
                         ["no evidence of", # from Amil Negatives #2, 3, 4, 5, 6, 7, 8, 10
                          "PROBABLE_NEGATED_EXISTENCE",
                          r"""(no|without)\s((definite|definitive|secondary|indirect)\s)?((radiographic|sonographic|CT)\s)?(evidence|signs)\s(of|for)""",
                          "forward"],]) #111

probables.prepend([["differential diagnosis would include",
                  "PROBABLE_EXISTENCE",
                  r"differential\s((diagnosis|considerations)\s)?((would|could)\sinclud[a-z]*)?",
                  "forward"],
                 ["concerning for","PROBABLE_EXISTENCE","","forward"],
                 ["is in the differential","PROBABLE_EXISTENCE",r"is\sin\sthe\sdifferential","backward"],
                 ["should be considered","PROBABLE_EXISTENCE","","bidirectional"],])

