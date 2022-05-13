import os
import sys
import wget
from ufal.udpipe import Model, Pipeline

def process(pipeline, text):
    entities = {'PROPN'}
    named = False #variable for remembering that we have encountered a proper name
    memory = []
    mem_case = None
    mem_number = None
    tagged_propn = []
    # process the text, get the result in the pipeline - conllu format
    processed = pipeline.process(text)
    # skip lines with service information:
    content = [l for l in processed.split('\n') if not l.startswith('#')]
    # extract lemmas, tags and morphological characteristics from the processed text
    tagged = [w.split('\t') for w in content if w]
    for t in tagged:
    if len(t) != 10: # if the list is short - the line does not contain
parsing, skip
continue
(word_id, token, lemma, pos, xpos, feats, head, deprel, deps, misc) = t
if not lemma or not token: # if the word is empty - skip
continue
if pos in entities: # separately process your own names
if '|' not in feats:
tagged_propn.append('%s_%s' % (lemma, pos))
continue
morph = {el.split('=')[0]: el.split('=')[1] for el in
feats.split('|')}
if 'Case' not in morph or 'Number' not in morph:
tagged_propn.append('%s_%s' % (lemma, pos))
continue
if not named:
 named = True
 mem_case = morph['Case']
 mem_number = morph['Number']
 if morph['Case'] == mem_case and morph['Number'] == mem_number:
 memory.append(lemma)
 if 'SpacesAfter=\\n' in misc or 'SpacesAfter=\s\\n' in misc:
 named = False
 past_lemma = '::'.join(memory)
memory = []
tagged_propn.append(past_lemma + '_PROPN ')
else:
named = False
past_lemma = '::'.join(memory)
memory = []
tagged_propn.append(past_lemma + '_PROPN ')
tagged_propn.append('%s_%s' % (lemma, pos))
else:
if not named:
if pos == 'NUM' and token.isdigit(): # Replace the numbers
with xxxxx of the same length
lemma = "0" * len(lemma)
