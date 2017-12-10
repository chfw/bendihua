# coding=utf-8
from __future__ import unicode_literals

import os
import json
from mock import patch, MagicMock
from nose.tools import eq_


@patch('fanyi.main.FANYI')
def test_translate(fake_translator):
    output_file = 'output-en.json'
    fake_translated_text = '沁园春 雪'
    fake_translator.translate = MagicMock(
        return_value=MagicMock(
            text=fake_translated_text
        )
    )
    expected = {
        'from': fake_translated_text,
        'nested': {
            'to': fake_translated_text
        }
    }
    from fanyi.main import translate

    options = {
        'dest_language': 'en',
        'output': output_file,
        'locale': os.path.join('tests', 'fixtures', 'test.json')
    }

    translate(options)

    with open('output-en.json', 'r') as f:
        content = json.load(f)
        eq_(content, expected)

    os.unlink(output_file)
