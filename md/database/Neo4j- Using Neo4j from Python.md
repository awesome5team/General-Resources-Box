<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Neo4j: Using Neo4j from Python](#neo4j-using-neo4j-from-python)
  - [install Neo4j](#install-neo4j)
  - [Using Neo4j from Python](#using-neo4j-from-python)
    - [Install py2neo](#install-py2neo)
    - [Connect to neo4j and restore the data in the csv file via Python](#connect-to-neo4j-and-restore-the-data-in-the-csv-file-via-python)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Neo4j: Using Neo4j from Python

## install Neo4j

- Install Homebrew

	```
	$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	```

- Before install neo4j, you need to download and install jdk from [oracle](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)

- To install neo4j for system Mac OS, run the following command:

	```
	$ brew install neo4j
	```
	
	if you cannot install neo4j with brew, you can try install by download in official site.

- Run the neo4j

	```
	$ neo4j console
	```
	
	 If execution result with 'command not found', you may need to do setting according following guide, either of below would be ok.
	 
	 
	 Create a symbolic link(recommended), here is a example:
	 
	```
ln -s /usr/local/Cellar/neo4j/2.1.5/bin/neo4j /usr/local/bin/neo4j
	```

	Or change the PATH by edit `~/.bash_profile`. Here is a example which add a new line: 
		 
	```
export PATH=$PATH:/usr/local/Cellar/neo4j/2.1.5/bin/
	```
- To view database, open http://localhost:7474/ in browser.

## Using Neo4j from Python

### Install py2neo

- install py2neo through pip

	```
	$ sudo pip install py2neo
	```
	
### Create a CSV file

Create a CSV file named modularity.csv to store the data, like the following is an example:

	 ```
	Id,Label,Modularity Class,PageRank
	" Sequoia"," Sequoia",0,0.011478213296893273
	" Accel"," Accel",0,0.016465271044444757
	" Intel"," Intel",1,0.0021984230303849425
	" nvidia"," nvidia",1,0.00255611355837637
	" Nike"," Nike",8,0.007497070150031853
	" adidas"," adidas",8,0.00658922457220539
	" Microsoft"," Microsoft",1,0.0021895290742890462
	" Dell"," Dell",1,0.015687861054210026
	" TXInstruments"," TXInstruments",2,0.0031547752695804897
	 ```


### Connect to neo4j and restore the data in the csv file via Python

create a python file named connTest.py to import pymongo as following:

	```
	from py2neo import neo4j, Graph, Node, Relationship
	import csv
	from config import NEO4J_DB_ADDR
	```

- create a instance bound to the default Neo4j server URI

	```
	graph = Graph(NEO4J_DB_ADDR)
	```
- csv module's reader 	object read sequences

	```
	pathCSV = 'csv/version2/'
	Nodes_file = open(pathCSV + 'modularity.csv', "rb") 
	reader = csv.reader(Nodes_file)
	```
- batch is linked to graph 	database

	```
	batch = neo4j.WriteBatch(graph)
	```
	```
	index = 0
	next(reader, None)
	for id, name, group, page_rank in reader:
	index = index + 1
	brand = batch.create(Node(name= name.strip().lower(), 	group= group))
	batch.set_labels(brand, 'Brand') 
		if index%5000 == 0:
		batch.submit() 
		print datetime.datetime.now() 	
		batch = neo4j.WriteBatch(graph)
	batch.submit()
	print 'Brand Restored'
	
	```
