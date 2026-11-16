# Autoplay on/off (per chat) - MongoDB me save hota hai, memory me cache.
try:
    from SHUKLAMUSIC.core.mongo import mongodb
    _col = mongodb.autoplay
except Exception:  # mongo na mile to sirf memory me chalega
    _col = None

_cache: dict = {}


async def get_autoplay(chat_id: int) -> bool:
    if chat_id in _cache:
        return _cache[chat_id]
    val = False
    if _col is not None:
        try:
            doc = await _col.find_one({"chat_id": chat_id})
            val = bool(doc and doc.get("enabled"))
        except Exception:
            val = False
    _cache[chat_id] = val
    return val


async def set_autoplay(chat_id: int, value: bool):
    _cache[chat_id] = bool(value)
    if _col is not None:
        try:
            await _col.update_one(
                {"chat_id": chat_id},
                {"$set": {"enabled": bool(value)}},
                upsert=True,
            )
        except Exception:
            pass


is_autoplay_on = get_autoplay
