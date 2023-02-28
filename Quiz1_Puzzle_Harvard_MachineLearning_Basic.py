#!/usr/bin/env python
# coding: utf-8

# In[85]:


from logic import *


# In[86]:


AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")


# In[87]:


BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")


# In[88]:


CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# In[89]:


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Not(And(AKnight, AKnave)),  # A cannot be both a knight and a knave
    Implication(And(AKnight, AKnave), AKnave),  # If A is both a knight and a knave, then A is a knave
    Implication(Or(AKnight, AKnave), AKnight)  # A is a knight if A's statement is true
)
# Add the information that A's statement says
knowledge0.add(And(AKnight, AKnave))


# In[90]:


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),
    Implication(And(AKnight, AKnave), AKnave),  
    Implication(Or(AKnight, AKnave), AKnight),
    Implication(And(BKnight, BKnave), BKnave),  
    Implication(Or(BKnight, BKnave), BKnight)
)
knowledge1.add(And(AKnave, BKnave))


# In[91]:


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),
    Implication(And(AKnight, AKnave), AKnave), 
    Implication(Or(AKnight, AKnave), AKnight),
    Implication(And(BKnight, BKnave), BKnave),  
    Implication(Or(BKnight, BKnave), BKnight)
)
knowledge2.add(Or(And(AKnight,BKnight), And(AKnave, BKnave)))
knowledge2.add(Or(And(AKnight,BKnave), And(AKnave, BKnight)))      


# In[92]:


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(And(AKnight, AKnave), AKnave),  
    Implication(Or(AKnight, AKnave), AKnight),
    Implication(And(BKnight, BKnave), BKnave),  
    Implication(Or(BKnight, BKnave), BKnight),
    Implication(And(CKnight, BKnave), CKnave),  
    Implication(Or(CKnight, CKnave), CKnight)
)
knowledge3.add(Or(AKnight, AKnave))
knowledge3.add(AKnave)
knowledge3.add(CKnave)
knowledge3.add(AKnight)


# In[93]:


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




