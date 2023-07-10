import os
from database import DATABASE_NAME, Session
import create_database_dz42 as db_creator

from fruits import Fruits
from vegetables import Vegetables
from canning import Canning

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
