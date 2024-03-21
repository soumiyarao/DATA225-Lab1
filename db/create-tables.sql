CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) DEFAULT NULL,
    email VARCHAR(255) DEFAULT NULL,
    password VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE ratings ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES Users(USER_ID);

insert into Users(User_id) select distinct user_id from ratings;

CREATE TABLE SearchHistory (
    search_id INT PRIMARY KEY AUTO_INCREMENT,
    search_string VARCHAR(255),
    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) on delete cascade
);

CREATE TABLE ViewHistory (
    view_id INT PRIMARY KEY AUTO_INCREMENT,
    tmdb_id INT,
    view_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) on delete cascade
);
