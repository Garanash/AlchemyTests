import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from quaries.core import SyncCore, AcyncCore
# from quaries.orm import SyncORM, AsyncORM

SyncCore.create_tables()
SyncCore.insert_data()
SyncCore.select_workers()

# create_tables()
# insert_data()
# # asyncio.run(async_insert_data())