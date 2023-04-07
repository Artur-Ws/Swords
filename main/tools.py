from collections import defaultdict
import weakref

debug_refs = []


def debug_log():
    for i, debug in enumerate(debug_refs):
        debug.log_info(i)
        debug.remove_if_expired()
