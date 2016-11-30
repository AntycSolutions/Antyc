
platform=`python -c "import platform; print(platform.system())"`

if [[ "$platform" == 'Linux' ]]; then
    source ../venv_antyc_website/bin/activate
elif [[ "$platform" == 'Windows' ]]; then
    source ../venv_antyc_website/Scripts/activate
else
    echo "Unsupported platform: $platform"
fi
