# coding=utf-8
import os
import time
import logging
import pytest
import click
from conftest import REPORT_DIR
from config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@click.command()
def run():
    logger.info("正在进行测试")
    now_time = time.strftime("%Y%m%d%H%M%S")
    Config.NEW_REPORT = os.path.join(REPORT_DIR, now_time)
    os.mkdir(Config.NEW_REPORT)
    os.mkdir(Config.NEW_REPORT + "/image")
    html_report = os.path.join(Config.NEW_REPORT, "report.html")
    pytest.main(["-s", "-v", Config.cases_path,
                 "--html=" + html_report])
    logger.info("正在生成报告")


if __name__ == '__main__':
    run()
