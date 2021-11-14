# Import urllib.request module
import urllib.request
import zipfile

from pathlib import Path
build_directory = Path(__file__).parent.parent / 'build'
zip_file = build_directory / 'bizhawk.zip'
bizhawk_folder = build_directory / 'bizhawk'
bizhawk_folder.mkdir(parents=True, exist_ok=True)

# Create a variable and pass the url of file to be downloaded
url = 'https://github.com/TASEmulators/BizHawk/releases/download/2.7/BizHawk-2.7-win-x64.zip'

# Copy a network object to a local file
urllib.request.urlretrieve(url, zip_file)


zip_file = zip_file

with zipfile.ZipFile(zip_file) as z:
    z.extractall(bizhawk_folder)
