import sqlite3

class Database:
    """
    This class represents the database.
    """
        
    def __init__(self) -> None:
        """
        Class constructor. It creates (if it doesn't exist) a database and
        stablishes a connection to it.
        """

        self.db = sqlite3.connect("biomaze.db")
        self.cursor = self.db.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            name TEXT NOT NULL,
            start_organ TEXT NOT NULL,
            time INT NOT NULL)           
        """)

        self.db.commit()

    def get_ranking(self) -> list[(str, int)]:
        """
        It gets the game ranking.

        Returns:
            a list, in ascending order considering time, containing tuples in the format (player's name, time).
            The time is stored in seconds. If an error occurs, the functions returns None.
        """

        try:
            self.cursor.execute("SELECT * FROM scores ORDER BY time ASC")
            result = self.cursor.fetchall()

            return result
        except:
            return None

    def new_score(self, name, start_organ, time) -> int:
        """
        It adds a new score on the database.

        Arguments:
            name: the player's name.
            start_organ: the start organ.
            time: the player's time in seconds.

        Returns:
            0 if successful,
            1 otherwise.
        """

        insertion_command = """
        INSERT INTO scores (name, start_organ, time) VALUES (?, ?, ?)                
        """

        try:
            self.cursor.execute(insertion_command, (name, start_organ, time))
            self.db.commit()

            return 0
        except:
            return 1
        
    def __del__(self):
        """
        Class destructor. It closes the connection to the database.
        """

        if hasattr(self, 'db'):
            self.db.close()