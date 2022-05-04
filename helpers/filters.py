1.from typing import Union, List

2.from pyrogram import filters

3.from config import COMMAND_PREFIXES

4.other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
5.

6.def command(commands: Union[str, List[str]]):
7.    return filters.command(commands, COMMAND_PREFIXES)
