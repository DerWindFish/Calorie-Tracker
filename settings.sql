-- settings.sql
CREATE DATABASE calorie_tracker;
CREATE USER calorie_tracker_admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE calorie_tracker TO calorie_tracker_admin;
