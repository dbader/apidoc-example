import random
import uuid

import bottle


@bottle.get('/api/v1/random/')
def get_random_number():
    return {
        'request_id': str(uuid.uuid4()),
        'result': random.random(),
    }


app = bottle.app()
