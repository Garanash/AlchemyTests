import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from quaries.orm import create_tables, insert_data, async_insert_data

create_tables()
insert_data()
# asyncio.run(async_insert_data())