import random

# Sample knowledge graph represented as a dictionary
knowledge_graph = {
    "Python": {
        "type": "programming language",
        "creator": "Guido van Rossum",
        "year": 1991,
        "paradigm": "object-oriented, imperative, functional"
    },
    "Java": {
        "type": "programming language",
        "creator": "James Gosling",
        "year": 1995,
        "paradigm": "object-oriented"
    },
    "Einstein": {
        "type": "scientist",
        "field": "theoretical physics",
        "famous_for": "theory of relativity",
        "year_of_birth": 1879
    },
    "Beethoven": {
        "type": "composer",
        "famous_for": "symphonies",
        "year_of_birth": 1770,
        "nationality": "German"
    }
}

def get_random_topic():
    """Select a random topic from the knowledge graph."""
    return random.choice(list(knowledge_graph.keys()))

