CREATE TABLE IF NOT EXISTS config_options (
    `reference` TEXT UNIQUE NOT NULL,
    `value` ANY
);