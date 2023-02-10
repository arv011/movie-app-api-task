from os import environ as env
import environ
env = environ.Env()

#This is for future multiple settings
# SETTING_ENVIRON = env.str("ENV", "settings.settings")

testcases_db = False

# if testcases_db: 
#     MOVIE_DB = env.db("DATABASE_URL", "postgres://postgres:arv@11111@localhost:5432/tester_arv_db")
#     MOVIE_DB_READ = env.db("DATABASE_URL", "postgres://postgres:arv@11111@localhost:5432/tester_arv_db")
