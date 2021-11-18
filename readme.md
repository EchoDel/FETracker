# Final Fantasy Free Enterprise Auto Tracker

Basic auto tracker for the current state of the world including;

* Retrieved Key Items
* Available Checks
* Used Key items

Data is also collected for the location each key item was found which will be presented in a future update.

# How to use

1. Install Python
2. Clone or download repository as zip
3. 

# How to contribute

Branch, program, test, submit PR with successful pytest runs.

## Testing

### How to setup testing environment

1. Clone Repository
2. Create virtual environment
3. run `pip install -e .[tests_require]`
4. Download the FE rom (http://ff4fe.com/get?id=bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC.KPRBTZVK77) Note this is needed to make sure the save states work. 
   * save ROM to build/
5. Run `python -m pytest` from the command line

# Todo

* Add support for bsnes
* Present the location each key item was found
* Add objectives, characters and bosses beaten
