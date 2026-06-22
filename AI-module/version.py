def version_space(examples):
    S = examples[0][:-1]
    G = [['?'] * len(S)]
    
    for ex in examples:
        f, l = ex[:-1], ex[-1]
        
        if l == 'Yes':
            S = ['?' if S[i] != f[i] else S[i] for i in range(len(S))]
            G = [g for g in G if all(g[i] in ['?', f[i]] for i in range(len(g)))]
        else:
            G = [g for g in G if not all(g[i] in ['?', f[i]] for i in range(len(g)))]
            for g in G[:]:
                for i in range(len(g)):
                    if g[i] == '?' and f[i] != S[i]:
                        new_g = g.copy()
                        new_g[i] = S[i]
                        if new_g not in G:
                            G.append(new_g)
    
    return S, G

# Test
data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

S, G = version_space(data)
print(f"S: {S}")
print(f"G: {G}")