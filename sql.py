# -*- coding: utf-8 -*-
import asyncio
import asyncpg
import logs
from config import USER, DB_PASSWORD, HOST, PORT

logger = logs.getLogger('app.sql')


async def create_db():
    create_db_command = open("database/create_tables.sql", "r").read()

    logger.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(user=USER,
                                     password=DB_PASSWORD,
                                     host=HOST,
                                     port=PORT)
    await conn.execute(create_db_command)
    await conn.close()
    logger.info("database was created")


async def create_pool():
    return await asyncpg.create_pool(user=USER,
                                     password=DB_PASSWORD,
                                     host=HOST,
                                     port=PORT)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())