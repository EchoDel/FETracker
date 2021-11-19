# Final Fantasy Free Enterprise Auto Tracker

Basic auto tracker for the current state of the world including;

* Retrieved Key Items
* Available Checks
* Used Key items

Data is also collected for the location each key item was found which will be presented in a future update.

**Note:**  The pass is **not** a key item so does not have a key item bit and must be **manually** toggled.

# How to use

1. Install Python
2. Clone or download repository as zip
3. Run `pip install -e .` to setup all the required libaries
4. Run `python main.py /path/to/FF4FE-rom`. The rom running in bizhawk should popup and a few seconds later the tracker.


## Testing

### How to setup testing environment

1. Clone Repository
2. Create virtual environment
3. run `pip install -e .[tests_require]`
4. Download the FE rom (http://ff4fe.com/get?id=bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC.KPRBTZVK77) Note this is needed to make sure the save states work. 
   * Save ROM to build/
5. Run `python -m pytest` from the command line

# Todo

* Add support for bsnes
* Add objectives, characters and bosses beaten. Not this needs support from the FE devs since there is no documentation on tracking bits for these.
