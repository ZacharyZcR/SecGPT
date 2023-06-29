import logging
import colorlog
import os
from utils.constants import LOG_DIR, LOG_FORMAT, LOG_COLORS_FORMAT, LOG_FILE, LOG_COLORS

class Log:
    def __init__(self, module_name):
        self.logger = logging.getLogger(module_name)
        self.logger.setLevel(logging.DEBUG)  # 设置为最低级别

        # 创建一个颜色格式化器
        color_formatter = colorlog.ColoredFormatter(
            LOG_COLORS_FORMAT,
            log_colors=LOG_COLORS
        )

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # 只在控制台显示INFO级别及以上的日志
        console_handler.setFormatter(color_formatter)  # 使用颜色格式化器

        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        if not os.path.exists(LOG_DIR + LOG_FILE):
            with open(LOG_DIR + LOG_FILE, 'w') as f:
                f.write("")
        file_handler = logging.FileHandler(LOG_DIR + LOG_FILE)
        file_handler.setLevel(logging.DEBUG)  # 在文件中保存所有级别的日志
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
