# kivy_image_enhancer

Simple test interface built with [Kivy](https://github.com/kivy/kivy) framework. Hats off to its developers - great job!

## Installation instructions

Starts like a usual Python project:

```bash
cd kivy_image_enhancer
py -m venv _venv
source _venv/bin/activate
pip3 install -r requirements.txt
```

Setup buildozer:
```bash
buildozer init
```

Edit the spec file buildozer.spec. Params - refer to [buildozer.spec documentation](https://buildozer.readthedocs.io/en/latest/specifications.html)

Now start a debug build of your application:
```bash
buildozer -v android debug
```

To test your app on the computer, run
```bash
python main.py
```

## Usage notes

- I couldn't make it work with main.kv file so far, so interface markup is within the code.

## Feedback
- Any notes are [welcome here](https://t.me/walsk)


For deployment on mobile devices check [Buildozer doc](https://buildozer.readthedocs.io/en/latest/quickstart.html#run-my-application) (it's readable, promise).

