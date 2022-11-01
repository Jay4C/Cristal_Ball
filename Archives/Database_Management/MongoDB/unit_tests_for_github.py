import unittest
import pymongo


class UnitTestsDatabaseManagementMongoDBForMesdamesDBForGitHub(unittest.TestCase):
    # ok
    def test_list_databases(self):
        print('test_list_databases')

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        print(myclient.list_database_names())

        myclient.close()

    # ok
    def test_create_database_mesdamesdb(self):
        print("test_create_database_mesdamesdb")

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mesdamesdb = myclient["mesdamesdb"]
        myclient.close()

    # ok
    def test_create_collection_mesdames_into_database_mesdamesdb(self):
        print("test_create_collection_mesdames_into_database_mesdamesdb")

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mesdamesdb = myclient["mesdamesdb"]
        mesdames_c = mesdamesdb["mesdames_c"]
        print(mesdamesdb.list_collection_names())
        myclient.close()

    # ok
    def test_insert_one_record_into_mesdames_collection(self):
        print('test_insert_one_record_into_mesdames_collection')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        database = "mesdamesdb"
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port) + "/" + database
        myclient = pymongo.MongoClient(uri)

        mesdamesdb = myclient["mesdamesdb"]
        mesdames_c = mesdamesdb["mesdames_c"]
        mydict = {"city": "Saint-Pierre", "pn": "0789111112", "link": "url"}
        x = mesdames_c.insert_one(mydict)
        print(x.inserted_id)

    # ok
    def test_list_all_records_from_mesdames_collection(self):
        print('test_list_all_records_from_mesdames_collection')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        database = "mesdamesdb"
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port) + "/" + database
        myclient = pymongo.MongoClient(uri)

        mesdamesdb = myclient["mesdamesdb"]
        mesdames_c = mesdamesdb["mesdames_c"]

        for x in mesdames_c.find():
            print(x)
            # print(x.get('pn'))

        myclient.close()

    # ok
    def test_delete_some_records_from_mesdames_collection(self):
        print('test_delete_some_records_from_mesdames_collection')

        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        mesdamesdb = myclient["mesdamesdb"]
        mesdames_c = mesdamesdb["mesdames_c"]

        records = [
            ''
        ]

        for record in records:
            myquery = {"pn": record}

            mesdames_c.delete_one(myquery)

        myclient.close()

    # ok
    def test_delete_all_records_from_mesdames_collection(self):
        print('test_delete_all_records_from_mesdames_collection')

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mesdamesdb = myclient["mesdamesdb"]
        mesdames_c = mesdamesdb["mesdames_c"]

        for x in mesdames_c.find():
            myquery = x
            mesdames_c.delete_one(myquery)

        myclient.close()


class UnitTestsDatabaseManagementMongoDBForCompanyDBForGitHub(unittest.TestCase):
    # ok
    def test_list_databases(self):
        print('test_list_databases')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        print(myclient.list_database_names())

        myclient.close()

    # ok
    def test_create_database_companydb(self):
        print("test_create_database_companydb")

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient['companydb']

        myclient.close()


class UnitTestsDatabaseManagementMongoDBForCompanyDBForCollectionSwitzerlandForGitHub(unittest.TestCase):
    # ok
    def test_create_collection_switzerland_into_database_companydb(self):
        print("test_create_collection_switzerland_into_database_companydb")

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        # Collection 'Switzerland'
        companydb = myclient["companydb"]
        switzerland = companydb["switzerland"]
        print(companydb.list_collection_names())

        myclient.close()

    # ok
    def test_insert_one_record_into_switzerland_collection(self):
        print('test_insert_one_record_into_switzerland_collection')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["companydb"]
        switzerland = companydb["switzerland"]
        my_dict = {
            'company_name': 'Elektra Energie Genossenschaft',
            'address': 'Dorfplatz 93673\xa0Linden',
            'phone_number': 'tel:+41317712307',
            'website': 'http://www.elektra-energie.ch',
            'email': "'info@elektra-energie.ch',",
            'activity': 'Electricit%C3%A9%2C+approvisionnement+en',
            'city': 'Suisse'
        }
        switzerland.insert_one(my_dict)
        myclient.close()

    # ok
    def test_list_all_records_from_switzerland_collection(self):
        print('test_list_all_records_from_switzerland_collection')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["companydb"]
        switzerland = companydb["switzerland"]

        for x in switzerland.find():
            print(x)

    # ok
    def test_list_all_records_from_switzerland_collection_for_email(self):
        print('test_list_all_records_from_switzerland_collection_for_email')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["companydb"]
        switzerland = companydb["switzerland"]

        myquery = {
            "city": "Genève",
            "activity": "avocat"
        }

        emails = []

        for x in switzerland.find(myquery):
            email = x.get('email').lower()

            if email != '':
                if email not in emails:
                    emails.append(email)

        for email in emails:
            print(email)

    # ok
    def test_delete_some_records_from_switzerland_collection(self):
        print('test_delete_some_records_from_switzerland_collection')

        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["mesdamesdb"]
        switzerland = companydb["switzerland"]

        records = [
            ''
        ]

        for record in records:
            myquery = {"pn": record}

            switzerland.delete_one(myquery)

    # ok
    def test_delete_all_records_from_switzerland_collection(self):
        print('test_delete_all_records_from_switzerland_collection')

        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["companydb"]
        switzerland = companydb["switzerland"]

        for x in switzerland.find():
            myquery = x
            switzerland.delete_one(myquery)


class UnitTestsDatabaseManagementMongoDBForCompanyDBForCollectionEuropagesForGitHub(unittest.TestCase):
    # ok
    def test_create_collection_europages_into_database_companydb(self):
        print("test_create_collection_europages_into_database_companydb")

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        # Collection 'Switzerland'
        companydb = myclient["companydb"]
        europages = companydb["europages"]
        print(companydb.list_collection_names())

        myclient.close()

    # ok
    def test_insert_one_record_into_europages_collection(self):
        print('test_insert_one_record_into_europages_collection')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["companydb"]
        europages = companydb["europages"]
        my_dict = {
            'company_name': 'SBA-TRAFOTECH GMBH',
            'address': 'Winkelleite 14  91332 Heiligenstadt I.ofr.',
            'phone_number': '+49 91988090',
            'website': 'http://www.sba.de',
            'email': "'info@sba.de',",
            'activity': 'Fabricant/ Producteur',
            'country': 'Allemagne'
        }
        europages.insert_one(my_dict)
        myclient.close()

    # ok
    def test_list_all_records_from_europages_collection(self):
        print('test_list_all_records_from_europages_collection')

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["companydb"]
        europages = companydb["europages"]

        for x in europages.find():
            print(x)

    # ok
    def test_delete_some_records_from_europages_collection(self):
        print('test_delete_some_records_from_europages_collection')

        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["mesdamesdb"]
        europages = companydb["europages"]

        records = [
            ''
        ]

        for record in records:
            myquery = {"pn": record}
            europages.delete_one(myquery)

    # ok
    def test_delete_all_records_from_europages_collection(self):
        print('test_delete_all_records_from_europages_collection')

        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)

        companydb = myclient["companydb"]
        europages = companydb["europages"]

        for x in europages.find():
            myquery = x
            europages.delete_one(myquery)


if __name__ == '__main__':
    unittest.main()
