import { createLogger, transports, format } from 'winston';
import 'winston-daily-rotate-file';
// import fs from 'fs';
// import path from 'path';

let logger;

export const setupLogging = () => {
    logger = createLogger({
        level: 'info',
        format: format.combine(
            format.timestamp(),
            format.printf(({ timestamp, level, message }) => `${timestamp} - ${level}: ${message}`)
        ),
        transports: [
            new transports.Console() // Log to console only
            // Remove file transport for frontend
        ]
    });

    logger.info('Logging setup complete'); // Test log message
};

setupLogging(); // Call this function to initialize the logger

export const logInfo = (message) => {
    if (logger) {
        logger.info(message);
    }
};

export const logError = (message, error) => {
    if (logger) {
        logger.error(`${message} - ${error}`);
    }
};
