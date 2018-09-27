import re
import getopt
from slackbot.bot import respond_to
from slackbot.bot import default_reply

import emojilib

from emoji_bot.upload import do_upload
from emoji_bot.errors import FormatError, AlreadyExistsError, UploadError
from slackbot_settings import bot_name, default_style, DEFAULT_REPLY, colors, fonts



@respond_to('help', re.IGNORECASE)
def help(message):
    try:
        print('got command help')
        message.send(DEFAULT_REPLY)
    except Exception as e:
        error_message=" :innocent: 不明なエラー  :innocent: \n\n"+\
            "  issue立ててくれたらいつか対応します。 @ https://github.com/toshi17/emojibot/issues"
        message.reply(error_message)
        print(e)

@respond_to('add ([^ ]+) ([-\w]+)$')
@respond_to('add ([^ ]+) ([-\w]+) (-.*)$')
def add(message, text, emoji_name, option=None):
    try:
        style = {
            'color': default_style['color'],
            'back_color': default_style['back_color'],
            'size_fixed': default_style['size_fixed'],
            'disable_stretch': default_style['disable_stretch'],
            'align': default_style['align'],
            'font_path': default_style['font_path'],
            'format': default_style['format']
        }

        if option:
            set_style(option, style)
        add_to_slack(message, text, emoji_name, style)
    except FormatError as e:
        error_message=" :warning: 構文エラー  :warning: \n\n"+\
            "  "+str(e)+": 入力フォーマットは以下の通りです。 \n" +\
            "  - `@"+bot_name+" add <text> <emoji_name> [option]`\n" +\
            "       _Options:_\n" +\
            "       - `-c, --color <text_color>` -- 文字色の設定\n" +\
            "       - `-b, --back <back_color>` -- 背景色の設定\n" +\
            "       - `-f, --font <font>` -- フォントの設定\n" +\
            "       ※ 色はRGB値か文字列で指定可能。RGB値で指定する場合は6桁か3桁の16進数で記述してください。\n" +\
            "       ※ emoji_nameは英数字、ハイフン、アンダーバーで指定してください。\n" +\
            "       ※ 例：@"+bot_name+" add プロ pro -c 000 -b FFFFFF\n"
        message.reply(error_message)
    except UploadError as e:
        error_message=" :no_entry: アップロードエラー  :no_entry: \n\n"+\
            "  アクセストークンが不正です。"
        message.reply(error_message)        
    except AlreadyExistsError as e:
        error_message=" :warning: アップロードエラー  :warning: \n\n"+\
            "   `:"+emoji_name+":`は既に :"+emoji_name+": で使用されています。別の名前を指定して下さい。"
        message.reply(error_message)
    except Exception as e:
        error_message=" :innocent: 不明なエラー  :innocent: \n\n"+\
            "   issue立ててくれたらいつか対応します。 @ https://github.com/toshi17/emojibot/issues"
        message.reply(error_message)
        print(e)

@respond_to('colors', re.IGNORECASE)
def color(message):
    print('got command colors')
    color_message = "\n  _Colors:_  \n"
    for color_name, color_code in colors.items():
        color_message += '   {}: {},'.format(color_name, '#'+color_code)
    message.reply(color_message)

@respond_to('fonts', re.IGNORECASE)
def font(message):
    print('got command fonts')
    font_message = "\n  _Fonts:_  \n"
    for font_name, font_path in fonts.items():
        font_message += '   {},'.format(font_name)
    message.reply(font_message)

def add_to_slack(message, text, emoji_name, style):
    try:
        print('got command add')
        print(text, emoji_name)

        print('- uploading {}'.format(text))
        data = emojilib.generate(
            text=text.replace('\\n', '\n'),
            width=128,
            height=128,
            color=style['color'],
            background_color=style['back_color'],
            size_fixed=style['size_fixed'],
            disable_stretch=style['disable_stretch'],
            align=style['align'],
            typeface_file=style['font_path'],
            format=style['format']
        )
        #upload to slack
        do_upload(data, emoji_name)

        message.reply("\n\n（´･ω･)╮)）－＝≡ :{}:  `:{}:`".format(emoji_name, emoji_name))
    except Exception as e:
        raise

def set_style(option, style):
    # repatter = re.compile('-([a-z]+) ([^ ]+)')
    # result = repatter.findall(option)
    opts, args = getopt.getopt(option.split(), "c:b:f:", ["color=", "back=", "font="])
    if len(args) > 0:
        raise FormatError('invalid option format')
    else:
        for opt in opts:
            if not opt[1]:
                raise FormatError('invalid option format')      
            elif opt[0] in ('-c', '--color'):
                color_code = get_color_code(opt[1])
                style['color'] = color_code
            elif opt[0] in ('-b', '--back'):
                color_code = get_color_code(opt[1])
                style['back_color'] = color_code
            elif opt[0] in ('-f', '--font'):
                font_path = get_font_path(opt[1])
                style['font_path'] = font_path

def get_color_code(text):
    repatter = re.compile('^([\da-fA-F]{6}|[\da-fA-F]{3})$')
    result = repatter.match(text)
    if result:
        color_code = result.group()
        if (len(color_code) == 3):
            color_code = color_code * 2
        return color_code+'FF'
    elif text in colors.keys():
        return colors[text]+'FF'
    else:
        raise FormatError('invalid color format')

def get_font_path(text):
    if text in fonts.keys():
        return fonts[text]
    else:
        raise FormatError('invalid font format')

