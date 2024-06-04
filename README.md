# MultiSiege

An all in one, clean and efficient launcher and downloader for handling multiple isolated instances of Rainbow Six Siege, heavily inspired by MultiMC.

MultiSiege is currently under development, so contributions are welcome!

## Installation

Clone the repository, and make a virtual environment.

```bash
python -m venv .venv
```

Active your virtual environment with the Activate.ps1 file, and install Python dependencies.

```bash
pip install -r requirements.txt
```

## Usage

The main entry point for the project is `main.py` (in the root level directory of the `src` folder)

Compiling into an executable file will only be used for releases.

```bash
pyinstaller MultiSiege.spec
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
If you would like to be a long term developer or discuss generally about the project speak to me on Discord: `@ernier6`

## License

[APACHE](http://www.apache.org/licenses/LICENSE-2.0)
