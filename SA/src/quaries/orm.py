from sqlalchemy import URL, create_engine, text, insert
from database import sync_engine, async_engine, session_factory, async_session_factory, Base
from models import WorkersOrm


class SyncORM:
    @staticmethod
    def create_tables():
        sync_engine.echo = True
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True
    @staticmethod
    def insert_data():
        with session_factory() as session:
            worker_bobr = WorkersOrm(username='Bobr')
            worker_volk = WorkersOrm(username="Volk")
            session.add_all([worker_bobr, worker_volk])
            session.commit()


class AsyncORM:
    @staticmethod
    def create_tables():
        async_engine.echo = True
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        async_engine.echo = True
    @staticmethod
    async def async_insert_data():
        async with async_session_factory() as session:
            worker_bobr = WorkersOrm(username='Bobr2')
            worker_volk = WorkersOrm(username="Volk2")
            session.add_all([worker_bobr, worker_volk])
            await session.commit()