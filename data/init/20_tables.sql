-- Unique Projects for ticket grouping
CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    prefix VARCHAR(5) UNIQUE,
    name TEXT,
    description TEXT
);
-- Types of tickets per-project, "feature", "bug", "task", etc...
CREATE TABLE ticket_types (
    id SERIAL PRIMARY KEY,
    project_id INT,
    name VARCHAR(20),
    -- color is a hex code
    color CHAR(6),
    CONSTRAINT ticket_types_pi FOREIGN KEY (project_id) REFERENCES project (id)
);
-- Ticket statuses per-project, "ready", "in progress", etc...
CREATE TABLE statuses (
    id SERIAL PRIMARY KEY,
    project_id INT,
    name VARCHAR(20),
    CONSTRAINT statuses_pi FOREIGN KEY (project_id) REFERENCES project (id)
);
-- Ticket link types per-project
CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    project_id INT,
    name VARCHAR(30),
    CONSTRAINT links_pi FOREIGN KEY (project_id) REFERENCES project (id)
);
-- ticket
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    project_id INT,
    status_id INT,
    type_id INT,
    title TEXT,
    description TEXT,
    CONSTRAINT tickets_pi FOREIGN KEY (project_id) REFERENCES project (id),
    CONSTRAINT tickets_si FOREIGN KEY (status_id) REFERENCES statuses (id),
    CONSTRAINT tickets_ti FOREIGN KEY (type_id) REFERENCES ticket_types (id)
);