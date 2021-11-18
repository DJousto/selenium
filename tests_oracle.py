import cx_Oracle
import config
import sqlite3 as lite

def connect_oracle():
	try:
	    connection = cx_Oracle.connect(
	        config.oracle_username,
	        config.oracle_password,
	        config.oracle_dsn,
	        encoding=config.oracle_encoding)

	    # affichage de la version
	    print(connection.version)
	    return connection
	except cx_Oracle.Error as error:
	    print(error)
	    return False

def connect_sqlite():
	try:
	    connection = lite.connect('./data/chinook.db', timeout=10, isolation_level = None)
	    return connection
	except Error as error:
	    print(error)
	    return False

###################
# fonctions de test
###################

# teste la connection à la base
def test_connection_sqlite():
	connection = connect_sqlite()
	assert connection!=False
	connection.close()

# teste la présence d'une table
def test_base_sqlite_albums():

	connection = connect_sqlite()
	cursor = connection.cursor()

	_SQL = "select * from albums"
	cursor.execute(_SQL)

	results = cursor.fetchall()
	results_list = [item[1] for item in results]
	print(results_list)

	assert len(results_list)

	connection.close()


def test_base_sqlite_album32():
	connection = connect_sqlite()
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM albums  where AlbumId=32")
	liste = [r for r in cursor.fetchall()]
	assert len(liste)>0
	connection.close()


