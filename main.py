print("truth table of logical and")
print("p","q","p^q", sep='\t\t|')
print("-"*22)

for p in {True, False}:
  for q in {True, False}:
    print(p, q, p and q, sep='\t|')
    

print("\n\ntruth table of logical or")
print("p","q","p^q", sep='\t\t|')
print("-"*29)

for p in {True, False}:
  for q in {True, False}:
    print(p, q, p or q, sep='\t|')

print("\n\ntruth table of logical not")
print("p","~p",sep='\t\t|')
print("-"*18)

for p in {True, False}:
    print(p, not p, sep='\t|')

print("\n\ntruth table of implication")
print("p","q","p->q", sep='\t\t|')
print("-"*29)

for p in {True, False}:
  for q in {True, False}:
    print(p, q, not p or q, sep='\t|')

print("\n\ntruth table of biconditional")
print("p","q","p<->q", sep='\t\t|')
print("-"*29)

for p in {True, False}:
  for q in {True, False}:
    print(p, q,  p==q, sep='\t|')
