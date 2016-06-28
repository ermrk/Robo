import logging

import Components
from server.ComponentCreator import ComponentCreator

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    ComponentCreator()
    Components.run()
