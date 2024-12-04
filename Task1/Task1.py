"""Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log."""

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.addFilter(lambda record: record.levelno < logging.WARNING)

warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('{asctime} - {levelname} - {message}', style = '{')
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug('Massage level: DEBUG')
logger.info('Massage level: INFO')
logger.warning('Massage level: WARNING')
logger.error('Massage level: ERROR')
logger.critical('Massage level: CRITICAL')
