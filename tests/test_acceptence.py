from os.path import abspath, join, dirname
import json

TEST_DATA_DIRECTORY = join(abspath(join(dirname(__file__))), 'data')


class TestBridgeOfDeath:

    @classmethod
    def setup_class(cls):
        with open(join(TEST_DATA_DIRECTORY, 'answers.json')) as json_file:
            cls.answers = json.load(json_file)

    def test_what_is_your_name(self):
        assert self.answers['name'] == "aurthur king of the britons"

    def test_what_is_your_quest(self):
        assert self.answers['quest'] == "to seek the holy grail"

    def test_what_is_the_airspeed_velocity_of_an_unladen_swallow(self):
        assert self.answers['air_speed_velocity_of_an_unladen_swallow'] == "african_or_european_swallow?"
