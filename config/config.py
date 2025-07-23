import yaml
import os
from pathlib import Path

# --- Constants ---
# 项目根目录
ROOT_DIR = Path(__file__).parent.parent
CONFIG_PATH = ROOT_DIR / "config" / "config.yaml"


# --- Functions ---
def load_config(path: str = CONFIG_PATH) -> dict:
    """
    加载YAML格式的配置文件。
    :param path: 配置文件的路径。
    :return: 包含配置信息的字典。
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            CONFIG = yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"配置文件未找到: {path}")
    except Exception as e:
        raise IOError(f"读取配置文件失败: {e}")

    # 将image_path转换为绝对路径
    if "image_path" in CONFIG and not os.path.isabs(CONFIG["image_path"]):
        CONFIG["image_path"] = str(ROOT_DIR / CONFIG["image_path"])

    return CONFIG


# --- Global Config ---
# 在模块加载时读取一次配置，供全局使用
CONFIG = load_config()

# --- Example Usage ---
if __name__ == '__main__':
    # 打印加载的配置，方便调试
    print("Project Root Directory:", ROOT_DIR)
    print("Loaded Configuration:")
    # 使用一个更安全的方式打印，避免敏感信息泄露
    config_to_print = {k: v for k, v in CONFIG.items() if "token" not in k and "password" not in k}
    print(config_to_print)
    # 检查图片路径
    image_path = CONFIG.get("image_path")
    if image_path:
        print("Image Path:", image_path)
        print("Image exists:", os.path.exists(image_path)) 