from sqlalchemy import URL, create_engine, text, insert, select
from database import sync_engine, async_engine, Base

from SA.src.models import WorkersOrm


class SyncCore:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_data():
        with sync_engine.connect() as conn:
            # stmt = """
            # INSERT INTO workers (username) VALUES('Bobr'),('Volk');
            # """
            stmt = insert('workers').values(
                [
                    {'username': "Bobriha"},
                    {'username': 'Volchiha'}
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select('workers')
            result = conn.execute(query)
            print(result.all())

class AcyncCore:
    @staticmethod
    async def create_tables():
        async_engine.echo = True
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        async_engine.echo = True

    @staticmethod
    async def insert_data():
        with async_engine.connect() as conn:
            # stmt = """
            # INSERT INTO workers (username) VALUES('Bobr'),('Volk');
            # """
            stmt = insert('workers').values(
                [
                    {'username': "Bobriha"},
                    {'username': 'Volchiha'}
                ]
            )
            await conn.execute(stmt)
            await conn.commit()

    @staticmethod
    async def select_workers():
        async with async_engine.connect() as conn:
            query = select('workers')
            result = await conn.execute(query)
            print(result.all())





