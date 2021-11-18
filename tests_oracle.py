import cx_Oracle
import config

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


###################
# fonctions de test
###################

# teste la connection à la base
def test_connection():
	connection = connect_oracle()
	assert connection!=False
	connection.close()

# teste la présence d'une table
def test_base_T_ADRESSE():

	connection = connect_oracle()
	cursor = connection.cursor()

	CommandeSQL = "select * from T_ADRESSE"
	cursor.execute(CommandeSQL)

	results = cursor.fetchall()
	results_list = [item[1] for item in results]
	print(results_list)

	assert len(results_list)

	connection.close()



