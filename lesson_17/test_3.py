# Найти элементы, принадлежащие множеству E: ∩ ∪ 
# E = ( (A\B) ∩ (C\D) ∪ (D\A) ∩ (B\C) )


A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')

M1 = (A.difference(B))
M2 = (C.difference(D))
M3 = (D.difference(A))
M4 = (B.difference(C)) 

T1 = M1.intersection(M2)
T2 = M3.intersection(M4)

E = T1.update(T2)

print('M1={0}, M2={1}, M3={2}, M4={3}, T1={4}, T2={5}, E={6}'.format(M1, M2, M3, M4, T1, T2, E))