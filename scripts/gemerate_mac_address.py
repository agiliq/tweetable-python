from uuid import getnode

def get_mac():
    return hex(getnode()) if getnode() == getnode() else None
