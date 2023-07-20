
class Transactions:

    @staticmethod
    def get_node_relationships(tx, entity_name: str):
        query = "MATCH(s)-[r]-(o) WHERE s.name = $entity_name RETURN s, r, o"
        result = tx.run(query, entity_name=entity_name)
        return result.data()
