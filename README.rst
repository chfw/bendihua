================================================================================
fanyi - 翻译 - अनुवाद  - käännös - Übersetzen - Traduire - перевод - Traduzir - Translate
================================================================================

.. image:: https://travis-ci.org/chfw/fanyi.svg?branch=master
   :target: http://travis-ci.org/chfw/fanyi

.. image:: https://codecov.io/gh/chfw/fanyi/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/chfw/fanyi


Usage
================================================================================

Given your locale as en.json::

   {
      "ui-button": "hello world"
   }

You run: `fy en.json -d zh-cn` and will get `output-zh-cn.json` as::

   {
      "ui-button": "你好，世界“
   }

What you run `fy en.json -d hi`? You will get it in `Hindi`::

  {
      "ui-button": "नमस्ते दुनिया"
  }

And it automatically supports `aurelia-i18n <https://github.com/aurelia/i18n>`_
locale format.

Command line options
--------------------------------------------------------------------------------

::
    usage: fy [-h] [-d DEST_LANGUAGE] [-o OUTPUT] locale.json

    positional arguments:
      locale.json           locale dictionary where keys are engineering tokens
                            and values are actual user interface words

    optional arguments:
      -h, --help            show this help message and exit
      -d DEST_LANGUAGE, --dest-language DEST_LANGUAGE
                            Destination language short code
      -o OUTPUT, --output OUTPUT
                            select a name for the output file. if omitted, output
                            name is defaulted to output-{dest-language}.json


Supported languages
--------------------------------------------------------------------------------

=====================  ============
language               short code
=====================  ============
afrikaans              af
albanian               sq
amharic                am
arabic                 ar
armenian               hy
azerbaijani            az
basque                 eu
belarusian             be
bengali                bn
bosnian                bs
bulgarian              bg
catalan                ca
cebuano                ceb
chichewa               ny
chinese (simplified)   zh-cn
chinese (traditional)  zh-tw
corsican               co
croatian               hr
czech                  cs
danish                 da
dutch                  nl
english                en
esperanto              eo
estonian               et
filipino               tl
finnish                fi
french                 fr
frisian                fy
galician               gl
georgian               ka
german                 de
greek                  el
gujarati               gu
haitian creole         ht
hausa                  ha
hawaiian               haw
hebrew                 iw
hindi                  hi
hmong                  hmn
hungarian              hu
icelandic              is
igbo                   ig
indonesian             id
irish                  ga
italian                it
japanese               ja
javanese               jw
kannada                kn
kazakh                 kk
khmer                  km
korean                 ko
kurdish (kurmanji)     ku
kyrgyz                 ky
lao                    lo
latin                  la
latvian                lv
lithuanian             lt
luxembourgish          lb
macedonian             mk
malagasy               mg
malay                  ms
malayalam              ml
maltese                mt
maori                  mi
marathi                mr
mongolian              mn
myanmar (burmese)      my
nepali                 ne
norwegian              no
pashto                 ps
persian                fa
polish                 pl
portuguese             pt
punjabi                pa
romanian               ro
russian                ru
samoan                 sm
scots gaelic           gd
serbian                sr
sesotho                st
shona                  sn
sindhi                 sd
sinhala                si
slovak                 sk
slovenian              sl
somali                 so
spanish                es
sundanese              su
swahili                sw
swedish                sv
tajik                  tg
tamil                  ta
telugu                 te
thai                   th
turkish                tr
ukrainian              uk
urdu                   ur
uzbek                  uz
vietnamese             vi
welsh                  cy
xhosa                  xh
yiddish                yi
yoruba                 yo
zulu                   zu
=====================  ============


Installation
================================================================================


.. code-block:: bash

    $ git clone https://github.com/chfw/fanyi.git
    $ cd fanyi
    $ python setup.py install

License
================================================================================

MIT

