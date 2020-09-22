from datetime import datetime

import std_hash


def test_version():
    assert std_hash.__version__ == '0.1.2'


def test_hash_OrderedDict():
    from collections import OrderedDict
    assert std_hash.hash(OrderedDict({
        'val1': 'value val1',
        datetime.fromtimestamp(15384793847): datetime.fromtimestamp(15384793847)
    })).hex() == 'd8c670dbbc3c215f52d757f09b381562b0a9afeb'


def test_hash_BaseModel():
    from pydantic import BaseModel, StrictStr

    class TestBaseModel(BaseModel):
        name: StrictStr = 'Ivan'

    assert std_hash.hash(TestBaseModel()).hex() == 'a4b578f0741047fc84508874498a10af6321d51b'
