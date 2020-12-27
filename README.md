Thanks so much for everyone who contributed, I just made it work for macos Big Sur <3
# alesisvsysex

Python tool for configuring Alesis MIDI controllers

Should work with V25, VMini, and VI49 controllers, and should be
(easily?) extensible to the V49, V61, VI25, and VI61 controllers.  Is
not expected to ever work with the Q-series (configured entirely from
the controller side) or VX49 (has that fancy DAW integration)
controllers.


from https://github.com/le1ca/alesisvsysex (original, V25 version)
from https://github.com/Baggypants/alesisvsysex (VMini version)



## Overview

The official tool for configuring these controllers only works on Windows. Fortunately, Travis Mick was able to [reverse engineer the SysEx protocol](https://lo.calho.st/projects/reverse-engineering-the-alesis-v-series-sysex-protocol/) and implement the first version of this program.

Currently, this software is only known to work on Linux, and only supports the Alesis V25, VMini, and VI49 controllers. It includes a model for the parts of the SysEx protocol that have been figured out (i.e., most of it), the ability to fetch and update the device configurations, and the ability to store and load configurations as files.

Save files should compatible with the windows editor software provided by Alesis for the V25 and VI49, but not for the VMini (for some reason the windows VMini editor uses a save format that differs from the pattern set by the V25 and VI49).  Additionally, the V25 and VMini save files are valid SysEx messages that can be sent to a device to set their configuration.

The GUI uses [PyQt5](http://pyqt.sourceforge.net/Docs/PyQt5/), and the MIDI layer uses [mido](https://mido.readthedocs.io/en/latest/).

## Dependencies

This software is written for Python 3.5+. It requires a system installation of PyQt5, portmidi, and an update to python. Install this with Homebrew and have pip binary linked:
 
`brew install python pyqt portmidi`
`pip3 install -U pip`

then run:

`pip3 install -r requirements.pip3`

## Launching the application

From this directory, you can run `python3 -m alesisvsysex` to launch the GUI.

An exception will be thrown if the MIDI controller cannot be detected when attempting to load or save a configuration. If you unplug the controller while loading or saving, you're in for a bad time. If someone wishes to make this more robust, please feel free.

## Running the test suite

From the same directory that you can launch the application, you can run `python3 -m unittest` to run the test suite.

## Contributing

Any contributions of bug fixes or improvements will be greatly appreciated, including adding support for a different OS or controller.

## License

This software is released under the terms of the MIT license. A copy of the license can be found in the `LICENSE` file.
