"""Platform for sensor integration."""
from __future__ import annotations

from datetime import timedelta, datetime
from distutils.command.config import config
import logging
import voluptuous as vol
from google_play_scraper import app


import requests
from homeassistant import const
from homeassistant.components.sensor import PLATFORM_SCHEMA,SensorEntity
from homeassistant.helpers.entity import Entity
from homeassistant import util
import homeassistant.helpers.config_validation as cv


_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Android_icon"
CONF_ENTITY_ID ='entity_id'
UPDATE_FREQUENCY = timedelta(seconds=1)
PLATFORM_SCHEMA = cv.PLATFORM_SCHEMA.extend(
    {

        vol.Required(CONF_ENTITY_ID): cv.string,

    }

)


def setup_platform(hass, config, add_entities, discovery_info):
    """Set up the Copasa sensors."""

    add_entities([AndroidIcon(config,hass)])







class AndroidIcon(SensorEntity):
    """Representation of a Copasa sensor."""

    def __init__(self,config,hass):
        """Initialize a new copasa sensor."""
        self.config = config
        self.hass = hass
        self._attr_name = "Android icon"
        self._state = None
        self.android_icon = None

        self.dados = self.hass.states.get('person.leonardo')
        # self.teste = self.dados.friendly_name




    @property
    def state(self):
        """Returns the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return icon."""

        return self.android_icon

    @util.Throttle(UPDATE_FREQUENCY)
    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self.android_icon = get_android_icon()
        self._state =' self.dados'
    @property
    def extra_state_attributes(self):
        """Return device specific state attributes."""
        self._attributes = {
            "invoice_details": self.dados


        }
        return  self._attributes



def get_android_title():

    result = app(
        "com.netflix.ninja",
        lang="en",  # defaults to 'en'
        country="us",  # defaults to 'us'
    )
    title = result['title']

    return title

def get_android_icon():

    result = app(
        "com.netflix.ninja",
        lang="en",  # defaults to 'en'
        country="us",  # defaults to 'us'
    )
    title = result['icon']

    return title
