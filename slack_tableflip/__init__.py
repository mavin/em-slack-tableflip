#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pylint: disable=anomalous-backslash-in-string
"""
EM Slack Tableflip Module: slack_tableflip.

    - Sets up Flask application and module constants

Copyright (c) 2015-2016 Erin Morelli

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
"""

import os
from threading import Thread
from datetime import date
import keen
from flask import Flask
from pkg_resources import get_provider


# =============================================================================
#  App Constants
# =============================================================================

# Set module name
__module__ = "slack_tableflip.{0}".format(__file__)


# Get module info
def set_project_info():
    """Set project information from setup tools installation."""
    # CUSTOMIZE THIS VALUE FOR YOUR OWN INSTALLATION
    base_url = 'https://libertatem-slack-tableflip.herokuapp.com'

    # Get app info from the dist
    app_name = 'slack_tableflip'
    provider = get_provider(app_name)

    return {
        'name': app_name,
        'name_full': 'Libertatem Slack Tableflip',
        'github_url': 'https://github.com/mavin/slack-tableflip',
        'version': '1.4',
        'version_int': 1.4,
        'package_path': provider.module_path,
        'copyright': '2015-{0}'.format(str(date.today().year)),
        'client_secret': os.environ['SLACK_CLIENT_SECRET'],
        'client_id': os.environ['SLACK_CLIENT_ID'],
        'base_url': base_url,
        'oauth_url': 'https://slack.com/oauth/authorize',
        'auth_url': '{0}/authenticate'.format(base_url),
        'user_url': '{0}/validate'.format(base_url),
        'team_url': '{0}/authorize'.format(base_url),
        'team_scope': [
            'commands'
        ],
        'user_scope': [
            'chat:write:bot',
            'chat:write:user',
            'identify'
        ]
    }

# Project info
PROJECT_INFO = set_project_info()

# Set the template directory
TEMPLATE_DIR = os.path.join(PROJECT_INFO['package_path'], 'templates')

# Allowed slash commands
ALLOWED_COMMANDS = [
    '/flip',
    '/fliptable',
    '/tableflip',
    '/flip_table',
    '/table_flip'
]

# Allowed flip types
# Sources:
#   http://www.emoticonfun.org/flip/
#   http://emojicons.com/table-flipping
#   http://tableflipping.com/
ALLOWED_TYPES = {
    'classic': "(╯°□°)╯︵ ┻━┻",
    'rage': "(ﾉಥ益ಥ）ﾉ﻿ ┻━┻",
    'whoops': "┬──┬﻿ ¯\_(ツ)",
    'two': "┻━┻ ︵╰(°□°)╯︵ ┻━┻",
    'tantrum': "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    'fury': "┻━┻彡 ヽ(ಠДಠ)ノ彡┻━┻﻿",
    'relax': "┬─┬ノ( º _ ºノ)",
    'teeth': "(ノಠ益ಠ)ノ彡┻━┻",
    'monocle': "(╯ಠ_ರೃ)╯︵ ┻━┻",
    'person': "(╯°□°）╯︵ /(.□. \)",
    'jake': "(┛❍ᴥ❍﻿)┛彡┻━┻",
    'owl': "(ʘ∇ʘ)ク 彡 ┻━┻",
    'laptop': "(ノÒ益Ó)ノ彡▔▔▏",
    'strong': "/(ò.ó)┛彡┻━┻",
    'yelling': "(┛◉Д◉)┛彡┻━┻",
    'shrug': "┻━┻ ︵﻿ ¯\(ツ)/¯ ︵ ┻━┻",
    'pudgy': "(ノ ゜Д゜)ノ ︵ ┻━┻",
    'battle': "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)",
    'return': "(ノ^_^)ノ┻━┻ ┬─┬ ノ( ^_^ノ)",
    'cry': "(╯'□')╯︵ ┻━┻",
    'freakout': "(ﾉಥДಥ)ﾉ︵┻━┻･/",
    'people': "(/ .□.)\ ︵╰(゜Д゜)╯︵ /(.□. \)",
    'force': "(._.) ~ ︵ ┻━┻",
    'bear': "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
    'magic': "(/¯◡ ‿ ◡)/¯ ~ ┻━┻",
    'robot': "┗[© ♒ ©]┛ ︵ ┻━┻",
    'opposite': "ノ┬─┬ノ ︵ ( \o°o)\\",
    'cute': "┻━┻ ︵ ლ(⌒-⌒ლ)",
    'glare': "(╯ಠ_ಠ）╯︵ ┻━┻",
    'dead': "(╯°□°）╯︵ /(x_x)|",
    'buffet': "(╯°□°）╯︵ ┻━━━┻ ",
    'adorable': "(づ｡◕‿‿◕｡)づ ︵ ┻━┻",
    'hypnotic': "(╯°.°）╯ ┻━┻",
    'bored': "(ノ゜-゜)ノ ︵ ┻━┻",
    'bomb': "( ・_・)ノ⌒●~*"
}

