# -*- coding: utf-8 -*-
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sql import create_pool
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())


loop = asyncio.get_event_loop()
db = loop.run_until_complete(create_pool())
