# brwse
`brwse` is a tool for browsing the web from your terminal.

## ⬇️ Installation
After cloning or installing the repository, the required dependencies must be installed. This can be done via [pip](https://pypi.org/project/pip/). Run the following command to install all requirements for this project:

```bash
pip install -r requirements.txt
```

## 🔍 Usage
To use brwse, open your terminal and navigate to the location where the script is stored. Then run the following command:
```bash
python brwse.py <engine> 'search query'
```

After running the command the first SERP of chosen search engine gets parsed and printed to the terminal.

### Available search engines:
- Google
    - ```bash
        python brwse.py google 'query'
        ```
## 📌 Environment variables
To easily call `brwse` from any given directory, add the script's directory to your Environment Variables. Not required for a successful installation, but still highly recommended.

How to update Environment Variables:
1. Use `Win + X` shortcut, then click **System**.
2. Click **Advanced system settings** under *Device Specifications*.
3. Click *Advanced* in the **System Properties** window, then **Environment Variables**.
4. In the *Environment Variables* window, under *System Variables*, navigate to **Path**.
5. Select **Path** and click **Edit**.
6. Click **New** and paste the directory where `brwse.py` is stored.
7. Click **Ok** twice to exit the windows.

Now, the script is globally accessible! You can use `brwse` from any directory with:
```bash
brwse <engine> 'query'
```

## 📦 Modules
- [`Typer`](https://typer.tiangolo.com/)
- [`Rich`](https://rich.readthedocs.io/en/stable/#) (bijgeleverd met Typer)
- [`BeautifulSoup4`](https://pypi.org/project/beautifulsoup4/)
- [`Requests`](https://requests.readthedocs.io/)