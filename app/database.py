import psycopg2


def get_db():
    """Return a new connection to the learning_db database."""
    return psycopg2.connect(
        dbname="learning_db",
        user="moon",
        password="moon123",
        host="localhost",
    )