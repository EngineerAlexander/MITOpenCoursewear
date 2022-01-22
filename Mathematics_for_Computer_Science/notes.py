# MODUS PONENS RULE
# (P, P IMPLIES Q)/Q where numerator is antecedents and denomenator is conclusion

# DEMORGAN'S LAW LIKE FROM STATS
# NOT(P AND Q) = NOT(P) OR NOT(Q)
# NOT(P OR Q) = NOT(P) AND NOT(Q)

# proof by truth tables like this
# size doubles with each additional variable so exponential growth
# useless for larger problems (too big too quick in circuits)
for p,q in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    rhs = not(p) and not(q)
    lhs = not(p or q)
    print('For p, q = ', p, ', ', q, ': lhs, rhs = ', lhs, ', ', rhs)

# P IMPLIES Q is False IFF p IS True and Q is False

# DISTRIBUTIVE LAW
# P AND (Q OR R) = (P AND Q) OR (P AND R)

# LUKASIEWICZ' PROOF SYSTEM
# Prove formulas by starting with axioms and then repeatedly applying the inference rule.