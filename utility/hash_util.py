import hashlib as hl
import json

# Limited export from util
__all__ = ['hash_string_256', 'hash_block']


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """ Hashes a block and returns a string representation of it. """
    # JSON library is using, because we need supply string to function
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hl.sha256(json.dumps(hashable_block, sort_keys=True).encode()).hexdigest()
