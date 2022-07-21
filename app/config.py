import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_NAME = 'db.db'

logging.basicConfig(filename="/var/log/logs.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
