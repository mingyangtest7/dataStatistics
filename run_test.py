import os
import subprocess
import sys

# --- Configuration ---
# 定义报告目录
ALLURE_RAW_DIR = "reports/allure_raw"
ALLURE_HTML_DIR = "reports/allure_html"

# --- Main Execution ---
if __name__ == "__main__":
    # 确保报告目录存在
    os.makedirs(ALLURE_RAW_DIR, exist_ok=True)

    # --- Step 1: Run Pytest ---
    print("--- Running Pytest Tests ---")
    pytest_command = [
        sys.executable, "-m", "pytest",
        "tests/",  # 指向新的测试目录
        f"--alluredir={ALLURE_RAW_DIR}",
        "--clean-alluredir",  # 每次运行时清理旧的原始报告
        "-s",  # 允许stdin输入（用于验证码输入）
        "-v"  # 使用详细输出
    ]

    # 执行pytest命令
    result = subprocess.run(pytest_command)

    # 如果测试执行失败，则退出
    if result.returncode != 0:
        print("\n--- Pytest finished with errors. Aborting. ---")
        sys.exit(result.returncode)

    # --- Step 2: Generate Allure Report ---
    print(f"\n--- Generating Allure HTML report in '{ALLURE_HTML_DIR}' ---")
    allure_generate_command = [
        "allure", "generate",
        ALLURE_RAW_DIR,
        "--output", ALLURE_HTML_DIR,
        "--clean"  # 每次生成时清理旧的HTML报告
    ]
    subprocess.run(allure_generate_command)

    # --- Step 3: Serve Allure Report ---
    print(f"\n--- Serving Allure report. Press Ctrl+C to stop. ---")
    print(f"--- Access at: http://<your-ip>:<port> ---")
    allure_serve_command = ["allure", "serve", ALLURE_RAW_DIR]

    try:
        subprocess.run(allure_serve_command)
    except KeyboardInterrupt:
        print("\n--- Allure server stopped. ---")
        sys.exit(0) 