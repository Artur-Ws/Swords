debug_refs = []


def debug_log() -> object:
    for i, debug in enumerate(debug_refs):
        debug.log_info(i)
        debug.remove_if_expired()
