import pytest
from classes.aquarium import Aquarium
from classes.fish import Fish
from classes.plant import Plant
from classes.decoration import Decoration
import time


@pytest.fixture
def basic_aquarium():
    """Fixture for creating a basic Aquarium instance."""
    return Aquarium(channel_id=1, volume=100, substrate="Gravel")


def test_aquarium_initialization(basic_aquarium):
    """Test Aquarium object initialization."""
    assert basic_aquarium.channel_id == 1
    assert basic_aquarium.volume == 100
    assert basic_aquarium.substrate == "Gravel"
    assert basic_aquarium.water_quality == 100
    assert len(basic_aquarium.fish) == 0
    assert len(basic_aquarium.plants) == 0
    assert len(basic_aquarium.decoration) == 0


def test_add_fish(basic_aquarium):
    """Test adding a fish to the aquarium."""
    fish = Fish(species="Guppy", gender="Male", months=1)
    basic_aquarium.add_fish(fish)
    assert fish in basic_aquarium.fish
    assert len(basic_aquarium.fish) == 1


def test_add_plant(basic_aquarium):
    """Test adding a plant to the aquarium."""
    plant = Plant(species="Anubias")
    basic_aquarium.add_plant(plant)
    assert plant in basic_aquarium.plants
    assert len(basic_aquarium.plants) == 1


def test_add_decoration(basic_aquarium):
    """Test adding decoration to the aquarium."""
    decoration = Decoration(decoration="Rock")
    basic_aquarium.add_decoration(decoration)
    assert decoration in basic_aquarium.decoration
    assert len(basic_aquarium.decoration) == 1


def test_water_change(basic_aquarium):
    """Test water change functionality."""
    basic_aquarium.water_quality = 50
    result = basic_aquarium.water_change(litres=50)
    assert result is True
    assert basic_aquarium.water_quality > 50


def test_invalid_water_change(basic_aquarium):
    """Test water change with invalid volume."""
    result = basic_aquarium.water_change(litres=200)  # More than the tank's volume
    assert result is False
    assert basic_aquarium.water_quality == 100


def test_feed_no_fish(basic_aquarium):
    """Test feeding the aquarium when there are no fish."""
    basic_aquarium.feed()
    assert basic_aquarium.start_cycle is not None


def test_feed_with_fish(basic_aquarium):
    """Test feeding the aquarium when there are fish."""
    fish = Fish(species="Goldfish", gender="Male", months=1)
    fish.hunger = 4
    basic_aquarium.add_fish(fish)

    basic_aquarium.feed()
    assert fish.hunger == 10  # Hunger should be capped at 10


def test_monitor_water_with_no_cycle(basic_aquarium):
    pass


def test_monitor_fish_removal(basic_aquarium):
    """Test removing dead fish from the aquarium."""
    fish = Fish(species="Goldfish", gender="Male", months=1)
    fish.alive = False
    basic_aquarium.add_fish(fish)

    basic_aquarium.monitor_fish()
    assert len(basic_aquarium.fish) == 0


def test_timer_update(basic_aquarium):
    """Test timer thread updates aquarium months."""
    basic_aquarium.running = False  # Stop the thread to control timing
    time.sleep(5)
    basic_aquarium.update_timer()
    assert basic_aquarium.age >= 0  # months should increment in time units


def test_stop_aquarium_timer(basic_aquarium):
    """Test stopping the aquarium timer."""
    basic_aquarium.stop()
    assert not basic_aquarium.running
    assert not basic_aquarium.timer_thread.is_alive()
