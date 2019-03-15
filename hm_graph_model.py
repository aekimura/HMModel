#!/usr/bin/env python


import networkx as nx
from matplotlib import pyplot as plt

mygraph = nx.DiGraph()

#start nodes
mygraph.add_edge('Start', 'Seattle', weight=0)
mygraph.add_edge('Start', 'Newport', weight=0)
mygraph.add_edge('Start', 'San Francisco', weight=0)
mygraph.add_edge('Start', 'USC', weight=0)

#day 1
mygraph.add_edge('Seattle', 'Boise', weight=494)
mygraph.add_edge('Newport', 'Boise', weight=561)
mygraph.add_edge('San Francisco', 'Boise', weight=648)
mygraph.add_edge('San Francisco', 'Salt Lake', weight=748)
mygraph.add_edge('San Francisco', 'Las Vegas', weight=630)
mygraph.add_edge('USC', 'Las Vegas', weight=275)
mygraph.add_edge('USC', 'Tucson', weight=528)

#day 2
mygraph.add_edge('Boise', 'Casper', weight=669)
mygraph.add_edge('Salt Lake', 'Casper', weight=402)
mygraph.add_edge('Salt Lake', 'Denver', weight=493)
mygraph.add_edge('Salt Lake', 'Albuquerque', weight=609)
mygraph.add_edge('Las Vegas', 'Albuquerque', weight=576)
mygraph.add_edge('Las Vegas', 'El Paso', weight=724)
mygraph.add_edge('Tucson', 'Albuquerque', weight=452)
mygraph.add_edge('Tucson', 'El Paso', weight=320)

#day 3
mygraph.add_edge('Casper', 'Pierre', weight=347)
mygraph.add_edge('Casper', 'Lincoln', weight=635)
mygraph.add_edge('Casper', 'Amarillo', weight=705)
mygraph.add_edge('Denver', 'Pierre', weight=526)
mygraph.add_edge('Denver', 'Lincoln', weight=667)
mygraph.add_edge('Denver', 'Amarillo', weight=424)
mygraph.add_edge('Albuquerque', 'Amarillo', weight=288)
mygraph.add_edge('Albuquerque', 'San Antonio', weight=714)
mygraph.add_edge('El Paso', 'Amarillo', weight=421)
mygraph.add_edge('El Paso', 'San Antonio', weight=555)

#day 4
mygraph.add_edge('Pierre', 'Minneapolis', weight=478)
mygraph.add_edge('Pierre', 'Kansas City', weight=598)
mygraph.add_edge('Lincoln', 'Minneapolis', weight=438)
mygraph.add_edge('Lincoln', 'Kansas City', weight=207)
mygraph.add_edge('Lincoln', 'Ft. Smith', weight=567)
mygraph.add_edge('Amarillo', 'Kansas City', weight=613)
mygraph.add_edge('Amarillo', 'Ft. Smith', weight=539)
mygraph.add_edge('Amarillo', 'Houston', weight=614)
mygraph.add_edge('San Antonio', 'Houston', weight=199)

#day 5
mygraph.add_edge('Minneapolis', 'Chicago', weight=465)
mygraph.add_edge('Minneapolis', 'St. Louis', weight=593)
mygraph.add_edge('Kansas City', 'Chicago', weight=527)
mygraph.add_edge('Kansas City', 'St. Louis', weight=256)
mygraph.add_edge('Kansas City', 'Nashville', weight=618)
mygraph.add_edge('Ft. Smith', 'St. Louis', weight=545)
mygraph.add_edge('Ft. Smith', 'Nashville', weight=501)
mygraph.add_edge('Ft. Smith', 'New Orleans', weight=601)
mygraph.add_edge('Houston', 'New Orleans', weight=352)

#day 6
mygraph.add_edge('Chicago', 'Pittsburg', weight=532)
mygraph.add_edge('Chicago', 'Roanoke', weight=717)
mygraph.add_edge('St. Louis', 'Pittsburg', weight=659)
mygraph.add_edge('St. Louis', 'Roanoke', weight=689)
mygraph.add_edge('Nashville', 'Roanoke', weight=435)
mygraph.add_edge('Nashville', 'Charlotte', weight=434)
mygraph.add_edge('Nashville', 'Talluhassee', weight=495)
mygraph.add_edge('New Orleans', 'Charlotte', weight=725)
mygraph.add_edge('New Orleans', 'Talluhassee', weight=388)

