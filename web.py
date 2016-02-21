import random
import uuid

import bottle


@bottle.get('/api/v1/random/')
def get_random_number():
    """
    @api {GET} /v1/random/ Generate a random number
    @apiName GetRandomNumber
    @apiGroup Random

    @apiDescription desc
    """
    return {
        'request_id': str(uuid.uuid4()),
        'result': random.random(),
    }


app = bottle.app()
