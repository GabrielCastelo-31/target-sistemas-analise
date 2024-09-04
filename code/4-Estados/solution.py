sp, rj, mg, es, outros = 6783643, 3667866, 2922988, 2716548, 1984953
total = sp + rj + mg + es + outros

sp_p = sp / total * 100
rj_p = rj / total * 100
mg_p = mg / total * 100
es_p = es / total * 100
outros_p = outros / total * 100
print(f'São Paulo: {sp_p:.2f}%')
print(f'Rio de Janeiro: {rj_p:.2f}%')
print(f'Minas Gerais: {mg_p:.2f}%')
print(f'Espírito Santo: {es_p:.2f}%')
print(f'Outros: {outros_p:.2f}%')

