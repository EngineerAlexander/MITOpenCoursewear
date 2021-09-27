# DEMORGAN'S LAW FROM STATS
# NOT(P OR Q) = NOT(P) AND NOT(Q)

# proof by truth tables like this
for p,q in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    rhs = not(p) and not(q)
    lhs = not(p or q)
    print('For p, q = ', p, ', ', q, ': lhs, rhs = ', lhs, ', ', rhs)
    
