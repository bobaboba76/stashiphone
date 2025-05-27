import requests

PROXY_URL = "https://xeovo.com/proxy/pw/MGEpOQtBnz1iN6SPxCCSUOoUCefQx8Ao/plain/config/"  # Замените на вашу ссылку
OUTPUT_PATH = "stash.yaml"

resp = requests.get(PROXY_URL)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(resp.text)
