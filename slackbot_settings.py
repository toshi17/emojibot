team_name = ''
bot_name = ''

API_TOKEN = ''
cookie = ''

fonts = {
   'noto' : './assets/fonts/NotoSansMonoCJKjp-Bold.otf',
   'ipag' : './assets/fonts/ipag.ttf',
   'mplus' : './assets/fonts/ipag.ttf',
}

colors = {
    'black': '000000',
 	'silver': 'c0c0c0', 
 	'gray': '808080',	 
 	'white': 'ffffff',	 
 	'maroon': '800000', 
 	'red': 'ff0000',
 	'purple': '800080',
 	'fuchsia': 'ff00ff',
 	'green': '008000',
 	'lime': '00ff00',
 	'olive': '808000',
 	'yellow': 'ffff00',
 	'navy': '000080',
 	'blue': '0000ff',
 	'teal': '008080',
 	'aqua': '00ffff'
}

default_style = {
    'color': '000000FF',
    'back_color': 'FFFFFFFF',
    'size_fixed': 'false',
    'disable_stretch': 'false',
    'align': 'center',
    'font_path': fonts['noto'],
    'format': 'png'
}

PLUGINS = [
    'emoji_bot.plugins',
]

DEFAULT_REPLY = " :wave: :robot_face: @"+bot_name+"は文字列から絵文字を作成するbotです。 \n\n"+\
            "  _Commands:_  \n" +\
            "  - `@"+bot_name+" add <text> <emoji_name> [option]` -- 文字列を絵文字として登録します。\n" +\
            "       _Options:_\n" +\
            "       - `-c, --color <text_color>` -- 文字色の設定\n" +\
            "       - `-b, --back <back_color>` -- 背景色の設定\n" +\
            "       - `-f, --font <font>` -- フォントの設定\n" +\
            "       ※ 色はRGB値か文字列で指定可能。RGB値で指定する場合は6桁か3桁の16進数で記述してください。\n" +\
            "       ※ emoji_nameは英数字、ハイフン、アンダーバーで指定してください。\n" +\
            "       ※ 例：@"+bot_name+" add プロ pro -c=000 -bc=FFFFFF\n" +\
            "  - `@"+bot_name+" colors` -- 色一覧が確認できます。\n" +\
            "  - `@"+bot_name+" fonts` -- フォント一覧が確認できます。\n"