# Allowed restore flip types
RESTORE_TYPES = {
    'relax': "{0} ノ( º _ ºノ)",
    'whoops': "{0} ¯\_(ツ)"
}

# Allowed word flip types
WORD_TYPES = {
    'word': "(╯°□°)╯︵ {0}",
    'rage': "(ﾉಥ益ಥ）ﾉ﻿ {0}",
    'teeth': "(ノಠ益ಠ)ノ彡{0}",
    'monocle': "(╯ಠ_ರೃ)╯︵ {0}",
    'jake': "(┛❍ᴥ❍﻿)┛彡{0}",
    'owl': "(ʘ∇ʘ)ク 彡 {0}",
    'strong': "/(ò.ó)┛彡{0}",
    'yelling': "(┛◉Д◉)┛彡{0}",
    'pudgy': "(ノ ゜Д゜)ノ ︵ {0}",
    'cry': "(╯'□')╯︵ {0}",
    'force': "(._.) ~ ︵ {0}",
    'bear': "ʕノ•ᴥ•ʔノ ︵ {0}",
    'magic': "(/¯◡ ‿ ◡)/¯ ~ {0}",
    'robot': "┗[© ♒ ©]┛ ︵ {0}",
    'cute': "{0} ︵ ლ(⌒-⌒ლ)",
    'glare': "(╯ಠ_ಠ）╯︵ {0}",
    'adorable': "(づ｡◕‿‿◕｡)づ ︵ {0}",
    'hypnotic': "(╯°.°）╯ {0}",
    'bored': "(ノ゜-゜)ノ ︵ {0}"
}

# Flipped character mapping
FLIPPED_CHARS = {
    " ": " ",
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ı",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "𐐒",
    "C": "Ɔ",
    "D": "p",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "ʞ",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Ό",
    "R": "ᴚ",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    "!": "¡",
    "?": "¿",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    ".": "˙",
    '"': ",,",
    "'": ",",
    "’": ",",
    "`": ",",
    "“": ",,",
    "”": ",,",
    "¿": "?",
    "&": "⅋",
    "_": "‾"
}


def report_event(name, event):
    """Asyncronously report an event."""
    # Set up thread
    event_report = Thread(
        target=keen.add_event,
        args=(name, event)
    )

    # Set up as asyncronous daemon
    event_report.daemon = True

    # Start event report
    event_report.start()


# =============================================================================
# Flask App Configuration
# =============================================================================

# Initalize flask app
APP = Flask(
    'libertatem-slack-tableflip',
    template_folder=TEMPLATE_DIR,
    static_folder=TEMPLATE_DIR
)

# Set up flask config
# SET THESE ENV VALUES FOR YOUR OWN INSTALLATION
APP.config.update({
    'SQLALCHEMY_DATABASE_URI': os.environ['DATABASE_URL'],
    'SECRET_KEY': os.environ['SECURE_KEY']
})
