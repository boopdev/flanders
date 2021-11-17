CREATE TABLE IF NOT EXISTS config_options (
    `reference` TEXT UNIQUE NOT NULL,
    `value` ANY
);

CREATE TABLE IF NOT EXISTS cog_repositories (
    `repository_reference` TEXT UNIQUE NOT NULL,
    `repository_url` TEXT NOT NULL
)