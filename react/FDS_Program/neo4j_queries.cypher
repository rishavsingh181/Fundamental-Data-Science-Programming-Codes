MATCH (p:Person)
WHERE p.age > 26
RETURN p.name, p.age;

MATCH (:Person)-[r:FRIENDS_WITH]->(:Person)
RETURN COUNT(r);

MATCH (a:Person {name:'Alice'})-[:FRIENDS_WITH]->(friends)
RETURN friends.name;

MATCH (a:Person)-[:FRIENDS_WITH]->(b:Person)-[:FRIENDS_WITH]->(c:Person)
RETURN a.name, c.name;