from dataclasses import dataclass, InitVar
from neo4j import GraphDatabase
from transactions import Transactions

@dataclass
class HistoryDatabase():
    uri: InitVar[str]
    user_name: InitVar[str]
    password: InitVar[str]

    def __post_init__(self, uri: str, user_name: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user_name, password))

    def close(self):
        self.driver.close()
    
    def execute_read(self, tx, entity_name):
        with self.driver.session() as session:
            results = session.execute_read(tx, entity_name)
        return results

if __name__ == "__main__":
    history = HistoryDatabase("neo4j://localhost:7687", "neo4j", "12345678")
    print(history.execute_read(Transactions.get_node_relationships, "History"))