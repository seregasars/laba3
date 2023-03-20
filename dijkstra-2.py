import math
graph = {
    'Algeria': {'Libya': 989, 'Mali': 1359, 'Mauritania': 463, 'Morocco': 1559, 'Niger': 956, 'Tunisia': 622, 'Western Sahara': 240},
    'Angola': {'Namibia': 1370, 'Zambia': 1112},
    'Benin': {'Burkina Faso': 1267, 'Niger': 1207, 'Nigeria': 676, 'Togo': 205},
    'Botswana': {'Namibia': 824, 'South Africa': 1526, 'Zambia': 977, 'Zimbabwe': 834},
    'Burkina Faso': {'Cote d\'Ivoire': 1005, 'Ghana': 962, 'Mali': 965, 'Niger': 472, 'Togo': 663},
    'Burundi': {'Rwanda': 213},
    'Cabo Verde': {'Senegal': 1256},
    'Cameroon': {'Central African Republic': 1301, 'Chad': 1102, 'Congo': 1142, 'Equatorial Guinea': 684, 'Gabon': 1104, 'Nigeria': 1594},
    'Central African Republic': {'Chad': 1176, 'Congo': 1743, 'South Sudan': 1163, 'Sudan': 1501},
    'Chad': {'Libya': 1400, 'Niger': 1165, 'Nigeria': 1485, 'Sudan': 969},
    'Comoros': {'Madagascar': 875},
    'Congo': {'Gabon': 1079, 'Democratic Republic of the Congo': 1298},
    'Democratic Republic of the Congo': {'Uganda': 765, 'Rwanda': 223, 'Tanzania': 1453, 'Zambia': 2163},
    'Djibouti': {'Eritrea': 126},
    'Egypt': {'Libya': 1115, 'Sudan': 1276},
    'Equatorial Guinea': {'Gabon': 234, 'Cameroon': 684},
    'Eritrea': {'Ethiopia': 982, 'Sudan': 682},
    'Eswatini': {'Mozambique': 1055, 'South Africa': 441},
    'Ethiopia': {'Djibouti': 982, 'Kenya': 867, 'Somalia': 1655, 'South Sudan': 1299, 'Sudan': 1071},
    'Gabon': {'Cameroon': 1104, 'Congo': 1079, 'Equatorial Guinea': 234},
    'Gambia': {'Senegal': 740},
    'Ghana': {'Ivory Coast': 1371, 'Burkina Faso': 962, 'Togo': 546},
    'Guinea': {'Ivory Coast': 1087, 'Liberia': 847, 'Mali': 1013, 'Senegal': 673, 'Sierra Leone': 1172},
    'Guinea-Bissau': {'Senegal': 449, 'Guinea': 386},
    'Kenya': {'Ethiopia': 867, 'Somalia': 682, 'South Sudan': 232, 'Tanzania': 1015, 'Uganda': 812},
    'Lesotho': {'South Africa': 160},
    'Liberia': {'Cote d\'Ivoire': 814, 'Guinea': 847, 'Sierra Leone': 446},
    'Libya': {'Sudan': 1636, 'Tunisia': 1092},
    'Madagascar': {'Mozambique': 595},
    'Malawi': {'Mozambique': 734, 'Tanzania': 475, 'Zambia': 837},
    'Mali': {'Algeria': 1359, 'Burkina Faso': 965, 'Cote d\'Ivoire': 1113, 'Guinea': 1013, 'Mauritania': 1241, 'Niger': 838, 'Senegal': 703},
    'Mauritania': {'Mali': 1241, 'Morocco': 1657, 'Senegal': 661, 'Western Sahara': 469},
    'Mauritius': {},
    'Morocco': {'Algeria': 1559, 'Mauritania': 1657},
    'Mozambique': {'Malawi': 734, 'South Africa': 491, 'Swaziland': 1055, 'Tanzania': 1512, 'Zambia': 1377, 'Zimbabwe': 1230},
    'Namibia': {'Angola': 1370, 'Botswana': 824, 'South Africa': 1447, 'Zambia': 2106},
    'Niger': {'Algeria': 956, 'Benin': 1207, 'Chad': 1165, 'Libya': 1415, 'Mali': 838, 'Nigeria': 1367},
    'Nigeria': {'Benin': 676, 'Cameroon': 1594, 'Chad': 1485, 'Niger': 1367},
    'Rwanda': {'Burundi': 213, 'Democratic Republic of the Congo': 223, 'Tanzania': 217},
    'Sao Tome and Principe': {},
    'Senegal': {'Gambia': 740, 'Guinea': 673, 'Guinea-Bissau': 449, 'Mauritania': 661, 'Mali': 703},
    'Seychelles': {},
    'Sierra Leone': {'Guinea': 1172, 'Liberia': 446},
    'Somalia': {'Djibouti': 180, 'Ethiopia': 1655, 'Kenya': 682},
    'South Africa': {'Botswana': 1526, 'Eswatini': 441, 'Lesotho': 160, 'Namibia': 1447, 'Mozambique': 491, 'Zimbabwe': 225},
    'South Sudan': {'Central African Republic': 1163, 'Democratic Republic of the Congo': 628},
    'Sudan': {'Central African Republic': 1589, 'Chad': 1373, 'Egypt': 1276, 'Eritrea': 605, 'Ethiopia': 1293, 'Libya': 1636, 'South Sudan': 1174},
    'Tanzania': {'Burundi': 451, 'Kenya': 1015, 'Malawi': 475, 'Mozambique': 1512, 'Rwanda': 217, 'Uganda': 858, 'Zambia': 338, 'Democratic Republic of the Congo': 1979},
    'Togo': {'Benin': 126, 'Burkina Faso': 638, 'Ghana': 877},
    'Tunisia': {'Algeria': 965, 'Libya': 1092},
    'Uganda': {'Democratic Republic of the Congo': 777, 'Kenya': 812, 'Rwanda': 362, 'South Sudan': 452, 'Tanzania': 858},
    'Zambia': {'Angola': 1065, 'Malawi': 734, 'Mozambique': 1377, 'Namibia': 2106, 'Tanzania': 338, 'Zimbabwe': 389},
    'Zimbabwe': {'Botswana': 866, 'Mozambique': 1230, 'South Africa': 225, 'Zambia': 389}
}

nodes = graph.keys()
lost = math.inf

start = "Algeria"
end = "Zimbabwe"
d = {p: lost for p in nodes} #p - point
p = {p: -1 for p in nodes}
d[start] = 0
s = set() #Множество непросмотренных вершин
s.add((0, start))
while len(s) != 0: #Идём по циклу, пока не просмотрим все вершины
    cur_v = s.pop()[1]
    for w in nodes:
        if w != cur_v and w in graph[cur_v].keys():
            if d[cur_v] + graph[cur_v][w] < d[w]: #Проверка минимальности нового значения
                if (d[w], w) in s:
                    s.remove((d[w], w)) #Удаление из непросмотренных вершин новой
                d[w] = d[cur_v] + graph[cur_v][w]
                p[w] = cur_v
                s.add((d[w], w)) #Добавление новых вершин
root = [end]
i = end
while p[i] != -1:
    root += [p[i]] #Формируем итоговый путь и инвертируем его, чтобы отобразить правильно
    i = p[i]
root.reverse()

output=''
for i in root:
    output+=str(i)+' --- '
print('Длина маршрута: ',d[end])
print('Территории, через которые идёт путь: ',output[:-4])