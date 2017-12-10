import sys
from mock import patch


class TestMain:
    def setUp(self):
        self.patcher = patch('fy.main.translate')
        self.fake_translate = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_single_params(self):
        test_input = 'test_input.json'
        args = ['fy', test_input]
        expected = {
            'dest_language': 'en',
            'output': 'output-en.json',
            'locale': test_input
        }
        with patch.object(sys, 'argv', args):
            from fy.main import main
            main()
            self.fake_translate.assert_called_with(expected)

    def test_output(self):
        test_input = 'test_input.json'
        custom_output = 'abc.json'
        args = ['fy', test_input, '-o', custom_output]
        expected = {
            'dest_language': 'en',
            'output': custom_output,
            'locale': test_input
        }
        with patch.object(sys, 'argv', args):
            from fy.main import main
            main()
            self.fake_translate.assert_called_with(expected)

    def test_dest_language(self):
        test_input = 'test_input.json'
        custom_output = 'abc.json'
        dest_language = 'zh'
        args = ['fy', test_input, '-o', custom_output, '-d', dest_language]
        expected = {
            'dest_language': dest_language,
            'output': custom_output,
            'locale': test_input
        }
        with patch.object(sys, 'argv', args):
            from fy.main import main
            main()
            self.fake_translate.assert_called_with(expected)
