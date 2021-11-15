# Final Fantasy Free Enterprise Auto Tracker

Basic auto tracker for the current state of the world including;

* Retrieved Key Items
* Used Key Items
* Available Checks


# How to contribute

Branch, program, test, submit PR with successful pytest runs.

## Testing

### How to setup testing environment
1. Create a dev environment
2. run `pip install -e .[tests_require]`
3. Download the FE rom (http://ff4fe.com/get?id=bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC.KPRBTZVK77) Note this is needed to make sure the save states work.
4. Run `python -m pytest` from the command line

# Todo

* Add a UI to the front end
* Add support for bsnes
* Add objectives, characters and bosses beaten
