"""Запускаем бота.

Точка входа для модуля.
Чтобы запустить бота:

.. code-block:: shell

    python -m doranime
"""

from doranime.config import BOT_TOKEN
from doranime.doranime import DoranimeBot

if __name__ == "__main__":
    DoranimeBot(BOT_TOKEN).run()