#day 7
mygraph.add_edge('Pittsburg', 'MIT', weight=680)
mygraph.add_edge('Pittsburg', 'Washington', weight=259)
mygraph.add_edge('Roanoke', 'MIT', weight=750)
mygraph.add_edge('Roanoke', 'Washington', weight=233)
mygraph.add_edge('Roanoke', 'Wilmington', weight=306)
mygraph.add_edge('Roanoke', 'Daytona Beach', weight=480)
mygraph.add_edge('Charlotte', 'Washington', weight=397)
mygraph.add_edge('Charlotte', 'Wilmington', weight=206)
mygraph.add_edge('Charlotte', 'Daytona Beach', weight=480)
mygraph.add_edge('Talluhassee', 'Wilmington', weight=496)
mygraph.add_edge('Talluhassee', 'Daytona Beach', weight=316)


#end nodes
mygraph.add_edge('MIT', 'End', weight=0)
mygraph.add_edge('Washington', 'End', weight=0)
mygraph.add_edge('Wilmington', 'End', weight=0)
mygraph.add_edge('Daytona Beach', 'End', weight=0)



##TO SHOW GRAPH
#pos = nx.layout.spring_layout(mygraph)
#nodes = nx.draw_networkx_nodes(mygraph, pos)
#edges = nx.draw_networkx_edges(mygraph, pos, arrowtype='->', width=3)
#edgelabels = nx.get_edge_attributes(mygraph, 'weight')
#nx.draw_networkx_labels(mygraph, pos, font_size=16, font_family='san-serif')
#plt.axis('off')
#plt.show()

days = [['Seattle', 'Newport', 'San Francisco', 'USC'],
	['Boise', 'Salt Lake', 'Las Vegas', 'Tucson'],
	['Casper', 'Denver', 'Albuquerque', 'El Paso'],
	['Pierre', 'Lincoln', 'Amarillo', 'San Antonio'],
	['Minneapolis', 'Kansas City', 'Ft. Smith', 'Houston'],
	['Chicago', 'St. Louis', 'Nashville', 'New Orleans'],
	['Pittsburg', 'Roanoke', 'Charlotte', 'Talluhassee'],
	['MIT', 'Washington', 'Wilmington', 'Daytona Beach']]

day_dict = dict()
current_nodes = set()
valid_paths = []

#day 0
for city in days[0]:
	day_dict[city] = mygraph.get_edge_data('Start', city)['weight']
	current_nodes.add(city)


#day 1
valid_pre = []
for city in days[1]:
	path_info = []
	pre = mygraph.predecessors(city)
	for p in pre:
		path_info.append((mygraph.get_edge_data(p, city)['weight']+day_dict[p], p, city))
	mpath = min(path_info)
	valid_paths.append(mpath)
	valid_pre.append(mpath[1])
	day_dict[city] = mpath[0]

to_remove = []
for d in day_dict:
	if d not in days[1]:
		if d not in valid_pre:
			to_remove.append(d)

for t in to_remove:
	del day_dict[t]


#day 2
valid_pre = []
for city in days[2]:
        path_info = []
        pre = mygraph.predecessors(city)
        for p in pre:
                path_info.append((mygraph.get_edge_data(p, city)['weight']+day_dict[p], p, city))
        mpath = min(path_info)
        valid_paths.append(mpath)
        valid_pre.append(mpath[1])
        day_dict[city] = mpath[0]

to_remove = []
for d in day_dict:
        if d in days[1]:
		if d not in valid_pre:
                        to_remove.append(d)

for t in to_remove:
	if t in day_dict.keys():
        	del day_dict[t]

invalid = [x[1] for x in valid_paths if x[2] not in day_dict.keys()]
for i in invalid:
	if i in day_dict.keys():
		del day_dict[i]

for v in valid_paths:
	for i in invalid:
		if v[1] == i:
			r = valid_paths.index(v)
			valid_paths.pop(r)


#day 3
valid_pre = []
for city in days[3]:
        path_info = []
        pre = mygraph.predecessors(city)
        for p in pre:
                path_info.append((mygraph.get_edge_data(p, city)['weight']+day_dict[p], p, city))
        mpath = min(path_info)
        valid_paths.append(mpath)
        valid_pre.append(mpath[1])
        day_dict[city] = mpath[0]

#print(valid_pre)
to_remove = []
for d in day_dict:
        if d in days[2]:
		if d not in valid_pre:
			to_remove.append(d)

