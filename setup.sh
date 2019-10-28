  
#!/usr/bin/env bash
set -e

# Copy config.ini.default if it exists
# Copy config.ini doesn't config.ini.default exist.
if [ -e config.ini.default ] && [ ! -e config.ini ]; then
    cp config.ini.default config.ini
    chmod a+w config.ini
fi

PYTHON=$(command -v python3)
VENV=venv

if [ -f "$PYTHON" ]; then

    if [ ! -d $VENV ]; then
        # Virtual environment create if doesn't exist.
        $PYTHON -m venv $VENV
    fi

    # Virtual environment activation; Install requirements.
    # shellcheck disable=SC1090
    . $VENV/bin/activate
    pip3 install wheel
    pip3 install -r requirements.txt

else
    >&2 echo "Cannot find Python 3. Please install it."
fi
