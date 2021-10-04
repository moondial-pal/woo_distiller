# woo_distiller
This app will scrape woocommerce endpoints and writes the requested data to a Google Cloud Platform Storage bucket.

**Data is sent to the cloud**:
- The app will send your data to either a GCP storage bucket or S3 storage.
## Adding your keys as environment variables:
1. Firstly, clone this repo.
2. Move into the woo_distiller directory.
3. Enter into python venv: 'python -m venv venv'
4. Then run the following command to activate the venv on your platform:

| Posix | Shell/zsh | 
| ----------- | ----------- |
| Command | `$ source venv/bin/activate` | 

| Posix | fish/csh/tcsh | 
| ----------- | ----------- |
| Command | `$ source venv/bin/activate` |

| Windows | PowerShell Core| 
| ----------- | ----------- |
| Command | `$ venv/bin/Activate.ps1` |

| Windows | cmd.exe | 
| ----------- | ----------- |
| Command | `C:\> venv\Scripts\activate.bat` |

| Windows | PowerShell | 
| ----------- | ----------- |
| Command | `PS C:\> venv\Scripts\Activate.ps1` |
