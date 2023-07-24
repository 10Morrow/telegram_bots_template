# -*- coding: utf-8 -*-
import logs
from loader import bot, dp
from aiogram.utils import executor

logger = logs.getLogger('app.bot')


async def on_startup(dp):
	logger.info('the bot started working.')


async def on_shutdown(dp):
	logger.info('the bot stopped working.')
	await bot.close()


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)