#print(to_remove)
for t in to_remove:
        if t in day_dict.keys():
		del day_dict[t]

invalid = [x[1] for x in valid_paths if x[2] not in day_dict.keys()]
#print(invalid)
for i in invalid:
	if i in day_dict.keys():
        	del day_dict[i]

for v in valid_paths:
        for i in invalid:
                if v[1] == i:
                        r = valid_paths.index(v)
                        valid_paths.pop(r)



#day 4
valid_pre = []
for city in days[4]:
        path_info = []
        pre = mygraph.predecessors(city)
        for p in pre:
                path_info.append((mygraph.get_edge_data(p, city)['weight']+day_dict[p], p, city))
        mpath = min(path_info)
        valid_paths.append(mpath)
        valid_pre.append(mpath[1])
        day_dict[city] = mpath[0]

to_remove = []
for d in day_dict:
        if d in days[3]:
                if d not in valid_pre:
                        to_remove.append(d)

for t in to_remove:
	if t in day_dict.keys():
	        del day_dict[t]

invalid = [x[1] for x in valid_paths if x[2] not in day_dict.keys()]
for i in invalid:
        if i in day_dict.keys():
		del day_dict[i]

for v in valid_paths:
        for i in invalid:
                if v[1] == i:
                        r = valid_paths.index(v)
                        valid_paths.pop(r)


#day 5
valid_pre = []
for city in days[5]:
        path_info = []
        pre = mygraph.predecessors(city)
        for p in pre:
                path_info.append((mygraph.get_edge_data(p, city)['weight']+day_dict[p], p, city))
        mpath = min(path_info)
        valid_paths.append(mpath)
        valid_pre.append(mpath[1])
        day_dict[city] = mpath[0]

to_remove = []
for d in day_dict:
        if d in days[4]:
                if d not in valid_pre:
                        to_remove.append(d)

for t in to_remove:
        if t in day_dict.keys():
                del day_dict[t]

invalid = [x[1] for x in valid_paths if x[2] not in day_dict.keys()]
for i in invalid:
        if i in day_dict.keys():
                del day_dict[i]

for v in valid_paths:
        for i in invalid:
		if v[1] == i:
                        r = valid_paths.index(v)
                        valid_paths.pop(r)




#day 6
valid_pre = []
for city in days[6]:
        path_info = []
        pre = mygraph.predecessors(city)
        for p in pre:
                path_info.append((mygraph.get_edge_data(p, city)['weight']+day_dict[p], p, city))
        mpath = min(path_info)
        valid_paths.append(mpath)
        valid_pre.append(mpath[1])
        day_dict[city] = mpath[0]

to_remove = []
for d in day_dict:
        if d in days[5]:
                if d not in valid_pre:
                        to_remove.append(d)

for t in to_remove:
        if t in day_dict.keys():
                del day_dict[t]

invalid = [x[1] for x in valid_paths if x[2] not in day_dict.keys()]
for i in invalid:
        if i in day_dict.keys():
                del day_dict[i]

for v in valid_paths:
        for i in invalid:
		if v[1] == i:
                        r = valid_paths.index(v)
                        valid_paths.pop(r)


#day 7
valid_pre = []
for city in days[7]:
        path_info = []
        pre = mygraph.predecessors(city)
        for p in pre:
                path_info.append((mygraph.get_edge_data(p, city)['weight']+day_dict[p], p, city))
        mpath = min(path_info)
        valid_paths.append(mpath)
        valid_pre.append(mpath[1])
        day_dict[city] = mpath[0]

to_remove = []
for d in day_dict:
        if d in days[6]:
                if d not in valid_pre:
                        to_remove.append(d)

for t in to_remove:
        if t in day_dict.keys():
                del day_dict[t]

invalid = [x[1] for x in valid_paths if x[2] not in day_dict.keys()]
for i in invalid:
        if i in day_dict.keys():
                del day_dict[i]

for v in valid_paths:
        for i in invalid:
                if v[1] == i:
                        r = valid_paths.index(v)
                        valid_paths.pop(r)




#traceback
days7_info = []
for d in days[7]:
	days7_info.append((day_dict[d], d))
cpath = min(days7_info)
c_path_l = [cpath[1]]

for i in range(7):
	for c in c_path_l:
		for v in valid_paths:
			if v[2] == c:
				if v[1] not in c_path_l:
					c_path_l.append(v[1])
c_path_l.reverse()
print('The best path is: ')
print(c_path_l)

#print(day_dict)
