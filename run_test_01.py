import pytest

if __name__ == "__main__":
    # pytest.main(["testDemo_01.py","-v","-s","--html=./test_report.html"])
    pytest.main(["testDemo_01.py", "-v", "-s", "--alluredir=/workspace/report/allure_raw"])