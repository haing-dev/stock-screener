import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT, "config.json")
LOCAL_PATH = os.path.join(ROOT, "local_settings.json")   # private: SEC name/email and API keys (never share)
PRIVATE_KEYS = ("user_agent", "twelvedata_api_key", "massive_api_key")
CACHE_DIR = os.path.join(ROOT, "cache")
OUTPUT_DIR = os.path.join(ROOT, "output")


def load_config(path=CONFIG_PATH):
    with open(path, encoding="utf-8") as f:
        cfg = json.load(f)
    if os.path.exists(LOCAL_PATH) and path == CONFIG_PATH:
        with open(LOCAL_PATH, encoding="utf-8") as f:
            cfg.update(json.load(f))
    if os.environ.get("TWELVEDATA_API_KEY"):
        cfg["twelvedata_api_key"] = os.environ["TWELVEDATA_API_KEY"]
    if os.environ.get("SEC_USER_AGENT"):
        cfg["user_agent"] = os.environ["SEC_USER_AGENT"]
    if os.environ.get("MASSIVE_API_KEY"):
        cfg["massive_api_key"] = os.environ["MASSIVE_API_KEY"]
    return cfg


def save_local(updates):
    cur = {}
    if os.path.exists(LOCAL_PATH):
        with open(LOCAL_PATH, encoding="utf-8") as f:
            cur = json.load(f)
    cur.update(updates)
    tmp = LOCAL_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cur, f, indent=2)
    os.replace(tmp, LOCAL_PATH)


def save_config(cfg, path=CONFIG_PATH):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
    os.replace(tmp, path)


def ensure_user_agent(cfg, path=CONFIG_PATH):
    """SEC asks every automated client to identify itself with a name and email."""
    if os.environ.get("SCREENER_FIXTURES"):
        return "offline-test test@example.com"
    ua = (cfg.get("user_agent") or "").strip()
    if ua and "@" in ua:
        return ua
    print()
    print("The SEC asks anyone downloading its data to identify themselves")
    print("(name + email, sent only to sec.gov). This is saved in local_settings.json.")
    name = ""
    while not name:
        name = input("  Your name: ").strip()
    email = ""
    while "@" not in email:
        email = input("  Your email: ").strip()
    ua = f"{name} {email}"
    cfg["user_agent"] = ua
    save_local({"user_agent": ua})
    print("  Saved.\n")
    return ua
