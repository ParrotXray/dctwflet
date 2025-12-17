import flet as ft

BOT_TAGS = {
    "music": ("音樂", ft.Icons.MUSIC_NOTE),
    "minigames": ("小遊戲", ft.Icons.GAMES),
    "fun": ("有趣", ft.Icons.EMOJI_EMOTIONS),
    "utility": ("工具", ft.Icons.BUILD),
    "management": ("管理", ft.Icons.SETTINGS),
    "customizable": ("可自訂", ft.Icons.PALETTE),
    "automation": ("自動化", ft.Icons.AUTO_FIX_HIGH),
    "roleplay": ("角色扮演", ft.Icons.PEOPLE),
    "nsfw": ("NSFW", ft.Icons.DO_NOT_DISTURB)
}

# gaming,community,anime,art,hangout,programming,acting,nsfw,roleplay,politics
SERVER_TAGS = {
    "gaming": ("遊戲", ft.Icons.VIDEOGAME_ASSET),
    "community": ("社群", ft.Icons.GROUP),
    "anime": ("動漫", ft.Icons.FLASH_ON),
    "art": ("藝術", ft.Icons.BRUSH),
    "hangout": ("閒聊", ft.Icons.FORUM),
    "programming": ("程式設計", ft.Icons.CODE),
    "programing": ("程式設計", ft.Icons.CODE),  # bro wtf API 作者的英文可能被當了
    "acting": ("表演", ft.Icons.MIC),
    "nsfw": ("NSFW", ft.Icons.DO_NOT_DISTURB),
    "roleplay": ("角色扮演", ft.Icons.PEOPLE),
    "politics": ("政治", ft.Icons.GAVEL)
}

TEMPLATE_TAGS = {  # 這根本是亂打的吧
    "community": ("支援", ft.Icons.GROUP),  # 這個好像應該還好
    "gaming": ("遊戲", ft.Icons.VIDEOGAME_ASSET),  # 這個也還好
    "anime": ("大型", ft.Icons.FLASH_ON),  # 我真的搞不懂了 (悲
    "art": ("趣味", ft.Icons.BRUSH),  # ???????
    "nsfw": ("NSFW", ft.Icons.DO_NOT_DISTURB),
}
