import sqlite3

def deleteRecord():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # Deleting single record now
        # Script can be executed as a scheduled task via Task Scheduler (Windows) or Cron (Unix)
        # Delete records of visitors older than 3 years (365 x 3 =1095)
        sql_delete_query = """DELETE FROM survey_visitor WHERE checkin < date('now', '-1095 day')"""
        cursor.execute(sql_delete_query)
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

deleteRecord()