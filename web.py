import os
import random
import uuid
import bottle


@bottle.get('/api/v1/random/')
def get_random_number():
    return {
        'request_id': str(uuid.uuid4()),
        'result': random.random(),
    }


bottle.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
