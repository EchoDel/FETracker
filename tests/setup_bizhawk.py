# Import urllib.request module
import urllib.request
import zipfile

from pathlib import Path
build_directory = Path(__file__).parent.parent / 'build'
zip_file = build_directory / 'bizhawk.zip'
bizhawk_folder = build_directory / 'bizhawk'

if not bizhawk_folder.exists():
    bizhawk_folder.mkdir(parents=True, exist_ok=True)
    # Most recent version of bizhawk as of 2021/11/14
    url = 'https://github.com/TASEmulators/BizHawk/releases/download/2.7/BizHawk-2.7-win-x64.zip'

    # Copy a network object to a local file
    urllib.request.urlretrieve(url, zip_file)

    # Unzip the bizhawk folder
    with zipfile.ZipFile(zip_file) as z:
        z.extractall(bizhawk_folder)
